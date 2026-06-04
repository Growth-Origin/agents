# Plantilla del guion del workshop de validación

Documento que produce el agente en el Paso 3 del flujo
(`workshop_validacion/guion_workshop.md`). Pensado para que el consultor
humano conduzca un workshop de 60–90 minutos con el cliente y co-valide
el CKB.

Idioma: español de España (peninsular). Si el cliente final está en
Latinoamérica y el operador pide explícitamente otra variante para el
documento que se compartirá con el cliente, puedes adaptar solo ese
documento. El resto del CKB sigue en peninsular.

## Cómo usar este guion

- El agente lo genera con los contenidos específicos del cliente.
- El consultor lo revisa antes del workshop, ajusta tiempos y prioridades
  según el cliente concreto.
- Durante el workshop se toma nota en
  `workshop_validacion/decisiones_pendientes.md`.
- Tras el workshop, el consultor (o una nueva ejecución del agente con
  las decisiones REALES aportadas por el consultor) actualiza los módulos
  afectados y promueve el estado del CKB de `borrador` a `validado`.

## Lo que el agente NO hace en el Paso 3

- **NO simula respuestas del cliente** en el workshop.
- **NO rellena `decisiones_pendientes.md`** con decisiones ficticias: lo
  entrega en blanco, con preguntas y placeholders, para que el consultor
  lo cumplimente con las respuestas reales durante la sesión.
- **NO produce `resultados_workshop.md`** ni equivalente por iniciativa
  propia. Ese archivo lo crea el consultor con las decisiones reales
  tras la reunión.
- **NO promociona el estado del CKB** de `borrador` a `validado` por sí
  mismo. La promoción la dispara el consultor cuando el workshop real ha
  ocurrido y las decisiones reales están registradas.

El workshop es presencial con el cliente. El agente solo provee las
herramientas (guion + lista de decisiones pendientes en blanco). Si el
operador quiere, en una ejecución posterior, el agente toma las
decisiones reales aportadas por el consultor y actualiza los módulos del
CKB, promoviendo entonces el estado a `validado`.

## Estructura del guion

~~~markdown
# Workshop de validación — [Nombre Cliente]

**Fecha prevista:** AAAA-MM-DD
**Duración:** 60–90 minutos
**Modalidad:** [presencial / videollamada]
**Asistentes esperados:**
- Del cliente: [nombres y rol].
- De la agencia: [nombres y rol].
**Documento de referencia:** CKB v0.1 (ver carpeta `ckb/`).

---

## Contexto para el consultor (no compartir tal cual con el cliente)

[Resumen ejecutivo de qué buscamos en el workshop: validar hipótesis,
cerrar incongruencias detectadas, autorizar diferenciales no explotados
a explorar, confirmar restricciones, confirmar voceros y autoría de
contenidos futuros].

[Las 3–5 cosas que NO podemos no resolver hoy].

---

## Apertura (5–10 min)

**Mensaje sugerido al abrir:**

«[Apertura literal: explicar brevemente qué es el CKB, qué hemos hecho
durante el onboarding, qué decisiones queremos cerrar hoy, cómo va a
funcionar la sesión y por qué cada decisión que se cierra ahora ahorra
correcciones después].»

---

## Bloque 1 — Identidad, negocio y momento (10–15 min)

Referencia: Módulo 1 del CKB.

**Hipótesis a validar:**

1. [Hipótesis abierta 1 del Módulo 1, formulada como pregunta directa].
2. [Hipótesis abierta 2].

**Datos a confirmar:**

- [Dato 1 que el agente no pudo cerrar, formulado como pregunta].
- [Dato 2].

**Preguntas afiladas para destrabar:**

- [Pregunta literal lista para leer en voz alta].

---

## Bloque 2 — Propuesta de valor, diferenciales e incongruencias (15–20 min)

Referencia: Módulo 2 del CKB. Suele ser el bloque más rico.

**Incongruencias detectadas que requieren decisión del cliente.** Por
cada una, presentar:

- Lo que dice la versión oficial: «[cita literal]» — fuente.
- Lo que dice la realidad observada: «[cita literal]» — fuente.
- Pregunta literal: «¿Cuál de las dos describe mejor el producto hoy?
  ¿Hay que ajustar la web, ajustar la oferta o convivir con la
  diferencia, y por qué?».

**Diferenciales no explotados a autorizar.** Por cada uno:

- Lo que detectamos: «[enunciado]» con evidencia.
- Implicación estratégica: «[qué pasaría si lo destacáramos]».
- Pregunta literal: «¿Os parece bien que lo incorporemos a la
  comunicación? ¿Hay alguna razón por la que no lo estabais
  destacando?».

---

## Bloque 3 — Voz, tono y restricciones de comunicación (10–15 min)

Referencia: Módulos 3 y 4.

**Confirmar:**

- Tono y registro detectados: [resumen]. ¿Os reconocéis en esta
  descripción?
- Glosario propuesto (términos a usar / términos a evitar): pegar la
  tabla y pedir validación.

**Restricciones de comunicación a clarificar:**

- Temas detectados como sensibles: [lista]. ¿Hay otros que no hayamos
  detectado?
- Competidores con los que no compararse explícitamente: ¿lista
  correcta?
- Datos confidenciales: ¿qué línea exacta hay entre lo publicable y lo
  reservado?

---

## Bloque 4 — Activos, expertise y voceros (10–15 min)

Referencia: Módulo 5. Crítico para la producción de contenido.

**Activos a confirmar:**

- Datos publicables detectados: [lista]. ¿Permiso para usarlos como
  citables en contenido externo?
- Casos de cliente: ¿permiso de publicación con métricas? ¿con cliente
  nombrado o anónimo?

**Voceros a confirmar:**

- Voceros identificados: [tabla]. ¿Confirmáis los nombres y
  prioridades?
- ¿Qué voceros aceptan firmar contenido producido en colaboración con
  la agencia?
- ¿Aceptan la exportación voluntaria de sus posts de LinkedIn para
  enriquecer el CKB? (recomendado para voceros de alta prioridad).

---

## Bloque 5 — Riesgos y siguientes pasos (5–10 min)

**Riesgos detectados que requieren decisión:**

[Por cada riesgo del apartado 4.5: enunciado + implicación + pregunta
para clarificar con el cliente].

**Siguientes pasos:**

- Tras este workshop, actualizamos el CKB con vuestras decisiones y lo
  promovemos a estado `validado`.
- A partir de ahí, todos los siguientes trabajos (estrategia,
  contenidos, campañas) parten del CKB validado.
- Mantenimiento vivo: cada nueva pieza relevante (estudio, lanzamiento,
  cambio de mensaje) actualiza el módulo afectado.

---

## Cierre (5 min)

«[Pregunta abierta de cierre: ¿hay algo importante que no hayamos tocado
o que os preocupe de cara a empezar a producir?].»

«[Acuerdos finales: fecha en que se envía el CKB validado, fecha del
primer hito de producción posterior].»
~~~

## Plantilla de decisiones pendientes

Documento que el consultor rellena durante el workshop:
`workshop_validacion/decisiones_pendientes.md`.

~~~markdown
# Decisiones pendientes — Workshop [Cliente] [Fecha]

## Decisiones cerradas hoy

| # | Tema | Decisión | Módulo CKB afectado |
|---|------|----------|---------------------|
| 1 |      |          |                     |

##