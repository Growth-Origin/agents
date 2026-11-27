# Guía del circuito — las 7 fases (Arquitecto de Sitio, Agente 5)

> Objetivo y output de cada fase, y el efecto de cada escenario. El agente no
> fusiona fases: cada una valida la anterior. Idioma: español de España.

## Efecto del escenario sobre el circuito

| Escenario | Efecto |
|-----------|--------|
| **EXISTENTE** | Circuito completo de 7 fases. El caso más habitual. |
| **NUEVA** | Se omiten la Fase 2 (inventario) y la detección de canibalizaciones existentes; todas las entidades nacen con acción «Crear». La **prevención** de canibalizaciones futuras (solapamiento de SERP) se mantiene íntegra. El factor QuickWin del TPS es 0 y su peso se redistribuye. |
| **MIGRACIÓN** | Circuito completo + capa de mapeo de redirecciones URL antigua → nueva (pestaña extra del Excel). |

## Fase 1 — Configuración (checkpoint de marco)

**Objetivo:** fijar el marco antes de tocar ningún dato.
Escenario · acceso a GSC (sí/no + declaración de limitación) · restricciones del
cliente (URLs intocables, CMS, capacidad/mes) · pesos del TPS y umbrales de
solapamiento ajustados con el consultor · verificación de inputs (si falta uno
obligatorio, **detenerse y pedirlo; nunca inventar datos de partida**).
**Output:** ficha de configuración (portada técnica del entregable, pestaña 0).

## Fase 2 — Inventario y diagnóstico (se omite en NUEVA)

**Objetivo:** saber exactamente qué existe hoy y cómo rinde.
Crawl (DataForSEO On-Page en Nivel 2; sitemap + lectura en Nivel 1) → URLs
indexables con título, H1 y tipo de página. Cruce con GSC → por URL: queries
principales, impresiones, clics, posición media → **keyword principal actual**
(query dominante por impresiones ponderadas por posición). **Detección de
canibalizaciones** (ver `anti-canibalizacion.md`). Clasificación preliminar:
activo con rendimiento / activo sin rendimiento / huérfana / duplicada /
obsoleta.
**Output:** inventario diagnóstico + registro de canibalizaciones con resolución
propuesta.

## Fase 3 — Benchmarking de arquitecturas competidoras

**Objetivo:** identificar el estándar estructural del sector y los huecos para
superarlo. **No se copia: se aprende el patrón y se busca la asimetría.**
De los 3–4 competidores líderes del 2.2 (o de observación propia declarada):
mapa de secciones, ratio landings/blog, profundidad media de clusters,
arquitectura de landings locales si existe. **Capa GEO:** qué tipos de página
aparecen citados por las IAs en los tres tipos de prompt del 2.2 (patrón
típico: comparativas y guías con datos propios concentran citación; homes y
landings genéricas casi nunca). Síntesis en **3–5 principios de arquitectura del
sector** + huecos estructurales.
**Output:** tabla comparativa + principios + huecos.

## Fase 4 — Clustering keyword/prompt → entidad de contenido (checkpoint de entidades)

**Objetivo:** el corazón del agente. Convertir las listas priorizadas en
**entidades de contenido** (futuras URLs) con dos criterios combinados:
solapamiento de SERP y cobertura de prompts. Metodología en
`clustering-entidades.md`.
**Checkpoint intermedio:** se muestra al consultor el listado de entidades con
sus zonas grises **antes** del cruce completo de la Fase 5; en sitios grandes
evita rehacer el mapa entero si una decisión estructural cambia.
**Output:** listado de entidades, cada una con keywords, prompts, intención
dominante y tipo.

## Fase 5 — Mapa de URLs final

**Objetivo:** cruzar inventario (F2) × entidades (F4) y asignar **una y solo una
acción** por elemento: MANTENER / OPTIMIZAR / CREAR / CONSOLIDAR-REDIRIGIR /
ELIMINAR.

| Acción | Condición |
|--------|-----------|
| MANTENER | URL existente que ya cubre bien su entidad (rendimiento correcto, sin canibalización) |
| OPTIMIZAR | URL existente con rendimiento mejorable o cobertura de prompts incompleta |
| CREAR | Entidad sin URL existente que la cubra |
| CONSOLIDAR-REDIRIGIR | Dos o más URLs sobre la misma entidad (resolución «consolidar»): fusión en la fuerte + 301 |
| ELIMINAR | URL sin entidad, sin tráfico, sin enlaces externos y sin valor de negocio declarado (las 4 a la vez) |

**Regla de prudencia:** Eliminar es lo más irreversible; exige las 4 condiciones
y revisión individual en el checkpoint. Ante la duda, Consolidar-Redirigir (que
preserva señales). Las URLs intocables del cliente quedan excluidas de
Optimizar/Consolidar/Eliminar.

**Doble capa del mapa:**

- **Plan de landings** (jerarquía descendente): Nivel 1 landings madre (una por
  servicio/producto core del CKB) · Nivel 2 landings variante (segmentos del ICP
  o casos de uso **con entidad propia que las justifique** — regla
  anti-inflación) · Nivel 3 landings locales (solo con componente geográfico; la
  granularidad la marca el hueco del benchmarking) · páginas comparativas (la
  apuesta GEO más directa, tratamiento editorial propio).
- **Clusters de blog** (pillar-cluster): cada pillar **declara la landing que
  alimenta** (sin salida a negocio, su TPS cae, salvo justificación GEO
  documentada); cada cluster lleva su **vocero recomendado** (del CKB) como
  palanca E-E-A-T/GEO — la ejecución es del agente de producción.

**Output:** mapa de URLs definitivo en doble capa, con acción, keywords y
prompts por URL.

## Fase 6 — Estrategia de interlinking

**Objetivo:** reglamento explícito de enlazado (R1–R5, anchors, 3 clics, cero
huérfanas, señalización GEO) + **matriz de enlaces obligatorios** para las URLs
de Olas 1–2. Detalle en `interlinking.md`.

## Fase 7 — Roadmap priorizado + checkpoint final (OBLIGATORIO)

**Objetivo:** puntuar cada tarea con el TPS (`scoring.md`), organizarlas en olas
según la capacidad de producción, y **detenerse** en el checkpoint del
consultor.

**Qué se presenta en el checkpoint:**

1. Resumen ejecutivo de la arquitectura (cifras clave, principios aplicados,
   apuestas diferenciales).
2. Puntos de decisión abiertos: todas las zonas grises (solapamiento 30–59 %)
   con la propuesta del agente y su justificación.
3. Lista completa de eliminaciones y consolidaciones, una a una.
4. Desviaciones deliberadas respecto al benchmarking, y por qué.
5. Incidencias derivadas (hallazgos fuera de alcance, huecos del estudio del
   Agente 4) para derivar al proceso correspondiente.

**Resultados posibles:** aprobado (se emite el entregable) · aprobado con
cambios (se incorporan, se recalculan los TPS afectados y se emite) · revisión
mayor (se vuelve a la fase correspondiente con la nueva directriz; **no se
parchea sobre el resultado**). El acta de validación queda en
`resumen_checkpoint.md` y en el `audit`.
