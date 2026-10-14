# Prueba comercial en Argentina: plan, medición y decisión

## Corrección (2026-10-14): tamaño del mercado
La conclusión anterior ("si después de verificar quedan menos de 10 agencias contactables, el mercado es chico") **estaba mal planteada y se retira**. Que 12 búsquedas encuentren pocas agencias mide **nuestro método de descubrimiento**, no el mercado.

RevenueBase (actualizado en septiembre de 2026) clasifica **514 empresas** como *IT recruitment firms* ([fuente](https://revenuebase.ai/companies/it-recruitment-firms/argentina)) y **317** como *IT staffing agencies* ([fuente](https://revenuebase.ai/companies/it-staffing-agencies/argentina)) en Argentina. Hay que leer estas cifras con cuidado:
- no son un conteo verificado de boutiques;
- las categorías se solapan;
- incluyen errores de clasificación (p. ej. consultoras de software);
- no se suman.

**Conclusión correcta:** hay probablemente decenas o cientos de candidatas. El cuello de botella es verificarlas a mano (web, actividad y canal). No sabemos todavía si el mercado alcanza en tamaño **útil** (agencias que paguen).

## Estado de la lista (2026-10-14)
`AGENCIES_AR.csv` tiene 7 agencias:
- **2 listas para contactar** cuando se resuelva lo legal: **HR Oasis** (mixta: local + clientes internacionales) y **BEON.tech** (internacional).
- **1 con actividad pero sin canal verificado:** Solutix.
- **4 por verificar o de reserva:** Nexton, Duhire, Bandit y Wall Chase.

La reserva sin verificar está en `EXCLUDED_OR_RESERVE_AR.csv`. **No llegué a 10 agencias verificadas en 12 búsquedas**, y no completé la lista a la fuerza. Para llegar a 10 hace falta abrir manualmente 10-15 webs de la reserva (~1 h con navegador) o habilitar el acceso web.

## Plan (2 semanas; nada se ejecuta sin tu autorización)
| Paso | Qué | Quién | Tiempo |
|---|---|---|---|
| 0 | Revisar este paquete y autorizar o corregir destinatarios, textos y base legal | Vos | 30 min |
| 1 | **Prueba ChatGPT** (`OFFERS_AR.md`) y registrarla en el tracker | Vos | 20 min |
| 2 | Abrir la web de las 7 agencias + 10 de la reserva: confirmar especialidad, actividad 2026 y el canal corporativo publicado (con su URL). Objetivo: 10 verificadas | Vos (o yo, con acceso web habilitado) | 1-1,5 h |
| 3 | Resolver los pendientes legales ⚠ de `LEGAL_AR.md`: consulta sobre la inscripción de la base y, si corresponde, inscribirla. Armar el pie con el texto literal | Vos (con asesoramiento) | variable |
| 4 | Enviar en 3 tandas de 5-6 emails personalizados (días 3, 4 y 5), desde tu email | Vos | 1,5 h |
| 5 | Responder y agendar las llamadas en 24 h | Vos | — |
| 6 | Un único seguimiento (días 9-10) | Vos | 30 min |
| 7 | Llamadas de 15 min con el guion y registro inmediato en el tracker | Vos | 30 min por llamada |
| 8 | Día 14: diagnóstico y decisión | Juntos | 1 h |

**En paralelo (opcional, sin costo):** la publicación de LinkedIn (`../kit/LINKEDIN_POST.md`), adaptada a Argentina.

## Qué se registra (`TRACKER_AR.csv`)
Contactos legítimos · respuestas · bajas · conversaciones · problemas mencionados espontáneamente (textual) · herramientas · qué tercerizan y cuánto gastan · respuesta a "¿por qué no ChatGPT?" · preferencia A/B/ninguno · pedidos de presupuesto · compras y monto · objeciones.

**No se calculan tasas sobre muestras tan chicas.** Se reportan conteos crudos.

## Diagnóstico si no hay ventas
| Síntoma | Qué falló | Qué hacemos |
|---|---|---|
| Menos de 2 respuestas de ~15 envíos | **Canal o mensaje** (o emails que nadie lee) | Cambiar asunto y ángulo en una segunda tanda; probar LinkedIn o eventos presenciales en Buenos Aires. **No concluir sobre el mercado** |
| Responden, pero no quieren hablar | **Oferta poco clara o poco relevante** | Pedir el motivo en una línea; ajustar |
| Hablan y no reconocen el problema ("tenemos más clientes de los que podemos atender", "el cuello de botella son los candidatos") | **Propuesta de valor equivocada** | Registrar el problema que sí nombran. Si 2 o más coinciden, evaluar pivotar hacia ese problema (alternativa C) |
| Reconocen el problema, pero "lo hago con ChatGPT o LinkedIn" | **Falta de diferenciación** | B descartado. A solo sigue si alguien valora el descubrimiento |
| Reconocen el problema y lo valoran, pero no pagan el precio | **Precio o mercado** (presupuesto argentino) | Comparar lo que pagarían con el piso de `OFFERS_AR.md`. Si están por debajo de USD 10/h, el mercado no alcanza |
| Pocas agencias contactables tras verificar | **Método de descubrimiento**, no necesariamente el mercado | Verificar más de la reserva (514/317 en directorios) antes de concluir algo sobre el mercado |

## Regla de decisión al día 14
- **Avanzar:** al menos 3 conversaciones; al menos 2 nombran espontáneamente el mismo problema; al menos 1 pide presupuesto o paga; y la respuesta a "¿por qué no ChatGPT?" deja un diferencial concreto.
- **Cambiar radicalmente:** hay conversaciones, pero el problema que aparece es otro, o nadie paga por encima del piso de costo.
- **Abandonar Hiring Intelligence:** con el canal funcionando (respuestas y conversaciones), las agencias no reconocen un problema pagable, o lo resuelven solas. En ese caso reutilizamos el método (validar la demanda primero) para la próxima idea.
- **Si falla el canal** (menos de 2 respuestas): una segunda tanda con otro ángulo antes de concluir. **Como máximo 1 iteración extra.**
