# Competitive Intelligence — Agente 2.2

Hace **ingeniería inversa de los competidores** que mejor posicionan en el nicho
del cliente para extraer palancas accionables de SEO y GEO: propone los
competidores, los disecciona en **once temas** en formato
**insight → implicación → acción**, y cierra con una síntesis accionable por
agente destino. Opera **humano-en-el-bucle**. Idioma de salida: **español de
España**.

## Cómo se invoca

- «agente 2.2» / «competitive-intelligence»
- «analiza los competidores de [cliente]» / «disecciona a la competencia»
- «battlecard SEO/GEO»

**Antes de invocarlo**, ten a mano el contexto del cliente (cualquiera vale): el
**CKB** (1.1), el **análisis de mercado del 2.1** (recomendado: ancla el benchmark
y nomina el top-5), o un **paquete de documentos externos** que el agente
normaliza.

## Cómo trabaja (paso a paso)

1. **Paso 0 — Nivel de investigación (te pregunta siempre):** Nivel 1 (sin
   herramientas, coste cero, datos duros aproximados o marcados) o Nivel 2 (solo
   DataForSEO, solo Semrush, o ambos) **con estimación de coste y OK antes de
   cualquier tirada grande**.
2. **Paso 0.b — Datos y enfoque:** slug, contexto y los parámetros que acotan el
   universo competitivo (sector/nicho, modelo, geografía, características, tipo de
   competidor).
3. **Paso 1 — Propuesta de competidores (checkpoint):** propone 3–5 candidatos
   con justificación (puede descubrir competidores SEO/GEO que el cliente no tenía
   en el radar) y **espera tu validación antes de diseccionar**.
4. **Paso 2 — Plan (checkpoint):** por competidor, los 11 temas y su presupuesto.
5. **Pasos 3–4 — Recopilar y sintetizar:** crawl y lectura, auditoría generativa
   con repeticiones (patrón y variabilidad, no foto única), PageSpeed, y la
   síntesis accionable 4.11.

## Qué outputs genera

Todo bajo `clientes/[slug-cliente]/competitive-intelligence/`:

| Archivo | Qué es |
|---------|--------|
| `propuesta_competidores.md` | Lista priorizada con justificación, **validada antes de diseccionar**. |
| `analisis_competitivo.md` | Los 11 temas por competidor (búsqueda, generativo, opinión de las IAs, backlinks, arquitectura, interlinking, E-E-A-T, hacks, personalidad, CMS/UX + síntesis). |
| `sintesis_accionable.md` | El tema 4.11 standalone: conclusiones con agente destino. Lo que los downstream leen primero. |
| `resumen_ejecutivo.pdf` | Resumen presentable de 2–4 páginas. |
| `_fuentes/` y `audit/` | Auditoría generativa, crawl, PageSpeed y registro de ejecución. |

## Quién consume su salida (downstream)

- **Estrategia (Capa 2):** keyword gap, link gap, orden de palancas.
- **Contenido (Capa 3):** hacks de utilidad, clusters a construir, E-E-A-T.
- **ICP Definer (Agente 3):** a quién sirven los competidores y qué opina la IA.
- **Strategic Keywords & Prompts (Agente 4):** validación competitiva del scoring.

## Lo que NO hace

No hace el retrato de mercado en abstracto (2.1), no define el ICP (Agente 3), no
fija la estrategia (Capa 2). Nada descriptivo sin acción.

## Buenas prácticas

- En **Nivel 1**, backlinks y volúmenes exactos quedan «requiere herramienta
  (Nivel 2+)»; el resto de temas (arquitectura, E-E-A-T, hacks, CMS/UX) se cubre
  entero sin coste.
- Al comparar con gigantes multi-negocio, acota el gap a la capa comparable
  (subcarpeta o unidad de negocio), no al dominio entero: si no, es ruido.
- Las cifras divergen entre herramientas: triangula y cita la fuente de cada dato.
- La opinión de la IA cambia rápido: re-audita periódicamente.
