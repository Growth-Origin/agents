# Contexto incompleto y paquete externo — Strategic Keywords & Prompts (Agente 4)

> Cómo trabajar cuando **faltan** algunos (o todos) los outputs de la Capa 1 (CKB, ICP,
> Mercado 2.1, Competidores 2.2). Objetivo: rendir con lo que haya, declarar los supuestos y
> **preguntar lo crítico** antes de ponderar. Idioma: español de España (peninsular).

## Principio

El contexto ideal es CKB (1.1) + ICP (Agente 3) + Mercado (2.1) + Competidores (2.2). Pero
el agente **no depende en duro** de ninguno: trabaja con lo disponible, lo normaliza a una
ficha de contexto, marca lo que falta y **pregunta cuando el hueco es crítico**. No inventa.

## Orden de actuación ante un hueco (supón lo menos posible)

Para CADA input que falte, en este orden, sin saltarte pasos:

1. **Investigar primero (Nivel 1, coste cero).** Cerrar el hueco con la web del cliente, el
   SERP, la observación de motores, reseñas y fuentes públicas. Si se cierra, queda con su
   fuente y su nivel de confianza.
2. **Preguntar si es decisivo.** Si el hueco afecta a la ponderación o a la selección y la
   investigación no lo resuelve, **parar y preguntar al consultor**. No avanzar sobre un
   supuesto en algo decisivo.
3. **Hipótesis visible (último recurso).** Si no es decisivo y no se puede investigar, dejar
   una **hipótesis explícita y trazada**, listada en el mapa de huecos. Nunca esconderla en
   una conclusión.

El sesgo por defecto es **investigar y preguntar antes que asumir**.

## Qué necesita sí o sí, y qué hacer si falta

| Necesita | Para qué | Si falta |
|----------|----------|----------|
| **Prioridades de negocio** (mercados, productos, foco) | Ponderar todo (el timón) | **Preguntar.** Sin esto la ponderación no es fiable. |
| **Persona objetivo + filtro anti-persona** (del ICP) | Encaje ICP y exclusión dura | **Preguntar** por la persona y por qué tráfico NO se quiere; proponer un filtro provisional como hipótesis. |
| **Vocabulario / demanda** (del 2.1) | Derivar candidatos de keyword/prompt | Derivar de la web del cliente, SERP y observación de motores; declararlo menos calibrado. |
| **Validación competitiva** (del 2.2) | Factor de validación en el scoring | Observar SERP/motores para inferir quién rankea o es citado; marcar confianza media/baja. |
| **Oferta y voz** (del CKB) | Encaje de negocio y lenguaje | Usar la web del cliente o un brief; normalizar. |

## Paquete de contexto externo (cuando no hay nada de la Capa 1)

1. El operador aporta rutas o pega documentos (brief, web, deck, export de keywords previo).
   El agente los **lee**.
2. Rellena la **ficha de contexto normalizado**, citando el origen de cada campo:
   `‹contexto-externo: [doc] | acceso | confianza | tipo›`. Guarda en
   `_fuentes/contexto_normalizado.md`.
3. Lo que no cubra y sea crítico (prioridades, persona, filtro anti-persona) se **pregunta**
   antes de ponderar.

### Ficha de contexto normalizado (plantilla)

~~~markdown
# Contexto del cliente (normalizado) — [Cliente]

**Origen:** CKB 1.1 / ICP (Agente 3) / 2.1 / 2.2 / paquete externo (lo que aplique)
**Documentos fuente:** [lista]

- **Sector y oferta:** ...
- **Prioridades de negocio (mercados/productos/foco):** ...  (timón de la ponderación)
- **Persona(s) objetivo:** ...
- **Filtro anti-persona (qué tráfico NO se quiere):** ...
- **Vocabulario/demanda conocida:** ...
- **Competidores de referencia:** ...
- **Mercados e idiomas:** ...

## Huecos críticos (preguntar antes de ponderar)
- [campo que falta y por qué bloquea]
~~~

## Mapa de huecos (se muestra en el checkpoint de la Fase 1)

Junto al Perfil de Ponderación, el agente presenta este mapa para que el supuesto nunca
viaje escondido a la selección:

~~~markdown
# Mapa de huecos — [Cliente]

| Input faltante | ¿Decisivo? | Qué investigué (Nivel 1) y encontré | Estado |
|----------------|-----------|--------------------------------------|--------|
| [p. ej. filtro anti-persona] | Sí | Revisé web/SERP; no concluyente | **PREGUNTA al consultor** |
| [p. ej. vocabulario de demanda] | No | Derivado de la web y del SERP | Cubierto (confianza media) |
| [p. ej. validación competitiva] | No | Observación de SERP/motores | Hipótesis trazada |

## Necesito que respondas antes de seguir
- [pregunta concreta 1]
- [pregunta concreta 2]
~~~

## Aviso de calidad

- El universo priorizado hereda la fiabilidad del contexto. Lo que venga sin fuente se trata
  como **hipótesis**, no como hecho, y se dice.
- Si más adelante se ejecutan los agentes de Capa 1 que faltaban, se re-prioriza con ellos
  sin reescribir el método.
- **Peor de los casos: preguntar más.** Es preferible una pregunta extra al consultor que un
  entregable construido sobre supuestos no validados.
