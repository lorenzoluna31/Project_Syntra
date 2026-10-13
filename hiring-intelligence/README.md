# Hiring Intelligence (nombre provisional)

Inteligencia comercial para **agencias boutique de selección tech en España**: empresas con **necesidad técnica verificada**, priorizadas por **antecedentes públicos de pagar intermediación** y depuradas de las que tienen **selección interna**. Cada dato con fuente y fecha.

## Estado al 2026-10-13
- **Ventas: 0. Contactos: 0.** No se envió nada a terceros.
- **Mejor oportunidad:** Prosper AI (Barcelona). Ronda, hub e intermediación de Manfred verificados por el fundador. **Aproximación condicional**: faltan 3 comprobaciones (`reports/PILOT_v2_2026-10-13.md`).
- **Hallazgo:** Manfred publica sus procesos con el nombre del cliente. Sirve para identificar empresas que ya pagaron intermediación (`CASES_EXTERNAL_RECRUITING.csv`, 9 casos).
- **Pero:** apuntar a empresas que ya usan agencias es una práctica de BD conocida, y existen herramientas como Arca24 JobRadar. **No hay ventaja competitiva demostrada**, solo una hipótesis comprobable (`MODELS.md`).
- **Próximo paso:** `EXPERIMENT_2.md` (A vs. B vs. C con 3 agencias, piloto de €150 por adelantado, criterios de descarte). Necesita las acciones del fundador de `NEXT_STEPS.md`.

## Limitaciones activas
- Sin acceso web directo: solo buscador, que devuelve resúmenes (`NETWORK_SETUP.md`). Límite de 200 búsquedas por turno.
- El cobro en EUR desde Argentina no está verificado.

## Archivos
| Archivo | Contenido |
|---|---|
| `NEXT_STEPS.md` | **Acciones del fundador**, autorizaciones y riesgos |
| `reports/PILOT_v2_2026-10-13.md` | Informe piloto actual (el v1 queda como histórico) |
| `VERIFICATION_STATUS.md` | Cada afirmación clasificada: verificada, parcial, inferida o no verificada |
| `CASES_EXTERNAL_RECRUITING.csv` | Casos con antecedentes públicos de intermediación |
| `MODELS.md` | Modelos A/B/C y respuestas a las preguntas de validación |
| `EXPERIMENT_2.md` | Próximo experimento comercial y oferta piloto |
| `outreach/MESSAGES.md` | Canales legales y mensajes por canal (nada enviado) |
| `BUSINESS_MODEL.md` | Propuesta, precio, costos y rentabilidad mínima |
| `COMPETITORS.md` | Competidores y la señal "ya usa agencias" |
| `RESEARCH.md` | Nicho, mercado, fuentes, legal y obstáculos |
| `OPPORTUNITIES.csv`, `tools/score.py` | Oportunidades con puntuación (`python3 tools/score.py`) |
| `PROSPECTS.csv` | Agencias compradoras |
| `EVIDENCE_LOG.csv` | Registro de afirmaciones y fuentes |
| `VALIDATION.md` | Hipótesis y resultados |
| `NETWORK_SETUP.md` | Cómo habilitar el acceso web y los límites observados |
| `tools/ats_snapshot.py` | Fotos fechadas de vacantes desde APIs públicas de ATS (probado solo con datos sintéticos) |
