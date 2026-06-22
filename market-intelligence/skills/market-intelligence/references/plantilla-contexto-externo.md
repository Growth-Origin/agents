# Paquete de contexto externo — Market Intelligence (Agente 2.1)

Cómo trabajar cuando **no hay CKB del Agente 1.1** y el contexto del cliente
viene de fuera (p. ej. el onboarding que hizo otra agencia, un brief, un deck,
la web). El objetivo: mantener el hilo del ecosistema sin depender en duro del
agente anterior. Idioma: español de España (peninsular).

## Principio

El agente necesita un **contexto mínimo del cliente** para anclar el análisis.
Ese contexto puede venir de tres sitios, y cualquiera vale:

1. El CKB del Agente 1.1 (`ckb/`).
2. Un análisis de mercado previo (re-ejecución).
3. **Este paquete externo:** documentos sueltos que aporta el operador.

Con el paquete externo, el agente **lee, normaliza y deja trazado** el contexto a
los mismos campos que tendría del CKB, marcando el origen. No inventa lo que no
esté; lo que falte se pregunta o se marca como hueco.

## Campos a normalizar (los que el análisis necesita sí o sí)

| Campo | De dónde suele salir en docs de otra agencia |
|-------|----------------------------------------------|
| Sector y vertical | Brief, web «sobre nosotros», deck |
| Propuesta de valor | Deck comercial, home de la web |
| Oferta (productos/servicios) | Web de servicios, tarifas, catálogo |
| Geografía e idiomas objetivo | Brief, dominios, fichas locales |
| Prioridades de negocio | Brief, acta de kickoff, objetivos pactados |
| Voceros / equipo | Web «equipo», LinkedIn corporativo, deck |
| Canales actuales | Web, enlaces a redes, GBP, blog |
| Voz de mercado / reseñas | Reseñas públicas (se recogen aparte si faltan) |

## Cómo ingerir el paquete

1. El operador indica las **rutas o pega los documentos** (PDF, docx, md, enlaces
   a la web). El agente los lee.
2. El agente **rellena la ficha de contexto normalizado** (abajo), citando de qué
   documento sale cada campo: `‹contexto-externo: [doc] p.X | acceso | confianza | tipo›`.
3. Lo que el paquete **no cubra** y sea crítico (p. ej. prioridades de negocio o
   geografía exacta), el agente lo **pregunta al operador** antes de seguir. No lo
   inventa.
4. Guarda la ficha en `_fuentes/contexto_normalizado.md` para que quede trazado y
   reutilizable por el 2.2 y los downstream.

## Ficha de contexto normalizado (plantilla)

~~~markdown
# Contexto del cliente (normalizado) — [Cliente]

**Origen del contexto:** CKB Agente 1.1 / análisis previo / paquete externo
**Documentos fuente:** [lista]

- **Sector y vertical:** ... ‹contexto-externo: [doc] | ...›
- **Propuesta de valor:** ...
- **Oferta:** ...
- **Geografía / idiomas objetivo:** ...
- **Prioridades de negocio:** ...  (clave para el módulo keyword)
- **Voceros / equipo:** ...
- **Canales actuales:** ...
- **Voz de mercado (si la hay):** ...

## Huecos de contexto (preguntar al operador o marcar)
- [campo que falta y por qué importa]
~~~

## Aviso de calidad y de hilo

- El análisis hereda la fiabilidad del contexto que recibe. Si el material de la
  otra agencia trae afirmaciones sin fuente, las tratas como **hipótesis**, no
  como hechos, y lo dices.
- Para no perder el hilo del ecosistema, esta ficha normalizada cumple el papel
  que cumpliría el CKB: el Agente 2.2 y los downstream la pueden leer igual. Si
  más adelante se construye el CKB de verdad, se sustituye sin reescribir el
  análisis.
