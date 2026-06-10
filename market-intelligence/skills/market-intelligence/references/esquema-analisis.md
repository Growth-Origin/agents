# Esquema del análisis de mercado — Agente 2.1

> Define la estructura del output del Market Intelligence Agent: los ocho
> bloques, la estructura de carpetas, la convención de trazabilidad, el mapeo de
> entradas desde el CKB y el contrato del Bloque 8 con los agentes downstream.
> El esquema es **estable**: las secciones no cambian de cliente a cliente;
> cambia el contenido.

## Idioma

Todo el contenido se redacta en **español de España (peninsular)**. Tú
(singular) y vosotros (plural): tienes, queréis, podéis, dime, mira, fíjate.
**Prohibido cualquier argentinismo** (vos, tenés, querés, podés, decime, mirá,
fijate sin tilde, dale como «ok», armá, pegá, andá, bárbaro, re- como
intensificador, qué onda, laburo, guita, che). Las citas literales se conservan
en su idioma original.

## Estructura de carpetas del output

Dentro de la carpeta de trabajo, bajo `clientes/[slug-cliente]/`:

```
clientes/[slug-cliente]/
└── market-intelligence/
    ├── analisis_mercado.md            # Los 8 bloques (documento principal)
    ├── conclusiones_accionables.md    # Bloque 8 standalone (contrato downstream)
    ├── resumen_ejecutivo.pdf          # Resumen presentable 2-4 págs (ver plantilla-resumen-pdf.md)
    ├── _fuentes/
    │   ├── auditoria_geo.md           # Log de la auditoría de motores generativos
    │   ├── demanda_busqueda.md        # Datos y resultados de demanda/keywords
    │   ├── citacion_plataformas.md    # Datos de citación por plataforma/canal
    │   └── influencers.md             # Candidatos localizados y su evidencia
    └── audit/
        ├── execution_log.json         # Parámetros, búsquedas, ajustes del analista
        └── sources_accessed.json      # Fuentes accedidas con fecha
```

El documento principal `analisis_mercado.md` lleva una cabecera de metadatos:

```markdown
# Análisis de mercado — [Nombre Cliente]

**Versión:** 0.1
**Fecha de la auditoría:** AAAA-MM-DD
**Sector / vertical:** ...
**Idioma / geografía del mercado:** ...
**Profundidad:** ligera | media | profunda
**Motores generativos auditados:** ...
**CKB de origen:** ruta y versión del CKB del Agente 1.1 usado como ancla
```

Recordatorio de re-ejecución: el panorama generativo y el peso de plataformas
cambian rápido. El documento lleva fecha y está pensado para re-auditarse
periódicamente (mensual en Nivel 2). Al re-ejecutar, no se sobrescribe en
silencio: se versiona.

## Estructura interna de cada bloque

Cada uno de los bloques 1–7 sigue la misma estructura:

1. **Síntesis** (1 párrafo): lo esencial del bloque, accionable.
2. **Detalle**: el contenido del bloque con sus campos (ver
   `plantillas-bloques.md`), en tablas cuando sean datos comparables.
3. **Evidencia y trazabilidad**: cada afirmación factual con su etiqueta.
4. **Huecos**: lo marcado como «dato no disponible» y por qué.

El Bloque 8 tiene formato propio (tabla de conclusiones → agente destino).

## Convención de trazabilidad

Idéntica a la del resto del ecosistema. Cada afirmación factual lleva:

`‹fuente: [tipo+ref] | acceso: AAAA-MM-DD | confianza: alta/media-alta/media/baja | tipo: hecho/interpretación/hipótesis›`

Tipos de fuente válidos en este agente:

- `web: [URL]` — página, artículo, estudio o dato indexado.
- `motor-geo: [motor] | consulta: "..."` — respuesta observada en un motor
  generativo (ChatGPT, Perplexity, Google AI Overviews, Gemini). Anota el motor
  y la consulta literal.
- `keywords: [herramienta/fuente]` — datos de volumen, tendencia o
  estacionalidad.
- `ckb: [módulo]` — dato heredado del Client Knowledge Base del Agente 1.1.
- `reseña: [plataforma]` — voz de mercado (anonimizada: rol y contexto, no
  nombre completo).

Regla de oro: sin fuente real, no hay afirmación. Lo no verificable va a
«dato no disponible», nunca se inventa.

**Trazabilidad atómica, no agregada.** La etiqueta va pegada a cada afirmación
factual, no en una lista de fuentes al final del bloque. Esto es especialmente
estricto con **datos cuantitativos** (cifras, porcentajes, precios, rankings,
recuentos de reseñas): cada uno lleva la fuente de ESE dato. Una lista de 15
fuentes al pie del bloque no permite saber cuál respalda el «81 %» y cuál el
«12.000 M€» — y eso, en un sector YMYL, no vale. Puedes añadir además un
consolidado de fuentes al final, pero no sustituye la etiqueta por dato.

**Cadena de confianza desde el CKB.** Los datos heredados del CKB se etiquetan
`ckb: [módulo]`. Si un dato del CKB provenía de un workshop con el cliente,
indicas si fue **validado** o sigue como **hipótesis**: no conviertes en «hecho»
algo que el CKB dejó sin validar. El análisis es tan fiable como el CKB que
consume.

## Mapeo de entradas: del CKB al análisis

El agente **no parte de cero**. Lee del CKB del Agente 1.1 y lo enriquece:

| Fuente en el CKB                   | Módulo CKB                | Uso en el análisis                                  |
|------------------------------------|---------------------------|-----------------------------------------------------|
| Sector y vertical                  | Identidad y negocio       | Acota el universo de investigación                  |
| Propuesta de valor                 | Propuesta de valor        | Define qué problema resuelve el cliente             |
| Productos / servicios (oferta)     | Propuesta de valor        | Mapea la demanda a buscar                           |
| Voceros identificados              | Activos, expertise, voceros | Base para E-E-A-T (Bloque 4) e influencers (Bloque 7) |
| Voz de mercado (reviews, jerga)    | Voz, tono y lenguaje      | Vocabulario real de la audiencia (Bloque 1)         |
| Canales actuales del cliente       | Activos, expertise, voceros | Punto de partida para plataformas (Bloque 6)       |

Si el cliente no pasó por el CKB Builder, se acuerda con el operador un pase
mínimo de contexto antes de investigar. No se inventa el contexto.

## Los ocho bloques (resumen)

Bloques **descriptivos** (1–7) y **capa accionable** (8):

1. **Demanda y comportamiento de búsqueda** — volumen y tipo de demanda;
   taxonomía de intenciones (informacional / comparativa / transaccional /
   navegacional); vocabulario real; query fan-out; preguntas frecuentes.
2. **Panorama generativo (GEO)** — fuentes citadas hoy por los motores;
   entidades y marcas que aparecen; huecos de respuesta; grado de solapamiento
   entre orgánico de Google y fuentes citadas por IA.
3. **Estructura del mercado** — segmentación de la demanda; madurez (educar vs
   convertir); estacionalidad; tendencias emergentes.
4. **E-E-A-T del sector** — qué señala autoridad en este nicho concreto:
   Experiencia, Expertise, Autoridad de entidad (cadenas `sameAs`), Confianza;
   medios y blogs más citados por la IA. Lista priorizada y concreta.
5. **Utilidad de contenido** — qué hace útil al contenido para usuario y para
   IA, como patrón del contenido que ya triunfa en el sector.
6. **Plataformas y canales** — veredicto entrar / no entrar / vigilar por
   plataforma y por canal propio nuevo, con datos de citación del sector.
7. **Influencers del sector** — veredicto sobre la palanca + lista corta de
   candidatos accesibles con autoridad temática.
8. **Conclusiones accionables (capa puente)** — ver contrato abajo.

El detalle de campos de cada bloque está en `plantillas-bloques.md`.

## Contrato del Bloque 8 con los agentes downstream

El Bloque 8 es la sección que los agentes downstream consumen primero. Es
concisa, priorizada y **explícita sobre a qué agente sirve cada conclusión**.
Cada conclusión es una afirmación verificable y autocontenida (no una
observación vaga).

| Conclusión accionable                                          | Agente destino                          |
|----------------------------------------------------------------|-----------------------------------------|
| Medios y blogs prioritarios para menciones/enlaces             | Estrategia (Capa 2) · Contenido (Capa 3)|
| Elementos E-E-A-T concretos que el sector premia               | Contenido (Capa 3) · ICP (1.2)          |
| Patrones de utilidad de contenido del sector (usuario + IA)    | Contenido (Capa 3)                      |
| Huecos de respuesta GEO sin cubrir                             | Contenido (Capa 3)                      |
| Formatos de contenido más citados en el nicho                  | Contenido (Capa 3)                      |
| Veredicto de plataformas: dónde estar y qué canal propio abrir | Estrategia (Capa 2) · Voceros           |
| Veredicto de influencers + lista de candidatos accesibles      | Estrategia (Capa 2)                     |
| Preguntas de alta intención sin respuesta autoritativa         | Estrategia · Contenido                  |
| Segmentos de demanda prioritarios                              | ICP (1.2)                               |
| Estacionalidad para el calendario                              | Estrategia (Capa 2)                     |

Cada fila del Bloque 8 debe poder leerse sin abrir el resto del documento: el
downstream tiene que poder actuar solo con esa línea.
