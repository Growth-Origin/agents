# Esquema del análisis de mercado — Agente 2.1

> Define los entregables del Market Intelligence Agent, su estructura de carpetas,
> la convención de trazabilidad, los tres orígenes de contexto y el mapeo a
> herramientas. El esquema es estable; cambia el contenido, no las secciones.

## Idioma

Todo en **español de España (peninsular)**. Tú (singular) y vosotros (plural).
**Prohibido cualquier argentinismo** (vos, tenés, querés, podés, decime, mirá,
fijate sin tilde, dale como «ok», armá, pegá, andá, bárbaro, re-, qué onda,
laburo, guita, che). Las citas literales se conservan en su idioma original.

## Estructura de carpetas del output

```
clientes/[slug-cliente]/
└── market-intelligence/
    ├── analisis_mercado_completo.md   # Doc en bruto extenso: TODO lo analizado (efecto "wow")
    ├── top5_competidores.md           # Top-5 competidores + highlights (puente al 2.2)
    ├── eeat_sector.md                 # Elementos E-E-A-T concretos del mercado del cliente
    ├── top50_preguntas.md             # ~50 preguntas más frecuentes del mercado y país
    ├── vocabulario_y_comunicacion.md  # Palabras que dan profesionalidad, tono, nivel técnico
    ├── plataformas_y_contenido.md     # Dónde, qué contenido y qué se premia (con explicación)
    ├── posicion_e_intensidad.md       # Posición del cliente + benchmark intensidad/dificultad/velocidad del sector
    ├── conclusiones_accionables.md    # Contrato downstream (cada conclusión con agente destino)
    ├── resumen_ejecutivo.pdf          # Resumen presentable 2-4 págs
    ├── _fuentes/
    │   ├── contexto_normalizado.md    # Ficha de contexto (CKB / análisis previo / paquete externo)
    │   ├── keywords.md                # Estudio keyword: top keywords, volumen, competencia, criterios
    │   ├── prompts.md                 # Estudio prompt: buyer personas + prompts + datos GEO Metrics
    │   ├── auditoria_geo.md           # Panorama generativo: prompts, posición, share of voice, dominios citados
    │   └── plataformas_citacion.md    # Datos de citación por plataforma/canal
    └── audit/
        ├── execution_log.json         # Parámetros, búsquedas vs presupuesto, herramientas usadas
        └── sources_accessed.json      # Fuentes accedidas con fecha y método
```

Cabecera de `analisis_mercado_completo.md`:

```markdown
# Análisis de mercado — [Cliente]
**Versión:** 0.2  ·  **Fecha:** AAAA-MM-DD
**Origen del contexto:** CKB 1.1 / análisis previo / paquete externo
**Geografía e idiomas:** ...
**Profundidad:** ligera | media | profunda
**Nivel de investigación:** 1 (sin herramientas) | 2 (con: DataForSEO · Semrush · ambos)
**Herramientas conectadas:** GEO Metrics [sí/no] · DataForSEO [sí/no] · Semrush/Ahrefs [sí/no]
**Motores GEO auditados:** ... (método: navegador / Chrome / GEO Metrics)
```

## Los tres orígenes de contexto (desacople)

El agente **no depende en duro del Agente 1.1**. El contexto puede venir de:

1. **CKB del Agente 1.1** (`ckb/`) — lo ideal.
2. **Análisis de mercado previo** — re-ejecución/actualización.
3. **Paquete de contexto externo** — docs de otra agencia, brief, web. Se
   normaliza con `plantilla-contexto-externo.md` y se guarda en
   `_fuentes/contexto_normalizado.md`.

Mapeo contexto → uso (igual sea cual sea el origen):

| Campo de contexto | Uso en el análisis |
|-------------------|--------------------|
| Sector y vertical | Acota el universo de investigación |
| Propuesta de valor / oferta | Mapea la demanda y las keywords semilla |
| Prioridades de negocio | Criterio nº 1 del módulo keyword |
| Geografía / idiomas | Acota mercado, país y cluster lingüístico |
| Voceros | E-E-A-T e influencers |
| Voz de mercado | Vocabulario real (vocabulario_y_comunicacion) |
| Canales actuales | Punto de partida de plataformas |

## Mapeo a herramientas (tool-agnóstico)

| Necesidad | Si está conectado | Fallback Nivel 1 |
|-----------|-------------------|-------------------|
| Volumen de búsqueda por keyword | **GEO Metrics** `get_keyword_execution` (volumen + chatbot_preference + tendencia 12m) · o **DataForSEO** | Lectura de SERP / autocompletar (aproximación) |
| Dificultad de keyword | **DataForSEO** · Semrush / Ahrefs | Lectura cualitativa del SERP |
| Panorama generativo / prompts / share of voice | **GEO Metrics** `list_project_prompts`, `get_ranking_prompt_details`, `get_project_overview` | Consultas directas a motores (Chrome/paste) |
| Sentiment / comparación con competidores por IA | **GEO Metrics** `get_sentiment_extraction` | Consultas directas + lectura |
| Backlinks | **DataForSEO** · Semrush / Ahrefs | **No disponible** (marcar Nivel 2+) |
| Core Web Vitals (si se evalúa) | — | PageSpeed Insights (gratis) |

Si GEO Metrics está conectado pero el cliente **no tiene proyecto**, el agente lo
dice y propone crearlo, o tira de Nivel 1. Registra siempre qué herramienta dio
cada dato.

## Convención de trazabilidad (atómica)

Cada afirmación factual lleva, pegada:

`‹fuente: [tipo+ref] | acceso: AAAA-MM-DD | confianza: alta/media-alta/media/baja | tipo: hecho/interpretación/hipótesis›`

Tipos de fuente: `web: [URL]`, `serp: "[consulta]"`, `motor-geo: [motor] | consulta | método`,
`geo-metrics: [tool] | proyecto/prompt/execution`, `keywords: [herramienta]`,
`ckb: [módulo]`, `contexto-externo: [doc]`, `pagespeed: [URL]`.

**Atómica, no agregada:** cada cifra/porcentaje/precio/ranking lleva la fuente de
ESE dato. Una lista al pie del bloque no sustituye la etiqueta por dato. Datos
heredados de un workshop: marcar validado o hipótesis.

## Los entregables, en detalle

1. **`analisis_mercado_completo.md`** — todo el análisis por bloques (demanda y
   búsqueda; panorama generativo; estructura de mercado; E-E-A-T; utilidad de
   contenido; plataformas; influencers; vocabulario; intensidad del sector) +
   conclusiones. Es la fuente; los demás entregables son vistas derivadas.
2. **`top5_competidores.md`** — 5 que mejor posicionan en el nicho + highlights de
   por qué (visibilidad orgánica, presencia en IA, solapamiento). Puente al 2.2.
3. **`eeat_sector.md`** — elementos E-E-A-T concretos que premia ESTE mercado, con
   evidencia (no genéricos). Varían por sector.
4. **`top50_preguntas.md`** — ~50 preguntas reales del mercado y país objetivo,
   agrupadas por tema (insumo de contenido y del módulo prompt).
5. **`vocabulario_y_comunicacion.md`** — léxico que da profesionalidad, tono e
   identidad comunicativa del sector, nivel técnico esperado, términos a usar y a
   evitar.
6. **`plataformas_y_contenido.md`** — plataformas con veredicto entrar/no
   entrar/vigilar, qué tipo de contenido y qué elementos se premian (búsqueda e
   IA), con explicación.
7. **`posicion_e_intensidad.md`** — (a) posición del cliente: keywords donde está
   y donde no, presencia/ausencia, espacios y oportunidades; (b) **benchmark de
   intensidad del sector**: dificultad, intensidad y velocidad, y simulación
   orientativa de intensidad de trabajo para competir (piezas/mes, publicaciones,
   paid aproximado, dónde). **Benchmark, no plan.**
8. **`conclusiones_accionables.md`** — cada conclusión, afirmación verificable y
   autocontenida, con agente destino (ICP Agente 3 / Estrategia / Contenido / Voceros /
   Agente 2.2).

## Contrato del entregable 8 con los downstream

| Conclusión | Agente destino |
|------------|----------------|
| Top keywords priorizadas + posición del cliente | Estrategia · Contenido · ICP (Agente 3) |
| Top-5 competidores a diseccionar | Agente 2.2 |
| Elementos E-E-A-T concretos del sector | Contenido · ICP (Agente 3) |
| Top-50 preguntas / huecos de respuesta GEO | Contenido (Capa 3) |
| Vocabulario y línea de comunicación | Contenido · Voceros |
| Veredicto de plataformas y formatos premiados | Estrategia · Voceros |
| Benchmark de intensidad/velocidad del sector | Estrategia (Capa 2) |
| Segmentos de demanda prioritarios | ICP (Agente 3) |

Cada fila se lee sin abrir el resto del documento.
