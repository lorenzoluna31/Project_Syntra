# Próximos pasos

> **2026-10-13: el plan activo y la lista de autorizaciones están en `DEMAND_VALIDATION.md` §8.** Lo de abajo queda como contexto. Las verificaciones 1 y 5 de Prosper ya las hizo el fundador. No se hace más investigación amplia.

Actualizado: 2026-10-13 (después de las rondas 2 y 3).

## Decisión de esta etapa
**No lanzar más investigación amplia.** Lo que falta para decidir son **5 verificaciones decisivas** y **autorizaciones tuyas**, no más búsquedas.

## Acciones del fundador (requieren tu intervención)

### Verificaciones decisivas (unos 60-90 min en total, con navegador)
1. **Prosper AI:** abrí [jobs.ashbyhq.com/prosper-ai](https://jobs.ashbyhq.com/prosper-ai) y anotá qué vacantes técnicas de Barcelona siguen publicadas hoy. Abrí la [oferta 8452 de Manfred](https://www.getmanfred.com/ofertas-empleo/8452/prosper-senior-product-engineer-ago26) y fijate si dice "Oferta cerrada el…". *Esto decide si Prosper es aproximable.*
2. **Prosper AI (LinkedIn, manual):** ¿hay alguien con cargo de Talent, Recruiter o People en Barcelona contratado después de junio de 2026? *Decide si el hub ya tiene TA.*
3. **Kompanion:** abrí la [nota de El Nacional](https://www.elnacional.cat/oneconomia/ca/empreses/kompanion-plataforma-emprenedors-aspira-ser-stripe-atlas-espanya_1704538_102.html) y confirmá la cita "de dos a unos ocho perfiles de ingeniería" y la fecha.
4. **Cobro:** intentá registrarte en **Payoneer** (y en Wise) como residente argentino y fijate si te ofrecen **datos de cuenta en EUR con IBAN** y qué comisión muestran. Consultá con un contador si tu situación (¿monotributo?) permite emitir **Factura E** por exportación de servicios y qué regla de liquidación de divisas aplica hoy. *Sin esto no se puede cobrar el piloto.*
5. **Manfred (2 minutos):** mirá cualquier oferta de getmanfred.com y confirmá si todas dicen "Oferta gestionada por: Manfred" o si existen ofertas publicadas directamente por empresas. *Decide si la señal es "proceso intermediado" o "anuncio en un portal".*

### Configuración (opcional pero recomendada)
6. Habilitar acceso web con la lista de `NETWORK_SETUP.md` (Custom). Agregar `getmanfred.com` y `jobs.ashbyhq.com`, ya incluidos en la lista.
7. El buscador tiene un límite de **200 búsquedas por turno**, compartidas entre todos los agentes. El propio buscador menciona la variable `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`. No la toques si no hace falta: la idea ahora es buscar menos, no más.

### Autorizaciones (no se hace nada sin tu sí)
8. Canal 1 (referidos): ¿a quién de tu red podés pedirle una presentación con una boutique tech española?
9. Canal 2: ¿autorizás publicar en tu LinkedIn la nota de "Señales de contratación tech" (`outreach/MESSAGES.md`), revisada por vos?
10. Consulta legal breve, opcional pero recomendable antes de escalar: LinkedIn y formularios como "medio equivalente" (LSSI art. 21) y llamadas a centralitas de empresa (LGTel art. 66).

## Lo que hago yo cuando vuelvas
- Con los resultados de 1-3: cerrar la ficha final de Prosper y Kompanion y preparar la **muestra de 1 empresa** para el Canal 1/2.
- Armar los informes A/B/C del `EXPERIMENT_2.md` para las 3 agencias (con red habilitada: 3-5 h de trabajo; sin red, mucho más lento).
- Si se habilita la red: correr `tools/ats_snapshot.py` sobre Prosper (Ashby), JetBrains (Greenhouse) y Aily Labs (Personio) para tener las primeras fotos fechadas.

## Riesgos, por capacidad de matar el negocio
1. **Sin disposición a pagar.** Se prueba con el piloto pago.
2. **La señal B la obtiene la agencia gratis** (Manfred es público) **y JobRadar rastrea ofertas de competidores.** Puede no haber valor añadido.
3. **Proveedor instalado:** las empresas B ya tienen intermediario y la boutique compite con él.
4. **Volumen insuficiente:** 1-3 oportunidades de calidad por mes por nicho; quizá no alcance para un servicio recurrente.
5. **Adquisición lenta:** sin email en frío, dependemos de referidos y contenido.
6. **Cobro desde Argentina:** no verificado.
7. **Costo de producción** sin acceso web directo: desproporcionado.
8. **Riesgo ético y reputacional:** que se perciba como "lista de clientes de un competidor". Mitigación: presentarlo como señal de madurez de compra, con necesidad nueva.
