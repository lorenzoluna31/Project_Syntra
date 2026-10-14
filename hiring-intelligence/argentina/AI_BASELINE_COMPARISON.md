# Comparación: nuestra ficha frente a una IA generalista con búsqueda web

**Fecha:** 2026-10-14.
**Método:** un asistente nuevo, sin acceso al repositorio ni a nuestras conclusiones, recibió el mismo objetivo: una ficha comercial de Prosper AI para una agencia de Barcelona, con los mismos 7 puntos. Tuvo un tope de **15 búsquedas**. Usó 14, en unos **12-15 minutos**, sin intervención humana.

**Limitaciones de la prueba:**
- El asistente es de la **misma familia de modelos** que usamos nosotros, con la misma herramienta de búsqueda. Mide "IA generalista con búsqueda", no ChatGPT en particular.
- Una sola empresa: **n = 1**.
- Nuestra ficha contó con verificación manual del fundador, la suya no.

## Resultado por criterio
| Criterio | IA generalista (14 búsquedas, ~15 min, 0 h humanas) | Nuestra ficha (`../kit/DEMO_1PAGE.md`: ~22 búsquedas + rondas previas + ~30 min de verificación del fundador) | Quién gana |
|---|---|---|---|
| **Exactitud de los datos** | Ronda, fecha, inversores, inversión en Barcelona y plan de 30 a 60 personas: correctos y coherentes con nuestras fuentes verificadas | Correctos, con 4 fuentes verificadas por un humano | Empate en los hechos básicos |
| **Cobertura de fuentes** | Más amplia: tech.eu, Fierce Healthcare, raising.fi, iymagazine, PitchBook y los portales de talento de a16z y Emergence | Menos fuentes, pero primarias y verificadas | **IA** en amplitud |
| **Vigencia de ofertas** | Lista 4 vacantes de Ashby con enlaces (incluidas las 2 que verificó el fundador). Detectó que el FDE fue **republicado hace 26 días** y un **AI PM con Madrid**. No pudo confirmar que estuvieran abiertas | 2 vacantes **verificadas abiertas por un humano** | **Nosotros** en certeza; **IA** en hallazgos extra (republicación, Madrid) |
| **Intermediarios externos** | **Falló.** Concluyó "no encontré evidencia de que use agencias". **No encontró las ofertas gestionadas por Manfred** (2024 y 2026) | Identificó a Manfred, qué puesto lleva y cuál no | **Nosotros**. Es la diferencia comercialmente más relevante |
| **Evidencias negativas** | Riesgo cultural ("selección llevada por fundadores, desconfían de agencias que envían muchos CV"); posible primera persona de People | Head of People en Nueva York; redes de talento de a16z/YC; proveedor ya instalado | Parecido |
| **Calidad de conclusiones** | Recomienda contactar con propuesta retained para los perfiles difíciles. Como no sabe de Manfred, **sugiere competir también por el Senior Product Engineer**, que Manfred ya gestiona | Recomienda no competir por el puesto de Manfred y ofrecer otro perfil | **Nosotros** gracias al dato de Manfred; en lo demás, la IA es comparable y a veces más concreta (momento, contacto con fundadores) |
| **Tiempo humano** | ~0 h (más unos 10 min para leerla) | Varias horas acumuladas | **IA**, por mucho |
| **Errores y omisiones** | Omisión crítica: Manfred. Citó un perfil personal de LinkedIn de un empleado (no lo replicamos por privacidad). Fundación incierta | Sin el AI PM de Madrid ni la republicación del FDE | — |

## Lectura honesta
1. **Para la mayoría de la ficha, una IA generalista produce un resultado comercialmente equivalente en ~15 minutos y sin trabajo humano.** Incluso aporta más fuentes y dos hallazgos que nosotros no teníamos.
2. **La única diferencia material fue detectar el intermediario (Manfred).** Pero esa diferencia es un **paso del método**: buscar el nombre de la empresa en los portales de intermediarios, empezando por getmanfred.com. No son datos propios. Vos lo encontraste por tu cuenta, y cualquier agencia (o un prompt mejor escrito) puede hacerlo.
3. **Conclusión para el Modelo B:** tal como está planteado (una ficha por empresa), **la diferenciación es insuficiente**. Una agencia que use ChatGPT u otro asistente con búsqueda obtiene el ~80% en minutos. Para sostener B haría falta otra diferenciación, por ejemplo:
   - un **historial propio** que una IA no tiene: fotos fechadas de vacantes y procesos de intermediarios a lo largo de meses (republicaciones, cuánto tiempo siguen abiertas, qué agencia lleva qué puesto);
   - **verificación humana con responsabilidad**: datos garantizados con reposición, cosa que la IA no ofrece;
   - o venderlo **integrado en otro servicio**, no como ficha suelta.

   Ninguna de estas variantes está validada. La primera requiere semanas de acumulación y un acceso web que hoy no tenemos.
4. **El Modelo A tampoco queda a salvo:** la misma IA podría generar listas de candidatas. Su valor dependería del filtro y de la verificación, y ya medimos que producirlos es caro.
5. **Pregunta obligatoria en las llamadas:** "¿Usan ChatGPT o algo parecido para investigar empresas? ¿Qué les falta?" Si la mayoría responde que con eso les alcanza, se **abandona B** y se reevalúa todo el producto.

## Registro
- La ficha completa de la IA quedó en el historial de la sesión. No la copiamos al repositorio porque contiene la URL de un perfil personal de LinkedIn.
- Búsquedas: 14 (IA). Tiempo: ~12-15 minutos.
