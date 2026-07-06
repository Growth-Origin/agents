# Plantillas — Market Intelligence (Agente 2.1)

Plantillas listas para rellenar. Las usas en el Paso 3 (síntesis). Idioma:
español de España (peninsular). Cada afirmación factual lleva su etiqueta de
trazabilidad atómica: `‹fuente | acceso: AAAA-MM-DD | confianza | tipo›`.

**Dos niveles de salida:**

- Los **bloques de abajo** son la estructura interna del documento extenso
  `analisis_mercado_completo.md` (el doc «wow» con todo).
- De ese documento se **derivan los entregables standalone**. Mapeo:

  | Entregable | Se nutre de los bloques |
  |------------|--------------------------|
  | `top5_competidores.md` | 2 (panorama) + 6 (plataformas) + observación de SERP |
  | `eeat_sector.md` | Bloque 4 |
  | `top50_preguntas.md` | Bloque 1 (preguntas) + módulo prompt |
  | `vocabulario_y_comunicacion.md` | Bloque 1 (vocabulario) + 5 |
  | `plataformas_y_contenido.md` | Bloques 5 y 6 |
  | `posicion_e_intensidad.md` | Bloques 1/2 (keywords) + 3 + benchmark de intensidad |
  | `conclusiones_accionables.md` | Bloque 8 |

  Las plantillas de los entregables que no son 1:1 con un bloque están al final
  del archivo, en «Plantillas de entregables derivados».

---

## Cabecera del documento

~~~markdown
# Análisis de mercado — [Nombre Cliente]

**Versión:** 0.1
**Fecha de la auditoría:** AAAA-MM-DD
**Sector / vertical:** ...
**Idioma / geografía del mercado:** ...
**Profundidad:** ligera | media | profunda
**Nivel de investigación:** 1 (sin herramientas) | 2 (herramientas: ...)
**Motores generativos auditados:** ...
**CKB de origen:** [ruta y versión del CKB del Agente 1.1]

## Síntesis ejecutiva (1 párrafo)

[Lo esencial del mercado en 4–6 frases: tipo de demanda, madurez, dónde está la
oportunidad GEO más clara, y la palanca prioritaria. Todo lo demás amplía esto.]
~~~

---

## Bloque 1 — Demanda y comportamiento de búsqueda

~~~markdown
## Bloque 1 — Demanda y comportamiento de búsqueda

**Síntesis:** [1 párrafo]

### Volumen y tipo de demanda
[Tamaño y naturaleza de la demanda existente. Aproximaciones declaradas como
tales si no hay dato exacto.] ‹fuente | acceso | confianza | tipo›

### Taxonomía de intenciones
| Intención       | Ejemplos de consulta real | Peso relativo en el sector |
|-----------------|---------------------------|----------------------------|
| Informacional   |                           |                            |
| Comparativa     |                           |                            |
| Transaccional   |                           |                            |
| Navegacional    |                           |                            |

### Vocabulario real de la audiencia
[Términos, jerga y sinónimos con que la gente busca — no como lo nombra el
cliente. Cita literal cuando aporte.] ‹fuente: reseña/web | ...›

### Query fan-out
[Las subconsultas en que los motores generativos descomponen las preguntas
principales. Crítico para GEO: los motores responden a los componentes, no a la
consulta literal.] ‹motor-geo: [motor] | consulta: "..."›

### Preguntas frecuentes de la audiencia
[Lista de preguntas reales — insumo directo para contenido GEO.]

### Huecos
[Campos marcados «dato no disponible» y por qué.]
~~~

---

## Bloque 2 — Panorama generativo (GEO)

~~~markdown
## Bloque 2 — Panorama generativo (GEO)

**Síntesis:** [1 párrafo: qué cita hoy la IA en este nicho y dónde están los huecos]

### Fuentes citadas hoy por los motores
| Consulta clave | Motor | Método de acceso | Dominios/fuentes citadas | Tipo de página |
|----------------|-------|------------------|--------------------------|----------------|
|                |       | navegador / paste / API / GEO Metrics |              |                |
‹motor-geo: [motor] | consulta: "..." | acceso | confianza | tipo›

> Registra qué motores se auditaron y cuáles quedaron pendientes (y por qué:
> login, sin acceso, etc.). No inventes la respuesta de un motor no auditado.

### Entidades y marcas que aparecen como respuesta
[Quién sale citado/recomendado, en qué consultas y en qué posición del
razonamiento.]

### Huecos de respuesta (oportunidad directa)
[Preguntas mal respondidas o sin fuente clara. Cada hueco = oportunidad de
contenido para el cliente.]

### Solapamiento orgánico Google ↔ fuentes citadas por IA  (CAMPO OBLIGATORIO)
[Grado de solapamiento observado y qué implica para la estrategia GEO. Reporta
una cifra o rango (p. ej. «~X % de las fuentes citadas también estaban en el top
orgánico de Google»). Confirmar el dato, no asumir el ~20 % de referencia. Si no
puedes calcularlo, escribe «dato no disponible» — no lo dejes en blanco.]

### Nota de no-determinación
[Señalar consultas cuya conclusión depende de una sola respuesta y, donde se
haya repetido, el patrón observado.]
~~~

---

## Bloque 3 — Estructura del mercado

~~~markdown
## Bloque 3 — Estructura del mercado

**Síntesis:** [1 párrafo]

### Segmentación de la demanda
[Cómo se divide la demanda. Insumo para el ICP (Agente 3), sin definirlo.]

### Madurez del sector
[¿Hay que educar o convertir? Implicaciones para el tipo de contenido.]

### Estacionalidad
[Picos y valles a lo largo del año. Insumo para el calendario (Capa 2).]

### Tendencias emergentes
[Señales de demanda futura.] ‹fuente | acceso | confianza | tipo›
~~~

---

## Bloque 4 — E-E-A-T del sector

~~~markdown
## Bloque 4 — E-E-A-T del sector

**Síntesis:** [1 párrafo: qué señala autoridad en ESTE nicho concreto]

| Dimensión   | Qué premia el sector (concreto, observado) | Evidencia |
|-------------|---------------------------------------------|-----------|
| Experiencia | [qué "prueba de haberlo hecho" exige la audiencia: capturas propias, datos de uso, casos] | ‹...› |
| Expertise   | [qué credenciales pesan: titulaciones, años, certificaciones del nicho] | ‹...› |
| Autoridad   | [entidad de autor verificable: qué registros importan — LinkedIn, ORCID, Wikidata, registros sectoriales — vía cadenas `sameAs`] | ‹...› |
| Confianza   | [transparencia de autoría, políticas editoriales, citas a fuentes primarias, reseñas verificadas] | ‹...› |

### Medios y blogs más citados por la IA en el sector
[Lista priorizada con frecuencia de citación observada. Ser citado por ellos
transfiere autoridad.]

> El output debe ser una lista de elementos E-E-A-T **concretos del sector**, no
> genéricos. "Los artículos citados llevan autor con LinkedIn verificado y ORCID"
> es accionable; "ten buena E-E-A-T" no lo es.
~~~

---

## Bloque 5 — Utilidad de contenido (usuario + IA)

~~~markdown
## Bloque 5 — Qué hace útil al contenido en este sector

**Síntesis:** [1 párrafo: qué patrones de los de abajo pesan más en este nicho]

| Señal de utilidad | Por qué importa al usuario | Por qué importa a la IA | Peso en este sector |
|-------------------|----------------------------|--------------------------|---------------------|
| Respuesta directa al inicio de cada sección | Resuelve rápido | Extrae el "answer-first" como cita | |
| Pasajes autocontenidos (~130–170 palabras) | Legible sin contexto | Unidad semántica citable aislada | |
| Datos originales y estadísticas verificables | Información nueva | El contenido con datos propios gana visibilidad | |
| Citas inline con enlace a fuente primaria | Permite verificar | Sube la confianza de recuperación | |
| Tablas comparativas con datos cuantificados | Decisión más fácil | Formato que la IA extrae y muestra | |
| Estructura clara (H2/H3/H4, listas, hechos arriba) | Escaneable | "Elementos atómicos" fáciles de citar | |
| Densidad de entidades reconocidas | Contexto completo | Mejor alineación semántica → más cita | |
| Frescura / refresco de contenido | Información vigente | El refresco sistemático supera al contenido nuevo | |

### Patrones específicos del sector
[Qué de lo anterior pesa más en este nicho concreto, con ejemplos observados en
el contenido que ya rankea y que la IA ya cita.] ‹fuente | ...›
~~~

---

## Bloque 6 — Plataformas y canales

~~~markdown
## Bloque 6 — Estrategia de plataformas y canales

**Síntesis:** [1 párrafo: dónde vale la pena estar para SEO/GEO, con datos de citación]

| Plataforma / canal | Citación observada en el sector | Veredicto | Justificación | Esfuerzo de mantenimiento |
|--------------------|----------------------------------|-----------|---------------|---------------------------|
| YouTube            |                                  | entrar / no entrar / vigilar | | |
| LinkedIn (artículos) |                                | | | |
| Reddit (hilos)     |                                  | | | |
| Directorios/reseñas (G2, Wikipedia, registros del nicho) | | | | |
| Foros/comunidades del nicho |                         | | | |
| Canal propio nuevo (Medium / X / newsletter / perfil de autor) | | | | |

> Referencias globales a confirmar por sector y motor: YouTube y LinkedIn
> (artículos, de creadores individuales) van en cabeza de citación; Reddit
> fuerte en Google AI Overviews y Perplexity; los directorios pesan en consultas
> comparativas. **Confirma el peso real por sector, no lo des por hecho.**
>
> Decisión de canal propio nuevo: recomiéndalo SOLO si (a) el sector muestra
> citación desde esa plataforma y (b) el cliente tiene un vocero capaz de
> alimentarlo de forma sostenida. Abrir canales que no se pueden mantener resta
> autoridad.
~~~

---

## Bloque 7 — Influencers del sector

~~~markdown
## Bloque 7 — Estrategia de influencers del sector

**Síntesis + veredicto:** [¿Vale la pena la palanca de influencers en este sector? Sí/No/Matizado, con el porqué]

> Principio rector: la evidencia indica que las campañas caras de grandes
> influencers no son el principal driver de citación por IA. Lo que mueve la
> aguja es la publicación consistente de expertos con autoridad temática, aunque
> tengan audiencia mediana o pequeña → enfoque de **influencers accesibles**.

### Lista corta de candidatos accesibles
| Candidato (rol/perfil público) | Plataforma | Autoridad temática | Audiencia | Motivo de encaje con el cliente | Tipo de colaboración sugerida |
|--------------------------------|------------|--------------------|-----------|----------------------------------|-------------------------------|
|                                |            |                    |           |                                  |                               |

> Cumplimiento: solo datos públicos indexados. **Prohibido el scraping
> autenticado de LinkedIn.** Minimización GDPR: solo lo necesario para el
> veredicto y la lista corta.
~~~

---

## Bloque 8 — Conclusiones accionables (capa puente)

Va dentro de `analisis_mercado.md` y también como `conclusiones_accionables.md`
aparte. Cada conclusión es una afirmación verificable y autocontenida, con su
agente destino.

~~~markdown
## Bloque 8 — Conclusiones accionables

| Conclusión accionable (afirmación autocontenida y verificable) | Agente destino |
|----------------------------------------------------------------|----------------|
| [Medios y blogs prioritarios para menciones/enlaces]           | Estrategia (Capa 2) · Contenido (Capa 3) |
| [Elementos E-E-A-T concretos que el sector premia]             | Contenido (Capa 3) · ICP (Agente 3) |
| [Patrones de utilidad de contenido del sector]                 | Contenido (Capa 3) |
| [Huecos de respuesta GEO sin cubrir]                           | Contenido (Capa 3) |
| [Formatos de contenido más citados en el nicho]                | Contenido (Capa 3) |
| [Veredicto de plataformas: dónde estar y qué canal propio abrir]| Estrategia (Capa 2) · Voceros |
| [Veredicto de influencers + lista de candidatos accesibles]    | Estrategia (Capa 2) |
| [Preguntas de alta intención sin respuesta autoritativa]       | Estrategia · Contenido |
| [Segmentos de demanda prioritarios]                            | ICP (Agente 3) |
| [Estacionalidad para el calendario]                            | Estrategia (Capa 2) |
~~~

Si una fila no aplica al cliente, se elimina (no se rellena con humo). Si
emerge una conclusión nueva relevante, se añade con su agente destino.

---

# Plantillas de entregables derivados

## `top5_competidores.md`

~~~markdown
# Top-5 competidores — [Cliente]

> Los 5 que mejor posicionan en el nicho objetivo. NO es disección (eso es el
> Agente 2.2); es la nominación con el porqué.

| # | Competidor | Tipo (directo/indirecto/aspiracional) | Por qué está en el top-5 (highlights) | Señal |
|---|------------|----------------------------------------|----------------------------------------|-------|
| 1 |            |                                        | [visibilidad orgánica / presencia en IA / solapamiento] | ‹fuente›|

**Para el Agente 2.2:** lista nominada lista para diseccionar, con el parámetro
de enfoque por el que entra cada uno.
~~~

## `top50_preguntas.md`

~~~markdown
# Top-50 preguntas del mercado — [Cliente] · [país]

Agrupadas por tema. Origen: búsqueda/SERP, módulo prompt (buyer personas) y GEO
Metrics. Insumo directo para contenido (FAQPage) y para el módulo prompt.

## [Tema 1]
1. [pregunta real] ‹fuente | ...›
...
~~~

## `vocabulario_y_comunicacion.md`

~~~markdown
# Vocabulario y línea de comunicación del sector — [Cliente]

- **Palabras que dan profesionalidad:** [términos del sector que generan confianza]
- **Términos a evitar / que restan:** ...
- **Tono e identidad comunicativa del sector:** [cercano/técnico/institucional…]
- **Nivel técnico esperado:** [plano divulgativo vs técnico, con ejemplos]
- **Léxico por idioma/geografía** (si aplica): ...
‹fuente: reseñas / contenido que rankea / contexto | ...›
~~~

## `posicion_e_intensidad.md`

~~~markdown
# Posición del cliente e intensidad del sector — [Cliente]

## a) Posición del cliente
- **Keywords donde está** (y posición aprox.): tabla con keyword, volumen, dónde aparece.
- **Keywords donde NO está** (oportunidad): ...
- **Presencia en IA:** dónde lo citan / dónde no.
- **Espacios y oportunidades a ocupar:** huecos concretos.
‹fuente | ...›

## b) Benchmark de intensidad del sector  (BENCHMARK, NO PLAN)
- **Dificultad:** fuerza de los dominios líderes, saturación, agregadores.
- **Intensidad:** frecuencia de publicación de los líderes, profundidad, refresco, peso de paid.
- **Velocidad:** cada cuánto se mueve el panorama y cuánto tarda en notarse el trabajo.
- **Simulación orientativa de intensidad de trabajo:** rango de piezas/mes,
  publicaciones, plataformas y paid orientativo para competir.
  > Orientativo, a dimensionar por la Capa 2 (Estrategia). No es plan ni presupuesto.
~~~
