# Medición, experimentación y optimización

## Índice
1. Tracking previo al lanzamiento
2. Embudo completo
3. KPIs
4. Diseño de experimentos
5. Plan de optimización de 30 días
6. Modo optimización: diagnóstico
7. Decisiones PAUSE / KEEP / ITERATE / SCALE

---

## 1. Tracking previo al lanzamiento

| Elemento | Qué comprobar | Bloquea el lanzamiento |
|---|---|---|
| Conversion tracking OpenAI | Píxel y/o Conversions API instalados y eventos recibidos en Ads Manager | Sí (y obligatorio para oCPC) |
| Deduplicación | Mismo event ID en píxel y CAPI | Sí si se usan ambos |
| UTMs | `utm_source=chatgpt&utm_medium=cpc&utm_campaign={campaña}&utm_content={adgroup_anuncio}` | Sí |
| Analítica (GA4 u otra) | Sesiones con UTM visibles; eventos clave marcados como conversión | Sí |
| CRM | El lead entra con origen y campaña; estados de cualificación definidos | Recomendado |
| Formularios | Envío probado, página de gracias o evento de envío | Sí |
| Llamadas | Número de seguimiento o evento de clic en teléfono | Si aplica |
| WhatsApp | Evento de clic y, si es posible, mensaje prellenado con referencia | Si aplica |
| Revenue | Valor de conversión o importación offline desde CRM | Recomendado en e-commerce y ticket alto |
| Consentimiento | Banner y modo de consentimiento compatibles con la medición (RGPD en España/UE) | Sí |

Sin tracking de conversión fiable, recomienda no lanzar: se estaría pagando por aprender nada.

## 2. Embudo completo

```
IMPRESSION → CLICK → ENGAGED SESSION → MICROCONVERSION → LEAD → QUALIFIED LEAD → SALE → REVENUE
```

Define para cada proyecto qué es una engaged session (p. ej. >30 s o 2 páginas), qué microconversiones cuentan (scroll al formulario, clic en CTA, uso de calculadora) y qué hace cualificado a un lead.

## 3. KPIs

| Tipo | Métricas | Uso |
|---|---|---|
| **Negocio** | CPA, CPL, CAC, ROAS, revenue, leads cualificados, coste por lead cualificado | Decidir si la campaña funciona |
| **Diagnóstico** | CTR, CPC, CPM, CVR, engagement, tasa de cualificación | Entender por qué funciona o no |

Una campaña nunca se declara exitosa solo por CTR o CPC. Define antes del lanzamiento:
- CPA/CPL objetivo y CPA/CPL máximo tolerable (a partir del valor del cliente).
- Umbral mínimo de datos para decidir (ver sección 4).

## 4. Diseño de experimentos

Ciclo: **HYPOTHESIS → TEST → DATA → LEARNING → SPLIT → SCALE**.

Plantilla de hipótesis:

> Creemos que **[ad group / hint / ángulo / landing A]** conseguirá **[mejor métrica de negocio]** que **[B]** porque **[razón basada en la intención]**. Lo consideraremos validado si **[criterio]** con al menos **[volumen mínimo]**.

Ejemplo: "Los propietarios que preguntan por la valoración de su vivienda tendrán un CPL al menos un 30 % inferior al de quienes preguntan por el mercado en general. Validado con ≥ 15 leads por grupo."

Reglas:
- Una variable por test (hint, o anuncio, o landing, o puja).
- Fija el volumen mínimo antes de mirar resultados (🔵 orientativo: ≥ 100 clics para leer CTR/CVR con cierta estabilidad; ≥ 10-20 conversiones por variante para comparar CPA).
- No toques un ad group en sus primeros días salvo problema grave de entrega o gasto.
- Registra cada cambio con fecha (Ads Manager tiene change log) para interpretar los datos.

Orden de test recomendado: 1) hints / hipótesis conversacional, 2) ángulo creativo, 3) landing, 4) puja y objetivo (p. ej. pasar de CPC a oCPC cuando haya volumen de conversiones).

## 5. Plan de optimización de 30 días

| Momento | Qué revisar | Acción típica |
|---|---|---|
| Día 1-2 | Entrega: impresiones, aprobación de anuncios, píxel disparando, gasto | Corregir rechazos, tracking o pujas que no entregan |
| Día 3-7 | CTR y CPC por ad group y anuncio | Detectar anuncios muy por debajo; no pausar aún por CPA |
| Día 7 | Primera lectura de CVR y calidad de sesión | Revisar landing si hay clics sin engagement |
| Día 14 | CPL/CPA por ad group; primera calidad de lead con ventas | Pausar lo claramente malo; iterar hints y ángulos |
| Día 21 | Leads cualificados y coste por lead cualificado | Redistribuir presupuesto hacia lo que convierte |
| Día 30 | Informe: hipótesis validadas y rechazadas, siguiente ola | SPLIT de ganadores, SCALE, nuevos tests; valorar oCPC |

## 6. Modo optimización: diagnóstico

Datos a pedir: periodo, spend, impresiones, clics, CTR, CPC, conversiones, CVR, CPA/CPL, leads cualificados, ventas, revenue; desglose por campaña, ad group, anuncio y landing; cualquier señal sobre los hints; cambios hechos durante el periodo.

Recorre la cadena y localiza el primer eslabón roto:

| Eslabón | Síntoma | Causas probables | Acción |
|---|---|---|---|
| DELIVERY | Pocas o ninguna impresión | Puja baja, hints demasiado estrechos o genéricos, presupuesto limitado, rechazo de política, poco inventario en el país | Subir puja hacia la guía de Ads Manager, reescribir hints, revisar política |
| CONTEXT | Impresiones pero CTR muy bajo en todos los anuncios | Hint que atrae conversaciones con otra intención | Acotar el hint, separar intenciones |
| CREATIVE | Un anuncio muy por debajo de sus hermanos | Ángulo o mensaje sin conexión | Pausar e iterar ese ángulo |
| CLICK | CTR bueno, CPC alto | Competencia, relevancia baja de la landing | Mejorar relevancia, ajustar puja |
| LANDING | Clics sin engagement, rebote alto | Message mismatch, velocidad, móvil | Landing específica, velocidad |
| CONVERSION | Engagement bueno, pocas conversiones | Fricción, CTA débil, oferta poco clara | Simplificar formulario, reforzar oferta |
| LEAD QUALITY | Muchos leads, pocos cualificados | Intención baja, oferta demasiado fácil | Subir intención del hint, añadir cualificación |
| SALES | Leads cualificados que no cierran | Seguimiento comercial, precio, timing | Revisar proceso comercial con el cliente |

## 7. Decisiones PAUSE / KEEP / ITERATE / SCALE

| Decisión | Criterio orientativo (🔵, ajustar al caso) |
|---|---|
| **PAUSE** | Volumen suficiente y CPA > 1,5-2× el máximo tolerable, o leads sistemáticamente no cualificados |
| **KEEP** | Dentro de objetivo o sin datos suficientes todavía |
| **ITERATE** | Cerca del objetivo o con un eslabón concreto roto que se puede corregir |
| **SCALE** | CPA por debajo del objetivo con volumen estable y calidad confirmada: subir presupuesto de forma gradual (🔵 +20-30 % cada pocos días) y hacer SPLIT de la hipótesis ganadora en variantes |

Entrega el resultado como tabla: elemento · datos · diagnóstico · decisión · siguiente test.
