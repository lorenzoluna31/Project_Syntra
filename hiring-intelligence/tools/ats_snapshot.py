"""Snapshot de vacantes públicas desde APIs oficiales de ATS.

Para cada empresa de un CSV (company,ats,token) consulta el endpoint público de su ATS,
guarda cada vacante observada con fecha en SQLite y compara con la observación anterior:
vacantes nuevas, cerradas y posibles republicaciones (mismo título+ubicación con un id nuevo
después de haber desaparecido). También clasifica títulos en técnicos / Talent Acquisition
(señal negativa para agencias) / otros.

Endpoints usados (públicos y documentados por cada proveedor):
  greenhouse: https://boards-api.greenhouse.io/v1/boards/{token}/jobs
  lever:      https://api.lever.co/v0/postings/{token}?mode=json   (lever-eu: api.eu.lever.co)
  ashby:      https://api.ashbyhq.com/posting-api/job-board/{token}
  personio:   https://{token}.jobs.personio.de/xml               (personio-com: .jobs.personio.com)
  workable:   https://apply.workable.com/api/v1/widget/accounts/{token}

Uso:
  python3 tools/ats_snapshot.py data/ats_targets.csv [--db data/ats_snapshots.sqlite]

Requiere acceso de red a esos dominios. Sin red, cada empresa se registra como error
(no se inventa nada).
"""
import argparse
import csv
import json
import re
import sqlite3
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

USER_AGENT = "hiring-intelligence-research/0.1 (public job board reader)"
TIMEOUT = 20

ENDPOINTS = {
    "greenhouse": "https://boards-api.greenhouse.io/v1/boards/{token}/jobs",
    "lever": "https://api.lever.co/v0/postings/{token}?mode=json",
    "lever-eu": "https://api.eu.lever.co/v0/postings/{token}?mode=json",
    "ashby": "https://api.ashbyhq.com/posting-api/job-board/{token}",
    "personio": "https://{token}.jobs.personio.de/xml",
    "personio-com": "https://{token}.jobs.personio.com/xml",
    "workable": "https://apply.workable.com/api/v1/widget/accounts/{token}",
}

TECH_RE = re.compile(
    r"engineer|developer|desarrollador|ingenier|programad|\bdata\b|datos|machine learning|\bml\b|"
    r"\bai\b|\bia\b|devops|\bsre\b|platform|cloud|security|seguridad|ciberseg|backend|back-end|"
    r"frontend|front-end|full.?stack|architect|arquitect|\bqa\b|mobile|\bios\b|android|\bcto\b|"
    r"scientist|cient[ií]fic|mlops|llm",
    re.I,
)
TA_RE = re.compile(r"talent acquisition|recruit|reclut|selecci[oó]n de personal|sourcer|headhunt", re.I)


def classify(title):
    if TA_RE.search(title or ""):
        return "talent_acquisition"
    if TECH_RE.search(title or ""):
        return "tech"
    return "other"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read()


def _job(job_id, title, location, url, published):
    return {
        "job_id": str(job_id),
        "title": (title or "").strip(),
        "location": (location or "").strip(),
        "url": url or "",
        "published_at": published or "",
    }


def parse(ats, raw):
    """Convierte la respuesta de cada ATS a una lista de dicts homogéneos."""
    if ats.startswith("personio"):
        root = ET.fromstring(raw)
        jobs = []
        for pos in root.iter("position"):
            get = lambda tag: (pos.findtext(tag) or "").strip()
            offices = [get("office")] + [o.text or "" for o in pos.iter("additionalOffice")]
            jobs.append(_job(get("id"), get("name"), ", ".join(o for o in offices if o), "", get("createdAt")))
        return jobs

    data = json.loads(raw)
    if ats == "greenhouse":
        return [
            _job(j.get("id"), j.get("title"), (j.get("location") or {}).get("name"), j.get("absolute_url"),
                 j.get("first_published") or j.get("updated_at"))
            for j in data.get("jobs", [])
        ]
    if ats.startswith("lever"):
        out = []
        for j in data:
            created = j.get("createdAt")
            if isinstance(created, (int, float)):
                created = datetime.fromtimestamp(created / 1000, tz=timezone.utc).isoformat()
            out.append(_job(j.get("id"), j.get("text"), (j.get("categories") or {}).get("location"),
                            j.get("hostedUrl"), created))
        return out
    if ats == "ashby":
        return [
            _job(j.get("id"), j.get("title"), j.get("location"), j.get("jobUrl"), j.get("publishedAt"))
            for j in data.get("jobs", []) if j.get("isListed", True)
        ]
    if ats == "workable":
        return [
            _job(j.get("shortcode"), j.get("title"),
                 ", ".join(x for x in (j.get("city"), j.get("country")) if x), j.get("url"), j.get("published_on"))
            for j in data.get("jobs", [])
        ]
    raise ValueError(f"ATS no soportado: {ats}")


SCHEMA = """
CREATE TABLE IF NOT EXISTS runs (
  run_id INTEGER PRIMARY KEY AUTOINCREMENT,
  company TEXT NOT NULL, ats TEXT NOT NULL, token TEXT NOT NULL,
  observed_at TEXT NOT NULL, ok INTEGER NOT NULL, error TEXT
);
CREATE TABLE IF NOT EXISTS observations (
  run_id INTEGER NOT NULL REFERENCES runs(run_id),
  job_id TEXT NOT NULL, title TEXT, location TEXT, url TEXT, published_at TEXT, category TEXT
);
"""


def connect(db_path):
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(db_path)
    con.executescript(SCHEMA)
    return con


def record(con, company, ats, token, observed_at, jobs=None, error=None):
    cur = con.execute(
        "INSERT INTO runs (company, ats, token, observed_at, ok, error) VALUES (?,?,?,?,?,?)",
        (company, ats, token, observed_at, int(error is None), error),
    )
    run_id = cur.lastrowid
    for j in jobs or []:
        con.execute(
            "INSERT INTO observations VALUES (?,?,?,?,?,?,?)",
            (run_id, j["job_id"], j["title"], j["location"], j["url"], j["published_at"], classify(j["title"])),
        )
    con.commit()
    return run_id


def _key(title, location):
    return (re.sub(r"\W+", " ", (title or "").lower()).strip(), (location or "").lower().strip())


def diff(con, company):
    """Compara las dos últimas ejecuciones exitosas de una empresa."""
    runs = [r[0] for r in con.execute(
        "SELECT run_id FROM runs WHERE company=? AND ok=1 ORDER BY run_id DESC LIMIT 2", (company,))]
    if not runs:
        return None
    jobs = lambda run: {r[0]: r for r in con.execute(
        "SELECT job_id, title, location, category FROM observations WHERE run_id=?", (run,))}
    latest = jobs(runs[0])
    previous = jobs(runs[1]) if len(runs) > 1 else {}
    new_ids = set(latest) - set(previous) if previous else set()
    closed_ids = set(previous) - set(latest)

    # Posible republicación: título+ubicación visto en una ejecución anterior con otro id,
    # que había desaparecido antes de reaparecer con id nuevo.
    reposts = []
    for jid in new_ids:
        _, title, location, _ = latest[jid]
        seen_before = con.execute(
            """SELECT DISTINCT o.job_id, o.title, o.location FROM observations o
               JOIN runs r ON r.run_id=o.run_id
               WHERE r.company=? AND r.run_id<? AND o.job_id<>?""", (company, runs[0], jid)).fetchall()
        for old_id, old_title, old_location in seen_before:
            if old_id not in latest and _key(old_title, old_location) == _key(title, location):
                reposts.append({"new_id": jid, "old_id": old_id, "title": title})
                break

    cats = {}
    for _, _, _, cat in latest.values():
        cats[cat] = cats.get(cat, 0) + 1
    return {
        "company": company,
        "open_total": len(latest),
        "by_category": cats,
        "talent_acquisition_titles": sorted(t for _, t, _, c in latest.values() if c == "talent_acquisition"),
        "tech_titles": sorted(t for _, t, _, c in latest.values() if c == "tech"),
        "new_since_previous": sorted(latest[j][1] for j in new_ids),
        "closed_since_previous": sorted(previous[j][1] for j in closed_ids),
        "possible_reposts": reposts,
        "compared_runs": runs,
    }


def run(targets_csv, db_path, fetcher=fetch, now=None):
    con = connect(db_path)
    observed_at = now or datetime.now(timezone.utc).isoformat(timespec="seconds")
    summaries = []
    with open(targets_csv, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            company, ats, token = row["company"].strip(), row["ats"].strip().lower(), row["token"].strip()
            if ats not in ENDPOINTS:
                record(con, company, ats, token, observed_at, error=f"ATS no soportado: {ats}")
                continue
            url = ENDPOINTS[ats].format(token=token)
            try:
                jobs = parse(ats, fetcher(url))
            except Exception as exc:  # red bloqueada, token incorrecto, formato inesperado
                record(con, company, ats, token, observed_at, error=f"{type(exc).__name__}: {exc}")
                summaries.append({"company": company, "error": f"{type(exc).__name__}: {exc}", "url": url})
                continue
            record(con, company, ats, token, observed_at, jobs)
            summary = diff(con, company)
            summary["url"] = url
            summaries.append(summary)
    return summaries


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("targets_csv")
    p.add_argument("--db", default="data/ats_snapshots.sqlite")
    args = p.parse_args(argv)
    summaries = run(args.targets_csv, args.db)
    print(json.dumps(summaries, ensure_ascii=False, indent=2))
    return 0 if all("error" not in s for s in summaries) else 1


if __name__ == "__main__":
    sys.exit(main())
