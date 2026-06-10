# Parámetros de enfoque y selección de competidores — Agente 2.2

Campos del Paso 0 y criterios con que el agente propone y valida la lista de
competidores. Idioma del diálogo: español de España (peninsular).

## Campos obligatorios (Paso 0)

| Campo | Descripción |
|-------|-------------|
| `slug_cliente` | Identificador del cliente (kebab-case). |
| `ckb_cliente` | Ruta a la carpeta `ckb/` del cliente (Agente 1.1). |
| `analisis_mercado` | Ruta al output del Agente 2.1 del cliente. Si no existe, se señala: el 2.2 rinde mucho más anclado en el 2.1. Acordar con el operador seguir sin él o ejecutarlo antes. |

## Parámetros de enfoque (acotan el universo competitivo)

El análisis se acota a lo que el cliente quiere posicionar. El agente recibe y
respeta:

| Parámetro | Ejemplos | Efecto en el análisis |
|-----------|----------|------------------------|
| `sector_nicho` | «software de facturación para autónomos», «clínica dental en Les Corts» | Define el universo competitivo |
| `modelo` | B2B / B2C / B2B2C | Cambia qué competidores y señales importan |
| `geografia` | ciudades / países / idioma objetivo | Acota a competidores que pelean ese territorio |
| `caracteristicas` | gama de precio, vertical, tamaño | Filtra a competidores realmente comparables |
| `tipo_competidor` | directo / indirecto / aspiracional | Permite analizar a quien el cliente quiere igualar |

## Parámetros opcionales

| Parámetro | Por defecto |
|-----------|-------------|
| `competidores_radar` | Lista que el cliente ya tiene en mente; se cruza con la propuesta del agente |
| `profundidad` | `muy_alta` (`media` / `alta` / `muy_alta`) |
| `nivel_implementacion` | 1 (sin APIs). El 2 desbloquea datos duros por API |

## Cómo se propone la lista de competidores (Paso 1)

**Punto clave:** un «competidor» para este agente es **quien posiciona bien en el
nicho objetivo**, no necesariamente el rival comercial que el cliente nombraría.
El agente puede descubrir competidores SEO/GEO que el cliente no tenía en el
radar.

El agente propone una **lista priorizada de candidatos** combinando:

1. **La lista nominada que dejó el Agente 2.1** en sus notas para agentes
   downstream (si existe), como punto de partida.
2. **Quién aparece en las respuestas de los motores generativos** para las
   consultas clave del nicho (presencia GEO real).
3. **Quién domina el SERP** para las consultas comerciales del nicho (visibilidad
   orgánica observada).
4. **Solapamiento de temática y oferta** con el cliente (comparabilidad según los
   parámetros de enfoque).
5. Los `competidores_radar` que aporte el operador.

Para cada candidato, la propuesta indica: por qué representa el «mejor en su
clase» para el nicho y los parámetros, su tipo (directo / indirecto /
aspiracional) y la señal que lo justifica (visibilidad orgánica, presencia en IA,
solapamiento). Número orientativo a diseccionar: **3–5 competidores**.

## Plantilla de recogida (lo que el agente muestra al operador)

~~~text
Para arrancar el análisis competitivo necesito:

OBLIGATORIOS
- slug_cliente: ...
- ckb_cliente (ruta a ckb/): ...
- analisis_mercado (ruta al output del Agente 2.1): ...

PARÁMETROS DE ENFOQUE
- sector_nicho: ...
- modelo: B2B / B2C / B2B2C
- geografia: ...
- caracteristicas: gama de precio / vertical / tamaño
- tipo_competidor: directo / indirecto / aspiracional

OPCIONALES
- competidores_radar: [los que el cliente ya tenga en mente]
- profundidad: media / alta / muy_alta [por defecto muy_alta]

Con esto propongo la lista de competidores y te la paso a validar ANTES de
diseccionar.
~~~

## Checkpoint

Tras la propuesta, el agente pregunta *«¿Validas o ajustas esta lista de
competidores antes de la disección?»* y espera el OK. El analista puede
añadir/quitar; el agente acata y deja constancia en `audit/execution_log.json`.
