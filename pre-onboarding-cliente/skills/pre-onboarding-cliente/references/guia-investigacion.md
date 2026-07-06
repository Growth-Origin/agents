# Guia de investigacion — marketing 360

Lentes de investigacion para el Paso 1. Objetivo: un pantallazo completo de
marketing del cliente, no solo SEO/GEO. Profundidad media: lo suficiente para
preparar una gran primera reunion, no un audit exhaustivo.

> Antes de empezar: confirma identidades (checkpoint del SKILL.md). Toda
> afirmacion con su etiqueta de trazabilidad. Lo no verificable va a "huecos".

## Lente 1 — Identidad y posicionamiento (web oficial)

Recorre home, producto/funcionalidades, pricing, "About"/equipo,
"Customers"/casos, "Industries", y paginas legales (Privacy, Terms, DPA, Cookies
— revelan subprocesadores, jurisdicciones, partners).

Extrae: propuesta de valor y diferenciales declarados (cita literal), ICP
declarado, producto/integraciones/pricing, social proof oficial.

## Lente 2 — Marca y mensaje

- Tono y estilo de la comunicacion. ¿Formal, cercano, tecnico, provocador?
- Narrativa de marca: origen, mision, el "por que".
- Consistencia del mensaje entre web, redes y materiales.
- Identidad visual a grandes rasgos si es observable.
- Vocabulario propio y claims que repite.

## Lente 3 — Canales y presencia digital

El corazon del pantallazo de marketing. Cubre cada canal y marca los huecos.

- **SEO:** impresion de visibilidad para terminos de su categoria; calidad y
  profundidad del contenido indexable.
- **GEO:** ¿aparece el cliente cuando se pregunta por "best [categoria] for
  [sector]" en LLMs? ¿antes o despues que competidores? Prueba 2-3 prompts
  estandar de la categoria.
- **Contenido owned:** blog/recursos (temas, frecuencia, autores, idiomas),
  newsletter, lead magnets, webinars.
- **Redes sociales:** plataformas activas (LinkedIn, Instagram, X, TikTok,
  YouTube...). Por cada una: frecuencia, formato dominante, engagement aparente,
  tono. ¿Donde concentran esfuerzo y donde estan ausentes?
- **Paid:** anuncios visibles o en bibliotecas publicas de anuncios si se
  detectan (p. ej. Meta Ad Library, Google Ads Transparency).
- **Email / owned audience:** indicios de captura de leads, referidos, comunidad.

### Como investigar redes de verdad (importante)

La busqueda web baja HTML sin ejecutar JavaScript, asi que LinkedIn y la mayoria
de las redes devuelven casi nada por esa via. Procedimiento en orden:

1. **Busqueda web primero** para lo que este indexado por Google (algun post,
   notas de prensa que citan publicaciones, perfiles cacheados).
2. **Navegador (Claude in Chrome) si esta disponible:** abre y lee las paginas
   reales — LinkedIn del/los founder(s), pagina de empresa en LinkedIn, perfiles
   de Instagram/X/TikTok/YouTube de la marca. Usa las herramientas de leer
   pagina (navegar + extraer texto). Es contenido publico visto desde el
   navegador del operador (que ya esta logueado): visita asistida, no scraping
   automatizado con login propio. Respeta los terminos: solo lectura de
   informacion publica, con humano en el bucle.
3. **Fallback de pegado manual:** si no hay navegador o el contenido pide login,
   pide al operador que pegue los posts recientes y el "about" de cada perfil.
4. Lo que aun asi no consigas, va a la seccion de huecos. No lo inventes ni lo
   estimes como si fuera dato.

## Lente 4 — Voz real del mercado

- Plataformas de resenas segun sector (G2, Capterra, TrustRadius, Trustpilot...):
  volumen, puntuacion media, sentimiento.
- Comentarios publicos en posts del cliente (LinkedIn/YouTube).
- Comunidades publicas relevantes (Reddit, foros del sector, HN si es tech).
- Noticias y prensa (12-18 meses): financiacion, lanzamientos, fichajes, premios.

Extrae: lenguaje real vs. jerga oficial; objeciones y elogios recurrentes (con
nº de menciones); casos de uso fuera del ICP declarado.

## Lente 5 — Footprint del equipo

Solo personas confirmadas en el checkpoint. Por cada una: temas dominantes,
posturas defendidas, apariciones publicas (podcasts, charlas, prensa) y — lo mas
importante — el **gap personal vs. corporate**: temas que defiende y que NO
aparecen en la comunicacion oficial del producto.

Para el LinkedIn del founder (la fuente mas rica y la que peor rinde por
busqueda web), aplica el mismo procedimiento de la Lente 3: navegador si esta
disponible, fallback de pegado manual, y lo que falte a huecos.

## Lente 6 — Nicho y competidores (superficial)

5-10 competidores (declarados / implicitos en resenas / ambientales que
aparecen al buscar la categoria), con una frase de posicionamiento cada uno.
Dinamicas y vocabulario de la categoria. Profundidad baja a proposito: no hagas
gap analysis ni benchmarking serio.

## Formato del documento de hallazgos

```
# Hallazgos de investigacion — [Cliente]
**Fecha:** [fecha]  |  **Fuentes consultadas:** [N]

## A. Identidad y posicionamiento
## B. Marca y mensaje
## C. Canales y presencia digital (SEO/GEO, contenido, social, paid, email)
## D. Voz del mercado y prensa
## E. Footprint del equipo
## F. Nicho y competidores
## G. Observaciones preliminares (incongruencias y gaps que saltan, sin desarrollar)
## H. Huecos de informacion (todo lo no verificable, a pedir o preguntar)
```

## Reglas

- Cada afirmacion con su etiqueta de trazabilidad.
- Fuentes inaccesibles: dilo explicitamente.
- Anonimiza reviewers/comentaristas; nombra solo personas clave del input.
- Descarta datos sensibles (Art. 9 GDPR).
- No interpretes en profundidad aqui: extrae y señala. La sintesis es el Paso 2.
