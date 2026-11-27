# Jev Keywords: evaluador de calidad de keywords

Herramienta complementaria del ecosistema. Toma un **Excel de keywords ya
trabajado** (por ejemplo, la salida del Agente 4 o un research externo) y lo
pasa por **Jev** (`typesafe-ai/jev`), un modelo de evaluación, vía Vercel AI
Gateway. Jev puntúa cada keyword y devuelve una **copia del Excel con columnas
nuevas**.

Jev no conoce volúmenes ni al cliente: solo juzga el contexto que le da Claude.
Por eso la calidad del resultado depende sobre todo del contexto del cliente
(idealmente, el CKB).

## Cómo se invoca

- «evalúa las keywords con Jev» / «jev keywords»
- «pasa el excel de keywords por Jev»
- «juzga la calidad de estas keywords»

## Qué necesita

- El **Excel de keywords**.
- Contexto del cliente: el **CKB** (Agente 1.1) si existe o, si no, lo
  trabajado en la conversación. Si falta información, pregunta.

## Cómo trabaja

1. **Inspección (gratis):** lee la estructura del Excel.
2. **Contexto:** redacta el contexto del cliente y el del Excel (qué significa
   cada columna) y **espera tu OK antes de gastar créditos**.
3. **Dry run (gratis)**, luego **prueba corta** (coste mínimo) y, al final,
   **ejecución completa**.
4. **Resumen** con los resultados.

## Qué entrega

Una copia del Excel con columnas de **relevancia, intención, funnel, potencial
GEO, prioridad, precisión** (la confianza del modelo) y un **veredicto**:
priorizar / revisar / descartar. Las preguntas se personalizan en
`preguntas.json` y los umbrales del veredicto, en la función `veredicto()` del
script.

## Requisitos

- **Python 3** con `openpyxl` (`pip install openpyxl`).
- Variable de entorno **`AI_GATEWAY_API_KEY`** con una clave de Vercel AI
  Gateway (cada persona usa la suya; **nunca** la escribas en el repo).
- Consume créditos del AI Gateway en la ejecución completa.
