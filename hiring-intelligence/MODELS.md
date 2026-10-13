# Modelos comerciales: oportunidades nuevas vs. antecedentes de reclutamiento externo

Fecha: 2026-10-13. Base: 8 casos en `CASES_EXTERNAL_RECRUITING.csv`, verificaciones en `VERIFICATION_STATUS.md` y 8 búsquedas decisivas de esta ronda. **Nada de esto está validado con compradores.**

## 1. Qué descubrimos realmente

1. **Manfred publica sus procesos con el nombre del cliente, el salario y un estado datable.** Es una consultora española de selección tech que cobra a la empresa el 15% del bruto anual, solo a éxito ([companies-form](https://www.getmanfred.com/en/companies-form)). Cada oferta "gestionada por Manfred" es, por tanto, evidencia pública de que **esa empresa contrató un servicio de intermediación de pago para ese proceso**. No prueba que haya pagado una comisión: el pago depende de que la contratación se cierre.
2. La exclusividad de Manfred es **por proceso y temporal (mínimo un mes)**. Manfred dice que, pasado ese mes sin candidato, entiende que la empresa pruebe otras opciones ([contrato v9](https://www.getmanfred.com/en/blog/nuestro-contrato-v9)). No es un proveedor exclusivo de la empresa.
3. **Apuntar a empresas que ya usan agencias es una práctica de BD conocida.**
   - Bullhorn lo recomienda: "a company that used a rival agency is already open to agency work".
   - Hay guías para descubrir los clientes ocultos de agencias competidoras (Liveforce, WizardSourcer).
   - Arca24, hoy parte de TeamSystem, vende **JobRadar**, que rastrea las ofertas que publican agencias competidoras. No sabemos su cobertura en España.

   **Conclusión: la idea no es nueva.**
4. Lo específico de España: la mayoría de agencias anonimizan al cliente ("importante empresa del sector"; es un supuesto sin medir). Manfred es una excepción visible. Pero **cualquier agencia tech española conoce Manfred** (es competidor directo) y puede revisar sus ofertas públicas gratis en minutos.

## 2. Tipos de relación con un intermediario (cómo clasificarlas sin inventar)
| Tipo | Evidencia que lo prueba | Cómo leerlo |
|---|---|---|
| **Proceso puntual** | 1 oferta gestionada | Disposición a pagar intermediación al menos una vez |
| **Cuenta recurrente** | 2 o más procesos (p. ej. Prosper 2024+2026, Valsea 4 en 3 meses) | Presupuesto habitual para intermediación. **Hay proveedor instalado** |
| **Histórico** | Último proceso hace más de 12 meses o la empresa internalizó TA (Aily Labs 2022) | Valor bajo: puede haber cambiado de modelo |
| **Proceso vigente con exclusividad** | Oferta abierta con menos de 1 mes | **No tocar ese puesto.** Competir ahí no es ético ni útil |
| **Proceso vigente sin exclusividad efectiva** | Oferta abierta más de 1 mes, o el mismo puesto en el ATS propio (Prosper) | Puede caber un segundo proveedor, pero solo con perfiles diferenciales |
| **Desconocido** | Lo que no se ve: contratos, PSL, acuerdos marco | Siempre "desconocido", nunca "sin proveedor" |

**Regla de redacción:** "Hay evidencia pública de que [empresa] usó un intermediario de pago para [puesto] en [fecha]". **Nunca** "trabaja con" ni "su proveedor es".

## 3. Comparación de modelos

| Criterio | A. Oportunidades nuevas (expansión sin antecedentes visibles) | B. Antecedentes de intermediario + necesidad nueva | C. "Lookalikes" de clientes históricos |
|---|---|---|---|
| Evidencia de disposición a pagar intermediación | Ninguna | **Sí, atribuible** (por proceso) | Indirecta (por parecido) |
| Competencia con un proveedor instalado | Baja o desconocida | **Alta** (Manfred u otro) | Baja |
| ¿La agencia lo puede obtener sola y gratis? | Sí (prensa de rondas, LinkedIn) | **Sí** (getmanfred.com es público) | Más difícil: requiere armar perfiles y buscar |
| ¿Lo ofrecen las herramientas? | Sí (Recruit Signals, Hirelytiq: rondas y expansión) | En parte (JobRadar rastrea ofertas de competidores; cobertura en España desconocida) | No encontramos producto |
| Volumen semanal estimado (BCN/MAD, software/IA, startups) | ~1-3 por mes con encaje (unas 30 rondas al mes en España, la mayoría sin encaje; **estimación**) | Bajo: los IDs de Manfred avanzan unos 200 en 7 meses (~7 ofertas por semana en toda España). Con filtro + necesidad nueva: ~0-2 por mes (**estimación**) | Depende del perfil; se puede ampliar |
| Precisión alcanzable | Media (necesidad sí, apertura desconocida) | **Alta en el antecedente**, baja en la vigencia del proceso | Baja hasta tener más de 30 casos |
| Riesgo de mala experiencia para el comprador | "No trabajamos con agencias" | "Ya tenemos proveedor" | "No se parecen tanto" |
| Mejor uso | Entrada temprana (Kompanion) | **Priorizar** dentro de A; argumento de venta ("ya pagaron por esto") | Escalar el descubrimiento si B demuestra valor |

**Veredicto honesto:**
- **B no es superior por tener más señales.** Mejora la *probabilidad de que la empresa pague a agencias*, pero empeora la *probabilidad de que necesite una nueva*, y su información es gratuita para el comprador.
- **A** por sí solo es un commodity.
- La combinación defendible, si existe, es **"A priorizado por la evidencia de B, con descarte por TA interno y con fechas"**:
  - empresas en expansión reciente;
  - con antecedente datable de pagar intermediación (o con el perfil de quienes lo hacen);
  - sin TA interno visible;
  - con perfiles que el proveedor instalado no está cubriendo (o procesos de más de 1 mes).

  Ninguna herramienta revisada declara esa combinación (evidencia débil).
- **C** es la idea más interesante a medio plazo, pero con 8 casos es anecdótica.
  - Patrón observado en 3 de 8 casos (Prosper, Tucuvi, InteractiveAI): **startup de IA aplicada, con Serie A reciente, que contrata ingenieros de producto o FDE**.
  - Para Tucuvi, el patrón "Serie A → oleada técnica intermediada al mes siguiente" es solo una inferencia de fechas.

## 4. Respuestas a las preguntas de validación

| Pregunta | Respuesta con lo que sabemos | Confianza |
|---|---|---|
| ¿Las boutiques necesitan saber qué empresas usan recruiters externos? | La industria lo considera útil (Bullhorn, guías de BD). **Ninguna boutique española lo confirmó.** | Baja (sin entrevistas) |
| ¿Sus herramientas ya lo dan? | Parcialmente: JobRadar rastrea ofertas de competidores; Manfred es público y gratis. No encontramos un producto que diga "usa agencias". | Media-baja |
| ¿Podemos producirlo con precisión? | El antecedente, sí (Manfred: cliente nombrado, fecha de cierre). La vigencia del proceso y la contratación final, no. La cobertura se limita a intermediarios que nombran al cliente (Manfred y quizá Talent Hackers, aún sin fechas). | Media |
| ¿Sirve si ya hay proveedor? | Solo si: (a) el proceso tiene más de 1 mes o se reabrió; (b) el volumen supera a un proveedor (Prosper: unas 30 incorporaciones previstas en 6 meses); (c) el perfil es de nicho o de liderazgo. Si no, es una mala oportunidad. | Media (inferido) |
| ¿Costo por oportunidad verificada? | **Medido:** las rondas 2 y 3 gastaron ~270 búsquedas, ~1,4M de tokens de subagentes y 19 agentes para obtener **1 oportunidad con mérito de aproximación (condicional)**, 1 candidata del Modelo A y 8 casos de referencia. Sin acceso web directo, el costo es desproporcionado. **Estimación con navegador:** 1,5-3 h por oportunidad verificada (verificar Prosper llevó 22 búsquedas, unos 60-90 min humanos). | Media |
| ¿Hay información nueva cada semana? | Para una agencia y especialidad: **no semanal**. Estimamos 1-3 oportunidades de calidad por mes. La cadencia realista es quincenal o mensual. | Baja-media (estimación) |
| ¿Qué agencia se beneficia más? | Boutiques especializadas en lo que Manfred cubre peor: IA/ML senior, liderazgo técnico (Head of Eng, Director of Product), stacks de nicho; y las que pueden ser "segundo proveedor" en oleadas grandes. **Inferido.** | Baja |
| ¿Disposición de pago? | **Sin evidencia.** No atribuimos ninguna. | — |

## 5. Implicación para el negocio
- No encontramos una **ventaja competitiva demostrada**. Encontramos **una hipótesis de producto más precisa y comprobable**, y una manera barata de refutarla: el experimento de `EXPERIMENT_2.md`.
- Si las agencias dicen "eso ya lo miro en Manfred" o "si ya tienen proveedor no me interesa", la ventaja de B cae, y el producto vuelve a ser investigación manual (A).
- Riesgo ético y comercial: vender a agencias "los clientes de Manfred" puede verse como prácticas agresivas. Hay que presentarlo como **señal de madurez de compra** sobre empresas con necesidad nueva, no como lista de clientes ajenos para robar.
