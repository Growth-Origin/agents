# ICP Definer — Agente 3

Define el **Cliente Ideal (ICP)** accionable de un cliente para SEO y GEO. Es el agente
más prescriptivo de la Capa de Conocimiento: convierte la inteligencia de mercado (2.1),
de competidores (2.2) y el CKB (1.1) en un conjunto mínimo de perfiles que el resto del
ecosistema usa para priorizar y calibrar. Opera **humano-en-el-bucle**: propone con
fundamento y el consultor valida. Idioma de salida: **español de España**.

## Cómo se invoca

Instálalo desde el marketplace y, en una conversación, dile alguna de estas frases:

- «agente 3»
- «define el ICP de [cliente]»
- «construye el ICP» / «buyer persona» / «perfil de cliente ideal» / «a quién le hablamos»

**Antes de invocarlo**, ten a mano el contexto del cliente (cualquiera de estos sirve, no
hace falta los tres): el **CKB** (Agente 1.1), los outputs del **Agente 2.1** (mercado) y
**2.2** (competidores), o un **paquete de documentos externos** (onboarding de otra
agencia, brief, web) que el agente normaliza. Si falta una fuente, el agente lo declara y
trabaja con lo disponible marcando los supuestos.

## Cómo trabaja (paso a paso)

1. **Paso 0 — Nivel de investigación (te pregunta siempre):**
   - **Nivel 1:** sin herramientas de pago. Solo Claude + búsqueda web + Claude in Chrome.
     Coste cero. Los datos duros (demografía, volúmenes, lenguaje literal) se aproximan o se
     marcan «requiere herramienta (Nivel 2+)».
   - **Nivel 2:** con herramientas (DataForSEO, Semrush, GEO Metrics, SimilarWeb,
     Gong/Fireflies, HubSpot). **Te da una estimación de coste antes de ejecutar** y espera
     tu OK antes de cualquier tirada grande (DataForSEO y Semrush consumen créditos).
2. **Paso 0.b — Contexto:** recoge `slug_cliente`, el contexto (CKB / 2.1-2.2 / paquete
   externo) y tu foco comercial y restricciones.
3. **Fase 1 — Dimensionar (checkpoint):** propone **cuántos perfiles** hacen falta y la
   **persona negativa**, con justificación. **Para y espera tu validación** antes de
   construir nada.
4. **Fase 2 — Construir:** por cada perfil validado, completa las cuatro capas (ICP +
   Buyer Persona + JTBD + capa GEO/SEO con la firma de prompt). Ancla cada dato en su
   fuente; lo que no puede anclar, lo marca como hipótesis.
5. **Fase 3 — Accionar:** genera el mapa de priorización, la matriz persona×etapa×intención,
   el filtro anti-persona y las conclusiones con su agente destino.

## Qué outputs genera

Todo bajo `clientes/[slug-cliente]/icp/`:

| Archivo | Qué es |
|---------|--------|
| `propuesta_perfiles.md` | Dimensionado de la Fase 1: nº de perfiles + persona negativa, **para validar antes de construir**. |
| `icp_perfiles.md` | Documento principal: los N perfiles con las cuatro capas (ICP + Persona + JTBD + GEO/SEO). |
| `outputs_accionables.md` | La capa puente: mapa de priorización, **matriz persona×etapa×intención**, filtro anti-persona y conclusiones por agente destino. |
| `icp_estructurado.json` | ICP en JSON para consumo automático de Estrategia y Contenido (recomendado en Nivel 2). |
| `resumen_ejecutivo.pdf` | Resumen presentable de 2–4 páginas para el cliente (o `.md` si el entorno no genera PDF). |
| `_fuentes/` | Contexto normalizado, voz de cliente, demografía y observación de motores. |
| `audit/` | Nivel elegido, herramientas, estimación y gasto real, y la validación de la Fase 1. |

## Quién consume su salida (downstream)

- **Estrategia (Capa 2):** perfil primario y orden de prioridad; filtro anti-persona;
  canales por persona.
- **Contenido (Capa 3):** matriz persona×etapa×intención; lenguaje real; objeciones a
  resolver.
- **Prompts GEO:** las firmas de prompt por persona.
- **Medición (Capa 4):** si se atrae al público correcto, no solo tráfico.

## Lo que NO hace

No hace el retrato de mercado (eso es el 2.1), no disecciona competidores concretos (el
2.2), ni fija la estrategia o el plan de contenidos (Capas 2 y 3). Si se le pide, lo
deriva.

## Buenas prácticas

- En **Nivel 1**, buena parte del valor queda como **hipótesis a validar** (sobre todo
  objeciones y lenguaje real). Para subir la calidad, lo que más aporta es **voz de cliente
  real** (reseñas, RFPs, o transcripciones de Gong/Fireflies en Nivel 2), más que las
  keywords.
- Es un artefacto con **ciclo de vida propio**: revísalo trimestralmente (ligero) y haz un
  refresco profundo anual o cuando el 2.1/2.2 detecten cambios de mercado.
- Valida siempre la Fase 1 con criterio de negocio: el agente propone, tú decides.
