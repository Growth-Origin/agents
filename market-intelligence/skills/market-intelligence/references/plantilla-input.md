# Plantilla de input — Paso 0 — Market Intelligence (Agente 2.1)

Campos que el agente recoge antes de investigar. Mismo formato cada vez: pregunta
solo lo que falte, cubre lo obligatorio. Idioma del diálogo: español de España
(peninsular).

## Paso 0 — Nivel de investigación (SIEMPRE lo primero)

Antes de pedir los datos, el agente pregunta el **nivel de investigación** y
espera respuesta (ver el Paso 0 del SKILL):

- **Nivel 1 — sin herramientas externas.** Solo Claude + búsqueda web + Claude
  in Chrome. Coste cero. Los datos duros se aproximan o se marcan «requiere
  herramienta (Nivel 2+)».
- **Nivel 2 — con herramientas externas.** Pregunta cuáles usar: solo
  DataForSEO, solo Semrush, o ambos (mejor para triangular). ⚠️ Consumen
  créditos / son de pago por uso; antes de una tirada grande, estimación de
  coste (método y tabla en `herramientas-nivel2.md`) y OK del operador.

La elección (nivel + herramientas) se registra en el `audit` y se respeta: en
Nivel 1 no se llama a ninguna herramienta externa aunque esté conectada.

## Obligatorios (Paso 0.b)

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

Al arrancar, el agente comprueba qué hay conectado y lo registra (las de pago
solo se usan en Nivel 2):

- **GEO Metrics** (conector MCP) → fuente primaria de GEO + volúmenes de keyword.
  Si está, busca el proyecto del cliente con `list_projects`. Sus lecturas no
  tienen coste por consulta.
- **DataForSEO** (conector MCP, **pago por uso**) → volúmenes exactos, dificultad
  de keyword, SERP y backlinks. Aplica el guardarraíl de coste del SKILL.
- **Semrush / Ahrefs** → alternativa para dificultad de keyword + backlinks. Si
  no hay ninguno conectado, esos datos se marcan «requiere herramienta (Nivel 2+)».
- **Nivel 1** siempre: búsqueda web, navegador, PageSpeed.

## Plantilla de recogida (lo que el agente muestra)

~~~text
Antes de nada: ¿qué nivel de investigación quieres?
- Nivel 1 (sin herramientas de pago): Claude + web + Chrome. Coste cero.
- Nivel 2 (con herramientas): solo DataForSEO, solo Semrush, o ambos.
  ⚠️ Consumen créditos; antes de tiradas grandes te doy una estimación de coste.

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

Herramientas: compruebo qué hay conectado (GEO Metrics, DataForSEO,
Semrush/Ahrefs) y te digo qué podré sacar de cada uno según el nivel elegido.

¿Confirmas o ajustas algo antes de que lea el contexto y monte el plan?
~~~

## Después del Paso 0

Con lo obligatorio cubierto: el agente normaliza el contexto (a
`_fuentes/contexto_normalizado.md`), deriva consultas clave y keywords semilla, y
**muestra el plan al operador antes de buscar** (checkpoint del Paso 1).
