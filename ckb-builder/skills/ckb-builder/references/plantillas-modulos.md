# Plantillas de los cinco módulos del CKB

Plantillas listas para rellenar de los cinco módulos consolidados y del
índice maestro. Las usas literalmente en el Paso 2 (síntesis) del flujo.

Todas siguen la estructura interna estándar definida en `esquema-ckb.md`:
metadata YAML + Síntesis (200–400 tokens) + Detalle + Evidencia +
Hipótesis abiertas + Notas para agentes downstream. Idioma: español de
España (peninsular).

---

## Módulo 0 — Índice maestro

Archivo: `ckb/00_indice_maestro.md`. Tamaño target: 400–800 tokens.

~~~markdown
# Client Knowledge Base — [Nombre Cliente]

**Versión CKB:** 0.1
**Fecha última actualización:** AAAA-MM-DD
**Estado global:** borrador | en-revisión | validado (workshop AAAA-MM-DD)

## Síntesis ejecutiva (1 párrafo)

[Quién es el cliente, qué hace, en qué fase está, qué tipo de relación
tenemos con él, principal hipótesis estratégica].

## Tesis estratégica central (2–3 frases)

[La hipótesis estratégica que define la relación con el cliente y que
toda la estrategia downstream debe respetar].

## Módulos disponibles

| ID | Módulo                                  | Versión | Última actualización | Confianza   | Tokens |
|----|-----------------------------------------|---------|----------------------|-------------|--------|
| 1  | Identidad y negocio                     | 1.0     | AAAA-MM-DD           | alta        | ~1800  |
| 2  | Propuesta de valor y diferenciales      | 1.0     | AAAA-MM-DD           | media-alta  | ~2200  |
| 3  | Voz, tono y lenguaje                    | 1.0     | AAAA-MM-DD           | media-alta  | ~2400  |
| 4  | Objeciones, fricciones y restricciones  | 1.0     | AAAA-MM-DD           | media       | ~2100  |
| 5  | Activos, expertise y voceros            | 1.0     | AAAA-MM-DD           | alta        | ~2300  |

**Total CKB:** ~N tokens
**Carga típica por tarea downstream:** 3.000–6.000 tokens

## Fuentes principales

- Memoria del Pre-Onboarding (AAAA-MM-DD).
- Transcripciones: N reunión(es) (duración total: NN min).
- Documentación entregada por el cliente: N documentos.
- Web del cliente: N páginas estratégicas + N artículos de blog
  procesados.
- LinkedIn corporativo: N posts.
- LinkedIn voceros: N posts.
- Apariciones externas: N (de ellas, M con transcripción procesada).

## Voceros identificados

| Nombre | Rol | Plataforma | Posts/mes | Engagement medio | Prioridad |
|--------|-----|------------|-----------|------------------|-----------|

## Decisiones del workshop (cuando exista)

[Resumen ejecutivo de las decisiones cerradas con el cliente en el
workshop. Lista actualizable].

## Changelog reciente

- v0.1 (AAAA-MM-DD): versión inicial tras el onboarding.
~~~

---

## Módulo 1 — Identidad y negocio

Archivo: `ckb/01_identidad_negocio.md`. Tamaño target: 1.500–2.500 tokens.

~~~markdown
---
modulo_id: "1"
modulo_nombre: "Identidad y negocio"
version: "1.0"
fecha_actualizacion: "AAAA-MM-DD"
autor: "Agente 1.1 CKB Builder v0.1"
confianza_global: "alta"
estado: "borrador"
fuentes_principales: ["memoria-agente-1", "entrevistas", "web"]
tokens_estimados: 1800
---

# Módulo 1 — Identidad y negocio

## Síntesis

[3–5 frases con los puntos esenciales: quién es el cliente, qué vende, a
quién, en qué momento está y cuál es el motivo de la relación con la
agencia. Esta sección es la que cargarán los agentes downstream que solo
necesiten referencia ligera].

## Detalle

### 1.1 Identidad del cliente

- Nombre legal [con fuente].
- Nombre comercial [con fuente].
- URL principal [con fuente].
- País HQ [con fuente].
- Mercados objetivo [con fuente].
- Idiomas de trabajo [con fuente].
- Sector / categoría declarada [con fuente].
- Descripción neutra en una frase [del agente].

### 1.2 Modelo de negocio

- Qué vende [con fuente].
- A quién (segmentos atendidos hoy) [con fuente].
- Cómo monetiza [con fuente].
- Ciclo de venta aproximado [con fuente o hipótesis].
- Tamaño operativo aparente [con fuente y caveat: no es due diligence].

### 1.3 Evidencia bruta sobre el ICP

> **PROHIBICIÓN ESTRICTA:** este apartado recoge evidencia. NO definas el
> ICP, NO produzcas un archivo de ICP, NO crees una carpeta `icp/`, NO
> generes una tabla de «los N ICPs del cliente». La definición y la
> nomenclatura del ICP son trabajo exclusivo del Agente 3 (ICP
> Definer). Lo que recoges aquí es input directo para el Agente 3.

- Sectores donde vende hoy [con fuente: deck, casos, web].
- Tamaños de empresa típicos [con fuente].
- Roles compradores observados [con fuente: entrevistas, casos].
- Geografías reales (no solo las declaradas) [con fuente].
- Patrones de uso descubiertos fuera del ICP declarado [con fuente].

### 1.4 Objetivos declarados y métricas

- Objetivos de negocio comunicados por el cliente [con fuente].
- Métricas que dice mirar [con fuente].
- Horizonte temporal (próximos 6, 12, 24 meses) [con fuente].
- Restricciones operativas declaradas que afectan a estos objetivos [con
  fuente].

### 1.5 Contexto del momento

- Fase actual (early, growth, scale) [con fuente o interpretación].
- Eventos relevantes recientes (rondas, lanzamientos, fichajes) [con
  fuente].
- Motivo de contactar a la agencia (heredado de la memoria del Agente 1
  §1) [con fuente].

## Evidencia

[Lista de las fuentes concretas que sostienen las afirmaciones
anteriores, con cita literal cuando aporte valor].

## Hipótesis abiertas

[Lista numerada de hipótesis que no se pudieron cerrar con la
información disponible y conviene confirmar en el workshop o en futuras
interacciones].

## Notas para agentes downstream

- Para el Agente 3 (ICP): la evidencia bruta del apartado 1.3 es input
  directo; valida X, Y y Z con el cliente antes de cerrar el ICP.
- Para los Agentes 2.1 y 2.2 (mercado y competencia): los mercados objetivo del
  apartado 1.1 y la fase del 1.5 condicionan el alcance competitivo.
- Para los agentes de producción de contenido: los objetivos del 1.4
  determinan la priorización editorial.
~~~

---

## Módulo 2 — Propuesta de valor y diferenciales

Archivo: `ckb/02_propuesta_valor_diferenciales.md`. Tamaño target:
1.800–3.000 tokens.

~~~markdown
---
modulo_id: "2"
modulo_nombre: "Propuesta de valor y diferenciales"
version: "1.0"
fecha_actualizacion: "AAAA-MM-DD"
autor: "Agente 1.1 CKB Builder v0.1"
confianza_global: "media-alta"
estado: "borrador"
fuentes_principales: ["entrevistas", "web", "documentacion", "memoria-agente-1"]
tokens_estimados: 2200
---

# Módulo 2 — Propuesta de valor y diferenciales

## Síntesis

[3–5 frases: cuál es la propuesta de valor oficial, cómo la percibe el
mercado de verdad, dónde están las brechas y qué diferenciales detectados
no se están explotando].

## Detalle

### 2.1 Propuesta de valor oficial

[Cómo se describe el cliente a sí mismo, con citas literales y fuente].

### 2.2 Diferenciales declarados

[Los 2–5 diferenciales que el cliente destaca, con cita literal y
fuente].

### 2.3 Percepción real del mercado

- Qué dicen reseñas (G2, Capterra, Trustpilot u otras según sector), con
  número de menciones y citas anónimas.
- Qué dice la prensa.
- Qué dicen los comentarios públicos a publicaciones del cliente o de
  los voceros.
- Lenguaje real del mercado frente a jerga oficial del cliente.

### 2.4 Diferenciales no explotados detectados

[Diferenciales que el mercado valora o que los voceros defienden en su
LinkedIn y que la comunicación oficial no destaca. Por cada uno:
enunciado, evidencia, implicación estratégica, pregunta de validación
para el workshop].

### 2.5 Incongruencias entre versión oficial y realidad

[Contradicciones directas con evidencia en ambos lados. Por cada una:
versión oficial (cita+fuente), versión real (cita+fuente), por qué
importa estratégicamente, pregunta de aclaración para el workshop].

## Evidencia

[Fuentes concretas que sostienen las afirmaciones].

## Hipótesis abiertas

[Hipótesis pendientes de validar].

## Notas para agentes downstream

- Para los agentes de producción de contenido: usa los diferenciales
  validados, no los meramente declarados.
- Para el Agente de drafting: las incongruencias del 2.5 son material
  potente para titulares y aperturas; consúltalas si vas a tocar un tema
  donde aparezcan.
- Para el Agente de SEO/GEO: la diferencia entre el vocabulario oficial
  y el del mercado (apartado 2.3) afecta a la elección de términos para
  optimizar.
~~~

---

## Módulo 3 — Voz, tono y lenguaje

Archivo: `ckb/03_voz_tono_lenguaje.md`. Tamaño target: 2.000–3.000
tokens.

~~~markdown
---
modulo_id: "3"
modulo_nombre: "Voz, tono y lenguaje"
version: "1.0"
fecha_actualizacion: "AAAA-MM-DD"
autor: "Agente 1.1 CKB Builder v0.1"
confianza_global: "media-alta"
estado: "borrador"
fuentes_principales: ["web", "documentacion", "linkedin", "memoria-agente-1"]
tokens_estimados: 2400
---

# Módulo 3 — Voz, tono y lenguaje

## Síntesis

[3–5 frases: cómo suena la marca, qué registro usa, qué la diferencia
lingüísticamente y dónde están los riesgos de salir de tono].

## Detalle

### 3.1 Tono y registro

- Eje formal-cercano: [posición + fuente + ejemplo].
- Eje técnico-divulgativo: [posición + fuente + ejemplo].
- Eje sobrio-provocador: [posición + fuente + ejemplo].
- Idioma principal y variantes por mercado.

### 3.2 Narrativa de marca

- Origen y misión: cómo la cuentan [con fuente].
- El «porqué» de la empresa [con fuente].
- Arcos narrativos recurrentes (problema-solución, héroe-mentor,
  tendencia-respuesta, etc.).
- Antagonistas a los que se opone explícitamente, si los hay.

### 3.3 Vocabulario propio

- Términos identitarios que el cliente repite consistentemente [con
  ejemplos y fuente].
- Claims propios que aparecen una y otra vez.
- Metáforas recurrentes.

### 3.4 Glosario operativo

**Términos a usar** (los del cliente):

| Término | Cómo usarlo | Cuándo aplica |
|---------|-------------|---------------|

**Términos a evitar** (jerga que el mercado no usa, palabras prohibidas
por la marca, vocabulario del competidor que no se debe adoptar):

| Término | Por qué evitarlo | Alternativa |
|---------|------------------|-------------|

### 3.5 Ejemplos canónicos

**On-brand** (5–10 frases reales, a imitar):

- «[Cita literal]» — fuente.

**Off-brand** (5–10 frases reales que no se deben imitar, con la razón):

- «[Cita literal]» — fuente — razón por la que es off-brand.

## Evidencia

[Fuentes concretas].

## Hipótesis abiertas

## Notas para agentes downstream

- Para todos los agentes de drafting: este módulo es lectura obligatoria
  antes de redactar cualquier cosa.
- Para el Agente de UX writing o microcopy: el apartado 3.4 es la base.
- Para el Agente de localización: el tono y vocabulario pueden variar
  por mercado; consulta también el apartado 1.1.
~~~

---

## Módulo 4 — Objeciones, fricciones y restricciones

Archivo: `ckb/04_objeciones_fricciones_restricciones.md`. Tamaño target:
1.800–3.000 tokens.

~~~markdown
---
modulo_id: "4"
modulo_nombre: "Objeciones, fricciones y restricciones"
version: "1.0"
fecha_actualizacion: "AAAA-MM-DD"
autor: "Agente 1.1 CKB Builder v0.1"
confianza_global: "media"
estado: "borrador"
fuentes_principales: ["entrevistas", "memoria-agente-1", "web"]
tokens_estimados: 2100
---

# Módulo 4 — Objeciones, fricciones y restricciones

## Síntesis

[3–5 frases: qué frena la compra y la satisfacción, qué no se puede
tocar, qué riesgos hay para la relación con la agencia].

## Detalle

### 4.1 Objeciones de leads y clientes potenciales

[Objeciones reales detectadas en ventas, customer success o reseñas, con
número de menciones, evidencia y posibles respuestas que el equipo de
ventas ya da].

| Objeción | Frecuencia | Fuente | Respuesta actual |
|----------|------------|--------|-------------------|

### 4.2 Fricciones operativas o de producto

[Quejas o fricciones reales detectadas en soporte público, reseñas o
entrevistas. Útiles para evitar contradicciones en contenido y para
priorizar mejoras].

### 4.3 Restricciones de comunicación

- Temas que el cliente NO quiere tocar [con razón si se conoce].
- Competidores con los que NO quiere compararse explícitamente.
- Datos confidenciales que no pueden publicarse.
- Aprobaciones internas requeridas para tipos concretos de contenido.

### 4.4 Sensibilidades sectoriales y regulatorias

- Sector específico (salud, financiero, infantil, etc.) y obligaciones
  derivadas.
- Mercados con regulaciones particulares (p. ej. GDPR en Europa, FTC en
  EE. UU.).
- Lenguaje sensible específico del sector.

### 4.5 Riesgos para la relación cliente-agencia

[2–5 riesgos detectados durante el onboarding. Por cada uno: enunciado,
evidencia, implicación para nuestro trabajo, pregunta de clarificación
para el workshop si aplica].

## Evidencia

[Fuentes concretas].

## Hipótesis abiertas

## Notas para agentes downstream

- Para todos los agentes de drafting: el apartado 4.3 es bloqueante; no
  se produce contenido que viole estas restricciones.
- Para el Agente de drafting de BOFU: el apartado 4.1 es el oro; cada
  objeción es una pieza potencial.
- Para el Agente de revisión legal o de marca, si existe: el apartado
  4.4 fija el marco mínimo.
~~~

---

## Módulo 5 — Activos, expertise y voceros

Archivo: `ckb/05_activos_expertise_voceros.md`. Tamaño target:
2.000–3.000 tokens.

~~~markdown
---
modulo_id: "5"
modulo_nombre: "Activos, expertise y voceros"
version: "1.0"
fecha_actualizacion: "AAAA-MM-DD"
autor: "Agente 1.1 CKB Builder v0.1"
confianza_global: "alta"
estado: "borrador"
fuentes_principales: ["documentacion", "web", "linkedin", "apariciones"]
tokens_estimados: 2300
---

# Módulo 5 — Activos, expertise y voceros

## Síntesis

[3–5 frases: qué activos publicables tiene el cliente, qué expertise
demostrable hay en el equipo y qué voceros pueden firmar contenido].

## Detalle

### 5.1 Datos publicables propios

[Estudios, métricas internas, benchmarks que el cliente puede publicar:
ya publicados o disponibles tras revisión. Por cada uno: dato concreto,
fuente, permiso de publicación, fecha de validez].

### 5.2 Casos de cliente con métricas

| Cliente representado | Sector | Problema resuelto | Métricas | Permiso |
|----------------------|--------|--------------------|----------|---------|

### 5.3 Premios, certificaciones, partnerships y prensa destacada

[Lista con fuente].

### 5.4 Voceros identificados — tabla resumen

| Nombre | Rol | Plataformas activas | Frecuencia | Engagement aparente | Prioridad | Identidad confirmada |
|--------|-----|---------------------|------------|---------------------|-----------|----------------------|

### 5.5 Detalle por vocero

Por cada vocero confirmado, repite la siguiente estructura:

#### Vocero — [Nombre, Rol]

- **Contexto profesional:** [trayectoria, empresas anteriores
  relevantes, tiempo en la empresa].
- **Frecuencia y consistencia:** [datos observados].
- **Temas dominantes:** [3–5 temas que repite, con ejemplos].
- **Posturas defendidas públicamente:** [a favor / en contra de qué; con
  citas literales].
- **Gap personal frente a corporate:** [temas que defiende
  personalmente y que NO aparecen en la comunicación oficial del
  cliente; este apartado es oro para contenidos firmados].
- **Apariciones externas destacadas:** [podcasts, conferencias, prensa,
  artículos firmados; con fecha, URL, breve resumen].
- **Estado de cobertura:** [completa vía exportación voluntaria;
  parcial vía búsqueda web; mínima por restricciones de acceso].

## Evidencia

[Fuentes concretas].

## Hipótesis abiertas

## Notas para agentes downstream

- Para los agentes de producción de contenido: este módulo es el motor
  del E-E-A-T y los contenidos firmados; siempre cargarlo cuando se
  vayan a firmar piezas con un miembro del equipo del cliente.
- Para el Agente de GEO: los datos publicables del apartado 5.1 son
  potenciales fuentes citables por LLMs; prioriza los que tengan
  metodología clara y métricas absolutas.
- Para el Agente de outreach o de medios: las apariciones externas del
  apartado 5.5 son la red de contactos efectiva.
~~~
