# Modelo de negocio y supuestos

> **Actualización 2026-10-13:** la oferta vigente y la economía completa (con adquisición) están en `DEMAND_VALIDATION.md` §2 y §5. La oferta de €150 por 3 empresas de abajo queda **retirada**.

Estado: **hipótesis, 0 ventas, 0 contactos.** Última actualización: 2026-10-13 (v2).

## Cambios de hipótesis en esta versión
| Antes | Ahora | Por qué |
|---|---|---|
| Vender "empresas con señales de contratación" | Vender **empresas con necesidad verificada, priorizadas por antecedente de pagar intermediación y depuradas de TA interno** | Las señales de contratación son un commodity (≥6 herramientas). Apuntar a "empresas que ya usan agencias" es una práctica de BD conocida, pero no encontramos quien la combine con necesidad nueva y descarte de TA en España (evidencia débil) |
| "Ninguna herramienta lo hace" | **Arca24 JobRadar** rastrea ofertas de agencias competidoras; las ofertas de Manfred son públicas | Evidencia de esta ronda (`MODELS.md`) |
| Piloto de €45, pagado si "resulta útil" | **€150, 100% por adelantado, con criterios objetivos y garantía de reposición** | El criterio subjetivo invita a trabajar gratis, y reclamar un impago desde Argentina es inviable |
| Cadencia semanal | **Quincenal o mensual** | El volumen estimado de oportunidades de calidad es de 1-3 por mes por nicho |

## Propuesta de valor a probar
> "Cada quincena, entre 3 y 5 empresas de tu ciudad y especialidad con **necesidad técnica verificada** (vacante comprobada o plan público con cifras). Para cada una: si hay **evidencia pública de que ya pagó intermediación** y en qué procesos, y **descartamos las que tienen selección interna**. Fuente y fecha en cada dato. Excluimos tus clientes actuales."

Se puede refutar: ver los criterios de `EXPERIMENT_2.md`.

## Precio piloto: €150 por adelantado

### Costo por informe (3 empresas verificadas + 2-3 descartes, con navegador normal)
| Tarea | Horas (estimación) |
|---|---|
| Descubrimiento: rondas, ofertas de intermediarios, ATS | 2-3 |
| Verificación: 0,5-1 h por empresa, incluidos los descartes | 1,5-3 |
| Redacción con hechos, inferencias y dudas | 1 |
| Comunicación con el comprador y lista de exclusión | 0,5-1 |
| **Total** | **5-8 h** |

**Base medida:** verificar Prosper AI llevó 22 búsquedas. Con navegador estimamos 60-90 minutos. Sin acceso web directo, el costo actual es desproporcionado y **no sirve como referencia de producción**.

### Cuentas
- €150 / 5-8 h = **€19-30 por hora bruta**.
- Comisiones de cobro con Payoneer (si está disponible):
  - Recibir desde un banco de la UE: 1% ([pricing oficial](https://www.payoneer.com/pricing/)).
  - Retirar a Argentina: 2% ([Payoneer Grow](https://www.payoneer.com/resources/how-to-use-payoneer/payoneer-grow/)).
  - Total ≈ €4,50 por pago. **Sin verificar** que un residente argentino obtenga una cuenta de recepción en EUR.
- Referencias de precio:
  - Recruit Signals Solo: €99-124/mes, con foco en UK y Países Bajos.
  - Una colocación vía Manfred para un puesto de €85K: 15% = €12.750. El piloto equivale a ~1,2% de **una** comisión.
- **No hay evidencia de disposición a pagar.** El precio es una hipótesis que se prueba con el pago.

### ¿Por qué no €45?
A 5-8 h, €45 son €6-9 por hora. Además, cada transferencia internacional tiene costos fijos. Un precio que no cubre el costo no valida un negocio: valida un regalo.

### ¿Por qué 100% por adelantado?
- Desde Argentina no hay forma práctica de reclamar un impago.
- El pago anticipado es la única señal de disposición a pagar que no se puede fingir.
- El riesgo del comprador se cubre con criterios objetivos y reposición, no con "si te gustó".

## Condiciones mínimas de rentabilidad (servicio recurrente)
| Escenario | Precio | Entregas/mes | Horas/mes por cliente | €/h | Clientes para USD 1.000/mes |
|---|---|---|---|---|---|
| Pesimista | €200/mes | 2 | 12 | €16 | ~5 (60 h/mes) |
| Intermedio | €250/mes | 2 | 9 | €27 | ~4 (36 h/mes) |
| Optimista (con herramientas y reutilización entre agencias de nichos distintos) | €300/mes | 2 | 6 | €50 | ~3 (18 h/mes) |

**Mínimo para que valga la pena:** al menos €250/mes por cliente y como mucho 9 h/mes, lo que exige automatizar el descubrimiento (`tools/ats_snapshot.py`, monitoreo de intermediarios y rondas). Por debajo de eso es freelance mal pagado.

**Reutilización legítima:** una misma empresa en expansión puede servir a agencias de especialidades distintas (IA vs. cloud) sin canibalizarse. A agencias que compiten en el mismo nicho y ciudad no se les vende la misma empresa en la misma quincena.

## Supuestos críticos (por riesgo)
1. Las boutiques valoran el antecedente de intermediación y el descarte de TA, y no lo obtienen ya solas (**desconocido**).
2. Pagan €150 por adelantado a un proveedor nuevo desde Argentina (**desconocido**).
3. Hay al menos 2 empresas B nuevas por mes por nicho (**estimado, dudoso**).
4. Podemos cobrar en EUR de forma legal y barata (**no verificado**).
5. Podemos conseguir conversaciones sin comunicaciones comerciales no solicitadas (**canal lento**).
