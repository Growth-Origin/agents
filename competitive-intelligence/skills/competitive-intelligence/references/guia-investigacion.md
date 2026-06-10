# Guía de investigación — Competitive Intelligence (Agente 2.2)

Guía operativa de los Pasos 3–4. Define cuánto investiga el agente, en qué
secuencia y con qué fuentes, para un comportamiento predecible. Idioma de salida:
español de España (peninsular); las citas literales se conservan en su idioma.

## Intensidad (parámetro `profundidad`)

Por defecto **muy_alta**. Por la naturaleza del análisis competitivo, este agente
admite un escalón por encima del Agente 2.1.

| Nivel | Búsquedas/consultas aprox. | Cuándo |
|-------|----------------------------|--------|
| `media` | 25–40 | Un solo competidor, validación rápida |
| `alta` | 40–70 | Estándar |
| `muy_alta` (estándar) | 70–120+ | Disección completa de 3–5 competidores |

El presupuesto es **por ejecución completa** (varios competidores × varios temas
× varios motores) y es **orientativo**: el agente para por saturación, o sigue si
un competidor crítico lo justifica **avisando al analista**.

**Aviso obligatorio al superar el presupuesto.** Si para cubrir un competidor o
tema crítico necesitas pasar del tope, paras, dices cuántas búsquedas llevas y por
qué necesitas más, y esperas el OK. No te pasas en silencio. El recuento final va
en `audit/execution_log.json`.

## Circuito de investigación (secuencia)

1. **LEER** CKB + outputs del Agente 2.1 + parámetros de enfoque.
2. **PROPONER** competidores candidatos (ver `parametros-enfoque.md`) y esperar
   validación del analista.
3. **PLANIFICAR:** por cada competidor validado, listar los 11 temas y las
   consultas/datos que requieren, marcando Nivel 1 vs «requiere herramienta
   (Nivel 2+)». Mostrar plan y presupuesto al analista.
4. **RECOPILAR DATOS** (Nivel 1):
   - **Datos duros (4.1):** aproximar por observación de SERP, declarándolo. Lo
     exacto (volúmenes, tráfico) se marca «requiere herramienta (Nivel 2+)».
   - **Backlinks (4.4):** marcar «requiere herramienta (Nivel 2+)» — sin
     sustituto público fiable. No aproximar a ojo.
   - **Crawl y lectura** (4.5, 4.6, 4.7, 4.8, 4.9): sitemap + fetch + muestreo de
     páginas estratégicas y de blog. Si una página renderiza por JavaScript,
     escalar a Claude in Chrome para esa página.
   - **CMS/stack/schema (4.10):** detectar leyendo el HTML y las cabeceras
     (generadores, librerías, datos estructurados JSON-LD). **Core Web Vitals**
     con **PageSpeed Insights** (gratuito): consultar la URL principal y 1–2
     páginas clave.
5. **AUDITORÍA GENERATIVA** (4.2, 4.3) — ver sección dedicada abajo.
6. **CHECKPOINT por tema:** ¿cada hallazgo está respaldado por datos recuperados,
   no por suposición? Si no, completar o marcar pendiente.
7. **SINTETIZAR por competidor** en formato insight→implicación→acción.
8. **AGREGAR** y redactar la síntesis accionable (4.11) con agente destino, el
   PDF y el audit.

## Auditoría generativa (temas 4.2 y 4.3) — el bloque diferencial

Por cada competidor:

1. Lanzas los **tres tipos de pregunta** a cada motor:
   - **De mercado:** «¿cuáles son las mejores soluciones / clínicas / proveedores
     para X?» → ¿aparece el competidor?, ¿en qué posición del razonamiento?
   - **Comparativas:** «¿X o Y, cuál es mejor para Z?» → cómo lo posiciona la IA
     frente a otros.
   - **Sobre el propio competidor:** «¿es fiable X?», «¿qué opinas de X?» → la
     opinión directa de la IA (fortalezas que le atribuye, qué dice que debería
     mejorar).
2. **Repites cada consulta varias veces** y reportas el **patrón y la
   variabilidad** observada, no una foto única (los LLMs son no-deterministas).
   Registras el número de repeticiones por consulta.
3. Cruzas **SEO↔GEO:** dado que buena parte de lo que la IA cita procede de
   resultados de Google, identificas qué páginas del competidor trabajan en los
   dos frentes.

### Vías de acceso a cada motor

ChatGPT y Gemini requieren sesión iniciada; no se consultan con una búsqueda web
anónima. Por defecto:

| Motor | Nivel 1 (sin coste) | Nivel 2 (API, automatable) |
|-------|---------------------|----------------------------|
| **Perplexity** | Búsqueda web / navegador asistido | Sonar API (citas nativas) |
| **ChatGPT** | **Claude in Chrome sobre tu sesión logueada** (por defecto); o el operador pega las respuestas | OpenAI Responses API con `web_search` (`url_citation`) |
| **Gemini** | **Claude in Chrome sobre tu sesión logueada** (por defecto); o el operador pega las respuestas | Gemini API con *Grounding with Google Search* (`groundingMetadata`) |
| **Google AI Overviews** | Observación directa en SERP | — |

**Regla prescriptiva (no silenciar el hueco):** intentas auditar los tres
motores. Para ChatGPT y Gemini, **por defecto usas Claude in Chrome** sobre la
sesión del operador. Si te topas con un **muro de login**, **PARAS y pides al
operador que inicie sesión (o que pegue las respuestas)**; no te saltas el motor
sin avisar. Solo si tras eso sigue sin haber acceso, marcas ese motor como «dato
no disponible (sin acceso)». Registras en el informe **con qué método** se obtuvo
cada respuesta.

**Patrón oro vs aproximación:** la app de consumo (Chrome o paste) es lo que ve el
cliente final y es el patrón oro. Las APIs con grounding son una aproximación
automatizable y barata (Nivel 2), útil para monitorización, pero su ranking y sus
fuentes pueden diferir de la app: trátalas como tendencia, no como foto idéntica,
y dilo. **GEO Metrics** se sitúa por encima como capa gestionada para el mercado
en español.

## Criterios de parada

Por tema y competidor, paras cuando se cumple lo primero de:

- Cada campo del tema está respaldado por datos recuperados, **o**
- Las últimas 2–3 búsquedas no aportan novedad (saturación), **o**
- Se alcanza el tope del presupuesto con lo crítico cubierto.

Lo no cubierto se marca **«dato no disponible»**; lo que depende de herramienta de
pago, **«requiere herramienta (Nivel 2+)»**. Nunca se inventa.

## Compliance (resumen operativo)

- Solo datos **públicos**; el crawl respeta `robots.txt` y un ritmo razonable.
- **Prohibido el scraping autenticado** (LinkedIn tras login, Sales Navigator,
  etc.). Para autores/fundadores del competidor, solo contenido público indexado.
- Minimización de datos personales (GDPR art. 5); anonimizar terceros.
- Herramientas de pago, solo dentro de su licencia (Nivel 2).
