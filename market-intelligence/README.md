# Market Intelligence — Agente 2.1

Construye un **retrato accionable y profundo del mercado** del cliente para SEO y
GEO: demanda y comportamiento de búsqueda, panorama generativo, E-E-A-T del sector,
plataformas, vocabulario, posición del cliente con benchmark de intensidad y
conclusiones accionables con agente destino. Opera **humano-en-el-bucle**. Idioma
de salida: **español de España**.

## Cómo se invoca

- «agente 2.1» / «market-intelligence»
- «analiza el mercado de [cliente]» / «retrato de mercado»
- «construye el market intelligence»

**Antes de invocarlo**, ten a mano el contexto del cliente (cualquiera de estos
sirve, no dependen en duro entre sí): el **CKB** (Agente 1.1), un **análisis de
mercado previo**, o un **paquete de documentos externos** (onboarding de otra
agencia, brief, web) que el agente normaliza.

## Cómo trabaja (paso a paso)

1. **Paso 0 — Nivel de investigación (te pregunta siempre):**
   - **Nivel 1:** sin herramientas de pago. Solo Claude + búsqueda web + Claude in
     Chrome. Coste cero. Los datos duros se aproximan o se marcan «requiere
     herramienta (Nivel 2+)».
   - **Nivel 2:** con herramientas (solo DataForSEO, solo Semrush, o ambos; GEO
     Metrics se lee gratis si está conectado). **Estimación de coste y OK antes de
     cualquier tirada grande.**
2. **Paso 0.b — Contexto:** slug, origen del contexto, geografía/idiomas,
   profundidad, motores GEO.
3. **Paso 1 — Plan (checkpoint):** lee el contexto, deriva consultas y keywords
   semilla, y te muestra el plan **antes de buscar**.
4. **Paso 2 — Investigación:** por bloques, con los módulos keyword y prompt
   (método de 5 buyer personas de trabajo + GEO Metrics) y la métrica obligatoria
   de solapamiento Google ↔ IA.
5. **Paso 3 — Síntesis:** los 10 entregables, siempre completos.

## Qué outputs genera

Todo bajo `clientes/[slug-cliente]/market-intelligence/`:

| Archivo | Qué es |
|---------|--------|
| `analisis_mercado_completo.md` | El documento extenso con todo el análisis (la fuente de los demás). |
| `top5_competidores.md` | Los 5 que mejor posicionan, con el porqué. **Puente al Agente 2.2.** |
| `eeat_sector.md` | Señales E-E-A-T concretas que premia ESTE sector. |
| `top50_preguntas.md` | ~50 preguntas reales del mercado y país objetivo. |
| `vocabulario_y_comunicacion.md` | Léxico, tono y nivel técnico del sector. |
| `plataformas_y_contenido.md` | Dónde estar, con veredicto entrar/no entrar/vigilar (incluye redes y canales propios). |
| `posicion_e_intensidad.md` | Posición del cliente + benchmark de intensidad del sector (**benchmark, no plan**). |
| `conclusiones_accionables.md` | El contrato downstream: cada conclusión con su agente destino. |
| `resumen_ejecutivo.pdf` | Resumen presentable de 2–4 páginas. |
| `_fuentes/` y `audit/` | Material de investigación y registro de ejecución. |

## Quién consume su salida (downstream)

- **Competitive Intelligence (2.2):** el top-5 nominado y el E-E-A-T del sector.
- **ICP Definer (Agente 3):** segmentos de demanda, plataformas, top preguntas.
- **Strategic Keywords & Prompts (Agente 4):** vocabulario, query fan-out, huecos GEO.
- **Estrategia (Capa 2) y Contenido (Capa 3):** benchmark de intensidad, plataformas,
  patrones de utilidad.

## Lo que NO hace

No disecciona competidores concretos (2.2), no define el ICP (Agente 3), no fija
la estrategia (Capa 2). La intensidad que entrega es benchmark, no plan.

## Buenas prácticas

- En **Nivel 1** el retrato es útil pero sin cifras de API; para volúmenes,
  dificultad y backlinks reales, Nivel 2.
- El panorama GEO cambia rápido: re-audita mensualmente (con GEO Metrics) o al
  menos trimestralmente.
- ChatGPT y Gemini se auditan con Claude in Chrome sobre tu sesión iniciada; si
  hay muro de login el agente PARA y te lo pide, no se salta el motor.
