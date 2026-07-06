# Herramientas de Nivel 2 y estimación de coste — Competitive Intelligence (Agente 2.2)

> Qué aporta cada herramienta, qué cobra y **cómo se estima el coste antes de una
> tirada grande** (guardarraíl del SKILL). Mismo método que los Agentes 3 y 4.
> Idioma: español de España.

## Mapa herramienta → tema

| Herramienta | Temas que alimenta | Qué aporta | Modelo de coste |
|-------------|--------------------|------------|-----------------|
| **GEO Metrics** | 4.1, 4.2, 4.3 | Rendimiento generativo (`get_project_overview`, `get_ranking_prompt_details`); opinión de la IA vs competidores (`get_sentiment_extraction`); volumen + `chatbot_preference` (`get_keyword_execution`) | **Lectura por conector = gratis.** Crear proyectos o ejecuciones en su web sí gasta (fuera del agente) |
| **DataForSEO** | 4.1, 4.4 | Keywords con volumen/dificultad/tráfico, SERP, ranked keywords del competidor, **backlinks y link gap** | **Pago por uso** (coste por llamada) |
| **Semrush / Ahrefs** | 4.1, 4.4 | Alternativa/triangulación de dificultad y backlinks; Semrush añade filtro por categoría/país en el link gap | **Unidades de API por report** (Semrush) |

## Qué cobra de verdad

- **Coste monetario directo:** **DataForSEO** (por llamada) y **Semrush** (unidades
  de API). Con 3–5 competidores el gasto escala rápido: estima siempre.
- **Sin coste por llamada:** GEO Metrics (lecturas). Recuerda su **bucle**: solo se
  leen prompts/ejecuciones que ya existan; si faltan, se generan, un humano los
  carga y ejecuta en la web, y luego se leen.

## Tabla de referencia de coste (para la estimación)

> Precios orientativos del uso real del ecosistema; **confírmalos con el plan
> vigente del operador antes de tiradas grandes** (los créditos exactos no son
> visibles desde el conector).

**Semrush (unidades de API por llamada):** `domain_rank` / overview 10 u.;
`backlinks_overview` 40 u.; `backlinks_comparison` (link gap) 40 u. por línea;
`backlinks_categories_profile` 40 u. por línea; `backlinks_ascore_profile` 100 u.

**DataForSEO (pago por llamada):** coste pequeño por petición; lo que escala es
el **número de llamadas x número de competidores** (ranked keywords por dominio,
keyword gap, backlinks por dominio, SERP por consulta). La factura crece con el
nº de competidores validados.

## Método de estimación (lo que el agente muestra antes de la tirada)

1. **Cuenta el trabajo:** nº de competidores validados x datos por competidor
   (ranked keywords, gap, backlinks) + consultas de SERP del plan.
2. **Traduce a llamadas:** agrupa en lotes por competidor; no repitas dominios.
3. **Aplica la tabla:** DataForSEO = nº de llamadas x coste por llamada del plan;
   Semrush = Σ(reports x unidades); GEO Metrics = 0 € por lectura.
4. **Presenta el rango y espera el OK** antes de ejecutar.

### Plantilla de aviso de coste

~~~text
Estimación de coste — Nivel 2 (análisis competitivo de [cliente])

Competidores validados: [N]   ·   Datos por competidor: keywords + gap + backlinks

- DataForSEO: ~[llamadas] llamadas ([N] x ranked/gap/backlinks + SERP) → coste por uso del plan
- Semrush (si se usa): ~[reports] reports x [unidades] u. = ~[total] unidades (link gap con filtro de categoría/país)
- GEO Metrics: lecturas sin coste ([nota del bucle si hay que cargar prompts])

Total estimado: [coste DataForSEO] + [unidades Semrush]. ¿Lo lanzo o ajusto competidores/alcance?
~~~

## Guardarraíl (no negociable)

- En **Nivel 1** no se llama a ninguna herramienta externa aunque esté conectada.
- En **Nivel 2** se consulta solo para los competidores validados en el Paso 1,
  en lotes, ciñéndose al presupuesto del nivel de profundidad.
- **Antes de cualquier tirada grande** de DataForSEO/Semrush: estimación + OK.
- Lo que no se recupere se marca «requiere herramienta (Nivel 2+)» o «dato no
  disponible»; nunca se inventa.
- Se registra en `audit/execution_log.json`: nivel, herramientas, estimación y
  gasto real.
