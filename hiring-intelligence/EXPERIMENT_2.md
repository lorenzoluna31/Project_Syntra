> **Plan activo reemplazado por `DEMAND_VALIDATION.md`** (2026-10-13). La oferta de €150 por 3 empresas se retiró porque prometía un volumen no demostrado. El diseño A/B/C queda como referencia para después de las conversaciones.

# Experimento 2: ¿valen más los antecedentes de reclutamiento externo que las alertas tradicionales?

Estado: **diseñado, no ejecutado.** No se contactó a nadie. Requiere tu autorización y antes que eso las verificaciones de `NEXT_STEPS.md`.

## Pregunta
Para una boutique tech española, ¿es más útil (y lo pagaría) un informe que prioriza empresas con **antecedente verificable de pagar intermediación** (Modelo B) o con **parecido a sus clientes históricos** (Modelo C) que un informe tradicional de expansión y contratación (Modelo A)? ¿A qué costo lo producimos?

## Hipótesis (preregistradas; no se reinterpretan después)
- **H-B1:** en el informe B, el % de empresas que la agencia "contactaría en 2 semanas" supera al de A en al menos 15 puntos, en al menos 2 de 3 agencias.
- **H-B2:** a la mayoría (2 de 3) de las agencias no les quita interés que la empresa ya use otro intermediario, siempre que el perfil o el volumen sean distintos.
- **H-B3:** producir una empresa B verificada no cuesta más de 1,5 veces lo que cuesta una A.
- **H-B4:** hay al menos 2 empresas B nuevas por mes en el nicho de cada agencia.
- **H-pago:** al menos 1 de 3 agencias paga el piloto (100% por adelantado) después de ver la muestra.

## Los tres compradores y qué información tendría valor para cada uno

| Agencia | Qué hace (fuente) | Información específica que le probaríamos | Por qué no es una lista genérica |
|---|---|---|---|
| **Kulturo** (Barcelona) | Headhunting de IA: ML, NLP, visión, LLM/agentes; talento fraccional para startups stealth; cobro a éxito; caso Murphy AI, de las primeras contrataciones a más de 20 personas ([kulturo.tech/programadores-ia](https://www.kulturo.tech/programadores-ia)) | **C:** startups de IA en Barcelona en la fase en que estaba Murphy AI (ronda reciente, menos de 20 personas, primeras contrataciones de IA). Ej.: Kompanion (de 2 a ~8 ingenieros para abril de 2027). **B:** Prosper AI (hub de IA en BCN, Manfred solo en roles de producto, Senior AI Engineer abierto) | Parte de su propio caso de éxito y de sus perfiles de IA. Separa los roles que ya lleva otro intermediario |
| **iTalenters** (Barcelona/Madrid; fundada en 2021) | Desarrollo, datos/IA, cloud, ciberseguridad, SAP, CTO/CIO; éxito, **RPO** y "Sourcing Service"; primeros candidatos en 7 días ([italenters.com](https://www.italenters.com/en/headhunting-it/)) | **B:** empresas con **oleadas** de contratación post-ronda que ya pagaron intermediación por procesos sueltos: candidatas a un RPO. Ej.: Prosper AI (~30 incorporaciones previstas en 6 meses), patrón Tucuvi (3 procesos al mes siguiente de la Serie A) | Apunta a su producto de mayor ticket (RPO), no a vacantes sueltas |
| **Akuaro** (Barcelona; datos solo de directorios) | IT, digital, producto y datos; Europa y LatAm; RPO, **market research y benchmarking salarial** ([herohunt](https://www.herohunt.ai/recruitment-agencies/akuaro/), [village.ai](https://village.ai/company/akuaro)) | **Benchmark de mercado** a partir de procesos intermediados con salario publicado (Prosper: hasta 85K + 10K; Tucuvi: 55-70K + variable; Valsea: 50-65K; Flexcompute: 100-120K), cruzado con qué empresas contratan qué perfiles | Complementa su línea de market research. *Riesgo: puede vernos como competencia.* |

**Advertencia:** los perfiles de iTalenters y Kulturo se leyeron en sus webs vía buscador; el de Akuaro, solo en directorios. Hay que confirmarlos antes de contactar.

## Diseño
1. **Preparación (sin contacto):** para cada agencia armamos 3 informes mini de 3 empresas cada uno, con el mismo formato y el mismo período (últimos 60 días) y su ciudad y especialidad:
   - **A (tradicional):** ronda o expansión + vacantes técnicas, sin filtro de antecedentes. Generado por regla mecánica (no elegido por nosotros, para no fabricar un rival débil).
   - **B (antecedentes):** A + antecedente verificable de pagar intermediación + descarte por TA interno + qué procesos ya lleva otro intermediario y desde cuándo.
   - **C (solo para Kulturo):** empresas parecidas a su caso Murphy AI.
2. **Registro del costo:** horas por empresa verificada en cada tipo (cronometrado).
3. **Fase ciega:** la agencia recibe las 6-9 fichas mezcladas, rotuladas X/Y/Z, con datos mínimos. Por cada empresa marca:
   - ¿ya la conocía?
   - ¿la contactaría en 2 semanas?
   - ¿sabe si usa otra agencia?
   - encaje de 1 a 5.
4. **Fase abierta:** se muestra el análisis completo y se repite la pregunta de contacto.
5. **Prueba de pago:** se ofrece el piloto pago del formato que la agencia prefiera. **Solo un pago cuenta como disposición a pagar.**
6. **Seguimiento a 30-60 días:** qué empresas contactó, si respondieron y el motivo de cada rechazo ("tenemos proveedor", "no usamos agencias", "no contratamos").

**Tamaño:** 3 agencias × 6-9 empresas. Es **direccional**, no estadístico. Se reportan conteos crudos.

## Criterios para descartar el enfoque de antecedentes (B)
Se abandona B, y queda A o se pivota, si se cumple **cualquiera** de estos:
1. B no supera a A en "contactaría" en al menos 2 de 3 agencias.
2. Al menos 2 agencias dicen "eso ya lo miro yo en Manfred" o "si ya tienen proveedor, no me interesa".
3. Una empresa B verificada cuesta más de 1,5 veces una A, o más de 3 h.
4. Encontramos menos de 2 empresas B nuevas por mes en el nicho de una agencia, lo que no alcanza para un servicio recurrente.
5. Ninguna de las 3 agencias paga el piloto tras ver la muestra. En ese caso se reevalúa todo el negocio, no solo B.

Se **continúa** con B si se cumplen H-B1 y H-pago (al menos 1 pago).

## Oferta piloto (reemplaza la de €45 a posteriori)
- **Entregable:** 3 empresas que cumplan **todos** estos criterios objetivos, más 2-3 descartes razonados. Entrega en 5 días hábiles.
  1. Evento disparador fechado en los últimos 60 días, con URL.
  2. Al menos 1 vacante técnica de su especialidad verificada en el ATS o web de la empresa, con URL y fecha de comprobación (o una declaración pública de contratación con cifras).
  3. Sin vacantes de TA o recruiter interno visibles en la fecha de comprobación.
  4. La empresa no está en la **lista de exclusión** que envía la agencia (clientes y empresas que ya conoce). Esto vuelve objetivo el criterio "nueva para la agencia".
  5. Cada afirmación etiquetada como hecho, inferencia o duda.
  6. (Versión B) Antecedente de intermediación, con URL y fecha, y el estado conocido de ese proceso.
- **Garantía:** si una empresa no cumple un criterio verificable, se repone en 3 días hábiles. "No me interesa" **no** da derecho a reposición.
- **Precio piloto: €150, 100% por adelantado** (justificación en `BUSINESS_MODEL.md`).
- **No incluye:** datos de contacto personales, garantía de que la empresa contrate agencias, ni exclusividad sobre hechos públicos.

## Lo que hace falta antes de ejecutarlo
Ver `NEXT_STEPS.md` → "Acciones del fundador".
