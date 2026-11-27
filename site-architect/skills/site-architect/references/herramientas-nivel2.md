# Herramientas de Nivel 2 y estimación de coste — Arquitecto de Sitio (Agente 5)

> Qué aporta cada herramienta, qué cobra y **cómo se estima el coste antes de
> proceder** (requisito del Paso 0). Este es el agente con mayor gasto potencial
> de API del ecosistema: el solapamiento de SERP se paga por par verificado.
> Idioma: español de España.

## Mapa herramienta → fase

| Herramienta | Fases que alimenta | Qué aporta | Modelo de coste |
|-------------|--------------------|------------|-----------------|
| **DataForSEO On-Page** | Fase 2 (inventario) | Crawl completo: URLs indexables, título, H1, tipo de página, metadatos | **Pago por uso** (por página crawleada) |
| **DataForSEO SERP** | Fases 2 (modo degradado) y 4 (solapamiento) | Top 10 por keyword para calcular el solapamiento de pares; rankings del propio sitio sin GSC | **Pago por uso** (una llamada por keyword y consulta) — **el gasto dominante** |
| **Search Console** | Fases 2 y 7 (quick-wins) | Rendimiento por query y página (12–16 meses); fuente primaria de canibalizaciones | **Gratis** (requiere acceso o export del cliente) |
| **GEO Metrics** | Fase 4 (matriz prompt→URL) | Estado de citación actual de los prompts priorizados | **Lectura por conector = gratis**; ejecuciones en su web sí gastan (fuera del agente) |

## Qué cobra de verdad

- **Coste monetario directo:** DataForSEO (On-Page por página; SERP por
  llamada). El solapamiento son **2 llamadas por par verificado** (una SERP por
  keyword, reutilizable vía caché): el número de pares frontera manda.
- **Sin coste:** GSC (el único requisito es el acceso del cliente) y las
  lecturas de GEO Metrics.

## Los tres controles de gasto (obligatorios)

1. **Pre-agrupación semántica sin API** (Fase 4, Paso 1): reduce los pares a
   verificar a los frontera dentro de cada pre-grupo y entre grupos limítrofes.
2. **Caché local de SERPs** (`_fuentes/solapamientos.csv`): una keyword
   consultada sirve para todos sus pares; nunca se repaga una SERP del mismo
   engagement.
3. **Estimación previa + OK**: antes del crawl y antes de la tanda de SERPs.

## Método de estimación (lo que el agente muestra en el Paso 0)

1. **Crawl:** nº aproximado de URLs del sitio (por el sitemap) × coste por
   página del plan.
2. **Solapamiento:** nº de keywords del universo (Top N del Agente 4) →
   pre-grupos estimados → **pares frontera** a verificar (típicamente entre 0,5
   y 1,5 × nº de keywords, según lo disperso del universo). Llamadas SERP ≈ nº
   de keywords implicadas en pares frontera (cada SERP se consulta una vez,
   caché mediante).
3. **Modo degradado sin GSC** (si aplica): añadir las SERPs de las keywords del
   propio sitio para la detección aproximada de canibalizaciones.
4. **Presentar el rango y esperar el OK** antes de proceder.

### Plantilla de aviso de coste

~~~text
Estimación de coste — Nivel 2 (arquitectura de [cliente])

Sitio: ~[P] páginas a crawlear   ·   Universo: Top [N] keywords + [M] prompts

- DataForSEO On-Page: ~[P] páginas → coste por uso del plan
- DataForSEO SERP: ~[K] llamadas (pares frontera tras pre-agrupación, con caché)
  [+ ~[K2] llamadas del modo degradado sin GSC, si aplica]
- Search Console: sin coste (necesito el export o el acceso: 12–16 meses)
- GEO Metrics: lecturas sin coste (estado de citación de los prompts)

Total estimado: [coste DataForSEO]. ¿Procedo o ajusto el alcance (menos pares,
crawl parcial por secciones)?
~~~

## Guardarraíl (no negociable)

- En **Nivel 1** no se llama a ninguna herramienta externa aunque esté
  conectada: pre-agrupación + verificación muestral manual, marcada «estimado».
- En **Nivel 2**, solo pares frontera, en lotes, con caché; nunca todos contra
  todos.
- **Antes del crawl y de la tanda de SERPs:** estimación + OK explícito.
- Lo que no se recupere se marca «requiere herramienta (Nivel 2+)» o «dato no
  disponible»; nunca se inventa.
- Se registra en `audit/execution_log.json`: nivel, estimación, gasto real,
  tamaño de la caché y pares verificados vs estimados.
