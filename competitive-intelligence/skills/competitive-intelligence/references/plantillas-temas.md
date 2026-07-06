# Plantillas de los once temas — Competitive Intelligence (Agente 2.2)

Plantillas rellenables de `analisis_competitivo.md`. Se aplican **por
competidor**. Todo hallazgo sigue **insight → implicación → acción**. Idioma:
español de España (peninsular). Cada afirmación factual lleva su etiqueta
`‹fuente | acceso | confianza | tipo›` pegada.

Recordatorio de nivel: lo que no se puede obtener en Nivel 1 se marca **«requiere
herramienta (Nivel 2+)»**; lo aproximado por SERP se declara como aproximación.
Nunca se inventa un dato duro.

---

## Cabecera por competidor

~~~markdown
# [Nombre del competidor] — [dominio]

**Tipo:** directo / indirecto / aspiracional
**Por qué está aquí:** [señal que lo justifica: visibilidad orgánica, presencia en IA, solapamiento]
**Síntesis (3-4 líneas):** [las 2-3 palancas más valiosas que el cliente puede accionar de este competidor]
~~~

---

## 4.1 Rendimiento de búsqueda (SEO clásico)

~~~markdown
## 4.1 Rendimiento de búsqueda

| Keyword / página | Señal observada | Nivel del dato |
|------------------|-----------------|----------------|
| [keyword o URL] | posición/intención aprox. observada en SERP | aproximación (SERP) |

- **Insight:** de qué vive su tráfico (páginas y consultas que concentran su
  visibilidad, según observación de SERP). ‹serp: "..." | ... | aproximación›
- **Implicación:** [por qué esas páginas le funcionan]
- **Acción:** [keyword gap a atacar; páginas que el cliente debería crear/mejorar]

> Volúmenes, posiciones y tráfico exactos + keyword gap cuantitativo:
> **requiere herramienta (Nivel 2+)** (DataForSEO).
~~~

---

## 4.2 Rendimiento generativo (GEO)

~~~markdown
## 4.2 Rendimiento generativo (GEO)

| Consulta | Motor | Método | Repeticiones | ¿Aparece? / páginas citadas |
|----------|-------|--------|--------------|------------------------------|

- **Insight:** para qué consultas lo citan los motores y qué páginas suyas se
  llevan las citas (a menudo distintas de las que rankean en Google).
- **Implicación:** dónde es fuerte en IA y dónde no.
- **Acción:** en qué prompts el cliente debe entrar; qué páginas del competidor
  imitar para ganar citación.
‹motor-geo: [motor] | consulta: "..." | método: chrome/paste/navegador | repeticiones: N | ...›
~~~

---

## 4.3 Opinión de las IAs sobre el competidor (bloque diferencial)

~~~markdown
## 4.3 Opinión de las IAs sobre el competidor

Tres tipos de pregunta, con repeticiones:

| Tipo | Consulta | Patrón observado | Variabilidad |
|------|----------|------------------|--------------|
| Mercado | «mejores ... para X» | [¿aparece?, posición] | [estable / fluctúa] |
| Comparativa | «X o Y para Z» | [cómo lo posiciona] | |
| Sobre el competidor | «¿es fiable X?» | [opinión, fortalezas, qué debería mejorar] | |

- **Insight:** qué opinión tiene la IA del competidor y para qué casos lo tiene
  en cuenta.
- **Implicación:** qué reputación le reconoce la IA (espejo de lo que el cliente
  querrá construir o evitar).
- **Acción:** qué fortalezas replicar y qué debilidades explotar.

> Nota de no-determinación: respuestas repetidas N veces; se reporta patrón, no
> foto única.
~~~

---

## 4.4 Perfil de enlaces (backlinks)

~~~markdown
## 4.4 Perfil de enlaces (backlinks)

**Estado en Nivel 1: requiere herramienta (Nivel 2+) — DataForSEO o Semrush/Ahrefs.**
No hay sustituto público fiable para el perfil de backlinks ni el link gap. Se
deja marcado para la ejecución de Nivel 2. (Si el operador aporta un export de
una herramienta, se procesa aquí.)

- **Insight / Implicación / Acción:** pendientes de datos de herramienta.
~~~

---

## 4.5 Arquitectura web

~~~markdown
## 4.5 Arquitectura web

- **Insight:** cómo organiza secciones, profundidad de URLs, jerarquía (silos,
  hubs, breadcrumbs). ‹web: [URLs] | ...›
- **Implicación:** qué decisiones estructurales le dan ventaja de posicionamiento.
- **Acción:** qué replicar y qué debilidad arquitectónica puede explotar el
  cliente para hacerlo mejor.
~~~

---

## 4.6 Interlinking y clusters de contenido

~~~markdown
## 4.6 Interlinking y clusters de contenido

- **Insight:** patrones de enlazado interno, páginas pilar, cómo agrupan temas
  (pillar + cluster) y qué topical authority han construido.
- **Implicación:** dónde tienen autoridad temática consolidada y dónde huecos.
- **Acción:** qué clusters debe construir el cliente; qué huecos del competidor
  atacar.
~~~

---

## 4.7 Estructura E-E-A-T del competidor

~~~markdown
## 4.7 Estructura E-E-A-T del competidor

Benchmark de las cuatro dimensiones, comparado con lo que el sector premia (según
Agente 2.1):

| Dimensión | Qué ha construido el competidor | vs lo que premia el sector (2.1) |
|-----------|----------------------------------|----------------------------------|
| Estrategia de autores | ¿autores nombrados?, ¿credenciales?, ¿entidad verificable (LinkedIn, ORCID, Wikidata vía sameAs)? | |
| Autoridad de marca | sobre-nosotros, políticas editoriales, prensa, premios, registros sectoriales | |
| Pruebas de experiencia | datos propios, casos, capturas originales | |
| Señales de confianza | transparencia, citas a fuentes, reseñas verificadas | |

- **Acción:** qué elementos E-E-A-T y de autoría debe construir el cliente para
  igualar o superar.
~~~

---

## 4.8 Hacks de utilidad de contenido

~~~markdown
## 4.8 Hacks de utilidad de contenido

- **Insight:** técnicas concretas que usan para que su contenido sea más útil y
  citable (respuesta directa al inicio, pasajes autocontenidos, tablas con datos,
  FAQs, frescura/refresco).
- **Implicación / Acción:** patrones replicables que el cliente debe adoptar.
~~~

---

## 4.9 Personalidad comunicativa

~~~markdown
## 4.9 Personalidad comunicativa

- **Insight:** tono, ángulo editorial, formatos propios, voz de marca diferencial.
- **Implicación:** qué contribuye a su posicionamiento y engagement.
- **Acción:** qué es replicable y qué es propio e inimitable (no copiar, inspirar).
~~~

---

## 4.10 CMS, código y UX

~~~markdown
## 4.10 CMS, código y UX

| Elemento | Hallazgo | Fuente |
|----------|----------|--------|
| CMS / stack | [detectado por HTML/cabeceras] | web |
| Schema / datos estructurados | [tipos JSON-LD detectados] | web |
| Core Web Vitals | [LCP/INP/CLS] | pagespeed |
| UX relevante | [decisiones que favorecen engagement] | web |

- **Insight / Implicación / Acción** por fila relevante.

> Site audit técnico profundo: **requiere herramienta (Nivel 2+)** (SE Ranking).
~~~

---

## 4.11 Síntesis accionable (capa puente)

Va dentro de `analisis_competitivo.md` y como `sintesis_accionable.md` aparte.
Por competidor y de forma agregada. Cada conclusión es afirmación verificable y
autocontenida, con su agente destino.

~~~markdown
## 4.11 Síntesis accionable

| Conclusión accionable (autocontenida y verificable) | Agente destino |
|------------------------------------------------------|----------------|
| [Keywords y páginas a atacar — gaps] | Estrategia · Contenido |
| [Prompts/IA donde el competidor es fuerte y el cliente debe entrar] | Estrategia · Contenido |
| [Qué opina la IA del competidor y qué aprender] | Estrategia · ICP (Agente 3) |
| [Objetivos de backlinks — link gap] *(pendiente Nivel 2+)* | Estrategia (Capa 2) |
| [Mejoras de arquitectura e interlinking a replicar/superar] | Estrategia · Contenido |
| [Elementos E-E-A-T y de autoría a construir] | Contenido · ICP (Agente 3) |
| [Hacks de utilidad replicables] | Contenido (Capa 3) |
| [Elementos de personalidad / UX / CMS a considerar] | Estrategia · Contenido |

### Mapa de conclusiones por agente destino
| Agente destino | Conclusiones |
|----------------|--------------|
| Estrategia (Capa 2) | ... |
| Contenido (Capa 3) | ... |
| Agente 3 (ICP) | ... |
~~~

Si una fila depende de un dato Nivel 2+ aún no disponible, se incluye igual con la
nota de qué herramienta la completará. Las filas que no apliquen se eliminan, no
se rellenan con humo.
