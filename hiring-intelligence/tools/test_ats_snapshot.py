"""Tests con respuestas SINTÉTICAS que imitan el formato documentado de cada ATS.

No prueban las APIs reales (la red estaba bloqueada al escribirlos): solo el parseo,
la clasificación y la detección de cambios. Validar contra APIs reales cuando haya red.
"""
import json
import os
import tempfile
import unittest

import ats_snapshot as ats

GREENHOUSE = json.dumps({"jobs": [
    {"id": 1, "title": "Senior ML Engineer", "location": {"name": "Barcelona"},
     "absolute_url": "https://x/1", "first_published": "2026-09-01T00:00:00Z"},
    {"id": 2, "title": "Talent Acquisition Partner", "location": {"name": "Madrid"},
     "absolute_url": "https://x/2", "updated_at": "2026-09-02T00:00:00Z"},
]}).encode()
LEVER = json.dumps([{"id": "a", "text": "Backend Developer", "categories": {"location": "Madrid"},
                     "hostedUrl": "https://l/a", "createdAt": 1790000000000}]).encode()
ASHBY = json.dumps({"jobs": [{"id": "z", "title": "Account Executive", "location": "Remote",
                              "jobUrl": "https://a/z", "publishedAt": "2026-10-01", "isListed": True},
                             {"id": "h", "title": "Hidden", "isListed": False}]}).encode()
WORKABLE = json.dumps({"jobs": [{"shortcode": "W1", "title": "Data Engineer", "city": "Valencia",
                                 "country": "Spain", "url": "https://w/1", "published_on": "2026-08-20"}]}).encode()
PERSONIO = b"""<?xml version="1.0"?><workzag-jobs>
<position><id>11</id><office>Barcelona</office><additionalOffices><additionalOffice>Madrid</additionalOffice></additionalOffices>
<department>Eng</department><name>Lead AI/ML Engineer</name><createdAt>2026-07-01T10:00:00+00:00</createdAt></position>
<position><id>12</id><office>Madrid</office><name>Senior Recruiter</name><createdAt>2026-07-03T10:00:00+00:00</createdAt></position>
</workzag-jobs>"""


class ParseTests(unittest.TestCase):
    def test_parsers(self):
        self.assertEqual([j["title"] for j in ats.parse("greenhouse", GREENHOUSE)],
                         ["Senior ML Engineer", "Talent Acquisition Partner"])
        lever = ats.parse("lever", LEVER)[0]
        self.assertEqual((lever["title"], lever["location"]), ("Backend Developer", "Madrid"))
        self.assertTrue(lever["published_at"].startswith("2026-"))
        self.assertEqual([j["job_id"] for j in ats.parse("ashby", ASHBY)], ["z"])
        self.assertEqual(ats.parse("workable", WORKABLE)[0]["location"], "Valencia, Spain")
        personio = ats.parse("personio", PERSONIO)
        self.assertEqual(personio[0]["location"], "Barcelona, Madrid")
        self.assertEqual(len(personio), 2)

    def test_classify(self):
        self.assertEqual(ats.classify("Talent Acquisition Partner - BCN/MAD"), "talent_acquisition")
        self.assertEqual(ats.classify("Técnico/a de Selección de Personal"), "talent_acquisition")
        self.assertEqual(ats.classify("Senior AI/ML Engineer"), "tech")
        self.assertEqual(ats.classify("Ingeniero/a de Datos"), "tech")
        self.assertEqual(ats.classify("Key Account Manager"), "other")


class RunTests(unittest.TestCase):
    def test_diff_and_repost(self):
        with tempfile.TemporaryDirectory() as tmp:
            targets = os.path.join(tmp, "t.csv")
            db = os.path.join(tmp, "db.sqlite")
            with open(targets, "w") as f:
                f.write("company,ats,token\nAcme,greenhouse,acme\n")

            def gh(jobs):
                return lambda url: json.dumps({"jobs": jobs}).encode()

            ml = {"id": 1, "title": "Senior ML Engineer", "location": {"name": "Barcelona"}}
            ta = {"id": 2, "title": "Talent Acquisition Partner", "location": {"name": "Madrid"}}
            ml_again = dict(ml, id=3)

            first = ats.run(targets, db, fetcher=gh([ml, ta]), now="2026-10-01T00:00:00+00:00")[0]
            self.assertEqual(first["open_total"], 2)
            self.assertEqual(first["talent_acquisition_titles"], ["Talent Acquisition Partner"])
            self.assertEqual(first["new_since_previous"], [])

            second = ats.run(targets, db, fetcher=gh([ta]), now="2026-10-08T00:00:00+00:00")[0]
            self.assertEqual(second["closed_since_previous"], ["Senior ML Engineer"])

            third = ats.run(targets, db, fetcher=gh([ta, ml_again]), now="2026-10-15T00:00:00+00:00")[0]
            self.assertEqual(third["new_since_previous"], ["Senior ML Engineer"])
            self.assertEqual(third["possible_reposts"], [{"new_id": "3", "old_id": "1", "title": "Senior ML Engineer"}])

    def test_network_error_is_recorded_not_invented(self):
        with tempfile.TemporaryDirectory() as tmp:
            targets = os.path.join(tmp, "t.csv")
            with open(targets, "w") as f:
                f.write("company,ats,token\nAcme,lever,acme\n")

            def boom(url):
                raise OSError("network blocked")

            out = ats.run(targets, os.path.join(tmp, "db.sqlite"), fetcher=boom)
            self.assertIn("network blocked", out[0]["error"])


if __name__ == "__main__":
    unittest.main()
