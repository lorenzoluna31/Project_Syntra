# Validación: hipótesis, experimentos y resultados

## Registro de resultados reales
| Fecha | Evento | Resultado |
|---|---|---|
| 2026-10-13 | Investigación de escritorio inicial | Hecha (ver RESEARCH.md). **0 contactos, 0 conversaciones, 0 ventas.** |
| 2026-10-13 | Producción del piloto (Kulturo) | 2 oportunidades utilizables + 1 descarte en ~40 búsquedas. Sin verificación manual todavía |
| 2026-10-13 | Rondas 2 y 3 (multiagente) | ~270 búsquedas y 19 agentes (4 fallaron por el límite de sesión). Resultado: 1 oportunidad condicional (Prosper AI), 1 Modelo A (Kompanion) y 9 casos de antecedentes. **0 contactos, 0 ventas** |
| 2026-10-13 | Verificación del fundador | El fundador abrió y confirmó 4 fuentes de Prosper AI (ronda, La Vanguardia, Manfred 8452 y 4815) |
| 2026-10-13 | Cambio de hipótesis | Se prueban los antecedentes de intermediación (Modelo B) y los parecidos a clientes de la agencia (Modelo C) contra el informe tradicional (A). Ver `EXPERIMENT_2.md` |

## Hipótesis a probar
| # | Hipótesis | Cómo se prueba | Criterio de éxito | Estado |
|---|---|---|---|---|
| H1 | Las boutiques tech españolas hacen prospección activa y les cuesta filtrar | 5 entrevistas | ≥3 de 5 dedican ≥3 h/semana a buscar empresas y lo describen como un problema | Pendiente |
| H2 | No tienen una herramienta que ya cubra esto en España | Pregunta 3 de la entrevista | ≥3 de 5 no usan herramienta de señales o dicen que no cubre bien España | Pendiente |
| H3 | Una muestra nuestra contiene empresas que no tenían en el radar | Muestra a ≥2 agencias | ≥1 empresa nueva y "contactable" por muestra | Pendiente |
| H4 | Pagan por eso | Oferta piloto de €150 por adelantado (antes €45) | ≥1 pago completado de 3 ofertas | Pendiente |
| H5 | Hay recurrencia | 2.ª compra o suscripción | ≥1 segunda compra en 30 días | Pendiente |
| H6 | El filtro de "equipo interno de TA" se valora | Preguntas 5-6 + reacción a los descartes | ≥2 agencias lo mencionan como útil sin que se lo sugiramos | Pendiente |
| H7 | El antecedente de intermediación (B) aumenta la intención de contacto frente a A | EXPERIMENT_2, fase ciega | B ≥ A + 15 pts en 2 de 3 agencias | Pendiente |
| H8 | Que haya un proveedor instalado no anula el interés | EXPERIMENT_2, motivos de rechazo | ≤1 de 3 agencias lo descarta por ese motivo | Pendiente |
| H9 | Hay suficiente oferta de empresas B | Conteo mensual por nicho | ≥2 nuevas por mes por nicho | Pendiente |

## Experimento 1 (REEMPLAZADO por `EXPERIMENT_2.md`; sus mensajes de 'entrevista sin oferta' quedan retirados) (4 semanas, ~3-4 h/semana)
**Semana 1**
1. Verificar el informe piloto (lista al final del informe). ~1,5 h
2. Abrir las webs de las 6 agencias de PROSPECTS.csv, completar el canal de contacto y descartar las que no encajen. ~1 h
3. Verificar el método de cobro (ver NEXT_STEPS). ~1 h
4. **Con tu autorización**, mandar el Mensaje 1/1b a 3 agencias (Kulturo, Akuaro, iTalenters).

**Semana 2**
5. Mandar el mensaje a las otras 3 y hacer los seguimientos.
6. Hacer las entrevistas que salgan; registrar respuestas textuales.
7. Ampliar la lista a 15 agencias con el ranking de Kulturo, Clutch y Connecting Hunters.

**Semana 3**
8. Mandar una muestra (1 empresa + 1 descarte) a quien la pida.
9. Mandar la oferta piloto a quien muestre interés.

**Semana 4**
10. Entregar los pilotos pagados, pedir feedback y ofrecer la versión recurrente.

## Reglas de decisión al final del experimento
- **Continuar:** ≥1 pago, o ≥3 entrevistas que confirmen H1+H2 y ≥1 pedido de muestra con reacción positiva concreta ("esta no la tenía").
- **Modificar:** las entrevistas muestran que el problema es otro (p. ej., "empresas tenemos de sobra, el problema es que respondan"). En ese caso se pivota a ese problema, sin forzar la hipótesis.
- **Abandonar este nicho:** con 15 agencias contactadas, <2 conversaciones; o ≥3 dicen que ya lo cubren con herramientas o gratis; o nadie paga €45 tras ver la muestra.
- Antes de abandonar por silencio, revisar canal y mensaje (ver criterios del documento maestro).

## Métricas a registrar
Agencias investigadas · contactos intentados · respuestas · entrevistas · muestras pedidas · ofertas enviadas · pagos · utilidad declarada · 2.ª compra · **horas por informe**.

## Cambio de prioridad (2026-10-13)
Se detiene la investigación amplia. Próxima evidencia: conversaciones con compradores (`DEMAND_VALIDATION.md`). Criterios de continuar, modificar o abandonar fijados en §4 antes de hablar con nadie.
