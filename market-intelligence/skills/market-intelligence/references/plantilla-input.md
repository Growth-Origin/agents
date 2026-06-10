# Plantilla de input — Paso 0 (toma de datos) — Market Intelligence (Agente 2.1)

Campos fijos que el agente recoge del operador antes de investigar. Mismo
formato cada vez: si algunos vienen en el mensaje del operador, el agente
pregunta solo lo que falte, pero siempre cubre los obligatorios y confirma los
parámetros por defecto. Idioma del diálogo: español de España (peninsular).

## Campos obligatorios

| Campo          | Descripción                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `slug_cliente` | Identificador del cliente, derivado del nombre comercial (kebab-case).      |
| `ckb_cliente`  | Ruta a la carpeta `ckb/` del cliente (output del Agente 1.1, CKB Builder). Es el ancla de todo el análisis. |

Si no existe CKB (cliente que no pasó por el Agente 1.1), el agente **no parte de
cero ni inventa el contexto**: acuerda con el operador un pase mínimo de contexto
(sector, propuesta de valor, oferta, voceros, canales actuales) antes de seguir.

## Parámetros de configuración (opcionales, con valor por defecto)

| Parámetro        | Descripción                                   | Por defecto                                              |
|------------------|-----------------------------------------------|---------------------------------------------------------|
| `idioma_mercado` | Idioma/geografía objetivo del análisis        | Detectar del CKB                                        |
| `n_consultas_geo`| Nº de consultas a probar en motores generativos| 10                                                      |
| `profundidad`    | Intensidad de investigación                    | `profunda` (`ligera` / `media` / `profunda`)            |
| `motores_geo`    | Motores generativos a auditar                  | ChatGPT, Perplexity, Google AI Overviews, Gemini        |

El detalle de qué implica cada nivel de `profundidad` (presupuesto de búsquedas y
reparto por bloque) está en `guia-investigacion.md`.

## Plantilla de recogida (lo que el agente muestra al operador)

~~~text
Para arrancar el análisis de mercado necesito confirmar estos datos:

OBLIGATORIOS
- slug_cliente: ...
- ckb_cliente (ruta a la carpeta ckb/ del cliente): ...

PARÁMETROS (si no dices nada, uso los valores por defecto)
- idioma_mercado: [por defecto, lo detecto del CKB]
- n_consultas_geo: [por defecto, 10]
- profundidad: ligera | media | profunda [por defecto, profunda]
- motores_geo: [por defecto, ChatGPT, Perplexity, Google AI Overviews, Gemini]

¿Confirmas o ajustas algo antes de que lea el CKB y monte el plan?
~~~

## Qué pasa después del Paso 0

Con los campos obligatorios cubiertos, el agente:

1. Lee el CKB y extrae el contexto que ancla el análisis (sector, propuesta de
   valor, oferta, voceros, voz de mercado, canales actuales).
2. Deriva las consultas clave y el reparto de investigación por bloque.
3. **Muestra el plan al operador y espera su OK antes de buscar** (checkpoint del
   Paso 1). No empieza a investigar sin esa validación.

Recordatorio: el agente conduce la investigación; el analista co-pilota y puede
ajustar consultas, foco o presupuesto en cualquier momento.
