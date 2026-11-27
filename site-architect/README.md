# Arquitecto de Sitio — Agente 5 (3.2 en la spec)

El **puente entre la estrategia y la producción**: convierte el universo
priorizado de keywords y prompts del Agente 4 en la **arquitectura definitiva
del sitio** — qué URLs existirán, cuáles se crean, se optimizan, se consolidan o
se eliminan — con prevención de canibalizaciones basada en datos y visión
híbrida SEO + GEO. Opera **humano-en-el-bucle** con checkpoint obligatorio.
Idioma de salida: **español de España**.

## Cómo se invoca

- «agente 5» / «agente 3.2» / «site-architect»
- «diseña la arquitectura de [cliente]» / «arquitecto de sitio»
- «mapa de URLs» / «plan de landings» / «clusters de blog» / «interlinking»

**Antes de invocarlo**, ten a mano: el Excel del **Agente 4** (o un keyword
research externo que el agente normaliza), los módulos del CKB
(servicios/prioridades/voceros), el bloque de arquitectura del **2.2**, y — si
el sitio existe — el export de **Search Console** (12–16 meses). Todo lo que
falte tiene fallback declarado; lo decisivo se pregunta.

## Cómo trabaja (paso a paso)

1. **Paso 0 — Nivel de investigación (te pregunta siempre):** Nivel 1 (sin
   herramientas: inventario por sitemap, solapamiento muestral «estimado») o
   Nivel 2 (DataForSEO On-Page + SERP) **con estimación de coste antes de
   proceder** — el solapamiento de SERP se paga por par verificado.
2. **Fase 1 — Configuración (checkpoint):** escenario (existente / nueva /
   migración), restricciones (URLs intocables, CMS, capacidad/mes), pesos del
   TPS y umbrales de solapamiento.
3. **Fase 2 — Inventario:** crawl + GSC → keyword principal por URL + detección
   de canibalizaciones (mínimo 2 señales concurrentes; modo degradado sin GSC).
4. **Fase 3 — Benchmarking:** patrones estructurales de los líderes del 2.2 y
   qué tipos de página generan citación IA; 3–5 principios del sector + huecos.
5. **Fase 4 — Clustering (checkpoint):** keywords agrupadas por solapamiento de
   SERP (≥60 % misma URL · 30–59 % zona gris · <30 % separadas), prompts
   asignados (ningún prompt huérfano) y entidades tipificadas.
6. **Fase 5 — Mapa final:** una acción por URL (mantener / optimizar / crear /
   consolidar-redirigir / eliminar), plan de landings con regla anti-inflación y
   clusters con vocero recomendado.
7. **Fase 6 — Interlinking:** reglamento R1–R5, anchors, 3 clics, cero
   huérfanas, señalización GEO + matriz de enlaces obligatorios.
8. **Fase 7 — Roadmap + checkpoint final (obligatorio):** TPS por tarea, olas de
   trabajo, y validación del consultor (zonas grises, eliminaciones una a una)
   antes de emitir nada definitivo.

## Qué outputs genera

En `clientes/[slug-cliente]/arquitectura-sitio/`:

| Archivo | Qué es |
|---------|--------|
| `arquitectura_sitio.xlsx` | Libro de 8 pestañas (9 en migración): Configuración · Mapa de URLs · Plan de landings · Clusters · Matriz prompt→URL · Canibalizaciones · Interlinking · Roadmap por olas · (Redirecciones). |
| `sitemap_visual.html` | Diagrama del estado final para presentar al cliente. |
| `resumen_checkpoint.md` | Lo presentado en el checkpoint + acta de validación. |
| `_fuentes/` y `audit/` | Crawl, GSC, solapamientos con caché, y registro de nivel/coste/validaciones. |

## Quién consume su salida (downstream)

- **Siguiente agente de Capa 3 (briefs y producción):** el mapa de URLs, la
  matriz prompt→URL y las reglas de interlinking son sus inputs directos.
- **Capa 4 (medición):** el mapa de URLs final es el universo de seguimiento
  SEO/GEO (cada URL lleva sus keywords y prompts objetivo).

## Lo que NO hace

No redacta contenidos ni briefs, no audita salud técnica (velocidad, CWV, logs),
no implementa nada en el CMS, no pone fechas (olas, no calendario) y no rehace
el estudio del Agente 4 (los huecos se reportan como incidencia).

## Buenas prácticas

- **El checkpoint no es opcional:** un error de arquitectura se multiplica en
  cada contenido producido. Revisa las eliminaciones una a una.
- Sin GSC el agente funciona, pero la detección de canibalizaciones es
  aproximada: consigue el acceso o el export siempre que puedas.
- En Nivel 2, la pre-agrupación semántica y la caché de SERPs son las que
  mantienen el coste a raya; no fuerces la verificación de todos los pares.
- Es re-ejecutable: ante un rediseño o expansión, nueva versión del mapa con
  fecha, sin rehacer el método.
