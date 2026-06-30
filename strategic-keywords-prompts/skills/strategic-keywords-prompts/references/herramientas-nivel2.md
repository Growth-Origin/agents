# Herramientas de Nivel 2 y estimación de coste — Strategic Keywords & Prompts (Agente 4)

> Qué aporta cada herramienta, qué cobra y **cómo se estima el coste antes de proceder**
> (requisito del Paso 0). Stack continuista con el Agente 2.2. Idioma: español de España.

## Mapa herramienta → mundo

| Herramienta | Mundo | Qué aporta | Modelo de coste |
|-------------|-------|------------|-----------------|
| **DataForSEO** | Keywords | Volumen y estacionalidad (`kw_data_*`), dificultad/competencia, CPC, intención y features de SERP (AI Overview, snippet) (`dataforseo_labs_search_intent`, `serp_*`), quién rankea | **Pago por uso** (coste por llamada) |
| **GEO Metrics** | Prompts | Citación de marca/competidores por motor (`get_ranking_prompt_details`), consistencia, huecos de citación y sentimiento (`get_sentiment_extraction`), volumen + `chatbot_preference` (`get_keyword_execution`) | **Lectura por conector = gratis**; ejecuciones en su web sí gastan (fuera del agente) |
| **Semrush** (opcional) | Keywords | Segunda fuente para **triangular** dificultad y audiencia | **Unidades de API por report** |

> Ahrefs / SE Ranking no son necesarios aquí; solo como segunda fuente de dificultad en
> despliegues de mayor escala (Nivel 3 de implementación).

## Qué cobra de verdad

- **Coste monetario directo:** **DataForSEO** (por llamada) y **Semrush** (unidades). Son
  los que hay que estimar y vigilar.
- **Sin coste por llamada:** GEO Metrics (lecturas). Pero recuerda el **bucle GEO Metrics**:
  solo se leen prompts ya cargados y ejecutados; si no existen, el agente los genera, avisa
  de que un humano debe cargarlos/ejecutarlos en la web (ahí está el coste/manual) y luego
  los lee.

## Tabla de referencia de coste (para la estimación)

> Precios orientativos heredados del uso de los Agentes 2.1/2.2; **confírmalos con el plan
> vigente del operador antes de tiradas grandes** (los créditos exactos no son visibles
> desde el conector).

**DataForSEO (pago por llamada):** coste pequeño por petición; lo que escala es el **número
de llamadas**. Endpoints típicos aquí: volumen/keyword (`kw_data` en lotes), dificultad,
SERP/intención (`serp_organic_live_advanced`, una por consulta), ranked keywords del
competidor. La factura crece con el nº de keywords candidatas y de consultas de SERP.

**Semrush (unidades por llamada):** `domain_rank` 10 u.; keyword overview ~10 u.; reports de
dificultad/audiencia, decenas según report. Solo si se activa para triangular.

## Método de estimación (lo que el agente muestra en el Paso 0)

1. **Cuenta el trabajo:** nº de keywords candidatas (derivadas del contexto, no del aire) y
   nº de prompts candidatos, según la **profundidad** elegida (Top 20/50/100) y un colchón
   de candidatos por encima del corte.
2. **Traduce a llamadas:** keywords en lotes para volumen; una llamada de SERP/intención por
   consulta que de verdad importe; prompts vía GEO Metrics (lectura gratis; ejecución en web
   si no existen).
3. **Aplica la tabla:** DataForSEO = nº de llamadas × coste por llamada del plan; Semrush =
   Σ(reports × unidades) si se usa; GEO Metrics = 0 € por lectura (nota del bucle de carga).
4. **Presenta el rango y espera el OK** antes de proceder.

### Plantilla de aviso de coste

~~~text
Estimación de coste — Nivel 2 (keywords y prompts de [cliente])

Profundidad: Top [N]   ·   Candidatos a consultar: ~[K] keywords / ~[P] prompts

- DataForSEO: ~[llamadas] llamadas (volumen en lotes + SERP/intención + ranked del competidor) → coste por uso del plan
- Semrush (si se usa): ~[reports] x [unidades] u. = ~[total] unidades
- GEO Metrics: lectura sin coste; [P] prompts — [ya existen / hay que cargarlos y ejecutarlos en web antes de leer]

Total estimado: [coste DataForSEO] + [unidades Semrush]. ¿Procedo o ajusto la profundidad/alcance?
~~~

## Guardarraíl (no negociable)

- En **Nivel 1** no se llama a ninguna herramienta externa aunque esté conectada.
- En **Nivel 2** se consulta **solo para candidatos relevantes** (derivados del contexto
  ponderado), en lotes, ciñéndose a la profundidad.
- **Antes de proceder** con DataForSEO/Semrush: estimación + OK explícito.
- Lo que no se recupere se marca «requiere herramienta (Nivel 2+)» o «dato no disponible».
- Se registra en `audit/execution_log.json`: nivel, profundidad, estimación y gasto real.
