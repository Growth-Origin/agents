# Plantilla del Excel — Strategic Keywords & Prompts (Agente 4)

> El entregable principal es un libro Excel (`top_keywords_prompts.xlsx`) de **cuatro
> pestañas**. Se construye con la skill **xlsx**. Si el entorno no puede generar Excel, se
> producen los datos en `.md`/`.csv` con la misma estructura y se avisa. Idioma del
> contenido: español de España (las keywords/prompts se conservan en su idioma).

## Pestaña 1 — «Top Keywords»

| Columna | Contenido |
|---------|-----------|
| Keyword | El término |
| Tema/Cluster | Tema fusionado al que pertenece |
| Persona | Persona objetivo (del ICP) |
| Etapa | Descubrimiento / Consideración / Decisión |
| Intención | Informacional / Comparativa / Transaccional |
| Volumen | Búsquedas mensuales *(Nivel 2; en Nivel 1 «requiere herramienta»)* |
| Dificultad | Competencia (índice) *(Nivel 2)* |
| Oportunidad | Volumen vs dificultad |
| CPC | Señal de valor comercial *(Nivel 2)* |
| SERP features | AI Overview / snippet / etc. *(Nivel 2)* |
| Competidor | Quién rankea y en qué posición |
| Encaje ICP | Score 0–100 |
| Prioridad negocio | Score 0–100 |
| KPS | Score compuesto |
| Tier | 1 / 2 / 3 |
| Rationale | Por qué entra / qué la empuja o frena |

## Pestaña 2 — «Top Prompts»

| Columna | Contenido |
|---------|-----------|
| Prompt | La consulta a la IA |
| Tema | Tema fusionado |
| Persona | Persona objetivo |
| Tipo de firma | Patrón de formulación de la persona (del ICP) |
| Motor(es) | Dónde es relevante (ChatGPT/Gemini/Perplexity/Claude/Copilot) |
| Estado citación | ¿Marca citada? ¿Competidor citado? *(Nivel 2; tendencia, no foto fija)* |
| Oportunidad IA | Score del hueco de citación |
| Encaje firma ICP | Score 0–100 |
| Prioridad negocio | Score 0–100 |
| PPS | Score compuesto |
| Tier | 1 / 2 / 3 |
| Cluster keyword vinculado | **El puente de fusión** con la pestaña de keywords |
| Rationale | Por qué entra |

> La columna **«Cluster keyword vinculado»** es el mecanismo de fusión hecho dato: conecta
> cada prompt con su tema-keyword y permite al siguiente agente trabajar por tema, no por
> canal.

## Pestaña 3 — «Criterios y ponderación»

Transparencia obligatoria. Documenta:

- La **configuración del Paso 0** (nivel, profundidad, foco).
- El **Perfil de Ponderación** (Fase 1): dimensiones y pesos validados.
- Los **pesos de scoring** usados (Fase 3): factores del KPS y del PPS.
- Qué quedó **«requiere herramienta (Nivel 2+)»** y por qué.

Responde a «¿por qué esta conclusión?». Sin esta pestaña, el entregable no es defendible
ante el cliente.

## Pestaña 4 — «Esbozo de priorización»

El roadmap topic-led de la Fase 4:

| Columna | Contenido |
|---------|-----------|
| Tema | Tema fusionado (JTBD subyacente) |
| Tipo | Doble victoria / SEO-led / GEO-led / Latente |
| Valor combinado | Score del tema (keyword + prompt) |
| Encaje ICP | Score 0–100 |
| Validación competitiva | Señal del 2.2 |
| Alcanzabilidad | Dificultad asumible (alta/media/baja) |
| Orden de ataque | Posición en el roadmap recomendado |
| Nota | Recomendación (p. ej. «doble victoria, arrancar aquí») |

## Cómo construirlo

1. Termina las Fases 1–4 (ponderación, recuperación, scoring, fusión).
2. Lee la skill **xlsx** y genera el libro con las cuatro pestañas y estas columnas.
3. Cada fila de keywords/prompts lleva su **rationale**; los datos duros llevan su marca de
   nivel cuando falten.
4. Guarda en `clientes/[slug-cliente]/estrategia-keywords-prompts/top_keywords_prompts.xlsx`.
