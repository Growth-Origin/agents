# Esquema del análisis competitivo — Agente 2.2

> Define la estructura del output del Competitive Intelligence Agent: los once
> temas, la síntesis accionable (4.11), la estructura de carpetas, la convención
> de trazabilidad, los inputs desde el CKB y el Agente 2.1, y el mapa tema→fuente
> con qué es Nivel 1 y qué queda en Nivel 2+. El esquema es estable; cambia el
> contenido, no las secciones.

## Idioma

Todo el contenido en **español de España (peninsular)**. Tú (singular) y vosotros
(plural): tienes, queréis, podéis, dime, mira, fíjate. **Prohibido cualquier
argentinismo** (vos, tenés, querés, podés, decime, mirá, fijate sin tilde, dale
como «ok», armá, pegá, andá, bárbaro, re- como intensificador, qué onda, laburo,
guita, che). Las citas literales se conservan en su idioma original.

## Estructura de carpetas del output

Dentro de la carpeta de trabajo, bajo `clientes/[slug-cliente]/`:

```
clientes/[slug-cliente]/
└── competitive-intelligence/
    ├── propuesta_competidores.md     # Lista priorizada + justificación (Paso 1, validada)
    ├── analisis_competitivo.md       # Los 11 temas por competidor (documento principal)
    ├── sintesis_accionable.md        # Tema 4.11 standalone (contrato downstream)
    ├── resumen_ejecutivo.pdf         # Resumen presentable 2-4 págs (plantilla-resumen-pdf.md)
    ├── _fuentes/
    │   ├── [competidor]_geo.md       # Auditoría generativa: consultas, repeticiones, citas, variabilidad
    │   ├── [competidor]_web.md       # Crawl/lectura: arquitectura, interlinking, E-E-A-T, hacks, CMS, CWV
    │   └── serp_keywords.md          # Observación de SERP y aproximaciones (lo exacto es Nivel 2+)
    └── audit/
        ├── execution_log.json        # Parámetros, competidores, búsquedas vs presupuesto, temas Nivel 2+
        └── sources_accessed.json     # Fuentes accedidas con fecha y método
```

Cabecera de `analisis_competitivo.md`:

```markdown
# Análisis competitivo — [Nombre Cliente]

**Versión:** 0.1
**Fecha:** AAAA-MM-DD
**Nivel de implementación:** 1 (sin APIs de pago)
**Parámetros de enfoque:** sector/nicho, modelo, geografía, características, tipo de competidor
**Competidores analizados:** [lista validada]
**CKB de origen:** ruta y versión
**Análisis de mercado de origen (2.1):** ruta y versión
**Motores generativos auditados:** [...] (método: navegador / Chrome / paste / API)
```

## Estructura interna de cada tema

Cada uno de los once temas se redacta en formato **insight → implicación →
acción**:

- **Insight:** qué hace el competidor (con el dato y su fuente).
- **Implicación:** por qué le funciona / qué ventaja le da.
- **Acción:** qué debe hacer el cliente para replicarlo, mejorarlo o superarlo.

Nada descriptivo sin su acción asociada. Usa tablas para lo comparable.

## Convención de trazabilidad

Cada afirmación factual lleva, pegada:

`‹fuente: [tipo+ref] | acceso: AAAA-MM-DD | confianza: alta/media-alta/media/baja | tipo: hecho/interpretación/hipótesis›`

Tipos de fuente válidos:

- `web: [URL]` — página del competidor o dato indexado.
- `serp: "[consulta]"` — observación directa del SERP (aproximación, no dato de herramienta).
- `motor-geo: [motor] | consulta: "..." | método: navegador/chrome/paste/api | repeticiones: N` — auditoría generativa.
- `pagespeed: [URL]` — Core Web Vitals vía PageSpeed Insights.
- `ckb: [módulo]` / `mercado-2.1: [bloque]` — datos heredados de agentes upstream.
- `herramienta: [DataForSEO/SE Ranking/GEO Metrics]` — solo cuando se active Nivel 2.

**Trazabilidad atómica, no agregada.** Cada cifra, ranking o dato técnico lleva la
fuente de ESE dato; una lista al pie del tema no sustituye la etiqueta por dato.
Los datos heredados se marcan validados o hipótesis según venían del CKB/2.1: no
conviertas en hecho lo que upstream dejó sin validar.

Regla de oro: sin fuente real, no hay afirmación. Lo no recuperable va a «dato no
disponible» o «requiere herramienta (Nivel 2+)», nunca se inventa.

## Inputs: del CKB y del Agente 2.1

| Fuente | Uso |
|--------|-----|
| CKB — sector, oferta, propuesta de valor | Contexto del cliente y filtro de comparabilidad |
| CKB — canales y activos actuales | Base para comparar con el competidor |
| Agente 2.1 — fuentes citadas por IA, E-E-A-T del sector | Evita duplicar; ancla el benchmark E-E-A-T (4.7) |
| Agente 2.1 — lista nominada de competidores (notas downstream) | Punto de partida de la propuesta del Paso 1 |
| Parámetros de enfoque (Paso 0) | Acotan todo el análisis |

## Los once temas

1. **4.1 Rendimiento de búsqueda (SEO clásico)** — top keywords que le aportan
   tráfico, páginas mejor posicionadas, keyword gap vs cliente. *(Nivel 2+ para
   volúmenes/tráfico exactos; Nivel 1 aproxima por SERP.)*
2. **4.2 Rendimiento generativo (GEO)** — para qué consultas lo citan los motores,
   qué páginas suyas se llevan las citas, cruce SEO↔GEO.
3. **4.3 Opinión de las IAs sobre el competidor** — preguntas de mercado +
   comparativas + sobre el propio competidor, con repeticiones. Bloque
   diferencial.
4. **4.4 Perfil de enlaces (backlinks)** — mejores enlaces, patrones de
   link-building, link gap. *(Nivel 2+: requiere SE Ranking; en Nivel 1 se marca
   pendiente.)*
5. **4.5 Arquitectura web** — estructura, jerarquía, qué le da ventaja, qué
   podría mejorar.
6. **4.6 Interlinking y clusters de contenido** — enlazado interno, páginas
   pilar, topical authority, huecos.
7. **4.7 Estructura E-E-A-T del competidor** — benchmark de las cuatro
   dimensiones, anclado en lo que el 2.1 dijo que premia el sector.
8. **4.8 Hacks de utilidad de contenido** — técnicas replicables (answer-first,
   pasajes autocontenidos, tablas, FAQs, frescura).
9. **4.9 Personalidad comunicativa** — tono, ángulo editorial, formatos propios;
   qué es replicable y qué es inimitable.
10. **4.10 CMS, código y UX** — stack y CMS (detectables), schema/datos
    estructurados, Core Web Vitals (PageSpeed), decisiones de UX. *(Site audit
    profundo: Nivel 2+.)*
11. **4.11 Síntesis accionable (capa puente)** — ver contrato abajo.

Detalle de campos en `plantillas-temas.md`.

## Mapa tema → fuente y nivel

| Tema | Fuente Nivel 1 (sin APIs) | Fuente Nivel 2+ |
|------|---------------------------|-----------------|
| 4.1 Keywords/páginas top/gap | Observación de SERP (aprox.) | DataForSEO (exacto) |
| 4.2 Rendimiento generativo | Consultas directas a motores | GEO Metrics |
| 4.3 Opinión de la IA | Consultas directas + repeticiones | GEO Metrics |
| 4.4 Backlinks + link gap | **No disponible** (marcar pendiente) | SE Ranking |
| 4.5 Arquitectura web | Crawl + lectura del agente | DataForSEO (crawl) |
| 4.6 Interlinking y clusters | Muestreo + análisis del agente | DataForSEO (crawl) |
| 4.7 E-E-A-T competidor | Lectura de páginas + 2.1 | — |
| 4.8 Hacks de utilidad | Lectura del agente | — |
| 4.9 Personalidad comunicativa | Lectura del agente | — |
| 4.10 CMS/código/UX | HTML + cabeceras + PageSpeed (gratis) | SE Ranking (site audit) |

## Contrato de la síntesis accionable (tema 4.11)

Cierre que los downstream consumen primero. Por competidor y de forma agregada;
cada conclusión, afirmación verificable y autocontenida con su agente destino.

| Conclusión accionable | Agente destino |
|-----------------------|----------------|
| Keywords y páginas a atacar (gaps) | Estrategia · Contenido |
| Prompts/IA donde el competidor es fuerte y el cliente debe entrar | Estrategia · Contenido |
| Qué opina la IA del competidor y qué aprender de ello | Estrategia · ICP (1.2) |
| Objetivos de backlinks (link gap) | Estrategia (Capa 2) |
| Mejoras de arquitectura e interlinking a replicar/superar | Estrategia · Contenido |
| Elementos E-E-A-T y de autoría a construir | Contenido · ICP (1.2) |
| Hacks de utilidad replicables | Contenido (Capa 3) |
| Elementos de personalidad / UX / CMS a considerar | Estrategia · Contenido |

Cada fila debe poder leerse sin abrir el resto del documento. Si una fila depende
de un dato Nivel 2+ aún no disponible, se incluye igual con la nota de qué
herramienta la completará.
