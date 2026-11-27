# Task Priority Score (TPS) y roadmap por olas — Fase 7 (Agente 5)

> Tercera pieza de la familia de scores del ecosistema, junto al KPS y el PPS
> del Agente 4. Como ellos, opera con **pesos configurables por engagement**
> (Fase 1) y es transparente y trazable. Idioma: español de España.

## Fórmula

```
TPS = (w1 · Potencial + w2 · QuickWin + w3 · Negocio) · Factor_Esfuerzo

donde w1 + w2 + w3 = 1   (por defecto: w1 = 0.45, w2 = 0.25, w3 = 0.30)
```

## Los cuatro factores

| Factor | Definición | Escala |
|--------|------------|--------|
| **Potencial** | Suma normalizada de los KPS y PPS de todas las keywords y prompts que la tarea cubre. Una tarea que resuelve una entidad rica en elementos prioritarios puntúa alto. | 0–100 (normalizado sobre el máximo del engagement) |
| **QuickWin** | Bonus para URLs existentes con posición media 5–15 en sus keywords objetivo (según GSC): el terreno donde optimizar produce resultados más rápidos. | 0–100 |
| **Negocio** | Prioridad declarada por el cliente para el servicio/línea al que sirve la tarea (módulo de prioridades del CKB). Hereda la ponderación por prioridad de cliente del Agente 4. | 0–100 |
| **Factor_Esfuerzo** | Multiplicador inverso al coste de ejecución: Optimizar (1.0) > Consolidar (0.85) > Crear (0.7). A igual potencial, la tarea barata va antes. | 0.7–1.0 |

**Casos degradados:** en escenario NUEVA el QuickWin es 0 y su peso se
redistribuye proporcionalmente entre Potencial y Negocio. Sin GSC, el QuickWin
no tiene fuente: se marca «dato no disponible», se redistribuye igual y se
declara en la configuración. Sin prioridades de negocio del CKB ni del cliente,
**se pregunta** (no se inventa el factor Negocio).

Ajustes típicos de pesos en la Fase 1: cliente que necesita resultados rápidos →
subir w2 (QuickWin); cliente en construcción de marca a largo plazo → subir w1
(Potencial).

## Organización en olas

Las tareas ordenadas por TPS se agrupan en **olas de trabajo** dimensionadas
según la capacidad de producción mensual declarada en la Fase 1:

- **Ola 1 — Impacto inmediato:** quick-wins de optimización + las
  canibalizaciones cuya resolución libera rendimiento retenido. Suele ser la ola
  de mayor retorno por esfuerzo.
- **Ola 2 — Construcción del núcleo:** landings madre y variantes de alta
  prioridad + pillars de los clusters principales + páginas comparativas (la
  apuesta GEO).
- **Ola 3 — Despliegue:** satélites, landings locales y variantes de segunda
  línea, consolidaciones no urgentes y eliminaciones.

Cada tarea del roadmap lleva su TPS **desglosado por factor** (pestaña «Roadmap
por olas») y sus dependencias (p. ej. un satélite no se produce antes que su
pillar; una consolidación antes que la optimización de la URL destino).

## Olas, no fechas (regla dura)

El agente entrega **prioridad relativa, no calendario**. Convertir olas en meses
es decisión del consultor con el cliente, en función de recursos reales y
estacionalidad. Esta frontera protege al agente de comprometer plazos que no
controla. Si el operador pide fechas, el agente lo deriva al consultor y deja
constancia.
