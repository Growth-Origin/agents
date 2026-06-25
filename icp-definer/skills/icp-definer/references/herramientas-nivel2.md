# Herramientas de Nivel 2 y estimación de coste — ICP Definer (Agente 3)

> Qué aporta cada herramienta a qué capa del perfil, qué cobra, y **cómo se estima el
> coste antes de ejecutar** (requisito del Paso 0). Idioma: español de España.

## Principio

El ICP es sobre todo **síntesis**: las herramientas no deciden el perfil, lo
**fundamentan** con demografía, lenguaje real y señales de comportamiento. En Nivel 1
no se llama a ninguna; en Nivel 2 se usan **solo las que el operador autorice** y
**siempre tras una estimación de coste**.

## Mapa herramienta → capa del perfil

| Herramienta | Capa que alimenta | Qué aporta | Modelo de coste |
|-------------|-------------------|------------|-----------------|
| **GEO Metrics** | GEO/SEO, Objeciones | Firma de prompt y rendimiento por persona (`get_ranking_prompt_details`); percepción de la IA sobre cliente y competidores (`get_sentiment_extraction`); volumen + `chatbot_preference` (`get_keyword_execution`) | **Lectura por conector = gratis.** Crear proyectos o ejecuciones en su web sí gasta (fuera del agente) |
| **DataForSEO** | GEO/SEO, ICP | Demografía por keyword/tendencia (`kw_data_dfs_trends_demography`); intención de búsqueda (`dataforseo_labs_search_intent`); volúmenes y segmentos de demanda | **Pago por uso** (coste por llamada) |
| **Semrush** | GEO/SEO, ICP | Datos de keyword, audiencia y `.Trends` (solape de audiencia, demografía) para triangular | **Unidades de API por report** |
| **SimilarWeb** | ICP (segmento), Canales | Demografía de audiencia, intereses, geografía, fuentes de tráfico, solape con competidores | **Suscripción** (lectura sin coste por llamada) |
| **Gong / Fireflies** | Buyer Persona, JTBD | Transcripciones reales → lenguaje literal, objeciones, pain points, trigger events | **Suscripción** (lectura sin coste por llamada) |
| **HubSpot (CRM)** | ICP (firmográficos, señales) | Clientes ganados reales → firmográficos, señales de comportamiento, trigger events observados | **Suscripción** (lectura sin coste por llamada) |

## Qué cobra de verdad

- **Coste monetario directo:** **DataForSEO** (por llamada) y **Semrush** (unidades de
  API). Son los dos que hay que estimar y vigilar.
- **Sin coste por llamada:** GEO Metrics (lecturas), SimilarWeb, Gong, Fireflies,
  HubSpot — van dentro de su suscripción. Se respetan sus límites de uso, pero no
  inflan la factura por consulta.

## Tabla de referencia de coste (para la estimación)

> Precios orientativos heredados del uso de los Agentes 2.1/2.2; **confírmalos con el
> plan vigente del operador antes de tiradas grandes** (los créditos exactos no son
> visibles desde el conector).

**Semrush (unidades de API por llamada):**

| Report | Unidades aprox. |
|--------|-----------------|
| `domain_rank` / overview | 10 |
| keyword overview / por keyword | 10 |
| reports de audiencia / `.Trends` | según report (decenas) |
| `backlinks_*` (si se usaran) | 40 por línea |

**DataForSEO (pago por llamada):** coste pequeño por petición; lo que escala es el
**número de llamadas** (una por lote de keywords / por tendencia demográfica / por
clasificación de intención). La factura crece con el nº de keywords y de perfiles.

## Método de estimación (lo que el agente muestra en el Paso 0)

1. **Cuenta el trabajo:** nº de perfiles a fundamentar (de la Fase 1) x nº de
   keywords/consultas por perfil (firma de prompt, intención, temas de alto valor).
2. **Traduce a llamadas:** agrupa en lotes (no una llamada por keyword suelta cuando el
   endpoint admite lotes).
3. **Aplica la tabla:** Semrush = Σ(reports x unidades); DataForSEO = nº de llamadas x
   coste por llamada del plan; las de suscripción = 0 € por llamada (solo nota de uso).
4. **Presenta el rango** y **espera el OK** antes de ejecutar.

### Plantilla de aviso de coste

~~~text
Estimación de coste — Nivel 2 (ICP de [cliente])

Perfiles a fundamentar: [N]   ·   Keywords/consultas por perfil: ~[K]

- DataForSEO: ~[llamadas] llamadas (demografía + intención + volumen) → coste por uso del plan
- Semrush: ~[reports] reports x [unidades] u. = ~[total] unidades
- GEO Metrics / SimilarWeb / Gong-Fireflies / HubSpot: lecturas dentro de suscripción (0 € por llamada)

Total estimado: ~[unidades Semrush] u. + [coste DataForSEO]. ¿Lo lanzo o ajusto el alcance?
~~~

## Guardarraíl (no negociable)

- En **Nivel 1** no se llama a ninguna herramienta externa aunque esté conectada.
- En **Nivel 2** se llama solo a las autorizadas, en lotes, ciñéndose al presupuesto.
- **Antes de cualquier tirada grande** de DataForSEO/Semrush: estimación + OK explícito.
- Lo que no se recupere se marca «requiere herramienta (Nivel 2+)» o «dato no
  disponible»; nunca se inventa un dato duro.
- Se registra en `audit/execution_log.json`: nivel, herramientas, estimación y gasto
  real.
