---
name: jev-keywords
description: Evalúa la calidad de un Excel de keywords ya trabajado con Jev (typesafe-ai/jev) vía Vercel AI Gateway. Claude genera un contexto del cliente (desde el chat o el CKB) y un contexto del Excel (qué significa cada columna), y Jev puntúa cada keyword en relevancia, intención, funnel, potencial GEO y prioridad, devolviendo una copia del Excel con columnas nuevas. Usar cuando el usuario diga "evalúa las keywords con Jev", "pasa el excel de keywords por Jev", "juzga la calidad de estas keywords", "jev keywords", o aporte un Excel de keywords para priorizar o filtrar.
---

# Evaluar keywords con Jev

Jev es un modelo de **evaluación**: no sabe volúmenes ni conoce al cliente. Solo juzga el texto que recibe (`state`) según las preguntas de `preguntas.json`. Por eso la calidad del resultado depende casi por completo del contexto que genera Claude en el paso 2.

Script: `scripts/evaluar_keywords.py` (Python 3 + openpyxl). La key se lee de `AI_GATEWAY_API_KEY`, en el proceso o en las variables de usuario de Windows. **No imprimas nunca la key.**

## Flujo

### 1. Localizar el Excel e inspeccionarlo (gratis)

Pide la ruta si no la tienes y ejecuta:

```bash
python "<dir de esta skill>/scripts/evaluar_keywords.py" "<excel>" --inspeccionar
```

Así ves las hojas, las columnas, los rangos, los valores distintos y las primeras filas. Si hay varias hojas, pregunta cuál evaluar (`--hoja`). Si la columna de keywords no se detecta por el nombre, usa `--col-keyword`.

### 2. Generar el contexto (dos partes) y validarlo con el usuario

Escribe `contexto-cliente.md` **en la misma carpeta que el Excel**. Si ya existe, léelo, muéstraselo al usuario y pregúntale si lo reutiliza o lo actualiza.

Plantilla (máximo ~350 palabras en total, porque va dentro de cada petición):

```markdown
# Contexto del cliente: <nombre>
- Qué vende:
- Cliente ideal (a quién le vende):
- Zona e idioma:
- Diferenciales:
- Lo que NO es / no le interesa: (clave para que Jev descarte falsos positivos)
- Objetivo SEO/GEO actual:

# Contexto del Excel
- Qué es este listado y cómo se construyó: (fuente, criterios que ya se aplicaron, qué significa "chequeada")
- Significado de cada columna relevante: (p. ej. "KD: dificultad 0–100 de Semrush, >50 es difícil para este dominio")
- Clasificaciones o notas propias del equipo y cómo interpretarlas:
```

Fuentes para el contexto del cliente, por orden de preferencia:
1. El CKB del cliente (salida de `ckb-builder`), si existe en el proyecto.
2. Lo trabajado en la conversación actual.
3. Si falta información: haz 3 o 4 preguntas concretas al usuario. **No inventes.**

El contexto del Excel sale de la inspección del paso 1 y de lo que el usuario haya contado sobre cómo trabajó el archivo. Si una columna es ambigua, pregunta.

**Muestra el contexto completo al usuario y espera su OK antes de gastar créditos.**

### 3. Dry run (gratis)

```bash
python ".../evaluar_keywords.py" "<excel>" --contexto "<carpeta>/contexto-cliente.md" --dry-run
```

Muestra al usuario cuántas keywords hay, el tamaño estimado y el `state` de ejemplo. Revisa que el state se lea bien y que los datos de la fila tengan sentido.

### 4. Prueba corta (coste mínimo)

```bash
python ".../evaluar_keywords.py" "<excel>" --contexto "..." --limite 10
```

Enseña al usuario las 10 filas evaluadas y pregunta si las notas le parecen coherentes. Si no lo son, ajusta el **contexto** (lo más habitual) o las instrucciones y criterios de `preguntas.json`, y repite la prueba.

### 5. Ejecución completa

Sin `--limite`. Genera `<excel>_jev.xlsx` al lado del original; el original no se modifica. Al final se imprimen las filas OK, los errores y el coste real.

### 6. Resumen para el usuario

Lee el Excel de salida y reporta: distribución de veredictos, precisión media, top 10 keywords a priorizar, keywords con alto potencial GEO, keywords con precisión baja (menos del 60%, conviene revisarlas a mano), descartes llamativos (alta prioridad según el equipo y baja según Jev, o al revés) y el coste total.

## Columnas que añade

Se añaden al final de la hoja, con cabecera destacada:

| Columna | Contenido |
|---|---|
| Jev · Relevancia (0-4) | encaje con el negocio y el cliente ideal |
| Jev · Intención | informacional / comercial / transaccional / navegacional / local |
| Jev · Funnel | TOFU / MOFU / BOFU |
| Jev · Potencial GEO | % de probabilidad de que sea una búsqueda en IA donde el cliente pueda ser citado |
| Jev · Prioridad (0-3) | combina encaje, datos del Excel y potencial GEO |
| Jev · Veredicto | priorizar / revisar / descartar |
| Jev · Precisión | % de seguridad media de Jev en sus respuestas para esa keyword |
| Jev · Error | vacío si la fila fue bien |

**Precisión** = media de la seguridad de Jev en cada respuesta: la probabilidad de la opción o del escalón elegido y, en GEO, la distancia al 50%. Es la **confianza del modelo, no un acierto verificado**; explícaselo así al usuario.

**Regla del veredicto** (función `veredicto()` del script):
1. Relevancia < 1.5 → **descartar** (si no encaja con el negocio, el GEO no la salva).
2. Prioridad ≥ 2.5, o prioridad ≥ 1.5 con potencial GEO ≥ 70% → **priorizar**.
3. Prioridad < 1 con GEO < 50% → **descartar**.
4. Resto → **revisar**.
5. Si sale "priorizar" pero la precisión es < 60% → baja a **revisar**.

## Personalizar

- **Preguntas:** edita `preguntas.json`. Tipos: `choice` (criteria = objeto opción→descripción), `score` (criteria = array de al menos 2 etiquetas, de menor a mayor) y `noul` (probabilidad booleana). Si el Excel ya trae una columna que responde una pregunta (p. ej. intención), quítala de las preguntas para no pagar dos veces. Para un cliente concreto, copia el archivo y pásalo con `--preguntas`.
- **Veredicto:** los umbrales están en la función `veredicto()` del script. Ajústalos si el usuario lo pide. Si cambias o renombras preguntas en `preguntas.json`, revisa también `veredicto()` y `OUTPUT_COLUMNS`, que usan las claves `relevancia`, `prioridad` y `potencial_geo`.

## Errores comunes

- `HTTP 403 customer_verification_required`: el team de Vercel no tiene tarjeta. Lo resuelve el usuario en el panel de AI Gateway.
- `HTTP 401`: key inválida o revocada.
- `--creditos` muestra el saldo sin gastar nada.
