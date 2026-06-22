# Plantilla de input — Paso 0 — Market Intelligence (Agente 2.1)

Campos que el agente recoge antes de investigar. Mismo formato cada vez: pregunta
solo lo que falte, cubre lo obligatorio. Idioma del diálogo: español de España
(peninsular).

## Obligatorios

| Campo | Descripción |
|-------|-------------|
| `slug_cliente` | Identificador del cliente (kebab-case). |
| `contexto_cliente` | El contexto del cliente, de UNO de estos tres orígenes (cualquiera vale): (a) CKB del Agente 1.1 (`ckb/`); (b) un análisis de mercado previo; (c) un **paquete de contexto externo** (docs de otra agencia, brief, web) — ver `plantilla-contexto-externo.md`. |

Si el contexto no cubre algo crítico (sector, geografía, prioridades de negocio),
el agente lo pregunta. No parte de cero ni inventa.

## Parámetros (opcionales, con valor por defecto)

| Parámetro | Descripción | Por defecto |
|-----------|-------------|-------------|
| `idioma_mercado` / geografía | Idioma y país/zona objetivo | Detectar del contexto |
| `profundidad` | Intensidad de investigación | `profunda` (`ligera`/`media`/`profunda`) |
| `n_consultas_geo` | Consultas a probar en motores generativos | 10 |
| `motores_geo` | Motores a auditar | ChatGPT, Perplexity, Google AI Overviews, Gemini |

## Detección de herramientas (el agente la hace solo)

Al arrancar, el agente comprueba qué hay conectado y lo registra:

- **GEO Metrics** (conector MCP) → fuente primaria de GEO + volúmenes de keyword.
  Si está, busca el proyecto del cliente con `list_projects`.
- **Semrush / Ahrefs** → dificultad de keyword + backlinks. Si no, esos datos se
  marcan «requiere herramienta (Nivel 2+)».
- **Nivel 1** siempre: búsqueda web, navegador, PageSpeed.

## Plantilla de recogida (lo que el agente muestra)

~~~text
Para arrancar el análisis de mercado necesito:

OBLIGATORIOS
- slug_cliente: ...
- contexto del cliente (elige una):
    · ruta al CKB (ckb/) del Agente 1.1, o
    · ruta a un análisis de mercado previo, o
    · paquete de contexto externo: rutas/documentos (brief, onboarding de otra
      agencia, web del cliente)

PARÁMETROS (si no dices nada, uso los valores por defecto)
- idioma_mercado / geografía: [lo detecto del contexto]
- profundidad: ligera | media | profunda [por defecto profunda]
- n_consultas_geo: [por defecto 10]
- motores_geo: [ChatGPT, Perplexity, Google AI Overviews, Gemini]

Herramientas: compruebo si GEO Metrics (y Semrush/Ahrefs) están conectados y te
digo qué podré sacar de cada uno.

¿Confirmas o ajustas algo antes de que lea el contexto y monte el plan?
~~~

## Después del Paso 0

Con lo obligatorio cubierto: el agente normaliza el contexto (a
`_fuentes/contexto_normalizado.md`), deriva consultas clave y keywords semilla, y
**muestra el plan al operador antes de buscar** (checkpoint del Paso 1).
