# Clustering keyword/prompt → entidad de contenido — Fase 4 (Agente 5)

> Una **entidad de contenido** es una futura URL: la unidad mínima de la
> arquitectura. La Fase 4 transforma las listas priorizadas del Agente 4
> (keywords con KPS, prompts con PPS) en entidades, en tres pasos. Idioma:
> español de España.

## Paso 1 — Agrupación de keywords por solapamiento de SERP

Para cada par de keywords candidatas a convivir se comparan sus SERPs (top 10)
y se calcula el porcentaje de URLs compartidas:

```
solapamiento(kw_A, kw_B) = URLs_comunes_top10 / 10
```

| Solapamiento | Interpretación | Decisión |
|--------------|----------------|----------|
| ≥ 60 % | Google trata ambas como la misma intención | **Misma URL obligatoria** |
| 30–59 % | Zona gris: intenciones parcialmente solapadas | **Evaluación cualitativa**: el agente propone y justifica; el consultor decide en el checkpoint |
| < 30 % | Intenciones distintas | **URLs separadas** |

Los umbrales son **configurables en la Fase 1** (en sectores con SERPs muy
volátiles conviene endurecer el umbral superior). Los valores aplicados quedan
en el `audit` y en la pestaña de configuración.

### Control de coste (obligatorio)

No se comparan todos los pares posibles:

1. **Pre-agrupación semántica y de raíz léxica** (barata, sin API): candidatos
   evidentes a convivir.
2. **Verificación con SERP solo de los pares frontera**: dentro de cada
   pre-grupo y en los límites entre grupos.
3. **Caché local de SERPs**: una SERP consultada no se repaga; los solapamientos
   calculados se guardan en `_fuentes/solapamientos.csv`.

**En Nivel 1** (sin API): la verificación es **muestral** — solo los pares
dudosos que la pre-agrupación señala, observados a mano o pegados por el
operador. Cada agrupación se marca **«verificado»** o **«estimado»**; la
proporción de estimados se declara en el entregable.

## Paso 2 — Asignación de prompts a entidades (capa GEO)

Cada prompt priorizado del Agente 4 se asigna a la entidad que debe responderlo,
con tres reglas:

- **Regla de cobertura total:** ningún prompt del top priorizado queda huérfano.
  Si un prompt no encaja en ninguna entidad nacida de las keywords, **genera su
  propia entidad** (hay intenciones conversacionales sin equivalente en keyword —
  es uno de los hallazgos estructurales del enfoque híbrido).
- **Regla de afinidad de intención:** el prompt va a la entidad cuya intención
  dominante coincide con la suya (informacional → pillar/satélite; comparativa →
  página comparativa; transaccional → landing).
- **Regla de concentración:** es preferible que una entidad responda varios
  prompts afines a fragmentar prompts hermanos en entidades distintas (lógica
  anti-canibalización aplicada a GEO: autoridad concentrada cita más).

El resultado es la **matriz prompt → URL** (pestaña propia del Excel), que el
agente de producción usará para el diseño answer-first de cada contenido. Si GEO
Metrics está conectado, el estado de citación actual de cada prompt enriquece la
matriz (lectura sin coste).

## Paso 3 — Tipificación de cada entidad

| Tipo | Intención dominante | Capa |
|------|---------------------|------|
| **Landing madre** | Transaccional/comercial principal (servicio o producto core) | Landings |
| **Landing variante** | Transaccional específica (variante, segmento, caso de uso) | Landings |
| **Landing local** | Transaccional + geográfica (si el negocio lo requiere) | Landings |
| **Página comparativa** | Comercial-investigación («X vs Y», «mejores X») — el tipo con máxima citación IA según el benchmarking típico | Landings / híbrida |
| **Pillar** | Informacional amplia (tema completo) | Blog |
| **Satélite** | Informacional específica (subtema del pillar) | Blog |

Cada entidad sale de la fase con: keywords asignadas (con KPS), prompts
asignados (con PPS), intención dominante, tipo y — tras la Fase 5 — su acción y
su lugar en la jerarquía.

## Checkpoint de entidades (antes de la Fase 5)

Se presenta al consultor: el listado de entidades, las **zonas grises** con
propuesta justificada, los prompts que generaron entidad propia y la proporción
verificado/estimado. En sitios grandes este checkpoint intermedio evita rehacer
el mapa completo si el consultor cambia una decisión estructural.
