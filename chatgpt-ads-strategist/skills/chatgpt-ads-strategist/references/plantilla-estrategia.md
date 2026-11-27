# Plantilla de estrategia ChatGPT Ads

Usa esta estructura exacta cuando haya información suficiente. Marca con la leyenda de evidencia (🟢🟡🔵🔴) cualquier dato sobre la plataforma.

## 1. EXECUTIVE SUMMARY
En 5-8 líneas: qué harías, por qué, con cuánto y qué esperas aprender en 30 días. Incluye el veredicto: ¿tiene sentido ChatGPT Ads para este negocio ahora?

## 2. OBJETIVO
- Conversión principal:
- Conversiones secundarias / microconversiones:
- Objetivo de campaña en Ads Manager (Reach / Clicks / Conversions) y por qué:

## 3. ICP
ICP situacional (situación, necesidad, problema, trigger, urgencia, alternativas, momento de compra).

## 4. BUYER SITUATIONS
| # | Situación | Intent | Opportunity Score | Prioridad | Oportunidad |
|---|---|---|---|---|---|

## 5. CONVERSATION MAP
Para las situaciones priorizadas: 5-10 conversaciones representativas con su nivel de intención.

## 6. CAMPAIGN ARCHITECTURE
```
CAMPAIGN …
├── AG01 … (hipótesis)
├── AG02 …
```
Tabla: ad group · hipótesis · intención · landing · puja máxima inicial.

## 7. CONTEXT HINTS
Por ad group, los hints exactos listos para copiar (bloque de código o lista numerada). Indica nivel BROAD/MEDIUM/HIGH si se testean.

## 8. ADS
Por ad group, 3-5 variantes: título · copy · ángulo · caracteres (validados con `calculadora.py anuncios`) · idea de imagen.

## 9. LANDING STRATEGY
Landing por ad group (existente o a crear), auditoría resumida y blueprint si hay que crearla.

## 10. BUDGET
- Mínimo de plataforma (verificado, con fecha):
- Presupuesto de aprendizaje recomendado (salida de `calculadora.py presupuesto`):
- Distribución por ad group y justificación:
- Qué se deja para la segunda ola si el presupuesto no alcanza:

## 11. TRACKING
Tabla de la sección 1 de `medicion-y-optimizacion.md` con estado (OK / Pendiente / No aplica) y responsable.

## 12. TESTING PLAN
Hipótesis numeradas con la plantilla (qué, contra qué, por qué, criterio, volumen mínimo) y orden de ejecución.

## 13. KPIs
- KPIs de negocio con objetivo y máximo tolerable:
- KPIs diagnóstico con rango esperado (🔵 si no hay benchmark local):
- Umbrales de decisión:

## 14. 30-DAY OPTIMIZATION PLAN
Calendario día 1-2, 3-7, 7, 14, 21, 30 adaptado al proyecto.

## 15. PRE-LAUNCH CHECKLIST

**Cuenta y cumplimiento**
- [ ] Cuenta de Ads Manager propia del anunciante, verificada; agencia añadida como usuario
- [ ] Método de pago configurado
- [ ] Oferta y claims revisados contra las Ads Policies vigentes (especial atención a sectores regulados)
- [ ] País de la campaña disponible y condiciones verificadas en la fecha de lanzamiento

**Campaña**
- [ ] Objetivo correcto (Reach / Clicks / Conversions) y evento de conversión seleccionado si es oCPC
- [ ] Presupuesto diario como control de ritmo; fechas definidas
- [ ] Nomenclatura aplicada
- [ ] Número de ad groups compatible con el presupuesto de aprendizaje

**Ad groups y anuncios**
- [ ] Una hipótesis por ad group, hints coherentes y sin keywords sueltas
- [ ] Puja máxima inicial definida (referencia oficial CPC: 3-5 USD; revisar guía de competitividad)
- [ ] 3-5 anuncios por grupo, longitudes validadas, sin claims inventados
- [ ] Imagen cuadrada legible en miniatura; favicon correcto
- [ ] Idioma del anuncio = idioma de la conversación objetivo

**Landing y medición**
- [ ] Message match anuncio ↔ landing comprobado
- [ ] Landing rápida y usable en móvil
- [ ] UTMs en todas las URLs finales
- [ ] Píxel / CAPI disparando y visibles en Ads Manager; deduplicación configurada
- [ ] Conversión visible en analítica y CRM con origen de campaña
- [ ] Consentimiento de cookies compatible con la medición

**Gobierno**
- [ ] Hipótesis escritas y umbrales de decisión acordados con el cliente
- [ ] Fechas de revisión en calendario (día 2, 7, 14, 21, 30)
- [ ] Responsable de calificar leads en el CRM identificado
