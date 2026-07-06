# Plantillas de entregables (Paso 2)

Con el documento de hallazgos, produce los 4 entregables. No resumas: cruza y
contrasta. El entregable 1 (memoria) usa el esquema de `esquema-memoria.md`.

---

## Entregable 1 — Archivo de memoria del cliente

Rellena completo el esquema de `esquema-memoria.md`, seccion por seccion, con la
convencion de trazabilidad. Las secciones 9-12 (hipotesis, incongruencias,
diferenciales/oportunidades, riesgos) son el corazon: ahi va tu valor cruzando
la version oficial con la realidad. La seccion 13 (huecos) debe quedar lista
para alimentar el Entregable 4. Guarda como
`clientes/[slug-cliente]/memoria_[slug-cliente].md`.

---

## Entregable 2 — Guion de entrevista de onboarding (modular)

El formato de reunion varia por cliente. El guion es modular: un nucleo que
siempre se usa + modulos que el consultor activa segun quien este en la sala.

```
# Guion entrevista de onboarding — [Cliente]
**Duracion orientativa:** [segun modulos]
**Como usar:** usa el NUCLEO siempre; suma modulos segun las personas presentes.

## Contexto previo (no compartir con el cliente)
[3-5 parrafos: que sabemos, hipotesis centrales, gaps detectados]

## Apertura (5 min) — texto sugerido
["Ya he leido tu web, tus redes, las resenas y la prensa; quiero ir directo a
lo que no me cuadra..."]

## NUCLEO — Decisor / founder (siempre)
[6-8 preguntas afiladas con texto literal + ramas de profundizacion
("si responde X, profundizar con Y")]

## MODULO A — Marketing / Growth (si esta presente)
[stack y canales actuales, contenido que funciono/fracaso y por que, mix de
adquisicion con numeros aproximados, metricas que miran, presupuesto, procesos,
que esperan de la agencia]

## MODULO B — Ventas / Customer Success (si esta presente)
[objeciones reales en demos, lenguaje exacto de clientes, competidores en deals
reales, casos de uso descubiertos post-lanzamiento, por que ganan/pierden]

## Cierre (5 min)
[pregunta abierta + acuerdos de proximos pasos]

## Anexo — Preguntas de profundizacion opcionales
```

Reglas: preguntas con texto literal listas para leer; basadas en evidencia
concreta, no genericas (mal: "¿que los diferencia?"; bien: "en el podcast con X
dijiste Y, pero la web dice Z, ¿cual describe mejor el producto hoy?"); cada
pregunta clave referencia la hipotesis/incongruencia que resuelve; tono adaptado
al estilo publico del decisor (seccion 7 de la memoria).

---

## Entregable 3 — Resumen ejecutivo de 1 hoja

Una sola hoja. Denso pero legible.

```
# Resumen ejecutivo — [Cliente] — preparacion reunion [fecha]

**Que es el cliente:** [2-3 frases]
**A quien entrevistamos:** [personas + rol]
**Por que nos contacto / contexto:** [1-2 frases, del input del operador]

## Las 3 cosas que NO puedes no saber
[3 hallazgos clave, una linea cada uno]

## Hipotesis estrategica central
[1 parrafo: que tipo de cliente es y que necesitamos confirmar/desmontar]

## Foto de marketing (1 vistazo)
[posicionamiento + canales fuertes + canales ausentes, en 3-4 lineas]

## Top incongruencias (max. 3)
[oficial vs. realidad -> pregunta]

## Oportunidades de marketing no explotadas (max. 3)
## Riesgos a tener en el radar (max. 3)
## Lo que NO sabemos y vamos a preguntar (max. 5)
```

---

## Entregable 4 — Pedido de documentacion y accesos

Email listo para que el consultor revise y envie. Se nutre de la seccion 13
(huecos) de la memoria.

Reglas: quirurgico (solo lo necesario, cada cosa con una linea de por que); tono
senior (ni servil ni distante); cerrar con "lo que no tengáis o no queráis
compartir, no pasa nada".

```
Asunto: Preparacion reunion onboarding — [Cliente] — material previo

Hola [contacto],

[1 frase de encuadre: queremos que esa reunion sea de maximo valor]

**Documentacion interna (si existe):**
- [items derivados de los huecos, cada uno con su por que: deck, ICP/buyer
  persona, guia de marca/tono, casos con metricas, top contenidos, plan de
  medios o de redes si lo tienen]

**Accesos (solo lectura, durante onboarding):**
- [GA4, Search Console, gestor de redes/ads, etc. — aclarando que los procesa
  otro proceso tras firmar el acuerdo correspondiente]

**Logistica:**
- [confirmar personas a entrevistar + disponibilidad de calendario]

**Una pregunta abierta:**
- ¿Hay algo especialmente sensible o confidencial que debamos saber antes?

[cierre + firma]
```

---

## Reglas generales de la sintesis

- No inventes datos fuera de los hallazgos. Lo que falte va a "huecos".
- Toda hipotesis e incongruencia se justifica citando los hallazgos.
- Mejor pocas hipotesis solidas que muchas especulativas.
- Marca siempre que es hecho, que es interpretacion y que es hipotesis.
- Guarda los 4 archivos segun la estructura del SKILL: la memoria en
  `clientes/[slug-cliente]/` y el resto en `clientes/[slug-cliente]/pre-onboarding/`.
