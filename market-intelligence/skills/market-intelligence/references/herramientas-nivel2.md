# Herramientas de Nivel 2 y estimación de coste — Market Intelligence (Agente 2.1)

> Qué aporta cada herramienta, qué cobra y **cómo se estima el coste antes de una
> tirada grande** (guardarraíl del SKILL). Mismo método que los Agentes 3 y 4.
> Idioma: español de España.

## Mapa herramienta → necesidad

| Herramienta | Qué aporta al 2.1 | Modelo de coste |
|-------------|-------------------|-----------------|
| **GEO Metrics** | Panorama generativo: prompts y rendimiento (`list_project_prompts`, `get_ranking_prompt_details`, `get_project_overview`); sentiment vs competidores (`get_sentiment_extraction`); volumen + `chatbot_preference` (`get_keyword_execution`) | **Lectura por conector = gratis.** Crear proyectos o ejecuciones en su web sí gasta (fuera del agente) |
| **DataForSEO** | Volúmenes exactos y estacionalidad, dificultad de keyword, SERP, backlinks | **Pago por uso** (coste por llamada) |
| **Semrush / Ahrefs** | Alternativa/triangulación para dificultad de keyword y backlinks | **Unidades de API por report** (Semrush) |

## Qué cobra de verdad

- **Coste monetario directo:** **DataForSEO** (por llamada) y **Semrush** (unidades
  de API). Son los que hay que estimar y vigilar.
- **Sin coste por llamada:** GEO Metrics (lecturas). Recuerda su **bucle**: solo se
  leen prompts/ejecuciones que ya existan en el proyecto; si faltan, se generan,
  un humano los carga y ejecuta en la web, y luego se leen.

## Tabla de referencia de coste (para la estimación)

> Precios orientativos del uso real del ecosistema; **confírmalos con el plan
> vigente del operador antes de tiradas grandes** (los créditos exactos no son
> visibles desde el conector).

**Semrush (unidades de API por llamada):** `domain_rank` / overview 10 u.;
keyword overview ~10 u. por keyword; `backlinks_*` 40 u. por línea;
`backlinks_ascore_profile` 100 u.

**DataForSEO (pago por llamada):** coste pequeño por petición; lo que escala es
el **número de llamadas** (volúmenes por lote de keywords, una consulta de SERP
por término que de verdad importe, backlinks por dominio). La factura crece con
el nº de keywords semilla y de dominios consultados.

## Método de estimación (lo que el agente muestra antes de la tirada)

1. **Cuenta el trabajo:** nº de keywords semilla del plan validado x métricas
   necesarias (volumen, dificultad) + nº de dominios para backlinks (si aplica).
2. **Traduce a llamadas:** agrupa en lotes (no una llamada por keyword suelta
   cuando el endpoint admite lotes).
3. **Aplica la tabla:** DataForSEO = nº de llamadas x coste por llamada del plan;
   Semrush = Σ(reports x unidades); GEO Metrics = 0 € por lectura.
4. **Presenta el rango y espera el OK** antes de ejecutar.

### Plantilla de aviso de coste

~~~text
Estimación de coste — Nivel 2 (análisis de mercado de [cliente])

Keywords semilla a consultar: ~[K]   ·   Dominios para backlinks: [D]

- DataForSEO: ~[llamadas] llamadas (volúmenes en lotes + SERP + backlinks) → coste por uso del plan
- Semrush (si se usa): ~[reports] reports x [unidades] u. = ~[total] unidades
- GEO Metrics: lecturas sin coste ([nota del bucle si hay que cargar prompts])

Total estimado: [coste DataForSEO] + [unidades Semrush]. ¿Lo lanzo o ajusto el alcance?
~~~

## Guardarraíl (no negociable)

- En **Nivel 1** no se llama a ninguna herramienta externa aunque esté conectada.
- En **Nivel 2** se consulta solo lo derivado del plan validado, en lotes,
  ciñéndose al presupuesto de búsquedas del nivel de profundidad.
- **Antes de cualquier tirada grande** de DataForSEO/Semrush: estimación + OK.
- Lo que no se recupere se marca «requiere herramienta (Nivel 2+)» o «dato no
  disponible»; nunca se inventa.
- Se registra en `audit/execution_log.json`: nivel, herramientas, estimación y
  gasto real.
