# Contexto incompleto y estudio externo — Arquitecto de Sitio (Agente 5)

> Cómo trabajar cuando **faltan** inputs aguas arriba: el Excel del Agente 4, los
> módulos del CKB, el benchmarking del 2.2 o el acceso a Search Console.
> Objetivo: rendir con lo que haya, declarar la degradación y **preguntar lo
> crítico** antes de diseñar. Idioma: español de España (peninsular).

## Principio

El contexto ideal es Agente 4 + CKB + 2.2 (+ 2.1 e ICP). Pero el agente **no
depende en duro** de ninguno: normaliza lo que reciba, marca lo que falta y
pregunta cuando el hueco es decisivo. No inventa. La arquitectura hereda la
fiabilidad de sus inputs, y esa fiabilidad **se declara** en la pestaña de
configuración y en el checkpoint.

## Orden de actuación ante un hueco (supón lo menos posible)

1. **Investigar primero (Nivel 1, coste cero):** web del cliente, sitemap,
   observación de SERP, benchmarking propio de competidores. Lo que se cierre,
   con su fuente y confianza.
2. **Preguntar si es decisivo:** si el hueco afecta a la jerarquía de landings,
   a la ponderación del TPS o a acciones irreversibles, **parar y preguntar**.
3. **Hipótesis visible (último recurso):** trazada, listada en el mapa de
   huecos, nunca escondida dentro de una decisión.

## Qué hacer si falta cada input

### Falta el Excel del Agente 4 (el input principal)

Dos vías, en este orden:

1. **Estudio externo que se normaliza.** El operador aporta un keyword research
   previo (de otra agencia, un export de herramienta, un Excel propio). El
   agente lo lee y lo **normaliza** a la estructura mínima: keyword/prompt ·
   intención · volumen (si lo trae) · prioridad aparente. Declara lo que el
   estudio externo NO trae: **scores KPS/PPS** (el Potencial del TPS se
   aproxima por volumen × intención, declarándolo), **filtro anti-persona** (se
   pregunta al consultor qué tráfico NO se quiere; sin respuesta, se marca el
   riesgo) y **prompts** (si no hay estudio de prompts, la capa GEO queda
   degradada: la matriz prompt→URL se construye solo con los prompts que el
   operador aporte o se marca como pendiente del Agente 4).
2. **Si no hay nada,** el agente lo dice con claridad y **propone ejecutar antes
   el Agente 4** (o, como mínimo, un pase rápido de su Fase 1–3). Diseñar
   arquitectura sin universo priorizado es construir sobre humo; el agente no lo
   hace en silencio.

La normalización queda en `_fuentes/contexto_normalizado.md` con el origen de
cada campo: `‹contexto-externo: [doc] | acceso | confianza | tipo›`.

### Faltan los módulos del CKB

- **Servicios/productos:** se extraen de la web del cliente (navegación,
  páginas de servicio), declarándolo.
- **Prioridades de negocio:** **se preguntan siempre** — ponderan el factor
  Negocio del TPS y ordenan la jerarquía de landings; sin ellas no hay
  priorización fiable.
- **Voceros:** la recomendación de vocero por cluster queda vacía con nota
  «pendiente de CKB»; no se inventan nombres.

### Falta el benchmarking del 2.2

El agente hace una **aproximación declarada**: observa la estructura de 2–3
competidores evidentes (sitemap + lectura de secciones) para extraer el patrón
del sector. Lo marca `‹benchmark: [competidor] | aproximación›`, señala que la
capa de citación IA queda sin fuente (eso lo daba el 2.2) y propone ejecutar el
2.2 si la arquitectura va a apoyarse fuerte en la asimetría estructural.

### Faltan el 2.1 o el ICP

Se pierde calibración, no viabilidad: la granularidad de landings locales y la
capa de personas de la matriz quedan menos ancladas. Se señala y se sigue.

### Falta Search Console

Ver el **modo degradado** en `anti-canibalizacion.md`: detección aproximada
marcada caso a caso, quick-win sin fuente (peso redistribuido, ver
`scoring.md`), y la limitación declarada en la configuración.

## Mapa de huecos (se muestra en el checkpoint de la Fase 1)

~~~markdown
# Mapa de huecos — [Cliente]

| Input faltante | ¿Decisivo? | Qué investigué (Nivel 1) y encontré | Estado |
|----------------|-----------|--------------------------------------|--------|
| [p. ej. Excel del Agente 4] | Sí | Normalizado estudio de [agencia]; sin KPS/PPS ni anti-persona | **PREGUNTA al consultor** (anti-persona) |
| [p. ej. benchmarking 2.2] | No | Observados 3 competidores (sitemap) | Aproximación declarada |
| [p. ej. GSC] | No | — | Modo degradado activo |

## Necesito que respondas antes de seguir
- [pregunta concreta 1]
- [pregunta concreta 2]
~~~

## Aviso de calidad

- Lo que venga sin fuente se trata como **hipótesis**, no como hecho, y se dice.
- Si más adelante se ejecutan los agentes que faltaban (4, 2.2, CKB), la
  arquitectura se **re-calibra** sin rehacer el método: se recalculan TPS y se
  revisan las zonas grises con los datos nuevos.
- **Peor de los casos: preguntar más.** Una pregunta extra al consultor es
  preferible a una arquitectura construida sobre supuestos no validados.
