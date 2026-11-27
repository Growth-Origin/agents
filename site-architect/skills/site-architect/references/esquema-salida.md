# Esquema de salida — Arquitecto de Sitio (Agente 5)

> Estructura del output, inputs con fallback, convención de trazabilidad y
> plantilla de recogida del Paso 0 y la Fase 1. El esquema es estable; cambia el
> contenido, no las secciones. Idioma: español de España (peninsular).

## Idioma

Todo en **español de España (peninsular)**. Tú (singular) y vosotros (plural):
tienes, queréis, podéis, dime, mira, fíjate. **Prohibido cualquier argentinismo**
(vos, tenés, querés, podés, decime, mirá, fijate sin tilde, dale como «ok», armá,
pegá, andá, bárbaro, re- como intensificador, qué onda, laburo, guita, che). Las
citas literales (keywords, prompts, anchors, títulos) se conservan en su idioma
original.

## Estructura de carpetas del output

Dentro de la carpeta de trabajo, bajo `clientes/[slug-cliente]/`:

```
clientes/[slug-cliente]/
└── arquitectura-sitio/
    ├── arquitectura_sitio.xlsx     # Entregable principal (8-9 pestañas, ver plantilla-excel.md)
    ├── sitemap_visual.html         # Diagrama del estado final (comunicación con el cliente)
    ├── resumen_checkpoint.md       # Lo presentado en el checkpoint + acta de validación
    ├── _fuentes/
    │   ├── contexto_normalizado.md # Si hubo paquete externo o inputs faltantes
    │   ├── inventario_crawl.csv    # Crawl del sitio (DataForSEO o sitemap+lectura)
    │   ├── gsc_export.csv          # Export de Search Console (si lo hay)
    │   └── solapamientos.csv       # Pares verificados con su % (y caché de SERPs)
    └── audit/
        ├── execution_log.json      # Nivel, escenario, pesos, umbrales, estimación y gasto real, checkpoints
        └── sources_accessed.json   # Fuentes accedidas con fecha y método
```

Cabecera del `resumen_checkpoint.md` y metadatos del libro:

```markdown
# Arquitectura de sitio — [Cliente]

**Versión:** 0.1   ·   **Fecha:** AAAA-MM-DD
**Escenario:** EXISTENTE / NUEVA / MIGRACIÓN
**Nivel de investigación:** 1 (sin herramientas) / 2 (DataForSEO On-Page + SERP [+ GSC API])
**Acceso a Search Console:** sí / no (modo degradado declarado)
**Pesos TPS:** w1=[0.45] w2=[0.25] w3=[0.30]  ·  **Umbrales solapamiento:** ≥[60]% / [30–59]%
**Inputs:** Agente 4 / CKB / 2.2 / 2.1 / ICP — rutas y versiones (o faltantes declarados)
**Estado:** borrador pendiente de checkpoint / validado (acta AAAA-MM-DD)
```

## Inputs con fallback (desacople)

| Input | Origen ideal | Si falta |
|-------|--------------|----------|
| Universo priorizado (keywords + prompts) | Agente 4 (Excel 4 pestañas) | Estudio externo normalizado (`plantilla-contexto-externo.md`); sin nada, proponer ejecutar el Agente 4 |
| Servicios, prioridades, voceros | CKB (1.1), carga selectiva vía índice maestro | Web del cliente o brief, declarado; prioridades de negocio se **preguntan** |
| Bloque de arquitectura competitiva | Agente 2.2 | Observación propia de 2–3 competidores (aproximación declarada) |
| Contexto de mercado (E-E-A-T, plataformas) | Agente 2.1 (recomendado) | Se omite la calibración; se señala |
| Matriz persona×etapa×intención | Agente 3 (ICP, recomendado) | Contexto para landings menos calibrado; se señala |
| Crawl del sitio | DataForSEO On-Page (Nivel 2) o sitemap+lectura (Nivel 1) | Solo se omite en NUEVA |
| Search Console | Cliente (export/API) | **Modo degradado** (ver `anti-canibalizacion.md`) |

## Convención de trazabilidad

Cada decisión estructural y cada dato llevan, pegados:

`‹fuente: [tipo+ref] | acceso: AAAA-MM-DD | confianza: alta/media-alta/media/baja | tipo: hecho/aproximación/hipótesis›`

Tipos de fuente válidos:

- `agente-4: [pestaña/fila]` — keywords, prompts, KPS/PPS heredados.
- `ckb: [módulo]` / `competidores-2.2: [tema]` / `mercado-2.1: [bloque]` / `icp: [perfil]` — heredados.
- `crawl: [URL]` — dato del inventario (título, H1, tipo de página).
- `gsc: [query|página]` — impresiones, clics, posición media, canibalización.
- `serp-overlap: [kwA]↔[kwB] NN% (verificado/estimado)` — decisión misma-URL-o-no.
- `benchmark: [competidor]` — patrón estructural observado.
- `contexto-externo: [doc]` — paquete externo normalizado.
- `cliente: [restricción/prioridad]` — input del consultor o el cliente.

Sin fuente real, no hay decisión: lo no recuperable va a «requiere herramienta
(Nivel 2+)» o «dato no disponible», nunca se inventa. Los datos heredados se
marcan validados o hipótesis según venían de upstream.

## Plantilla de recogida (Paso 0 + Fase 1)

~~~text
Antes de diseñar la arquitectura necesito configurar el engagement.

1) NIVEL DE INVESTIGACIÓN
- Nivel 1 (sin herramientas de pago): inventario por sitemap + lectura; solapamiento de SERP
  muestral (marcado «estimado»); canibalizaciones por señales on-page (+ GSC si me pasas el export).
- Nivel 2 (con herramientas): DataForSEO On-Page (crawl) + SERP (solapamiento medido).
  ⚠️ El solapamiento cobra por llamada (2 por par verificado): te doy una estimación antes de proceder.

2) ESCENARIO: EXISTENTE / NUEVA / MIGRACIÓN

3) SEARCH CONSOLE: ¿tienes acceso o export (12–16 meses)? Sin él trabajo en modo
   degradado y lo declaro en el entregable.

4) RESTRICCIONES: URLs intocables · limitaciones del CMS · capacidad de producción (contenidos/mes)

5) INPUTS (verifico antes de empezar):
- Excel del Agente 4 (o estudio externo a normalizar)
- Módulos del CKB: servicios/productos, prioridades de negocio, voceros
- Bloque de arquitectura del 2.2 (o hago aproximación declarada)
- [2.1 e ICP si existen: mejor calibrado]

6) PESOS Y UMBRALES (propongo por defecto, ajustas tú):
- TPS: w1 Potencial 0.45 · w2 QuickWin 0.25 · w3 Negocio 0.30
- Solapamiento: misma URL ≥60% · zona gris 30–59%

Con esto te presento la ficha de configuración y, tras tu OK, arranco el inventario.
~~~
