"""Puntuación experimental de oportunidades (OPPORTUNITIES.csv).

No es una probabilidad de compra: es un orden de prioridad con pesos provisionales.
Cualquier valor en `exclusion_critica` descarta la oportunidad, sin importar el puntaje.
Uso: python tools/score.py [ruta_csv]
"""
import csv
import sys

# Pesos provisionales: se ajustan con el feedback de los compradores.
WEIGHTS = {
    "encaje": 0.20,
    "actualidad": 0.15,
    "calidad_evidencia": 0.15,
    "actividad_contratacion": 0.15,
    "apertura": 0.20,
    "accesibilidad": 0.05,
    "diferencial": 0.10,
}
RISK_WEIGHT = 0.10  # Se resta: un riesgo de 0-5 descuenta hasta 0,5 puntos.


def score(row):
    total = sum(float(row[k]) * w for k, w in WEIGHTS.items())
    return round(total - float(row["riesgo"]) * RISK_WEIGHT, 2)


def main(path="OPPORTUNITIES.csv"):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        row["_score"] = score(row)
        row["_excluded"] = bool(row["exclusion_critica"].strip())
    rows.sort(key=lambda r: (r["_excluded"], -r["_score"]))
    for r in rows:
        status = f"EXCLUIDA ({r['exclusion_critica']})" if r["_excluded"] else "ok"
        print(f"{r['id']:4} {r['empresa']:20} {r['_score']:5.2f}/5  {status}")


if __name__ == "__main__":
    main(*sys.argv[1:])
