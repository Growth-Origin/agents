# Plantilla del Excel y del sitemap visual — Arquitecto de Sitio (Agente 5)

> El entregable principal es un libro Excel (`arquitectura_sitio.xlsx`) de
> **8 pestañas** (9 en escenario MIGRACIÓN). Se construye con la skill **xlsx**.
> Si el entorno no puede generar Excel, se producen los datos en `.md`/`.csv`
> con la misma estructura y se avisa. Idioma del contenido: español de España
> (keywords, prompts y anchors se conservan en su idioma).

## Pestaña 0 — «Configuración»

Ficha del engagement (portada técnica): escenario · nivel de investigación ·
acceso a GSC (y modo degradado si aplica) · restricciones del cliente (URLs
intocables, CMS, capacidad/mes) · pesos TPS aplicados · umbrales de solapamiento
aplicados · inputs recibidos y faltantes declarados · estimación y gasto real de
Nivel 2. Columnas: Parámetro · Valor · Observaciones.

## Pestaña 1 — «Mapa de URLs final»

Todas las URLs del estado final del sitio.

| Columna | Contenido |
|---------|-----------|
| URL | Actual o propuesta |
| Acción | Mantener / Optimizar / Crear / Consolidar-Redirigir / Eliminar |
| Tipo | Landing madre/variante/local · comparativa · pillar · satélite · otra |
| Capa | Landings / Blog / Corporativa |
| Keywords asignadas | Con su KPS (del Agente 4) |
| Prompts asignados | Con su PPS |
| Cluster / Jerarquía | A qué cluster o rama de landings pertenece |
| Justificación | Dato que sostiene la acción (solapamiento, GSC, benchmarking) |
| TPS | Score de la tarea asociada |
| Ola | 1 / 2 / 3 |

## Pestaña 2 — «Plan de landings»

Jerarquía comercial completa. Columnas: Landing · Nivel
(madre/variante/local/comparativa) · Servicio del CKB · Entidad ·
Justificación de existencia (regla anti-inflación: entidad con demanda propia).

## Pestaña 3 — «Clusters de blog»

Pillars y satélites por cluster. Columnas: Cluster · Pillar · Satélites ·
Landing que alimenta · Vocero recomendado · Justificación GEO si no alimenta
landing.

## Pestaña 4 — «Matriz prompt → URL»

Cada prompt priorizado y su URL responsable. Columnas: Prompt · PPS · URL
asignada · Tipo de intención · Regla aplicada (cobertura total / afinidad /
concentración) · Estado de citación (si GEO Metrics está conectado).

## Pestaña 5 — «Canibalizaciones»

Casos detectados y su resolución. Columnas: Query afectada · URLs implicadas ·
Señales concurrentes · Resolución (consolidar/diferenciar/canonicalizar) ·
Detección (GSC / aproximada) · Estado (aprobada en checkpoint).

## Pestaña 6 — «Interlinking»

Reglamento (R1–R5, política de anchors, 3 clics, cero huérfanas, señalización
GEO) + matriz de enlaces obligatorios de Olas 1–2. Columnas de la matriz: URL ·
Enlaces entrantes mínimos · Enlaces salientes mínimos · Anchor principal ·
Variantes de anchor.

## Pestaña 7 — «Roadmap por olas»

Todas las tareas ordenadas. Columnas: Tarea · Acción · URL · TPS (desglosado
por factor: Potencial / QuickWin / Negocio / Esfuerzo) · Ola · Dependencias
entre tareas.

## Pestaña 8 — «Redirecciones» (solo MIGRACIÓN)

Mapeo completo. Columnas: URL origen · URL destino · Tipo (301) · Motivo.

## Entregable secundario: sitemap visual (`sitemap_visual.html`)

Representación gráfica del estado final: jerarquía de landings, clusters con
sus pillars y satélites, y flechas del flujo de autoridad principal (R1).
Formato HTML autocontenido (o Mermaid embebido) que se abre en el navegador.
Función de comunicación: **el Excel es el documento de trabajo; el sitemap
visual es el que se presenta al cliente**. Marca con color la acción de cada
nodo (crear / optimizar / mantener / consolidar) y no incluye ningún dato que no
esté ya en el Excel.

## Cómo construirlo

1. Termina las Fases 1–7 con el checkpoint aprobado.
2. Lee la skill **xlsx** y genera el libro con las pestañas y columnas de arriba.
3. Cada fila del mapa lleva su justificación; los datos que falten llevan su
   marca («requiere herramienta (Nivel 2+)», «estimado», «modo degradado»).
4. Genera el sitemap visual desde el mapa final.
5. Guarda todo en `clientes/[slug-cliente]/arquitectura-sitio/`.
