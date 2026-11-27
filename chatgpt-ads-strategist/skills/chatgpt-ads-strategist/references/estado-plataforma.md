# Estado de la plataforma ChatGPT Ads — foto fija

**Fecha de la foto: 15 de septiembre de 2026.** La plataforma está en beta y cambia rápido. Si han pasado más de ~30 días o el dato decide algo importante (presupuesto, país, objetivo, política), reverifica con web search antes de afirmarlo.

Leyenda: 🟢 OFICIAL · 🟡 OBSERVADO · 🔵 HIPÓTESIS · 🔴 NO DEMOSTRADO

## Fuentes a consultar primero

1. help.openai.com → colección "ChatGPT Ads" (artículos "Ads in ChatGPT: The Basics", "Launch Campaigns", "Create Campaigns for ChatGPT").
2. developers.openai.com/ads → medición (píxel, Conversions API).
3. openai.com/policies/ad-policies → políticas y contextos sensibles.
4. openai.com/index → anuncios de expansión y novedades.
5. Secundarias (solo 🟡): Search Engine Land, Search Engine Roundtable, blogs de agencias que operan la plataforma. Úsalas para detectar novedades y luego busca la confirmación oficial.

## Quién ve los anuncios

- 🟢 No se muestran a usuarios de Plus, Pro ni planes Business, ni a cuentas identificadas como menores de 18 (por edad declarada o predicción de edad). En la práctica, la audiencia son usuarios Free y Go.
- 🟢 Los anunciantes no reciben las conversaciones de los usuarios y la publicidad no influye en las respuestas de ChatGPT.
- 🟢 OpenAI aplica salvaguardas de brand safety para no mostrar anuncios en contextos sensibles (detalle en Ads Policies).

## Mercados

- 🟢 Piloto en EE. UU. desde febrero de 2026; Ads Manager self-serve (beta) en EE. UU. desde mayo de 2026.
- 🟢 Expansión a 31 mercados europeos (EEE + Suiza, España incluida) con anuncios activos desde el 24 de agosto de 2026; acceso self-serve vía Ads Manager en esos mercados desde el 31 de agosto de 2026.
- 🟡 Antes, otra ola internacional (Reino Unido, México, Brasil, Japón, Corea del Sur, entre otros); total aproximado de ~40 mercados.
- 🟡 La segmentación por debajo de país (estado, ciudad, código postal) solo existiría en EE. UU. por ahora: una campaña "Barcelona" sería en la práctica una campaña "España". **Verificar antes de prometer segmentación local.** Si no hay segmentación local, la localía se trabaja en hints, copy y landing.

## Estructura y formato

- 🟢 Jerarquía: Campaign (objetivo, presupuesto, fechas, países) → Ad group (temas, intenciones y clústeres de context hints; puja máxima) → Ad.
- 🟢 Unidad de anuncio, debajo de la respuesta de ChatGPT: nombre del anunciante, favicon, título, copy, landing e imagen.
- 🟢 Longitudes recomendadas en la guía de lanzamiento: título 16-24 caracteres, copy 32-48 caracteres; el sistema rechaza esquemas que no cumplan los requisitos.
- 🟡 Máximos aceptados reportados: título hasta 50 y copy hasta 100 caracteres. Escribe a la recomendación: en móvil los títulos largos se truncan.
- 🟡 Imagen cuadrada (reportado hasta 1200×1200 px); mejor un objeto simple que una composición recargada.
- 🟡 Campañas de feed de producto con carrusel multi-producto en pruebas desde agosto de 2026. No hay vídeo documentado.
- 🟡 Carga masiva (bulk upload) por CSV disponible; el esquema completo no está totalmente documentado en público.
- 🟡 Cada anunciante necesita su propia cuenta; las agencias se añaden como usuarios. No hay equivalente a un MCC.

## Selección, subasta y pujas

- 🟢 El sistema elige anuncios por relevancia y resultados esperados, usando el contexto e intención de la conversación, la landing, el título, el copy, los context hints y, si el usuario tiene activada la personalización, señales de su experiencia más amplia en ChatGPT.
- 🟢 Los context hints se definen a nivel de ad group; describen conversaciones, temas o keywords donde la oferta es relevante. **No son keywords de concordancia exacta ni garantizan la entrega** en conversaciones concretas.
- 🟢 Subasta de segundo precio ponderada por relevancia: la puja es solo una variable; la relevancia del anuncio y la landing también cuenta.
- 🟢 Objetivos Reach (CPM) y Clicks (CPC), con puja máxima por ad group. Recomendación oficial para CPC: empezar con puja máxima de 3-5 USD por clic. Ads Manager puede mostrar indicación de competitividad de la puja.
- 🟡 Objetivo Conversions (oCPC) disponible desde el verano de 2026: se paga por clic pero se puja hacia un evento de conversión. Requiere tracking configurado antes y un evento estándar soportado; una campaña CPM/CPC existente no se convierte en oCPC. **Confirmar en la documentación oficial vigente.**
- 🟡 CPM por defecto reportado de 60 USD; CPM medios reportados bajando de ~60 a ~25 USD tras abrir el self-serve en EE. UU. Mercados nuevos = subastas poco pobladas al principio (🔵 ventana de coste bajo para quien llega pronto).
- 🟡 Audiencias personalizadas y exclusiones geográficas añadidas en verano de 2026.

## Presupuesto

- 🟡 El mínimo de 50.000 USD del piloto gestionado desapareció con el self-serve.
- 🟡 Reportado un mínimo de 25 USD/día por campaña para EE. UU. **Desconocido para España/UE: verificar en Ads Manager.**
- 🟡 OpenAI recomienda presupuesto diario como control de ritmo; el presupuesto total de campaña es un límite de gasto, no un control de pacing, y el gasto puede acumularse rápido.

## Medición

- 🟢 Reporting de Ads Manager Beta: impresiones, clics, spend, CTR, CPC medio, CPM medio y conversiones.
- 🟢 Medición de conversiones configurable en Ads Manager (guía en developers.openai.com/ads).
- 🟢 Los parámetros estáticos (UTMs) persisten en el clic y llegan a la analítica habitual.
- 🟢 Impresiones, clics y CTR aparecen en minutos; el spend puede tardar más (spend a cero no significa que no haya cargos).
- 🟡 OpenAI Pixel y Conversions API; el píxel captura un identificador de clic (reportado como `oppref`). Si se usan ambos, enviar el mismo event ID para deduplicar.
- 🟡 Integraciones de medición de terceros añadidas en verano de 2026.
- 🟢 Reporting agregado: sin acceso a conversaciones individuales ni datos personales.

## Lo que aún no sabemos bien (tratar como 🔴 hasta confirmar)

- Qué peso relativo tienen hints, copy y landing en el matching.
- Cuántos hints por ad group son óptimos.
- Si existen exclusiones de contexto (negativos) funcionales.
- Qué CPC y CVR reales tiene cada vertical en España.
- Informes por hint o por tipo de conversación.

Cuando el usuario pregunte algo de esta lista, dilo claramente y propón un test para averiguarlo en su cuenta.
