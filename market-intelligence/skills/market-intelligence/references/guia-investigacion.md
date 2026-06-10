# Guía de investigación — Market Intelligence (Agente 2.1)

Guía operativa de los Pasos 1–2 del flujo. Define **cuánto** investiga el agente
y **en qué secuencia**, para que su comportamiento sea predecible y no dependa de
la improvisación. Sin esto, el agente puede quedarse corto (rellenar con
conocimiento genérico, lo que las reglas prohíben) o dispararse en coste.

## Idioma

Recordatorio: todo lo que escribas o produzcas se redacta en español de España
(peninsular). Las citas literales (consultas reales, respuestas textuales de un
motor) se conservan en su idioma original; la síntesis que las rodea va en
peninsular.

## Niveles de intensidad (parámetro `profundidad`)

El operador elige el nivel por cliente. El estándar es `profunda`.

| Nivel               | Búsquedas aprox. | Cuándo usarlo                                       |
|---------------------|------------------|----------------------------------------------------|
| `ligera`            | 8–12             | Retrato rápido, cliente pequeño, validación inicial |
| `media`             | 15–25            | Equilibrio profundidad/coste                        |
| `profunda` (estándar)| 30–50           | Exhaustivo por bloque; cliente o sector complejo    |

El número es un **presupuesto orientativo, no una cuota a llenar**: si alcanzas
saturación de información antes del tope, paras y lo declaras.

**Aviso obligatorio al superar el presupuesto.** Si para cubrir un bloque crítico
necesitas pasar del tope del nivel, **paras, avisas al analista con cuántas
búsquedas llevas y por qué necesitas más, y esperas su OK** antes de continuar.
No te pasas del presupuesto en silencio (en un run real es fácil irse de 50 a 75
sin darte cuenta). El recuento final de búsquedas frente al presupuesto va en
`audit/execution_log.json`.

## Reparto de búsquedas por bloque (nivel `profunda`)

Como guía, no como camisa de fuerza:

| Bloque                          | Búsquedas orientativas               |
|---------------------------------|--------------------------------------|
| 1 · Demanda y búsqueda          | 5–8                                  |
| 2 · Panorama generativo (GEO)   | 8–12 (las 10 consultas en los motores)|
| 3 · Estructura de mercado       | 3–5                                  |
| 4 · E-E-A-T del sector          | 4–6                                  |
| 5 · Utilidad de contenido       | 3–5                                  |
| 6 · Plataformas y canales       | 4–6                                  |
| 7 · Influencers                 | 4–6                                  |

En `ligera` y `media`, se escala el reparto a la baja manteniendo prioridad en
los bloques 1 y 2 (los más densos en datos).

## Circuito de investigación (secuencia)

El agente sigue este circuito de principio a fin:

1. **LEER CKB** → extraer sector, oferta, voceros, voz de mercado, canales
   actuales. (Paso 1.1 del SKILL.)
2. **PLANIFICAR** → derivar las consultas clave (por defecto 10) y listar los
   huecos de información que cada bloque necesita cubrir. **Mostrar el plan al
   analista antes de buscar** y esperar su OK. (Paso 1.2–1.3 del SKILL.)
3. **INVESTIGAR** por bloques, en orden (1→7):
   - Empezar con búsquedas amplias (1–2 términos), luego estrechar.
   - Cada query debe ser distinta de la anterior; si una falla, reformular con
     otro ángulo, no repetir.
   - Para el Bloque 2, auditar cada motor generativo con las consultas clave y
     registrar fuentes citadas, entidades y huecos (ver «Auditoría de motores
     generativos» abajo).
4. **CHECKPOINT de saturación** → antes de cerrar cada bloque, comprobar: ¿cada
   campo del bloque está respaldado por algo recuperado, no por conocimiento
   genérico? Si no, buscar lo que falte. Si sí, avanzar.
5. **SINTETIZAR** → redactar los bloques 1–7 (descriptivos).
6. **CONCLUIR** → redactar el Bloque 8 accionable, con agente destino de cada
   conclusión.

## Auditoría de motores generativos (Bloque 2, el núcleo GEO)

Es el bloque diferencial. Procedimiento:

1. Tomas las consultas clave validadas en el plan (por defecto 10), redactadas
   como las formularía la audiencia real, no como las nombra el cliente.
2. Para cada motor de `motores_geo` (por defecto ChatGPT, Perplexity, Google AI
   Overviews, Gemini), lanzas las consultas y registras, por consulta y motor:
   - **Fuentes citadas**: qué dominios y qué tipo de páginas (guía, comparativa,
     ficha de producto, foro, etc.).
   - **Entidades y marcas** que aparecen en la respuesta.
   - **Huecos de respuesta**: preguntas mal respondidas o sin fuente clara =
     oportunidad directa para el cliente.
3. Anotas el **grado de solapamiento** (campo OBLIGATORIO del Bloque 2) entre los
   resultados orgánicos de Google y las fuentes citadas por la IA. Cómo se
   calcula: para cada consulta clave, miras el top de fuentes citadas por el
   motor y el top orgánico de Google, y reportas qué proporción coincide (p. ej.
   «de las fuentes citadas por Perplexity en 10 consultas, ~X % también
   aparecían en el top 10 orgánico de Google»). Como referencia del sector, el
   solapamiento ha caído por debajo del 20 % en muchos nichos, lo que confirma
   que GEO requiere estrategia propia; **confirma el dato observado, no lo des
   por sentado, y si no puedes calcularlo lo marcas «dato no disponible» en vez
   de omitirlo.**
4. **Nota de no-determinación:** las respuestas de los LLMs fluctúan. Cuando una
   conclusión dependa de una sola respuesta, señálalo; cuando puedas, repite la
   consulta y reporta el patrón, no una foto única.
5. Guardas el log completo en `_fuentes/auditoria_geo.md`.

**Regla prescriptiva (no silenciar el hueco):** intentas auditar todos los
motores de `motores_geo`. Para **ChatGPT y Gemini**, que requieren sesión
iniciada, **por defecto usas Claude in Chrome sobre la sesión logueada del
operador**. Si te topas con un **muro de login**, **PARAS y pides al operador que
inicie sesión (o que pegue las respuestas)**, en vez de saltarte el motor en
silencio. Solo si tras eso sigue sin haber acceso, marcas ese motor como «dato no
disponible (sin acceso)» y no inventas su respuesta.

### Vías de acceso a cada motor (cómo conseguir las respuestas)

ChatGPT y Gemini requieren sesión iniciada; no se consultan con una búsqueda web
anónima. Opciones, de menos a más infraestructura:

| Motor | Nivel 1 (sin coste) | Nivel 2 (API, automatable) |
|-------|---------------------|----------------------------|
| **Perplexity** | Búsqueda web / navegador asistido | **Sonar API** (citas nativas) |
| **ChatGPT** | **Claude in Chrome** sobre tu sesión logueada, o el operador pega las respuestas | **OpenAI Responses API** con la tool `web_search` (devuelve `url_citation`) |
| **Gemini** | **Claude in Chrome** sobre tu sesión logueada, o el operador pega las respuestas | **Gemini API** con *Grounding with Google Search* (`groundingMetadata` con queries, resultados y citas) |
| **Google AI Overviews** | Observación directa en SERP (no siempre aparecen en YMYL local ES) | — |

**Patrón oro vs aproximación:** la app de consumo (vía Chrome o paste) es lo que
ve el cliente final y es el patrón oro para GEO. Las APIs con grounding son una
**aproximación automatizable y barata** (más que GEO Metrics), útil para
monitorización a escala, pero su ranking y conjunto de fuentes pueden diferir de
la app: trátalas como tendencia, no como foto idéntica, y dilo en el informe.
**GEO Metrics** (Nivel 2+) se sitúa por encima como capa ya gestionada para el
mercado en español.

Elijas la vía que elijas, **registras en el Bloque 2 con qué método se obtuvo
cada respuesta** (navegador, paste, API o GEO Metrics), porque cambia la
fiabilidad de la lectura.

## Rol del analista (Nivel 1)

El agente **conduce** toda la investigación con búsqueda web; el analista
**co-pilota**: revisa el plan del Paso 1 y puede, en cualquier momento, pedir
cambios — más profundidad en un bloque, reorientar el foco, descartar una fuente
poco fiable, o ampliar/recortar el presupuesto de búsquedas. El agente acata
esos ajustes y deja constancia de ellos en `audit/execution_log.json`.

## Criterios de parada

El agente deja de investigar un bloque cuando se cumple lo primero de:

- Cada campo del bloque está respaldado por fuentes recuperadas, **o**
- Las últimas 2–3 búsquedas no aportan información nueva (saturación), **o**
- Se alcanza el tope del presupuesto del nivel y los campos críticos están
  cubiertos.

Si al parar quedan campos sin cubrir, el agente los marca como **«dato no
disponible»** en vez de inventarlos.

## Datos que requieren herramienta de pago (Nivel 2+)

En Nivel 1 toda la investigación es búsqueda web. Si un campo requiere datos que
solo dan herramientas de pago (volúmenes exactos de keywords, citación IA
medida por plataforma), tienes dos opciones, en este orden:

1. Aproximar con búsqueda web y señales públicas, declarando que es aproximación.
2. Marcar **«requiere herramienta (Nivel 2+)»** si no hay forma pública de
   aproximarlo.

Nunca inventes la cifra. El Nivel 2 desbloquea estos datos por API (datos de
keywords, citación IA) con re-auditoría mensual automatizada vía n8n.
