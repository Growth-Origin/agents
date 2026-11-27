# Sistema anti-canibalización — Arquitecto de Sitio (Agente 5)

> La canibalización (dos o más URLs del mismo sitio compitiendo por la misma
> intención) diluye señales, degrada CTR y desestabiliza posiciones. En GEO el
> efecto es análogo: contenido fragmentado en varias URLs débiles genera menos
> citación que una URL consolidada y autoritativa. Se ataca en dos frentes.
> Idioma: español de España.

## Frente 1 — Detección de canibalizaciones existentes (Fase 2)

### Las 4 señales (vía Search Console)

| Señal | Cómo se mide | Umbral orientativo |
|-------|--------------|--------------------|
| Alternancia de URLs | Una misma query muestra 2+ URLs del sitio con impresiones significativas en el periodo | Segunda URL con ≥20 % de las impresiones de la primera |
| Inestabilidad de posición | Desviación de la posición media de la query anómalamente alta frente a queries de volumen similar | Evaluación relativa, no valor absoluto |
| CTR degradado | CTR de la query claramente inferior al esperable para su posición media | Comparación contra la curva CTR/posición del propio sitio |
| Duplicidad de intención on-page | Títulos/H1 de dos URLs apuntando a la misma intención (del crawl) | Revisión cualitativa asistida |

**Regla de las 2 señales:** ninguna señal aislada confirma canibalización; se
requieren **al menos dos señales concurrentes** para registrar un caso. Evita
falsos positivos (p. ej. un post de blog y una landing que coexisten
legítimamente en una query ambigua).

### Las 3 resoluciones posibles

| Resolución | Cuándo aplica | Acción resultante en el mapa |
|------------|---------------|-------------------------------|
| **Consolidar** | Misma intención, ninguna URL aporta valor diferencial; la débil no tiene enlaces ni negocio propio | Fusionar contenido en la URL fuerte + 301 de la débil. Acción CONSOLIDAR-REDIRIGIR |
| **Diferenciar** | Las intenciones son realmente distintas pero el contenido actual las confunde (títulos, enfoque) | Re-enfocar una de las URLs hacia su intención propia. Acción OPTIMIZAR en ambas, con nota de diferenciación |
| **Canonicalizar** | Duplicidad técnica o variantes necesarias por negocio (filtros, versiones) que no deben competir | Canonical hacia la URL principal. Acción MANTENER con nota técnica |

Cada caso queda en la pestaña «Canibalizaciones» del Excel con la query
afectada, las URLs implicadas, las señales concurrentes, la resolución propuesta
y su estado (aprobada o no en el checkpoint).

## Frente 2 — Prevención de canibalizaciones futuras (Fase 4)

La prevención **no es una fase separada: está embebida en el clustering**. La
decisión de si dos keywords van a la misma URL o a URLs distintas se toma
midiendo el **solapamiento de sus SERPs** (ver `clustering-entidades.md`). Si
Google muestra resultados mayoritariamente idénticos para dos keywords, las
trata como la misma intención → misma URL obligatoria. Si las SERPs difieren,
separarlas no es canibalizar: es cubrir intenciones distintas. La arquitectura
nace, por diseño, sin canibalizaciones.

La misma lógica se aplica a los prompts (regla de concentración): es preferible
que una entidad responda varios prompts afines a fragmentar prompts hermanos en
entidades distintas — autoridad concentrada cita más que contenido disperso.

## Modo degradado sin Search Console

Sin acceso a GSC, el Frente 1 opera en modo aproximado:

- Se detectan URLs del propio sitio que rankean simultáneamente para las mismas
  keywords (vía DataForSEO SERP en Nivel 2, u observación de SERP en Nivel 1).
- Se cruza con la duplicidad de intención on-page (títulos/H1 del crawl).
- **Cada caso se marca «detección aproximada — confirmar con GSC»** y la
  limitación se declara en la pestaña de configuración y en el
  `resumen_checkpoint.md`.

El quick-win bonus del TPS también pierde su fuente sin GSC: el factor se marca
como no disponible y su peso se redistribuye (ver `scoring.md`).
