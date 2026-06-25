# Esquema de salida — ICP Definer (Agente 3)

> Define la estructura del output del ICP Definer: las carpetas, las cabeceras, la
> convención de trazabilidad, los inputs (CKB / 2.1 / 2.2 / paquete externo) y la
> plantilla de recogida del Paso 0. El esquema es estable; cambia el contenido, no las
> secciones.

## Idioma

Todo el contenido en **español de España (peninsular)**. Tú (singular) y vosotros
(plural): tienes, queréis, podéis, dime, mira, fíjate. **Prohibido cualquier
argentinismo** (vos, tenés, querés, podés, decime, mirá, fijate sin tilde, dale como
«ok», armá, pegá, andá, bárbaro, re- como intensificador, qué onda, laburo, guita,
che). Las citas literales (lenguaje real, reseñas, transcripciones, respuestas de un
motor) se conservan en su idioma original.

## Estructura de carpetas del output

Dentro de la carpeta de trabajo, bajo `clientes/[slug-cliente]/`:

```
clientes/[slug-cliente]/
└── icp/
    ├── propuesta_perfiles.md     # Dimensionado (Fase 1): nº de perfiles + persona negativa, VALIDADO
    ├── icp_perfiles.md           # Los N perfiles con las 4 capas (documento principal)
    ├── outputs_accionables.md    # Mapa priorización + matriz persona x etapa x intención + filtro anti-persona + conclusiones
    ├── icp_estructurado.json     # ICP en JSON para consumo automático downstream (recomendado en Nivel 2)
    ├── resumen_ejecutivo.pdf     # Resumen presentable 2-4 págs (plantilla-resumen-pdf.md)
    ├── _fuentes/
    │   ├── contexto_normalizado.md   # Contexto del cliente (CKB / 2.1 / 2.2 / paquete externo)
    │   ├── voz_cliente.md            # Lenguaje real, objeciones, JTBD (reseñas, foros, Gong/Fireflies)
    │   ├── demografia_audiencia.md   # Demografía e intereses (SimilarWeb / DataForSEO / Semrush) o aproximación
    │   └── firma_prompt.md           # Observación de motores: cómo formula cada persona sus preguntas a la IA
    └── audit/
        ├── execution_log.json        # Nivel elegido, herramientas, estimación y gasto real, validación Fase 1
        └── sources_accessed.json     # Fuentes accedidas con fecha y método
```

Cabecera de `icp_perfiles.md`:

```markdown
# ICP y buyer personas — [Nombre Cliente]

**Versión:** 0.1
**Fecha:** AAAA-MM-DD
**Nivel de investigación:** 1 (sin herramientas) / 2 (con [herramientas])
**Modelo:** B2B / B2C / B2B2C
**Nº de perfiles (validado):** [N] + 1 persona negativa
**Perfil primario:** [nombre]
**Origen del contexto:** CKB 1.1 / Agente 2.1 / Agente 2.2 / paquete externo (rutas y versiones)
**Estado:** borrador pendiente de validación humana
```

## Estructura interna de cada perfil

Cada perfil se redacta con las cuatro capas de `esqueleto-perfil.md`: **ICP**
(cuenta/segmento) → **Buyer Persona** (individuo) → **JTBD** (motivación) → **GEO/SEO**
(firma de prompt, funnel, canales). Se omiten los campos que no aplican al negocio.

## Convención de trazabilidad

Cada afirmación factual o atributo clave lleva, pegada:

`‹fuente: [tipo+ref] | acceso: AAAA-MM-DD | confianza: alta/media-alta/media/baja | tipo: hecho/interpretación/hipótesis›`

Tipos de fuente válidos:

- `ckb: [módulo]` — dato heredado del CKB (Agente 1.1).
- `mercado-2.1: [bloque]` — segmentos de demanda, plataformas, E-E-A-T del sector.
- `competidores-2.2: [tema]` — a quién sirven los competidores, opinión de la IA, gaps.
- `voz-cliente: [reseña/foro/transcripción]` — lenguaje real, objeciones, JTBD.
- `web: [URL]` — página o dato público indexado.
- `motor-geo: [motor] | consulta: "..." | repeticiones: N` — observación de la firma de prompt.
- `herramienta: [DataForSEO/Semrush/GEO Metrics/SimilarWeb/HubSpot/Gong/Fireflies]` — solo en Nivel 2.
- `cliente: [input/foco comercial]` — lo que aporta el consultor o el cliente.

**Trazabilidad atómica, no agregada.** Cada cifra demográfica, volumen o señal lleva
la fuente de ESE dato. Los datos heredados se marcan validados o hipótesis según
venían del CKB/2.1/2.2: no conviertas en hecho lo que upstream dejó sin validar.

Regla de oro: sin fuente real, no hay afirmación. Lo no recuperable va a «dato no
disponible» o «requiere herramienta (Nivel 2+)», nunca se inventa. Las «fairytale
personas» están prohibidas.

## Inputs: contexto del cliente (3 orígenes) + 2.1/2.2

El contexto puede venir del **CKB (1.1)**, de los **outputs del Agente 2.1 (mercado)
y/o 2.2 (competidores)**, o de un **paquete de contexto externo** (docs de otra
agencia), que se normaliza a `_fuentes/contexto_normalizado.md`. No hay dependencia
dura del Agente 1.1.

| Fuente | Uso en el ICP |
|--------|----------------|
| Contexto (CKB / 2.1 / paquete externo) — sector, oferta, propuesta de valor, voz | Ancla la capa ICP y el lenguaje real |
| Agente 2.1 — segmentos de demanda distintos | Insumo nº 1 del dimensionado (¿cuántas personas?) |
| Agente 2.1 — plataformas y canales del nicho | Capa GEO/SEO: dónde busca cada persona |
| Agente 2.1 — top preguntas / huecos GEO | Firma de prompt y temas de alto valor |
| Agente 2.2 — a quién sirven los competidores, opinión de la IA | Objeciones, percepción y posicionamiento de la persona |
| Input del cliente — foco comercial, restricciones, casos ganados | Prioriza el perfil primario y acota nº de perfiles |

## Plantilla de recogida (lo que el agente muestra al operador en el Paso 0)

~~~text
Antes de definir el ICP necesito dos cosas.

1) NIVEL DE INVESTIGACIÓN
- Nivel 1 (sin herramientas de pago): solo Claude + búsqueda web + Claude in Chrome. Coste cero.
- Nivel 2 (con herramientas): DataForSEO / Semrush / GEO Metrics / SimilarWeb / Gong-Fireflies / HubSpot.
  ⚠️ DataForSEO y Semrush consumen créditos. Si eliges Nivel 2, te doy una estimación de coste antes de ejecutar.
¿Qué nivel quieres? (y, si es Nivel 2, qué herramientas)

2) CONTEXTO
OBLIGATORIO
- slug_cliente: ...
- contexto_cliente (UNO vale): ckb/ ó outputs del 2.1/2.2 ó paquete de docs externos
RECOMENDADO
- analisis_mercado (2.1) y analisis_competitivo (2.2): mejor calibrado si existen
- input_cliente: foco comercial, segmentos prioritarios, restricciones, clientes ganados

Con esto dimensiono cuántos perfiles hacen falta y te lo paso a validar ANTES de construir.
~~~
