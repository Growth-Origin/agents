# Esqueleto del perfil — Fase 2 (ICP Definer, Agente 3)

> Las cuatro capas con que se construye cada perfil: ICP (cuenta/segmento) → Buyer
> Persona (individuo) → JTBD (motivación) → GEO/SEO (la que conecta con el ecosistema).
> No todos los campos aplican a todos los negocios: incluye los relevantes y omite el
> relleno (nada de «marca de café favorita» en B2B). Idioma: español de España.

## Regla transversal

**Demografía nunca sola.** Todo perfil debe explicar **cómo decide**, no solo quién es.
Cada atributo clave se ancla en datos (CKB / 2.1 / 2.2 / herramientas / cliente) o se
marca como **hipótesis a validar**, con su etiqueta de trazabilidad. Las «fairytale
personas» inventadas están prohibidas.

## Adaptación B2B / B2C

- **B2B:** la capa ICP es firmográfica/tecnográfica con **comité de compra**. Una
  persona por rol relevante. JTBD **funcional** dominante. Sin lifestyle fluff.
- **B2C:** la capa ICP es un **segmento de audiencia** (no empresa). La persona pesa
  más en lo **psicográfico**. JTBD **emocional y social** más relevantes.

## 1. Capa ICP (nivel cuenta / segmento)

- **Firmográficos (B2B):** sector, tamaño, facturación, geografía, estructura.
- **Segmento (B2C):** rango de edad/etapa vital, nivel adquisitivo, contexto, geografía.
- **Tecnográficos:** qué herramientas/plataformas ya usa (señal de madurez y encaje).
- **Señales de comportamiento:** patrones que indican buen encaje (visitas,
  contratación, engagement con cierto contenido). *(Nivel 2: HubSpot/SimilarWeb.)*
- **Eventos disparadores (trigger events):** qué cambio dispara la búsqueda de solución
  **ahora** (nueva ronda, cambio de liderazgo, mandato, expansión, dolor agudo).
- **Criterios de descalificación:** qué hace que una cuenta NO encaje (anti-patrones).

## 2. Capa Buyer Persona (nivel individuo)

- **Rol y contexto:** cargo/situación, a quién responde, en qué equipo.
- **Rol en la decisión:** decisor / influenciador / usuario / bloqueador (en B2B, su
  lugar en el comité).
- **KPIs y motivaciones:** por qué métrica le miden (B2B) o qué resultado personal busca
  (B2C). Qué le quita el sueño.
- **Pain points:** los problemas concretos que vive, en su lenguaje.
- **Objeciones:** qué le frena a decidir, qué miedos tiene (p. ej. «me quemé con una
  migración fallida»). *(Nivel 2: oro en transcripciones de Gong/Fireflies.)*
- **Lenguaje real:** cómo nombra su problema y su solución — vocabulario literal para el
  contenido. Se cita textual (`voz-cliente: ...`).

## 3. Capa JTBD (motivación)

Formulada con el **job statement** clásico:

> «Cuando [situación], quiero [motivación/acción], para poder [resultado esperado].»

- **Job funcional:** la tarea práctica que quiere resolver.
- **Job emocional:** cómo quiere sentirse (seguro, competente, sin estrés).
- **Job social:** cómo quiere ser percibido por otros.
- **Disparador de contexto:** la circunstancia que activa el job.
- **Resultado esperado (outcome):** cómo mide el éxito de «haber contratado» la
  solución.

## 4. Capa GEO/SEO (la que conecta con el resto del ecosistema)

Es lo que hace este ICP específico para una agencia SEO/GEO, y no un ICP de marketing
genérico:

- **Firma de prompt (prompt signature):** las formas concretas en que esta persona
  formula preguntas a la IA. Los motores generativos responden a **personas, no a
  keywords**: una persona lista describe quién es, qué necesita y qué opciones valora
  («mejor para agencias creativas que ya usan X»). Capturas ese patrón de formulación.
  *(Nivel 1: observación directa de motores. Nivel 2: GEO Metrics `get_ranking_prompt_details`.)*
- **Etapa del recorrido (funnel stage):** descubrimiento / consideración / decisión —
  define qué tipo de contenido necesita.
- **Intención de búsqueda dominante:** informacional / comparativa / transaccional, por
  etapa. *(Nivel 2: DataForSEO `search_intent`.)*
- **Canales donde busca y decide:** Google, ChatGPT, Perplexity, YouTube, Reddit, foros
  del nicho. Cruza con el bloque de plataformas del Agente 2.1. *(Nivel 2: SimilarWeb
  fuentes de tráfico.)*
- **Temas y subtemas de alto valor:** los que esta persona busca y que correlacionan con
  conversión (no con volumen). *(Nivel 2: DataForSEO/Semrush volumen + GEO Metrics
  `chatbot_preference`.)*

## Ficha rellenable (por perfil)

```markdown
## Perfil [N] — [Nombre] · [primario / secundario / negativo]

### ICP (cuenta / segmento)
- Firmográficos / Segmento: ... ‹fuente | ...›
- Tecnográficos: ...
- Señales de comportamiento: ...
- Trigger events: ...
- Criterios de descalificación: ...

### Buyer Persona
- Rol y contexto: ...
- Rol en la decisión: ...
- KPIs y motivaciones: ...
- Pain points: ...
- Objeciones: ...
- Lenguaje real (citas textuales): "..." ‹voz-cliente: ...›

### JTBD
- Job statement: "Cuando ..., quiero ..., para poder ..."
- Funcional / Emocional / Social: ...
- Disparador de contexto: ...
- Outcome (cómo mide el éxito): ...

### GEO/SEO
- Firma de prompt: "..." / "..." ‹motor-geo: ... | repeticiones: N›
- Etapa de funnel dominante: ...
- Intención dominante por etapa: ...
- Canales donde busca y decide: ...
- Temas/subtemas de alto valor: ...
```
