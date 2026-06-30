# Scoring y fusión — Fases 3 y 4 (Strategic Keywords & Prompts, Agente 4)

> El corazón del agente: el doble scoring (KPS para keywords, PPS para prompts), la
> selección por tiers y la fusión topic-led. Los pesos por defecto son **ajustables por el
> consultor** (salida de la Fase 1). Idioma: español de España (peninsular).

## Principio

Cada keyword y cada prompt recibe un **Score de Prioridad compuesto, transparente y
trazable**. El filtro anti-persona es **exclusión dura**: no compra entrada con volumen.
Cada selección lleva su **rationale** (por qué entra, qué la empuja, qué la frena).

## Keyword Priority Score (KPS)

| Factor | Qué mide | Peso por defecto |
|--------|----------|------------------|
| Oportunidad | Volumen vs dificultad (hueco real alcanzable) | 25% |
| Encaje ICP | ¿La persona objetivo busca esto, en una etapa valiosa? | 25% |
| Prioridad de negocio | Alineación con mercados/productos priorizados | 20% |
| Validación competitiva | Un competidor comparable rankea y le aporta tráfico | 15% |
| Valor de intención | Transaccional/comercial > informacional (según foco) | 15% |
| **Filtro anti-persona** | **Exclusión dura** si atrae a la persona negativa | **Excluyente** |

## Prompt Priority Score (PPS)

| Factor | Qué mide | Peso por defecto |
|--------|----------|------------------|
| Oportunidad IA | Hueco de citación (nadie/competidor citado, sin respuesta clara) | 30% |
| Encaje firma-de-prompt | ¿Coincide con cómo la persona formula a la IA? | 25% |
| Prioridad de negocio | Alineación con prioridades del cliente | 20% |
| Validación competitiva | El competidor es citado y le funciona | 15% |
| Relevancia de motor | Peso por el motor que importa a esta audiencia | 10% |
| **Filtro anti-persona** | **Exclusión dura** si el prompt sirve a la persona negativa | **Excluyente** |

## Cálculo y datos faltantes

- Cada factor se normaliza a 0–100 y se combina con su peso → score 0–100.
- En **Nivel 1**, los factores que dependen de datos duros (Oportunidad, Valor de intención,
  Oportunidad IA, estado de citación) se aproximan por SERP/observación **declarándolo**, o
  se marcan «requiere herramienta (Nivel 2+)». El score se calcula con lo disponible y se
  anota qué factor quedó pendiente, para no dar un número falsamente preciso.
- Nunca se inventa una métrica para rellenar un factor.

## Selección

1. Ordena por score descendente.
2. Aplica el **filtro anti-persona** como exclusión dura (elimina, no penaliza).
3. Corta en el **Top N** definido en el Paso 0 (20 / 50 / 100).
4. Asigna **tier de prioridad (1 / 2 / 3)** para que el corte no sea binario: tier 1 lo
   prioritario, tier 3 lo que entra pero espera.
5. Escribe el **rationale** de cada elemento.

## Fase 4 — Fusión keywords ↔ prompts (topic-led)

No se tratan como listas paralelas: se **agrupan por tema/JTBD subyacente, no por canal**.
Una misma necesidad tiene una cara-keyword (Google) y una cara-prompt (IA); además, gran
parte de lo que la IA cita procede de Google, así que un tema fuerte en SEO se vuelve
citable en IA si se estructura bien.

### Clasificación de temas

| Tipo de tema | Definición | Implicación estratégica |
|--------------|------------|--------------------------|
| **Doble victoria** | Fuerte en keyword **y** en prompt | Máxima prioridad: un esfuerzo, dos canales |
| **SEO-led** | Fuerte en keyword, débil en prompt | Trabajar SEO; vigilar si se vuelve citable |
| **GEO-led** | Fuerte en prompt, débil en keyword | Territorio de IA sin ocupar; contenido answer-first |
| **Latente** | Débil en ambos pero alto encaje ICP/negocio | Apuesta de futuro; baja prioridad inmediata |

### Esbozo de priorización (primer roadmap)

Ordena los temas por **valor combinado × encaje ICP × validación competitiva ×
alcanzabilidad**. Recomendación de arranque típica: empezar por las **dobles victorias con
alto encaje ICP y dificultad asumible**, porque rentabilizan un solo esfuerzo en los dos
frentes. Este esbozo es el puente directo al agente de Contenido/Arquitectura, que lo
convertirá en pillars, clusters y mapeo a URLs (eso ya no es trabajo de este agente).
