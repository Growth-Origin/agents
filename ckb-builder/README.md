# CKB Builder — Agente 1.1

Construye el **Client Knowledge Base (CKB)** consolidado de un cliente nuevo tras el
onboarding: transforma la memoria del Pre-Onboarding, las transcripciones de las
entrevistas y la documentación del cliente en un activo estructurado, trazable y
mantenible que usan todos los agentes downstream. Idioma de salida: **español de
España**.

## Cómo se invoca

- «agente 1.1» / «ckb-builder»
- «construye el CKB de [cliente]»
- «destila el material del onboarding» / «promueve la memoria a CKB»
- «añade esta transcripción al CKB»

**Antes de invocarlo**, ten a mano: la memoria del Pre-Onboarding
(`clientes/[slug]/memoria_[slug].md`), las transcripciones de las entrevistas
(`.txt`, `.vtt`, `.docx` o `.md`) y, si existe, la documentación entregada por el
cliente. Mínimo para arrancar: slug + memoria (o acuerdo de recogerla) + un vocero
conocido.

## Cómo trabaja (paso a paso)

1. **Paso 0 — Toma de datos:** formulario fijo (slug, memoria, transcripciones,
   voceros, documentación opcional).
2. **Paso 1 — Recolección:** promueve la memoria a versión 0 del CKB, procesa
   transcripciones y documentación, recoge la web (sitemap + WebFetch) y LinkedIn
   (con **checkpoint de identidad de voceros**: te pide confirmar identidades antes
   de profundizar).
3. **Paso 2 — Síntesis:** redacta los cinco módulos consolidados + el índice
   maestro, con trazabilidad en cada afirmación.
4. **Paso 3 — Workshop:** genera el guion del workshop de validación y la tabla de
   decisiones pendientes **en blanco** (la sesión la conduce un humano; el agente
   no simula respuestas ni promociona el estado del CKB).

## Qué outputs genera

Todo bajo `clientes/[slug-cliente]/ckb/`:

| Archivo | Qué es |
|---------|--------|
| `00_indice_maestro.md` | Portada que todos los agentes downstream cargan siempre. |
| `01…05_*.md` | Los cinco módulos: Identidad y negocio; Propuesta de valor; Voz, tono y lenguaje; Objeciones y restricciones; Activos, expertise y voceros. |
| `_meta/` | Versiones, changelog, permisos, voceros. |
| `_fuentes/` | Material crudo procesado (memoria, transcripciones, docs, web, LinkedIn). |
| `workshop_validacion/` | Guion del workshop + decisiones pendientes en blanco. |
| `audit/` | Registro de ejecución y fuentes accedidas. |

## Quién consume su salida (downstream)

- **Market Intelligence (2.1) y Competitive Intelligence (2.2):** contexto del
  cliente (sector, oferta, voceros, voz de mercado).
- **ICP Definer (Agente 3):** la evidencia bruta sobre el ICP del Módulo 1.3.
- **Strategic Keywords & Prompts (Agente 4) y Contenido:** propuesta de valor,
  vocabulario, restricciones, activos y voceros.

## Lo que NO hace

No define el ICP (eso es el Agente 3), no analiza mercado ni competidores (2.1 y
2.2), no hace keyword research (Agente 4) y no simula el workshop: produce las
herramientas y el consultor conduce la sesión real.

## Buenas prácticas

- El CKB es un activo vivo: cada pieza nueva relevante (estudio, lanzamiento,
  cambio de mensaje) actualiza el módulo afectado.
- La promoción de estado (`borrador` → `en-revisión` → `validado`) la decide el
  consultor; `validado` solo tras el workshop real con el cliente.
- Para voceros de alta prioridad, la exportación voluntaria de LinkedIn
  (Settings → Get a copy of your data) da cobertura completa y compliance perfecto.
