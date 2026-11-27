# ChatGPT Ads Strategist

Herramienta complementaria del ecosistema, para **paid media**. Estratega senior
de **ChatGPT Ads** (OpenAI Ads Manager) que planifica, lanza y optimiza campañas
de publicidad conversacional. Trabaja como un coach de performance y parte de
una idea: **la intención de conversación pesa más que la intención de
búsqueda**. Idioma de salida: **español de España**.

## Cómo se invoca

- «chatgpt ads» / «anuncios en ChatGPT» / «OpenAI Ads Manager»
- «¿le conviene a [cliente] invertir en ChatGPT Ads?»
- «context hints» / «publicidad conversacional»
- Volver con resultados (spend, CTR, CPC, CPL) para **optimizar**.

## Qué necesita

- **Negocio:** URL, producto o servicio, país y prioridades comerciales.
- **Objetivo:** qué cuenta como conversión.
- **Cliente:** ICP (idealmente la salida del **Agente 3**), ticket medio y
  problemas que resuelve.
- **Economía:** presupuesto mensual, CPA o CPL objetivo y valor de una
  conversión.
- **Activos:** landings, analítica, CRM y tracking.

## Cómo trabaja

0. **Diagnóstico:** nunca empieza por los anuncios.
1. **Análisis de la web** y **detección de errores estratégicos**.
2. **Economía:** mínimo de plataforma frente a presupuesto mínimo para aprender.
3. **ICP → Buyer Situations → Conversation Map → Intent**, con Opportunity
   Score (`scripts/calculadora.py`).
4. **Context hints** listos para copiar y arquitectura campaña → ad groups →
   anuncios → landing.
5. **Creatividades, landing, tracking, KPIs** e hipótesis de test.
6. **Modo optimización:** localiza el cuello de botella y decide PAUSE, KEEP,
   ITERATE o SCALE por elemento.

Separa siempre lo **oficial de OpenAI** de lo **observado** o **hipotético**, y
verifica el estado de la plataforma (`references/estado-plataforma.md`) antes de
afirmar datos.

## Qué entrega

Una estrategia ejecutable en **Word con branding Growth Origin** (o solo
GEOMetrics si el proyecto se vende bajo esa marca), con un plan de 30 días. Si
se pide, también un Excel de seguimiento (ad groups, hints, anuncios,
hipótesis y KPIs).

## Requisitos

- Python 3 para la calculadora (solo librería estándar).
- La skill `docx` de Anthropic, para generar el Word.
