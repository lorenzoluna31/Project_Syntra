# Dos propuestas para agencias argentinas y comparación de valor y costo

**Ambos modelos son EXPERIMENTALES.** Los precios (USD 90 por oportunidad, USD 150 por 3 fichas) son hipótesis calculadas desde el costo: no hay compradores, ni recompras, ni ventaja competitiva comprobada. En las conversaciones se investiga cuánto les cuesta hoy el problema y qué usan para resolverlo. No se cambian los precios por intuición ni se trabaja gratis.

**No elegimos ganador antes de hablar con compradores.** Los precios son **hipótesis para probar**, calculados desde el costo. No sabemos cuánto pagan las agencias argentinas: **no hay ninguna evidencia de disposición a pagar**.

## Modelo A: Descubrimiento de oportunidades
**Qué recibe la agencia:** empresas que **no** nos indicó, con señales verificables de que van a contratar perfiles de su especialidad y antecedentes de usar intermediarios, más los descartes razonados.
- **Alcance:** 1 nicho definido por la agencia (p. ej. "devs y datos para empresas de EE. UU. que contratan en LatAm" o "IT en Argentina"). Hasta **8 horas** de investigación en 7 días hábiles. Entregamos **todas** las empresas que cumplan los criterios, entre 0 y 3.
- **Criterios objetivos:**
  1. Evento fechado en los últimos 90 días, con URL.
  2. Vacante del nicho comprobada, con URL y fecha.
  3. Sin TA interno visible.
  4. No figura en la lista de exclusión que la agencia nos manda antes de empezar.
  5. Hechos, inferencias y dudas separados.
- **Precio a probar:** **USD 90 por empresa que cumple los criterios** (o su equivalente en ARS), con un máximo de USD 270.
- **Pago:** anticipo de USD 90, que se devuelve completo si entregamos 0 empresas.
- **Diferencial posible:** información que la agencia no tiene.
- **Riesgo:** ya vimos que cuesta mucho producirla. De cada ~10 candidatas, 1 resulta utilizable.

## Modelo B: Investigación de cuentas que elige la agencia
**Qué recibe la agencia:** una ficha de una página (formato `../kit/DEMO_1PAGE.md`) por cada empresa que **ella** elige.
- **Alcance:** 3 empresas, entregadas en 5 días hábiles.
- **Contenido de la ficha:** financiación y expansión, vacantes técnicas abiertas, tecnologías que piden, indicios de TA interno, intermediarios con evidencia pública y plan de contratación declarado. Cada campo con fuente y fecha, o con la marca "no encontrado".
- **Precio a probar:** **USD 50 por ficha, USD 150 las tres**, 100% al encargar.
- **Devolución:** si una ficha no se entrega a tiempo o tiene un dato falso a la fecha indicada, se corrige o se devuelven USD 50.
- **Diferencial posible:** ahorro de tiempo y la verificación de intermediarios y TA.
- **Riesgo:** es lo más fácil de reemplazar con ChatGPT o Perplexity con búsqueda web y LinkedIn.

## Costos y precio mínimo (estimaciones; se cronometran en el primer piloto)
| Concepto | A (por oportunidad) | B (por ficha) |
|---|---|---|
| Producción, con el descarte incluido | ~3 h (yield ~1 de cada 10 candidatas) | ~1,5 h |
| Revisión y soporte | ~0,5 h | ~0,25 h |
| **Subtotal** | **~3,5 h** | **~1,75 h** |
| Adquisición por cliente pagador (contactos, llamadas, propuesta) | ~10 h (**supuesto**: nunca adquirimos un cliente) | ~10 h (idem) |

**Precio mínimo según la tarifa horaria objetivo, por paquete de 3:**
| Tarifa objetivo | A, 1 sola compra (20,5 h) | A, 4 recompras (~4,3 h/opp) | B, 1 sola compra (15,25 h) | B, 4 recompras (~2,6 h/ficha) |
|---|---|---|---|---|
| USD 10/h | USD 68/opp | USD 43/opp | USD 51/ficha | USD 26/ficha |
| USD 15/h | USD 103/opp | USD 65/opp | USD 76/ficha | USD 39/ficha |
| USD 25/h | USD 171/opp | USD 108/opp | USD 127/ficha | USD 65/ficha |

**Lectura:**
- Sin recompra, ningún modelo es rentable a precios plausibles. **La recompra es la condición del negocio**, no un extra.
- B es más barato de producir, pero su techo de precio lo marca lo que la agencia puede hacer sola con ChatGPT y LinkedIn en ~20 minutos. **Si eso da algo parecido, B vale cerca de cero.**
- A tiene más diferencial potencial, pero cuesta el doble y su volumen es incierto.
- **Meta de USD 1.000/mes:**
  - A USD 90/opp: ~11 oportunidades al mes, ~40 h.
  - B USD 50/ficha: 20 fichas al mes, ~35 h, y además ~7 clientes recurrentes.

  En ambos casos es medio tiempo dedicado a servicios. **Solo escala si una parte importante se automatiza**, y eso no lo probamos.

## Comparación con IA generalista
Ver `AI_BASELINE_COMPARISON.md`, la prueba hecha con un asistente nuevo, sin contexto, con el mismo objetivo y un tope de búsquedas comparable.
