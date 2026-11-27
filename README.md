# Growth Origin — Marketplace de agentes

Marketplace de plugins de Growth Origin para Claude Code / Cowork.
Contiene los agentes del ecosistema de onboarding y construcción del
conocimiento del cliente.

## Plugins incluidos

- **pre-onboarding-cliente** (v0.4.0) — Agente 1.0: prepara la primera
  reunión de onboarding de un cliente nuevo con investigación de
  marketing 360 y cuatro entregables (memoria, guion de entrevista,
  resumen ejecutivo y pedido de documentación).
- **ckb-builder** (v0.3.0) — Agente 1.1: construye el Client Knowledge
  Base consolidado del cliente tras el onboarding: cinco módulos
  consolidados, índice maestro y guion del workshop de validación.
- **market-intelligence** (v0.4.1) — Agente 2.1: retrato accionable del
  mercado del cliente para SEO y GEO en ocho bloques (con selector de
  nivel de investigación), más conclusiones accionables y resumen
  ejecutivo en PDF.
- **competitive-intelligence** (v0.4.1) — Agente 2.2: ingeniería inversa
  de los competidores que mejor posicionan, diseccionados en once temas
  (formato insight→implicación→acción), con síntesis accionable y
  resumen ejecutivo en PDF.
- **icp-definer** (v0.1.1) — Agente 3: define el Cliente Ideal accionable
  (ICP + buyer persona + JTBD + capa GEO/SEO con firma de prompt) más la
  persona negativa, la matriz persona×etapa×intención y el filtro
  anti-persona. Humano-en-el-bucle, con selector de nivel de
  investigación y estimación de coste en Nivel 2.
- **strategic-keywords-prompts** (v0.1.0) — Agente 4: primer agente de la
  Capa de Estrategia. Cruza el conocimiento de la Capa 1 con datos de
  búsqueda (DataForSEO) y de IA (GEO Metrics) y entrega un universo
  priorizado de keywords y prompts (scoring KPS/PPS, filtro anti-persona,
  fusión topic-led y esbozo de priorización) en un Excel de 4 pestañas.
  Selector de nivel de investigación con estimación de coste en Nivel 2.
- **site-architect** (v0.1.0) — Agente 5 (3.2 en la spec): convierte el
  universo priorizado del Agente 4 en la arquitectura definitiva del sitio
  (mapa de URLs con acción por URL, plan de landings, clusters de blog,
  matriz prompt→URL, interlinking SEO+GEO y roadmap por olas con TPS), con
  anti-canibalización por solapamiento de SERP y checkpoint humano
  obligatorio. Selector de nivel con estimación de coste.

Próximos agentes del ecosistema (por construir): briefs y producción de
contenido (Capa 3) y medición (Capa 4).

Idioma de salida de todos los agentes: **español de España**
(peninsular). Sin argentinismos.

---

## Publicar este marketplace (lo hace quien mantiene los plugins)

1. Crear un repositorio en GitHub bajo la cuenta de Growth Origin (por
   ejemplo `Growth-Origin/agents`).
2. Subir el contenido de esta carpeta tal cual (en la raíz del repo
   deben quedar `.claude-plugin/marketplace.json` y las dos carpetas de
   plugins).

   ```bash
   cd "growth-origin-agents"
   git init
   git add .
   git commit -m "Marketplace Growth Origin — los seis agentes"
   git branch -M main
   git remote add origin https://github.com/Growth-Origin/agents.git
   git push -u origin main
   ```

3. Listo. Si el repo es público, el equipo lo instala sin invitaciones.
   Si es privado, cada persona del equipo necesita acceso al repo.

---

## Instalar los plugins (lo hace cada persona del equipo, una vez)

### En Cowork (la app de escritorio)

`Ajustes → Plugins → Add plugin` y pegar `Growth-Origin/agents`. Después
instalar los plugins que se necesiten (`pre-onboarding-cliente`,
`ckb-builder`, `market-intelligence`, `competitive-intelligence`,
`icp-definer`, `strategic-keywords-prompts`, `site-architect`) por separado
desde el mismo panel.

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
```

---

## Recibir actualizaciones

Cada persona corre la actualización cuando quiera:

```
/plugin update pre-onboarding-cliente
/plugin update ckb-builder
/plugin update market-intelligence
/plugin update competitive-intelligence
/plugin update icp-definer
/plugin update strategic-keywords-prompts
/plugin update site-architect
```

La actualización es manual por defecto: no se cambia nada en la máquina
de nadie sin que lo pida.

---

## Publicar una versión nueva (mantenimiento)

1. Editar los archivos del plugin afectado dentro de su carpeta
   (`pre-onboarding-cliente/`, `ckb-builder/`, `market-intelligence/`,
   `competitive-intelligence/`, `icp-definer/`,
   `strategic-keywords-prompts/` o `site-architect/`).
2. Subir el número de versión en su `.claude-plugin/plugin.json`
   (por ejemplo `0.3.0` → `0.4.0`).
3. Commit y push al repo.
4. Avisar al equipo para que corra `/plugin update [nombre]`.

Cada plugin tiene su versión propia y su ciclo independiente, aunque
viven en el mismo marketplace.

---

## Estructura del repo

```
growth-origin-agents/
├── .claude-plugin/
│   └── marketplace.json        # define el marketplace y lista los plugins
├── pre-onboarding-cliente/     # plugin 1 (Agente 1.0)
│   ├── .claude-plugin/plugin.json
│   ├── README.md
│   └── skills/pre-onboarding-cliente/
├── ckb-builder/                # plugin 2 (Agente 1.1)
│   ├── .claude-plugin/plugin.json
│   ├── README.md
│   └── skills/ckb-builder/
├── market-intelligence/        # plugin 3 (Agente 2.1)
│   ├── .claude-plugin/plugin.json
│   ├── README.md
│   └── skills/market-intelligence/
├── competitive-intelligence/   # plugin 4 (Agente 2.2)
│   ├── .claude-plugin/plugin.json
│   ├── README.md
│   └── skills/competitive-intelligence/
├── icp-definer/                # plugin 5 (Agente 3)
│   ├── .claude-plugin/plugin.json
│   ├── README.md
│   └── skills/icp-definer/
├── strategic-keywords-prompts/ # plugin 6 (Agente 4)
│   ├── .claude-plugin/plugin.json
│   ├── README.md
│   └── skills/strategic-keywords-prompts/
└── site-architect/             # plugin 7 (Agente 5 · 3.2 en la spec)
    ├── .claude-plugin/plugin.json
    ├── README.md
    └── skills/site-architect/
```
