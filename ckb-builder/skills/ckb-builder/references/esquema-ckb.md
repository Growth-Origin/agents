# Esquema del Client Knowledge Base (CKB) — versión consolidada 0.1

> Pieza central del Agente 1.1 (CKB Builder). Es el knowledge base persistente
> del cliente, con esquema **estable**: cinco módulos consolidados más un
> índice maestro. Las secciones no cambian de cliente a cliente; cambia el
> contenido. Está pensado para crecer modularmente: cuando un módulo
> polifacético resulte costoso de mantener, se parte en submódulos atómicos
> según el documento de referencia del agente, sin romper a los consumidores
> downstream.
>
> Nombre de archivo al rellenar cada módulo: `[NN]_[nombre].md` dentro de la
> carpeta `ckb/` del cliente.

## Idioma del CKB

Todo el contenido del CKB se redacta en **español de España (peninsular)**.
Tú (singular) y vosotros (plural). Conjugaciones verbales: tienes, queréis,
podéis, dime, mira, fíjate. **Prohibido cualquier argentinismo**: ni vos,
tenés, querés, podés, decime, mirá, fijate (sin tilde), dale (como "ok"),
armá, pegá, andá, ahí como muletilla, bárbaro, re- como intensificador, qué
onda, laburo, guita.

Ejemplos de equivalencia para no confundirse:

| No usar (argentinismo) | Usar (peninsular) |
|------------------------|-------------------|
| decime                 | dime              |
| mirá                   | mira              |
| fijate                 | fíjate            |
| dale (como "ok")       | vale              |
| armá un dossier        | monta un dossier  |
| tenés / querés / podés | tienes / quieres / puedes |
| vos                    | tú                |
| ahí como muletilla     | (eliminar)        |
| re-importante          | muy importante    |

## Convención de trazabilidad (no negociable)

Toda afirmación factual lleva una etiqueta compacta al final de la línea o
del bloque:

`‹fuente: [tipo+ref] | acceso: AAAA-MM-DD | confianza: alta/media-alta/media/baja | tipo: hecho/interpretación/hipótesis›`

- **tipo+ref**: una de estas formas:
  - `entrevista: [rol] [mm:ss]` — p. ej. `entrevista: CEO 32:14`
  - `doc: [nombre] p.[página]` — p. ej. `doc: deck-ventas-2026 p.7`
  - `web: [URL]`
  - `linkedin: [URL del post]`
  - `aparición: [tipo, nombre, fecha]` — podcasts, conferencias, prensa.
  - `memoria-agente-1: [sección]` — cuando la fuente viene del archivo de
    memoria del Pre-Onboarding.
- **confianza**: alta (varias fuentes coincidentes); media-alta (una fuente
  oficial fiable); media (interpretación bien apoyada por evidencia parcial);
  baja (inferencia con poca evidencia, conviene marcar como hipótesis).
- **tipo**: hecho (verificable en la fuente citada); interpretación (lectura
  del agente sobre hechos); hipótesis (a confirmar en el workshop con el
  cliente o en futuras interacciones).

Lo no verificable **no se afirma**: pasa a la sección de **Hipótesis
abiertas** del módulo correspondiente y alimenta el guion del workshop.

## Estructura interna estándar de cada módulo

Todos los módulos siguen la misma plantilla. Esto permite que los agentes
downstream sepan dónde buscar lo que necesitan sin leer el módulo completo.

Bloque YAML inicial con la metadata:

```yaml
---
modulo_id: "1"
modulo_nombre: "Identidad y negocio"
version: "1.0"
fecha_actualizacion: "AAAA-MM-DD"
autor: "Agente 1.1 CKB Builder v0.1"
confianza_global: "alta | media-alta | media | baja"
estado: "borrador | en-revisión | validado"
fuentes_principales: ["memoria-agente-1", "entrevistas", "web", "docs"]
tokens_estimados: 1800
---
```

A continuación, cinco secciones fijas en este orden:

1. **Síntesis** (200–400 tokens). Los 3–5 puntos esenciales del módulo. Es
   lo que carga un agente downstream que solo necesita referencia ligera.
2. **Detalle**. Contenido completo, organizado en los subapartados
   consistentes del módulo (los listamos abajo, módulo a módulo).
3. **Evidencia**. Fuentes concretas que sostienen las afirmaciones (qué
   entrevista con timestamp, qué documento con página, qué URL, qué post
   de LinkedIn), con citas literales cuando sean reveladoras.
4. **Hipótesis abiertas**. Cosas no validadas al 100% que conviene
   confirmar en el workshop con el cliente.
5. **Notas para agentes downstream**. Avisos concretos para los agentes
   que consuman este módulo. Ejemplo: "Para el Agente 1.2 (ICP): valida
   X, Y y Z antes de cerrar el ICP".

## Los cinco módulos consolidados (versión 0.1)

### Módulo 0 — Índice maestro

Único documento que TODOS los agentes downstream cargan siempre. Ligero
(400–800 tokens). Estructura:

```markdown
# Client Knowledge Base — [Nombre Cliente]

**Versión CKB:** 0.1
**Fecha última actualización:** AAAA-MM-DD
**Estado global:** borrador | en-revisión | validado (workshop AAAA-MM-DD)

## Síntesis ejecutiva (1 párrafo)
Quién es este cliente, qué hace, en qué fase está, qué relación tenemos.

## Tesis estratégica central (2–3 frases)
La hipótesis estratégica que define la relación con el cliente.

## Módulos disponibles

| ID | Módulo                                  | Versión | Última actualización | Confianza | Tokens |
|----|-----------------------------------------|---------|----------------------|-----------|--------|
| 1  | Identidad y negocio                     | ...     | ...                  | ...       | ...    |
| 2  | Propuesta de valor y diferenciales      | ...     | ...                  | ...       | ...    |
| 3  | Voz, tono y lenguaje                    | ...     | ...                  | ...       | ...    |
| 4  | Objeciones, fricciones y restricciones  | ...     | ...                  | ...       | ...    |
| 5  | Activos, expertise y voceros            | ...     | ...                  | ...       | ...    |

**Total CKB:** ~N tokens
**Carga típica por tarea downstream:** 3.000–6.000 tokens

## Fuentes principales
- Memoria del Pre-Onboarding (AAAA-MM-DD).
- Transcripciones de entrevistas: N (con duraciones).
- Documentación entregada por el cliente: N documentos.
- Web del cliente: N páginas procesadas (sitemap + WebFetch + Chrome).
- LinkedIn corporativo: N posts procesados.
- LinkedIn voceros: N posts procesados.

## Voceros identificados

| Nombre | Rol | Plataforma | Frecuencia | Prioridad |
|--------|-----|------------|------------|-----------|

## Changelog reciente
- v0.1 (AAAA-MM-DD): versión inicial tras onboarding.
```

### Módulo 1 — Identidad y negocio

Consolida del documento de referencia del agente los módulos 01 (negocio),
02 (evidencia ICP) y 04 (objetivos).

**Subapartados del Detalle:**

- 1.1 Identidad del cliente — nombre legal, comercial, URL, HQ, mercados,
  idiomas, sector/categoría declarada, descripción neutra en una frase.
- 1.2 Modelo de negocio — qué vende, a quién, cómo monetiza, ciclo de
  venta aproximado, tamaño operativo aparente (no es due diligence
  financiera; es contexto operativo).
- 1.3 Evidencia bruta sobre el ICP — datos verificables sobre clientes
  reales: sectores donde vende hoy, tamaños típicos, roles compradores,
  geografías. **PROHIBICIÓN ESTRICTA:** este apartado recoge evidencia.
  NO define el ICP, NO produce un archivo de ICP, NO crea una carpeta
  `icp/`, NO genera una tabla de «los N ICPs del cliente». La definición
  y la nomenclatura del ICP son trabajo exclusivo del Agente 1.2 (ICP
  Definition). Lo que recoges aquí es el input que el Agente 1.2 leerá.
- 1.4 Objetivos declarados y métricas — qué objetivos de negocio comunica
  el cliente y qué métricas dice mirar (crecimiento, retención,
  expansión geográfica, etc.).
- 1.5 Contexto del momento — fase actual del cliente (early, growth,
  scale), eventos relevantes recientes (rondas, lanzamientos, fichajes),
  motivo de contactarnos (heredado de la memoria del Agente 1).

### Módulo 2 — Propuesta de valor y diferenciales

Consolida 03 (propuesta de valor) más la parte cruzada de 07 que comparaba
versión oficial con percepción real del mercado.

**Subapartados del Detalle:**

- 2.1 Propuesta de valor oficial — cómo se describe el cliente a sí mismo,
  con citas literales y fuente.
- 2.2 Diferenciales declarados — los 2–5 diferenciales que el cliente
  destaca, con citas y fuente.
- 2.3 Percepción real del mercado — qué dicen reseñas, prensa, comentarios
  públicos. Lenguaje real vs. jerga oficial. Elogios y críticas
  recurrentes.
- 2.4 Diferenciales no explotados detectados — cosas que el mercado valora
  en el cliente y la comunicación oficial no destaca, o cosas que el
  founder defiende en su LinkedIn y no aparecen en la web.
- 2.5 Incongruencias entre versión oficial y realidad — contradicciones
  directas con evidencia en ambos lados, y pregunta de aclaración para el
  workshop.

### Módulo 3 — Voz, tono y lenguaje

Consolida 05 (tono) y 06 (lenguaje).

**Subapartados del Detalle:**

- 3.1 Tono y registro — formal / cercano / técnico / provocador, con
  ejemplos.
- 3.2 Narrativa — cómo cuenta su historia (origen, misión, "por qué") y
  arcos narrativos recurrentes.
- 3.3 Vocabulario propio — términos y claims que el cliente repite y son
  parte de su identidad lingüística.
- 3.4 Glosario operativo — lista de términos a **usar** (los del cliente)
  y términos a **evitar** (jergas que el mercado no usa, palabras
  prohibidas por la marca).
- 3.5 Ejemplos canónicos — 5–10 frases on-brand (a imitar) y 5–10 frases
  off-brand (a no imitar), extraídas de fuentes reales con cita.

### Módulo 4 — Objeciones, fricciones y restricciones

Consolida 07 (objeciones) y 10 (restricciones y sensibilidades).

**Subapartados del Detalle:**

- 4.1 Objeciones de leads y clientes potenciales — qué frena la compra,
  con evidencia de ventas / customer success o de reseñas.
- 4.2 Fricciones operativas o de producto — quejas o fricciones reales
  detectadas en reseñas, soporte público o entrevistas.
- 4.3 Restricciones de comunicación — temas que el cliente NO quiere
  tocar, competidores con quienes no quiere compararse explícitamente,
  datos confidenciales que no pueden publicarse.
- 4.4 Sensibilidades sectoriales y regulatorias — específicas del sector
  (médico, financiero, infantil, etc.) o de mercados concretos.
- 4.5 Riesgos para la relación cliente-agencia — discrepancias entre el
  discurso del founder y el equipo, expectativas irreales, dependencias
  operativas (timing, recursos del cliente para revisar contenido, etc.).

### Módulo 5 — Activos, expertise y voceros

Consolida 08 (activos citables) y 09 (expertise demostrable). Es la parte
estratégicamente más valiosa para producir contenido GEO y E-E-A-T.

**Subapartados del Detalle:**

- 5.1 Datos publicables propios — estudios, métricas internas, benchmarks
  que el cliente puede publicar (ya publicados o disponibles para
  publicar tras revisión).
- 5.2 Casos de cliente con métricas — publicados o internos; con cliente
  representado, problema resuelto, métricas, permiso de publicación.
- 5.3 Premios, certificaciones, partnerships, prensa destacada.
- 5.4 Voceros identificados — personas dentro del cliente con presencia
  pública relevante (founders, C-suite, expertos internos). Tabla
  resumen: nombre, rol, plataformas activas, frecuencia, engagement
  aparente, prioridad.
- 5.5 Detalle por vocero — para cada uno: temas dominantes, posturas
  defendidas públicamente, apariciones externas (podcasts, conferencias,
  prensa), gap personal vs. corporate (lo que defiende en su perfil
  personal y no aparece en la comunicación oficial — oro para futuros
  contenidos firmados por la persona).

## Cómo se promueve la memoria del Agente 1 al CKB

El Agente 1 (Pre-Onboarding) deja un archivo `memoria_[cliente].md` con
14 secciones. El CKB Builder NO parte de cero: lo toma como input y lo
expande con las entrevistas y la documentación entregada. Mapeo
aproximado:

| Memoria del Agente 1                  | Módulo del CKB                                  |
|---------------------------------------|-------------------------------------------------|
| §1 Identidad                          | Módulo 1 (1.1, 1.5)                             |
| §2 Personas clave                     | Módulo 5 (5.4, 5.5)                             |
| §3 Posicionamiento / propuesta oficial| Módulo 2 (2.1, 2.2); §3.2 → Módulo 1 (1.3)      |
| §4 Marca y mensaje                    | Módulo 3 (3.1, 3.2, 3.3)                        |
| §5 Canales y presencia digital        | Módulo 5 (5.4); Módulo 3 (3.4); input futuro 1.4|
| §6 Voz real del mercado               | Módulo 2 (2.3); Módulo 4 (4.1, 4.2)             |
| §7 Footprint del equipo               | Módulo 5 (5.4, 5.5)                             |
| §8 Nicho y competidores               | Módulo 1 (1.5) + input futuro 1.3               |
| §9 Hipótesis a validar                | Hipótesis abiertas en cada módulo               |
| §10 Incongruencias                    | Módulo 2 (2.5)                                  |
| §11 Diferenciales no explotados       | Módulo 2 (2.4)                                  |
| §12 Riesgos                           | Módulo 4 (4.5)                                  |
| §13 Huecos de información             | Material directo para el guion del workshop     |
| §14 Log                               | Changelog del CKB                               |

Cuando exista una memoria del Agente 1, el CKB Builder la trata como
**versión 0** del CKB y la enriquece con el resto del material. Cuando no
exista (cliente que llega sin haber pasado por el Pre-Onboarding), el
agente recoge ese material internamente como paso previo.

## Reglas de uso por agentes downstream

- El módulo 0 (índice maestro) se carga siempre: es la portada.
- Para tareas concretas, cargar solo los módulos relevantes (típicamente
  2–3). Ejemplos:
  - Redacción de blog post BOFU sobre una objeción → módulos 3, 4 y 5.
  - Definición del ICP (futuro Agente 1.2) → módulos 1, 2 y 4 (en
    particular 4.1).
  - Estrategia editorial → módulos 2, 3 y 5.
- Si un agente downstream necesita más, mejor cargar el módulo entero que
  intentar reconstruirlo desde fragmentos.

## Camino a la versión completa de 12 módulos

Cuando un módulo consolidado se vuelva costoso de mantener (mucho
contenido heterogéneo, mucho movimiento en una sola sección,
descoordinación entre subapartados), se parte en los submódulos atómicos
del documento de referencia, manteniendo numeración compatible:

- Módulo 1 → 01 Negocio, 02 Evidencia ICP, 04 Objetivos.
- Módulo 2 → 03 Propuesta de valor (la parte de percepción real puede
  pasar a 07 si se separa de objeciones).
- Módulo 3 → 05 Tono, 06 Lenguaje.
- Módulo 4 → 07 Objeciones, 10 Restricciones.
- Módulo 5 → 08 Activos, 09 Expertise.

El paso no rompe nada: los agentes downstream consumen vía índice
maestro, que se reescribe con los IDs nuevos. Las referencias internas se
actualizan en un único cambio coordinado.

## Bloque de control de la carpeta del CKB

Junto a los módulos vive una carpeta `_meta/` con:

- `versiones.json` — registro de versiones del CKB y de cada módulo.
- `changelog.md` — bitácora legible de cambios.
- `permisos.json` — qué se puede procesar, retenciones, base legal
  aplicada.
- `voceros_identificados.json` — registro estructurado de voceros con su
  estado (confirmado por humano, prioridad, fuentes).

Y una carpeta `_fuentes/` con el material crudo procesado:

- `memoria_agente_1.md` (copia del input).
- `transcripciones/` (las N que haya, una por entrevista).
- `documentacion_cliente/` (PDFs, decks, manuales).
- `web/` (resumen del crawl + páginas estratégicas en markdown).
- `linkedin_corporate/` y `linkedin_voceros/`.
- `apariciones_externas/`.

## Estructura completa de la carpeta del cliente

```
clientes/[slug-cliente]/
├── ckb/
│   ├── 00_indice_maestro.md
│   ├── 01_identidad_negocio.md
│   ├── 02_propuesta_valor_diferenciales.md
│   ├── 03_voz_tono_lenguaje.md
│   ├── 04_objeciones_fricciones_restricciones.md
│   ├── 05_activos_expertise_voceros.md
│   ├── _meta/
│   │   ├── versiones.json
│   │   ├── changelog.md
│   │   ├── permisos.json
│   │   └── voceros_identificados.json
│   └── _fuentes/
│       ├── memoria_agente_1.md
│       ├── transcripciones/
│       ├── documentacion_cliente/
│       ├── web/
│       ├── linkedin_corporate/
│       ├── linkedin_voceros/
│       └─