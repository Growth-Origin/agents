# Plantilla del resumen ejecutivo en PDF — ICP Definer (Agente 3)

> Estructura del entregable `resumen_ejecutivo.pdf`: documento presentable de **2–4
> páginas** que condensa el ICP para que un humano (operador, director o cliente) lo lea
> sin abrir los `.md`. Idioma: español de España (peninsular).

## Reglas del PDF

1. **Es un resumen, no un volcado.** Nunca contiene un dato que no esté ya en
   `icp_perfiles.md` / `outputs_accionables.md`.
2. **Presentable.** Limpio, jerarquía clara, tablas solo cuando aportan. Sin la maraña
   de etiquetas de trazabilidad (esas viven en el `.md`); nota al pie de «fuentes y
   trazabilidad completas en el documento detallado».
3. **Honesto con los niveles.** Indica qué quedó **«requiere herramienta (Nivel 2+)»**
   (típicamente demografía exacta, volúmenes, señales de CRM) y qué se aproximó.
4. **Marca el estado.** Es un **borrador pendiente de validación humana**: el consultor
   valida y afina en sesión con el cliente.
5. **Coherente con el ecosistema.** Si hay una skill de marca/estilo
   (`brand-guidelines`, `theme-factory`), aplícala sobria y consistente; si no, diseño
   limpio por defecto.

## Cómo generarlo

A partir de los `.md` ya redactados: HTML maquetado a PDF, o la skill `pdf`. Si el
entorno no puede generar PDF, produce `resumen_ejecutivo.md` con esta estructura y
avisa.

## Estructura (2–4 páginas)

1. **Portada / cabecera** — «ICP y buyer personas — [Cliente]», subtítulo «Resumen
   ejecutivo · SEO/GEO». Metadatos compactos: fecha, modelo (B2B/B2C), nivel de
   investigación, nº de perfiles validado, perfil primario, origen del contexto,
   versión, «borrador pendiente de validación humana».

2. **Síntesis ejecutiva** (1 párrafo): a quién le hablamos, por qué nos compra y cómo
   decide — el perfil primario en una frase, y por qué es el primario.

3. **Mapa de perfiles** — mini-tabla: perfil, tipo (primario/secundario/negativo),
   prioridad, y la frase que lo define. Incluye la persona negativa.

4. **Perfil primario en detalle** — media página: JTBD (job statement), 2–3 objeciones
   clave, lenguaje real (2–3 citas), firma de prompt (2–3 ejemplos) y canales donde
   busca.

5. **Matriz accionable (extracto)** — la tabla persona x etapa x intención del perfil
   primario, con el tipo de contenido y el agente destino.

6. **Filtro anti-persona** — 3–5 keywords/prompts a evitar y por qué (qué tráfico sin
   valor traen).

7. **Conclusiones por agente destino** — tabla compacta (Estrategia / Contenido /
   Prompts GEO) con lo prioritario; marca lo que depende de Nivel 2+.

8. **Huecos y nivel** — qué quedó «requiere herramienta (Nivel 2+)», qué se aproximó, y
   el siguiente paso (validar en sesión, activar Nivel 2, o pasar a Estrategia/Contenido
   con lo que ya hay).

9. **Pie** — «ICP detallado, fuentes y trazabilidad completas en `icp_perfiles.md` y
   `outputs_accionables.md`. Revisión sugerida: trimestral ligera, refresco profundo
   anual o ante cambios de mercado.»

## Longitud orientativa

- Portada + síntesis + mapa de perfiles: 1 página.
- Perfil primario + matriz: 1–2 páginas.
- Filtro anti-persona + conclusiones + huecos: 1 página.

Si excede 4 páginas, prioriza el perfil primario y la matriz: el detalle del resto vive
en los `.md`.
