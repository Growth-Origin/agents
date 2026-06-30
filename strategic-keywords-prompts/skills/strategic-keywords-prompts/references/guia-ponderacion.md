# Guía de ponderación — Fase 1 (Strategic Keywords & Prompts, Agente 4)

> Cómo se construye el **Perfil de Ponderación Estratégica**: el conjunto de pesos que guía
> la búsqueda (Fase 2) y el scoring (Fase 3). Es el «criterio de negocio + posicionamiento»
> hecho explícito y numérico, y lo que después permite justificar cada selección. Idioma:
> español de España (peninsular).

## Principio

El error de un agente mediocre sería tratar todas las fuentes por igual. Este agente
**pondera**: las **prioridades del cliente actúan como multiplicadores** sobre todo lo
demás. Se construye **antes** de buscar datos y se valida con el consultor (checkpoint).

## Cómo se pondera (preguntas que responde el brief ponderado)

1. **¿Qué mercados/productos prioriza el cliente?** → multiplicador de prioridad sobre los
   términos asociados.
2. **¿Cuál es la persona primaria (del ICP)?** → sus firmas de prompt y su vocabulario pesan
   más.
3. **¿Qué les funciona a los competidores comparables (del 2.2)?** → señal de validación con
   peso según comparabilidad.
4. **¿Dónde están los huecos GEO del mercado (del 2.1)?** → oportunidad de prompt con peso
   alto (territorio sin ocupar).
5. **¿Qué excluye el filtro anti-persona (del ICP)?** → **lista de exclusión dura**: no
   entra en la selección, tenga el volumen que tenga.

## Perfil de Ponderación Estratégica (salida de la fase)

Tabla revisable por el consultor **antes** de buscar datos:

| Dimensión de contexto | Peso por defecto | Ajustable por |
|-----------------------|------------------|----------------|
| Prioridades de negocio (mercado/producto) | Alto (multiplicador ×1.0–1.5) | Foco de mercado (Paso 0) |
| Encaje con ICP / persona primaria | Alto | Foco de persona (Paso 0) |
| Validación competitiva | Medio-alto | Comparabilidad del competidor |
| Demanda / oportunidad de mercado | Medio | Foco de objetivo (Paso 0) |
| Huecos GEO sin ocupar | Alto (solo prompts) | — |
| Filtro anti-persona | Exclusión dura | ICP |

## Cómo el foco del Paso 0 mueve los pesos

- **Foco de objetivo = Conversión** → sube el peso del valor de intención
  (transaccional/comercial) en el KPS; **Tráfico** lo baja a favor de volumen/oportunidad;
  **Equilibrado** los deja por defecto.
- **Foco de mercado** → aplica el multiplicador de prioridad (hasta ×1.5) a los términos del
  mercado elegido.
- **Foco de persona = solo la primaria** → concentra el peso de encaje en sus firmas de
  prompt y vocabulario; **todas** → reparte entre perfiles.

## Checkpoint

Muestras el Perfil de Ponderación y preguntas *«¿Validas o ajustas estos pesos antes de
buscar datos?»*. Esperas el OK. Lo que decida el consultor se registra en
`audit/execution_log.json` y rige el scoring de la Fase 3.
