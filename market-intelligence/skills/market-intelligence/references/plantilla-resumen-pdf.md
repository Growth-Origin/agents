# Plantilla del resumen ejecutivo en PDF — Market Intelligence (Agente 2.1)

Estructura del entregable `resumen_ejecutivo.pdf`: un documento presentable de
**2–4 páginas** que condensa todo lo encontrado para que un humano (operador,
director o el propio cliente) lo lea sin abrir los `.md`. Idioma: español de
España (peninsular).

## Reglas del PDF

1. **Es un resumen, no un volcado.** Nunca contiene un dato que no esté ya en
   `analisis_mercado_completo.md`. Si algo no cabe, se queda fuera; el detalle vive en los
   `.md`.
2. **Presentable.** Pensado para enseñar a un director o a un cliente: limpio,
   con jerarquía clara, tablas solo cuando aportan. Sin la maraña de etiquetas de
   trazabilidad (esas viven en el `.md`); el PDF puede llevar una nota al pie de
   «fuentes y trazabilidad completas en el análisis detallado».
3. **Honesto con los huecos.** Incluye una sección breve de limitaciones (qué
   motores no se auditaron, qué datos quedaron «dato no disponible»). No vende
   más certeza de la que hay.
4. **Coherente con el ecosistema.** Si está disponible la skill de marca/identidad
   (p. ej. `brand-guidelines` o `theme-factory`), aplica un estilo sobrio y
   consistente. Si no, un diseño limpio por defecto.

## Cómo generarlo

Construye el PDF a partir del `analisis_mercado_completo.md` ya redactado. Vía recomendada:
montar un HTML bien maquetado y convertirlo a PDF, o usar la skill `pdf` del
entorno. Si en tu entorno no hay forma de generar PDF, produce
`resumen_ejecutivo.md` con esta misma estructura y avisa de que el PDF queda
pendiente; no lo des por hecho.

## Estructura (2–4 páginas)

1. **Portada / cabecera**
   - Título: «Análisis de mercado — [Cliente]».
   - Subtítulo: «Resumen ejecutivo · SEO/GEO».
   - Metadatos compactos: fecha, ámbito geográfico, idiomas, profundidad,
     motores GEO auditados, versión, «borrador pendiente de revisión humana».

2. **Síntesis ejecutiva** (1 párrafo, el del `analisis_mercado_completo.md`).

3. **Tres titulares** — las 3 conclusiones de mayor impacto, en una línea cada
   una (los mismos que encabezan `conclusiones_accionables.md`).

4. **Hallazgos clave por bloque** — una caja o fila por bloque (1–7) con 1–3
   bullets del hallazgo más accionable de cada uno. Condensado, no exhaustivo.

5. **Dónde está el cliente en el panorama generativo** — mini-tabla con los wins
   (dónde aparece) y los huecos GEO priorizados (las oportunidades). Es el
   corazón del valor del agente; merece destaque.

6. **Conclusiones accionables por agente destino** — tabla compacta:
   cuántas conclusiones por destino (ICP 1.2 / Estrategia / Contenido / Voceros)
   y las 2–3 prioritarias de cada uno. El detalle completo, en
   `conclusiones_accionables.md`.

7. **Limitaciones y próximos pasos** — motores no auditados, datos «no
   disponibles», y el siguiente paso natural (p. ej. Agente 2.2 con la lista
   nominada de competidores, o refinamiento del ICP en el 1.2).

8. **Pie** — «Análisis detallado, fuentes y trazabilidad completas en
   `analisis_mercado_completo.md`. Re-auditoría sugerida: trimestral.»

## Longitud orientativa

- Portada + síntesis + titulares: 1 página.
- Hallazgos por bloque + panorama generativo: 1–2 páginas.
- Conclusiones por destino + limitaciones: 1 página.

Si el contenido empuja más allá de 4 páginas, prioriza síntesis y recorta
detalle: para el detalle ya están los `.md`.
