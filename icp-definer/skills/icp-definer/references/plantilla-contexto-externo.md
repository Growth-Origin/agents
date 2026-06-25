# Paquete de contexto externo — ICP Definer (Agente 3)

> Cómo trabajar cuando **no hay CKB (1.1) ni outputs del 2.1/2.2** y el contexto del
> cliente viene de fuera (onboarding de otra agencia, brief, deck, web). Objetivo:
> mantener el hilo del ecosistema sin depender en duro de los agentes anteriores.
> Idioma: español de España (peninsular).

## Principio

El agente necesita un **contexto mínimo del cliente** para anclar el ICP. Ese contexto
puede venir de tres sitios, y cualquiera vale:

1. El CKB del Agente 1.1 (`ckb/`).
2. Los outputs del Agente 2.1 (mercado) y/o 2.2 (competidores).
3. **Este paquete externo:** documentos sueltos que aporta el operador.

Con el paquete externo, el agente **lee, normaliza y deja trazado** el contexto a los
mismos campos que tendría del CKB, marcando el origen. No inventa lo que no esté; lo
que falte se pregunta o se marca como hueco.

## Campos a normalizar (los que el ICP necesita sí o sí)

| Campo | De dónde suele salir en docs de otra agencia | Para qué capa del ICP |
|-------|----------------------------------------------|------------------------|
| Sector y vertical | Brief, web «sobre nosotros», deck | ICP (firmográficos/segmento) |
| Propuesta de valor y oferta | Deck comercial, home, web de servicios | JTBD, objeciones |
| Modelo (B2B/B2C/B2B2C) | Brief, web | Dimensionado y adaptación |
| Geografía e idiomas objetivo | Brief, dominios, fichas locales | ICP, canales |
| Segmentos / clientes objetivo | Brief, casos de éxito, testimonios | Dimensionado (nº de perfiles) |
| Prioridades de negocio / foco comercial | Brief, acta de kickoff | Perfil primario |
| Voz de mercado / reseñas / testimonios | Reseñas públicas, web, casos | Lenguaje real, objeciones |
| Canales actuales | Web, redes, blog, GBP | Capa GEO/SEO (canales) |

## Cómo ingerir el paquete

1. El operador indica las **rutas o pega los documentos** (PDF, docx, md, enlaces). El
   agente los lee.
2. El agente **rellena la ficha de contexto normalizado** (abajo), citando de qué
   documento sale cada campo: `‹contexto-externo: [doc] p.X | acceso | confianza | tipo›`.
3. Lo que el paquete **no cubra** y sea crítico (modelo de negocio, segmentos
   prioritarios, foco comercial) lo **pregunta al operador** antes de dimensionar. No
   lo inventa.
4. Guarda la ficha en `_fuentes/contexto_normalizado.md` para que quede trazado y
   reutilizable.

## Ficha de contexto normalizado (plantilla)

~~~markdown
# Contexto del cliente (normalizado) — [Cliente]

**Origen del contexto:** CKB 1.1 / outputs 2.1-2.2 / paquete externo
**Documentos fuente:** [lista]

- **Sector y vertical:** ... ‹contexto-externo: [doc] | ...›
- **Modelo:** B2B / B2C / B2B2C
- **Propuesta de valor y oferta:** ...
- **Geografía / idiomas objetivo:** ...
- **Segmentos / clientes objetivo:** ...  (clave para dimensionar)
- **Prioridades de negocio / foco comercial:** ...  (clave para el perfil primario)
- **Voz de mercado / lenguaje real (si lo hay):** "..." (citas textuales)
- **Canales actuales:** ...

## Huecos de contexto (preguntar al operador o marcar)
- [campo que falta y por qué importa para el ICP]
~~~

## Aviso de calidad y de hilo

- El ICP hereda la fiabilidad del contexto que recibe. Si el material de la otra agencia
  trae afirmaciones sin fuente, las tratas como **hipótesis**, no como hechos, y lo
  dices.
- Esta ficha normalizada cumple el papel que cumpliría el CKB: si más adelante se
  construye el CKB de verdad (o se ejecutan el 2.1/2.2), se sustituye sin reescribir el
  ICP.
- Sin 2.1/2.2, el dimensionado (¿cuántos segmentos de demanda hay?) se apoya en lo que
  digan los documentos y la observación de motores/SERP; lo señalas como menos calibrado
  y propones ejecutarlos.
