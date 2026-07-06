# Plantilla del resumen ejecutivo en PDF — Competitive Intelligence (Agente 2.2)

Estructura del entregable `resumen_ejecutivo.pdf`: documento presentable de
**2–4 páginas** que condensa el análisis competitivo para que un humano
(operador, director o cliente) lo lea sin abrir los `.md`. Idioma: español de
España (peninsular).

## Reglas del PDF

1. **Es un resumen, no un volcado.** Nunca contiene un dato que no esté ya en
   `analisis_competitivo.md` / `sintesis_accionable.md`.
2. **Presentable.** Limpio, jerarquía clara, tablas solo cuando aportan. Sin la
   maraña de etiquetas de trazabilidad (esas viven en el `.md`); nota al pie de
   «fuentes y trazabilidad completas en el análisis detallado».
3. **Honesto con los niveles.** Indica claramente qué quedó **«requiere
   herramienta (Nivel 2+)»** (típicamente backlinks y volúmenes exactos) y qué
   motores GEO no se pudieron auditar.
4. **Coherente con el ecosistema.** Si está disponible una skill de marca/estilo
   (`brand-guidelines`, `theme-factory`), aplícala sobria y consistente; si no,
   diseño limpio por defecto.

## Cómo generarlo

A partir de los `.md` ya redactados: HTML maquetado a PDF, o la skill `pdf`. Si el
entorno no puede generar PDF, produce `resumen_ejecutivo.md` con esta estructura y
avisa.

## Estructura (2–4 páginas)

1. **Portada / cabecera** — «Análisis competitivo — [Cliente]», subtítulo
   «Resumen ejecutivo · SEO/GEO». Metadatos compactos: fecha, parámetros de
   enfoque, competidores analizados, nivel de investigación (1/2), motores GEO
   auditados (con método), versión, «borrador pendiente de revisión humana».

2. **Síntesis ejecutiva** (1 párrafo): las palancas competitivas más valiosas que
   el cliente puede accionar.

3. **Competidores analizados** — mini-tabla: competidor, tipo (directo /
   indirecto / aspiracional), y su mayor fortaleza y mayor debilidad explotable.

4. **Palancas clave por competidor** — por cada competidor, 2–4 bullets con los
   hallazgos más accionables (insight→acción condensado).

5. **Síntesis accionable agregada** — tabla compacta de conclusiones por agente
   destino (Estrategia / Contenido / ICP Agente 3), con las prioritarias. Marca las
   que dependen de Nivel 2+.

6. **Huecos y nivel** — qué quedó «requiere herramienta (Nivel 2+)» (backlinks,
   volúmenes exactos), qué motores GEO no se auditaron y por qué, y el siguiente
   paso (activar Nivel 2, o pasar a Estrategia/Contenido con lo que ya hay).

7. **Pie** — «Análisis detallado, fuentes y trazabilidad completas en
   `analisis_competitivo.md` y `sintesis_accionable.md`. Re-auditoría sugerida:
   trimestral.»

## Longitud orientativa

- Portada + síntesis + competidores: 1 página.
- Palancas por competidor: 1–2 páginas.
- Síntesis agregada + huecos: 1 página.

Si excede 4 páginas, prioriza síntesis y recorta detalle: el detalle vive en los
`.md`.
