# Growth Origin — Marketplace de agentes

Marketplace de plugins de Growth Origin para Claude Code / Cowork.
Contiene los agentes del ecosistema de onboarding y construcción del
conocimiento del cliente.

## Plugins incluidos

- **pre-onboarding-cliente** (v0.3.0) — prepara la primera reunión de
  onboarding de un cliente nuevo con investigación de marketing 360 y
  cuatro entregables (memoria, guion de entrevista, resumen ejecutivo
  y pedido de documentación).
- **ckb-builder** (v0.1.0) — construye el Client Knowledge Base
  consolidado del cliente tras el onboarding: cinco módulos
  consolidados, índice maestro y guion del workshop de validación.

Próximos agentes del ecosistema (por construir): 1.2 ICP Definition,
1.3 Market & Competitive Intelligence, 1.4 Search & Prompt Landscape.

Idioma de salida de todos los agentes: **español de España**
(peninsular). Sin argentinismos.

---

## Publicar este marketplace (lo hace quien mantiene los plugins)

1. Crear un repositorio en GitHub bajo la cuenta de Growth Origin (por
   ejemplo `GrowthOrigin/agents`).
2. Subir el contenido de esta carpeta tal cual (en la raíz del repo
   deben quedar `.claude-plugin/marketplace.json` y las dos carpetas de
   plugins).

   ```bash
   cd "growth-origin-agents"
   git init
   git add .
   git commit -m "Marketplace Growth Origin — pre-onboarding-cliente v0.3.0 + ckb-builder v0.1.0"
   git branch -M main
   git remote add origin https://github.com/GrowthOrigin/agents.git
   git push -u origin main
   ```

3. Listo. Si el repo es público, el equipo lo instala sin invitaciones.
   Si es privado, cada persona del equipo necesita acceso al repo.

---

## Instalar los plugins (lo hace cada persona del equipo, una vez)

### En Cowork (la app de escritorio)

`Ajustes → Plugins → Add plugin` y pegar `GrowthOrigin/agents`. Después
instalar `pre-onboarding-cliente` y `ckb-builder` por separado desde el
mismo panel.

### En Claude Code (terminal)

```
/plugin marketplace add GrowthOrigin/agents
/plugin install pre-onboarding-cliente@growth-origin
/plugin install ckb-builder@growth-origin
```

---

## Recibir actualizaciones

Cada persona corre la actualización cuando quiera:

```
/plugin update pre-onboarding-cliente
/plugin update ckb-builder
```

La actualización es manual por defecto: no se cambia nada en la máquina
de nadie sin que lo pida.

---

## Publicar una versión nueva (mantenimiento)

1. Editar los archivos del plugin afectado dentro de su carpeta
   (`pre-onboarding-cliente/` o `ckb-builder/`).
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
├── pre-onboarding-cliente/     # plugin 1
│   ├── .claude-plugin/plugin.json
│   ├── README.md
│   └── skills/pre-onboarding-cliente/
└── ckb-builder/                # plugin 2
    ├── .claude-plugin/plugin.json
    └── skills/ckb-builder/
```
