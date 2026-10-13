# Acceso web para la verificación: qué cambiar y qué implica

## Situación (comprobada el 2026-10-13)
- `curl`, `WebFetch` y `tools/ats_snapshot.py` fallan con `CONNECT tunnel failed, response 403` o `ENOTFOUND` contra cualquier dominio que no sea un registro de paquetes o GitHub. Probados: kulturo.tech, mirairisktech.com, elreferente.es, boards-api.greenhouse.io, api.lever.co, mirai.jobs.personio.com, ailylabs.jobs.personio.com, wise.com, bcra.gob.ar, afip.gob.ar.
- Solo funciona el buscador (`WebSearch`), que devuelve un resumen de las páginas, no la página. **No sirve como verificación de un informe que se vende como "verificado".**

## Qué tenés que cambiar (configuración oficial de Claude Code en la nube)
Documentación: <https://code.claude.com/docs/en/cloud-environments>, sección *Network access*.

1. En la sesión, abrí el menú del entorno en la barra de título → **Edit**. También se puede desde la lista de entornos en claude.ai/code.
2. En **Network access** elegí **Custom**. En apps viejas la opción puede llamarse *Limited* y mostrar el campo *Allowed domains*.
3. Marcá la casilla para **incluir la lista por defecto de gestores de paquetes**. Sin ella, `pip` y `git` dejan de funcionar.
4. Pegá los dominios de abajo en **Allowed domains**, uno por línea. Un `*.` inicial habilita todos los subdominios. Agrego también el dominio raíz por si el comodín no lo cubre.
5. Guardá. Según la documentación, las sesiones existentes toman el cambio **en un minuto, sin reiniciar**. Avisame y lo pruebo con `tools/ats_snapshot.py`.

### Lista mínima propuesta

```
# Fuentes de rondas y expansión (prensa)
elreferente.es
*.elreferente.es
ecosistemastartup.com
cincodias.elpais.com
elespanol.com
*.elespanol.com
eleconomista.es
*.eleconomista.es
expansion.com
*.expansion.com
seedtable.com
*.seedtable.com
webcapitalriesgo.com
*.webcapitalriesgo.com

# APIs y páginas públicas de empleo (vacantes verificables)
boards-api.greenhouse.io
job-boards.greenhouse.io
job-boards.eu.greenhouse.io
boards.greenhouse.io
api.lever.co
jobs.lever.co
api.eu.lever.co
jobs.eu.lever.co
api.ashbyhq.com
jobs.ashbyhq.com
apply.workable.com
*.jobs.personio.de
*.jobs.personio.com
*.teamtailor.com
*.factorialhr.com
welcometothejungle.com
*.welcometothejungle.com
getmanfred.com
*.getmanfred.com

# Agencias y directorios de agencias
kulturo.tech
*.kulturo.tech
italenters.com
*.italenters.com
clutch.co
*.clutch.co
goodfirms.co
*.goodfirms.co
sortlist.es
*.sortlist.es

# Empresas investigadas (se agregan caso a caso)
mirairisktech.com
*.mirairisktech.com
ailylabs.com
*.ailylabs.com

# Fuentes oficiales: cobros, impuestos y normativa
wise.com
*.wise.com
payoneer.com
*.payoneer.com
stripe.com
*.stripe.com
paypal.com
*.paypal.com
bcra.gob.ar
*.bcra.gob.ar
afip.gob.ar
*.afip.gob.ar
arca.gob.ar
*.arca.gob.ar
boletinoficial.gob.ar
*.boletinoficial.gob.ar
boe.es
*.boe.es
aepd.es
*.aepd.es
agenciatributaria.gob.es
*.agenciatributaria.gob.es
contrataciondelestado.es
*.contrataciondelestado.es
```

Los dominios de las agencias y empresas nuevas que surjan de esta ronda de investigación están en `RESEARCH.md` → "Dominios a agregar".

## Qué permisos implica
- **Custom (recomendado):** Claude puede hacer peticiones HTTP solo a esos dominios (más los de paquetes y GitHub). Riesgo acotado: una página maliciosa de esos dominios podría intentar inyectar instrucciones, pero Claude no podría enviar datos a dominios fuera de la lista. El repositorio no tiene secretos.
- **Costo práctico:** cada empresa nueva que investiguemos necesita que agregues su dominio. Para la fase de verificación de 3-5 empresas es manejable.
- **Full (alternativa, no recomendada por defecto):** cualquier dominio. Es más cómodo para descubrir empresas nuevas, pero amplía la superficie de exfiltración. Si la usás, que sea temporal (una sesión de investigación) y después volvé a Custom.
- **LinkedIn: no lo agregues.** Su acuerdo de usuario prohíbe el acceso automatizado. La revisión de LinkedIn queda manual y a tu cargo.

## Qué voy a verificar en cuanto haya acceso
1. Cada URL citada en `reports/` y `OPPORTUNITIES.csv`: que exista, que la fecha y el texto coincidan, y guardar la fecha de acceso.
2. Vacantes vivas por API (Personio, Greenhouse, Lever, Ashby, Workable) con `tools/ats_snapshot.py`. Las fotos fechadas quedan en `data/ats_snapshots.sqlite` y permiten detectar republicaciones con el tiempo.
3. Páginas oficiales de Wise, Payoneer, BCRA y ARCA para el método de cobro.

## Otros límites observados (2026-10-13)
- **WebSearch:** máximo de **200 búsquedas por turno**, compartidas entre todos los agentes. El mensaje de error menciona la variable `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`. No es un problema de red: es un tope de uso.
- **Límite de sesión de la cuenta:** en la ronda 3, 4 agentes fallaron con "You've hit your session limit".
- **Dominios que el buscador no lee:** lavanguardia.com, expansion.com, elconfidencial.com, elperiodico.com, europapress.es, economiadigital.es. Con acceso web directo (Custom) se podrían abrir; agregarlos a la lista si hacen falta.
- Agregar también: `getprosper.ai`, `tucuvi.com`, `kompanion.es`, `elnacional.cat`, `tech.eu`, `beckershospitalreview.com`, `capital-riesgo.es`, `talenthackers.net`, `arca24.com`.
