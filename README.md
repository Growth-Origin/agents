# Growth Origin: marketplace de agentes

Marketplace de plugins de Growth Origin para **Claude Code** y **Cowork**. Reúne
los agentes que usamos para **analizar a un cliente**, desde la primera reunión
hasta la arquitectura de su web, más tres herramientas complementarias.

Idioma de salida de todos los agentes: **español de España** (peninsular), sin
argentinismos.

---

## Mapa rápido

```
 CAPA 1 · CONOCER AL CLIENTE                CAPA 2 · ESTRATEGIA          PRODUCCIÓN
 ┌──────────────┐   ┌──────────┐   ┌───────────────┐   ┌──────────┐   ┌──────────────┐   ┌──────────────┐
 │ 1.0 Pre-     │ → │ 1.1 CKB  │ → │ 2.1 Mercado   │ → │ 3 ICP    │ → │ 4 Keywords y │ → │ 5 Arquitecto │
 │ onboarding   │   │ Builder  │   │ 2.2 Competen. │   │ Definer  │   │   prompts    │   │   de sitio   │
 └──────────────┘   └──────────┘   └───────────────┘   └──────────┘   └──────────────┘   └──────────────┘

 HERRAMIENTAS COMPLEMENTARIAS (se usan cuando hacen falta)
 · Prospector de links locales  · Jev Keywords (evalúa el Excel del Agente 4)  · ChatGPT Ads Strategist
```

Cada agente **lee lo que dejó el anterior**, pero ninguno depende de él en duro:
si falta un paso, trabaja con lo que haya (o con documentos externos) y te
pregunta lo crítico.

| # | Plugin | En una línea | Versión |
|---|---|---|---|
| 1.0 | `pre-onboarding-cliente` | Prepara la primera reunión con un cliente nuevo | 0.4.0 |
| 1.1 | `ckb-builder` | Convierte el onboarding en la base de conocimiento del cliente | 0.3.0 |
| 2.1 | `market-intelligence` | Retrato del mercado del cliente para SEO y GEO | 0.4.1 |
| 2.2 | `competitive-intelligence` | Ingeniería inversa de los competidores que mejor posicionan | 0.4.1 |
| 3 | `icp-definer` | Define el cliente ideal y la persona a excluir | 0.1.1 |
| 4 | `strategic-keywords-prompts` | Universo priorizado de keywords y prompts de IA | 0.1.0 |
| 5 | `site-architect` | Arquitectura definitiva del sitio y roadmap | 0.1.0 |
| — | `local-link-prospector` | Directorios, citaciones y links locales gratuitos | 0.1.0 |
| — | `jev-keywords` | Puntúa con Jev la calidad de un Excel de keywords | 0.1.0 |
| — | `chatgpt-ads-strategist` | Estrategia y optimización de campañas en ChatGPT Ads | 0.1.0 |

---

## Qué hace cada plugin

### 1.0 · Pre-onboarding (`pre-onboarding-cliente`)

- **Para qué:** llegar preparado a la primera reunión con un cliente nuevo.
  Investiga fuentes públicas con mirada de marketing 360.
- **Cuándo:** antes de la reunión de onboarding. Frases: «pre-onboarding»,
  «prepara este cliente», «armame el onboarding de [cliente]».
- **Necesita:** la URL del cliente y a quién vas a entrevistar.
- **Entrega:** 4 archivos en `clientes/[slug]/`: **memoria del cliente**, **guion
  de entrevista** modular, **resumen ejecutivo** de una hoja y **email de pedido
  de documentación y accesos**.
- **Siguiente:** CKB Builder.

### 1.1 · CKB Builder (`ckb-builder`)

- **Para qué:** destilar todo el material del onboarding en el **Client
  Knowledge Base** (CKB), la fuente de verdad del cliente para todos los
  agentes siguientes.
- **Cuándo:** después de las entrevistas. Frases: «agente 1.1», «construye el
  CKB de [cliente]», «añade esta transcripción al CKB».
- **Necesita:** la memoria del Pre-onboarding, las transcripciones de las
  entrevistas y, si existe, la documentación del cliente.
- **Entrega:** **5 módulos** (Identidad y negocio · Propuesta de valor ·
  Voz y tono · Objeciones y restricciones · Activos y voceros), un **índice
  maestro** y el **guion del workshop de validación** con el cliente.
- **Siguiente:** Mercado (2.1).

### 2.1 · Market Intelligence (`market-intelligence`)

- **Para qué:** entender el mercado del cliente con foco en SEO y GEO.
- **Cuándo:** con el CKB listo. Frases: «agente 2.1», «analiza el mercado de
  [cliente]».
- **Necesita:** el CKB, un análisis previo o un paquete de documentos externos.
- **Entrega:** un documento en 8 bloques (top-5 competidores, E-E-A-T, top-50
  preguntas, vocabulario, plataformas y posición del cliente con benchmark), las
  conclusiones y un **resumen ejecutivo en PDF**.
- **Requisitos:** te pregunta el nivel. **Nivel 1** sin herramientas; **Nivel
  2** con DataForSEO, Semrush o GEO Metrics, **con estimación de coste**.
- **Siguiente:** Competencia (2.2).

### 2.2 · Competitive Intelligence (`competitive-intelligence`)

- **Para qué:** hacer ingeniería inversa de los competidores que mejor
  posicionan y sacar palancas accionables.
- **Cuándo:** después del 2.1 (que nomina el top-5). Frases: «agente 2.2»,
  «analiza los competidores de [cliente]», «battlecard SEO/GEO».
- **Necesita:** el CKB y, recomendado, la salida del 2.1.
- **Entrega:** cada competidor diseccionado en **11 temas** (búsqueda,
  generativo, qué opinan las IAs, backlinks, arquitectura, interlinking,
  E-E-A-T, hacks de utilidad, personalidad, CMS/UX) en formato
  **insight → implicación → acción**, una síntesis por agente destino y un
  resumen en PDF.
- **Requisitos:** igual que el 2.1, en dos niveles y con estimación de coste.
- **Siguiente:** ICP (3).

### 3 · ICP Definer (`icp-definer`)

- **Para qué:** definir **a quién le habla** el cliente, en formato accionable
  para SEO y GEO.
- **Cuándo:** con la Capa 1 hecha. Frases: «agente 3», «define el ICP de
  [cliente]», «buyer persona».
- **Necesita:** el CKB y las salidas del 2.1 y el 2.2 (con cualquiera alcanza).
- **Entrega:** el **ICP + buyer persona + JTBD + capa GEO/SEO** (con la firma de
  prompt), la **persona negativa**, la **matriz persona × etapa × intención**, el
  **filtro anti-persona** y un resumen en PDF. Humano en el bucle: valida contigo.
- **Requisitos:** dos niveles. El Nivel 2 consume créditos (DataForSEO,
  Semrush, GEO Metrics y SimilarWeb).
- **Siguiente:** Keywords y prompts (4).

### 4 · Keywords y prompts estratégicos (`strategic-keywords-prompts`)

- **Para qué:** decidir **por qué búsquedas y por qué preguntas a la IA**
  vale la pena competir.
- **Cuándo:** con el ICP definido. Frases: «agente 4», «prioriza keywords»,
  «keywords y prompts estratégicos».
- **Necesita:** CKB, ICP, Mercado y Competidores (cuanto más, mejor calibrado).
- **Entrega:** un **Excel de 4 pestañas** con el universo priorizado. Incluye
  scoring transparente (**KPS** para keywords y **PPS** para prompts), el filtro
  anti-persona como exclusión dura, una fusión por tema (doble victoria /
  SEO-led / GEO-led / latente) y un esbozo de priorización. Te pregunta la
  profundidad: Top 20, 50 o 100.
- **Requisitos:** **Nivel 2** con DataForSEO y GEO Metrics, con estimación de
  coste.
- **Siguiente:** Arquitecto de sitio (5). Opcional: pasar el Excel por **Jev
  Keywords**.

### 5 · Arquitecto de sitio (`site-architect`)

- **Para qué:** convertir la estrategia en **la web concreta**: qué URLs
  existen y qué se hace con cada una.
- **Cuándo:** con el Excel del Agente 4. Frases: «agente 5», «diseña la
  arquitectura de [cliente]», «mapa de URLs», «plan de landings».
- **Necesita:** el Excel del Agente 4 (o un research externo), el CKB, el bloque
  de arquitectura del 2.2 y, si el sitio ya existe, el export de **Search
  Console** (12–16 meses).
- **Entrega:** **mapa de URLs** con acción por URL (mantener, optimizar, crear,
  consolidar o eliminar), plan de landings, clusters de blog con vocero, matriz
  prompt → URL, reglamento de interlinking SEO+GEO y **roadmap por olas** con
  Task Priority Score. Previene canibalizaciones por solapamiento de SERP.
  **Checkpoint humano obligatorio.**
- **Requisitos:** Nivel 2 con DataForSEO On-Page + SERP, con estimación de
  coste.

### Herramienta · Prospector de links locales (`local-link-prospector`)

- **Para qué:** encontrar **dónde dar de alta gratis** a un negocio local
  (España y LATAM) para mejorar su SEO y GEO local.
- **Cuándo:** clientes con ficha de Google o con negocio local. Frases:
  «dónde doy de alta este negocio», «directorios para esta ficha», «links
  gratuitos para SEO local».
- **Necesita:** la URL de la ficha de Google Business Profile o de la web.
- **Entrega:** un mapa priorizado de citaciones NAP (que refuerzan la ficha) y
  backlinks (que refuerzan la web), verificado en vivo con la URL de alta y la
  fase de ejecución, en un **Excel checklist**.
- **Requisitos:** ninguno de pago.

### Herramienta · Jev Keywords (`jev-keywords`)

- **Para qué:** tener una **segunda opinión automática** sobre la calidad de
  un Excel de keywords.
- **Cuándo:** después del Agente 4 o con cualquier keyword research. Frases:
  «evalúa las keywords con Jev», «jev keywords».
- **Necesita:** el Excel y el contexto del cliente (mejor si es el CKB).
- **Entrega:** una copia del Excel con relevancia, intención, funnel, potencial
  GEO, prioridad, precisión y un **veredicto** (priorizar / revisar /
  descartar). Siempre hace un dry run gratis antes de gastar.
- **Requisitos:** **Python 3 + `openpyxl`** y la variable de entorno
  **`AI_GATEWAY_API_KEY`** (Vercel AI Gateway). Cada persona usa su propia
  clave.

### Herramienta · ChatGPT Ads Strategist (`chatgpt-ads-strategist`)

- **Para qué:** decidir si al cliente le conviene anunciarse en **ChatGPT
  Ads** y, si le conviene, diseñar y optimizar la campaña.
- **Cuándo:** propuestas de paid media o campañas ya en marcha. Frases:
  «anuncios en ChatGPT», «context hints», «optimiza mi campaña de ChatGPT Ads».
- **Necesita:** la web, el objetivo de conversión, el presupuesto y el CPA
  objetivo y, mejor aún, el ICP del Agente 3.
- **Entrega:** diagnóstico, Buyer Situations y Conversation Map, **context hints
  listos para copiar**, estructura de campaña, presupuesto de aprendizaje,
  tracking, KPIs y plan de 30 días, todo en un **Word con branding Growth
  Origin**. En modo optimización decide PAUSE, KEEP, ITERATE o SCALE.
- **Requisitos:** Python 3 (calculadora incluida) y la skill `docx`.

---

## Instalar (cada persona del equipo, una vez)

### En Cowork (la app de escritorio)

`Ajustes → Plugins → Add plugin`, pegar `Growth-Origin/agents` e instalar desde
ese panel los plugins que vayas a usar.

### En Claude Code (terminal)

```
/plugin marketplace add Growth-Origin/agents
/plugin install pre-onboarding-cliente@growth-origin
/plugin install ckb-builder@growth-origin
/plugin install market-intelligence@growth-origin
/plugin install competitive-intelligence@growth-origin
/plugin install icp-definer@growth-origin
/plugin install strategic-keywords-prompts@growth-origin
/plugin install site-architect@growth-origin
/plugin install local-link-prospector@growth-origin
/plugin install jev-keywords@growth-origin
/plugin install chatgpt-ads-strategist@growth-origin
```

No hace falta instalarlos todos: cada uno funciona por su cuenta.

> **Si ya tenías alguna de estas skills suelta** (en `~/.claude/skills` o
> instalada desde otro sitio), desinstala la copia vieja para que Claude no use
> dos versiones distintas.

---

## Recibir actualizaciones

```
/plugin marketplace update growth-origin
/plugin update <nombre-del-plugin>
```

La actualización es manual: no cambia nada en la máquina de nadie sin que lo
pida.

---

## Publicar una versión nueva (mantenimiento)

1. Edita los archivos del plugin dentro de su carpeta.
2. Sube la versión en su `.claude-plugin/plugin.json` (por ejemplo, `0.3.0` →
   `0.4.0`) y en la tabla de arriba.
3. Si es un plugin nuevo, regístralo en `.claude-plugin/marketplace.json`.
4. Haz commit y push, y avisa al equipo para que actualice.

> **El repo es público.** Nunca subas claves, `.env`, datos ni nombres de
> clientes reales. Las claves van siempre en variables de entorno.

---

## Estructura del repo

```
growth-origin-agents/
├── .claude-plugin/marketplace.json   # define el marketplace y lista los plugins
├── <plugin>/                         # uno por agente o herramienta
│   ├── .claude-plugin/plugin.json    # nombre, versión y descripción
│   ├── README.md                     # cómo se usa
│   └── skills/<plugin>/              # SKILL.md + references/ + scripts/
└── …
```
