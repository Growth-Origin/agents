# Esquema de salida — Strategic Keywords & Prompts (Agente 4)

> Estructura del output, inputs aguas arriba, convención de trazabilidad y plantilla de
> recogida del Paso 0. El esquema es estable; cambia el contenido, no las secciones.
> Idioma: español de España (peninsular).

## Idioma

Todo en **español de España (peninsular)**. Tú (singular) y vosotros (plural): tienes,
queréis, podéis, dime, mira, fíjate. **Prohibido cualquier argentinismo** (vos, tenés,
querés, podés, decime, mirá, fijate sin tilde, dale como «ok», armá, pegá, andá, bárbaro,
re- como intensificador, qué onda, laburo, guita, che). Las citas literales (keywords,
prompts, respuestas de motor) se conservan en su idioma original.

## Estructura de carpetas del output

Dentro de la carpeta de trabajo, bajo `clientes/[slug-cliente]/`:

```
clientes/[slug-cliente]/
└── estrategia-keywords-prompts/
    ├── top_keywords_prompts.xlsx   # Libro de 4 pestañas (entregable principal)
    ├── resumen_ejecutivo.md        # Resumen breve para el consultor (o PDF si se pide)
    ├── _fuentes/
    │   ├── contexto_normalizado.md  # Contexto aguas arriba (CKB / ICP / 2.1 / 2.2 / externo)
    │   ├── candidatos.md            # Candidatos derivados del contexto antes de puntuar
    │   ├── datos_keywords.md        # Exports/observaciones de DataForSEO (o aproximación SERP)
    │   └── datos_prompts.md         # Lecturas de GEO Metrics / observación de motores
    └── audit/
        ├── execution_log.json       # Nivel, profundidad, foco, estimación y gasto real, validaciones
        └── sources_accessed.json    # Fuentes accedidas con fecha y método
```

Cabecera del resumen y metadatos del libro:

```markdown
# Universo priorizado de keywords y prompts — [Cliente]

**Versión:** 0.1   ·   **Fecha:** AAAA-MM-DD
**Nivel de investigación:** 1 (sin herramientas) / 2 (DataForSEO + GEO Metrics [+ Semrush])
**Profundidad:** Top 20 / 50 / 100
**Foco:** objetivo [Tráfico/Conversión/Equilibrado] · mercado [...] · persona [todas/primaria]
**Inputs:** CKB / ICP (Agente 3) / Mercado (2.1) / Competidores (2.2) — rutas y versiones (o faltantes)
**Estado:** borrador pendiente de validación humana
```

## Inputs aguas arriba (todo lo de la Capa 1) + fallback

| Fuente | Qué aporta | Si falta |
|--------|------------|----------|
| Cliente / consultor | Prioridades reales: mercados, productos, márgenes, objetivos, foco comercial. **El timón.** | Preguntar: sin prioridades no hay ponderación fiable. |
| CKB (1.1) | Oferta, propuesta de valor, voz, voceros. Contexto base. | Usar paquete externo o lo que aporte el cliente. |
| ICP (Agente 3) | Buyer personas, **firmas de prompt** por persona, etapa/intención, **filtro anti-persona**. | Proponer encaje provisional como hipótesis; preguntar por la persona objetivo y el filtro. |
| Mercado (2.1) | Demanda, vocabulario real, query fan-out, huecos GEO, plataformas, preguntas frecuentes. | Derivar vocabulario de la web/SERP y observación de motores; declararlo menos calibrado. |
| Competidores (2.2) | Keyword gap, prompts donde el competidor es fuerte, qué opina la IA. | Observar SERP/motores para inferir validación competitiva; marcar confianza. |

**Regla de fallback:** trabajas con lo que haya, lo declaras y marcas supuestos. Si falta
algo **crítico** (filtro anti-persona, persona objetivo, prioridades de negocio),
**preguntas** antes de ponderar. No inventas.

## Convención de trazabilidad

Cada dato duro y cada selección llevan, pegada:

`‹fuente: [tipo+ref] | acceso: AAAA-MM-DD | confianza: alta/media-alta/media/baja | tipo: hecho/aproximación/hipótesis›`

Tipos de fuente válidos:

- `ckb: [módulo]` / `icp: [perfil/firma]` / `mercado-2.1: [bloque]` / `competidores-2.2: [tema]` — heredados.
- `herramienta: DataForSEO [endpoint]` / `herramienta: GEO Metrics [endpoint]` / `herramienta: Semrush [report]` — Nivel 2.
- `serp: "[consulta]"` — observación directa del SERP (aproximación, Nivel 1).
- `motor-geo: [motor] | consulta: "..." | repeticiones: N` — observación de citación.
- `cliente: [prioridad/foco]` — input del consultor o el cliente.

Sin fuente real, no hay dato: lo no recuperable va a «requiere herramienta (Nivel 2+)» o
«dato no disponible», nunca se inventa.

## Plantilla de recogida (Paso 0)

~~~text
Antes de priorizar keywords y prompts necesito configurar el entregable.

1) NIVEL DE INVESTIGACIÓN
- Nivel 1 (sin herramientas de pago): Claude + web + Chrome. Coste cero; datos duros aproximados o marcados.
- Nivel 2 (con herramientas): DataForSEO (keywords) + GEO Metrics (prompts), Semrush opcional.
  ⚠️ DataForSEO/Semrush consumen créditos. Si es Nivel 2, te doy una estimación de coste antes de proceder.

2) PROFUNDIDAD (obligatoria): Top 20 / Top 50 / Top 100 (por keywords y por prompts)

3) FOCO (opcional)
- objetivo: Tráfico / Conversión / Equilibrado [def. Equilibrado]
- mercado: [si hay varios, cuál prioriza] [def. todos]
- persona: todas / solo la primaria [def. primaria con peso]

4) CONTEXTO (lo que tengas; con más, mejor calibrado)
- CKB (1.1), ICP (Agente 3), Mercado (2.1), Competidores (2.2), o paquete externo
- prioridades del cliente: mercados, productos, márgenes, objetivos, foco comercial

Con esto construyo el Perfil de Ponderación y te lo paso a validar ANTES de buscar datos.
~~~
