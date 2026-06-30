# Strategic Keywords & Prompts — Agente 4

Primer agente de la **Capa de Estrategia** (el «agente bisagra»). Cruza todo el conocimiento
de la Capa 1 (CKB, ICP, mercado, competidores) con datos duros de búsqueda (DataForSEO) y de
IA (GEO Metrics) para entregar un **universo priorizado de keywords y prompts**, con scoring
transparente y un primer esbozo de qué trabajar primero. No es un extractor: es un decisor
que justifica cada elección. Opera **humano-en-el-bucle**. Idioma de salida: **español de
España**.

## Cómo se invoca

«agente 4», «keywords y prompts estratégicos», «prioriza keywords», «universo de keywords y
prompts», «strategic keywords».

**Antes de invocarlo**, ten a mano el contexto de la Capa 1 (con más, mejor calibrado):
CKB (1.1), **ICP (Agente 3)**, Mercado (2.1) y Competidores (2.2). Si falta alguno, trabaja
con lo que haya o con un paquete externo; si falta algo crítico (prioridades de negocio,
persona objetivo, filtro anti-persona), te lo preguntará.

## Cómo trabaja

1. **Paso 0 — Configuración (pregunta siempre):**
   - **Nivel de investigación:** Nivel 1 (sin herramientas, coste cero, datos duros
     aproximados o marcados) o Nivel 2 (DataForSEO + GEO Metrics, Semrush opcional) **con
     estimación de coste antes de proceder**.
   - **Profundidad (obligatoria):** Top 20 / 50 / 100.
   - **Foco (opcional):** objetivo (tráfico/conversión/equilibrado), mercado, persona.
2. **Fase 1 — Ponderación (checkpoint):** construye el Perfil de Ponderación Estratégica
   (las prioridades del cliente son multiplicadores) y lo valida contigo antes de buscar.
3. **Fase 2 — Recuperación:** deriva candidatos del contexto y recupera datos solo para los
   relevantes (DataForSEO keywords, GEO Metrics prompts).
4. **Fase 3 — Scoring:** KPS (keywords) y PPS (prompts); filtro anti-persona como exclusión
   dura; corte en Top N y tiers; rationale por fila.
5. **Fase 4 — Fusión topic-led:** agrupa por tema/JTBD y clasifica (doble victoria / SEO-led
   / GEO-led / latente); genera el esbozo de priorización.
6. **Fase 5 — Entregables:** el Excel de 4 pestañas.

## Qué outputs genera

En `clientes/[slug-cliente]/estrategia-keywords-prompts/`:

| Archivo | Qué es |
|---------|--------|
| `top_keywords_prompts.xlsx` | Libro de 4 pestañas: **Top Keywords**, **Top Prompts**, **Criterios y ponderación**, **Esbozo de priorización**. |
| `resumen_ejecutivo.md` | Resumen breve para el consultor. |
| `_fuentes/` | Contexto normalizado, candidatos, datos de keywords y de prompts. |
| `audit/` | Nivel, profundidad, foco, estimación y gasto real, validaciones. |

## Quién consume su salida

- **Contenido/Arquitectura (siguiente agente):** convierte el universo priorizado y el
  esbozo en pillars, clusters y mapeo a URLs.
- **Prompts GEO:** los prompts priorizados por motor.
- **Estrategia:** el orden de ataque y los criterios.

## Lo que NO hace

No mapea keyword→URL ni diseña la arquitectura de pillars/clusters (eso es del siguiente
agente), no hace el retrato de mercado (2.1) ni el ICP (Agente 3). Para en el universo
priorizado + esbozo.

## Buenas prácticas

- El stack es continuista con el Agente 2.2 (DataForSEO + GEO Metrics): mismas credenciales.
- En **Nivel 1** el entregable es una preselección estratégica **sin cifras** (volumen,
  dificultad, citación marcados como pendientes). Para números reales, Nivel 2.
- La **explicabilidad es un entregable**: la pestaña de criterios y los rationale hacen el
  Excel defendible ante el cliente.
- Es re-priorizable: la demanda y la citación en IA cambian; re-ejecútalo periódicamente.
