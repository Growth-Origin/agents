# Pre-Onboarding de Cliente — Agente 1.0

Plugin para preparar la primera reunión de onboarding de un cliente nuevo.
A partir de la URL del cliente y de quién va a la reunión, investiga fuentes
públicas con una mirada de **marketing 360** y deja todo listo para que el
consultor llegue con hipótesis y preguntas afiladas en vez de preguntas
genéricas. Idioma de salida: **español de España**.

Hecho por **Growth Origin**. Uso interno del equipo.

## Qué hace

Investiga al cliente cubriendo: posicionamiento y propuesta de valor, marca y
mensaje, canales y presencia digital (SEO/GEO, contenido, redes sociales, paid,
email), voz real del mercado, footprint del equipo fundador y contexto del
nicho/competencia. Después cruza la versión oficial del cliente con la realidad
del mercado y detecta lo que no es obvio.

## Qué entrega (4 archivos por cliente)

1. **Archivo de memoria del cliente** — un knowledge base que queda guardado y
   crece con el tiempo; lo reusan futuras reuniones y el CKB Builder (Agente 1.1).
2. **Guion de entrevista de onboarding** — modular, se adapta a quién esté en la
   reunión (founder, marketing, ventas).
3. **Resumen ejecutivo de 1 hoja** — para llegar listo de un vistazo.
4. **Pedido de documentación y accesos** — email para pedirle al cliente lo
   justo y necesario antes de la reunión.

Se guardan en `clientes/[slug-cliente]/` dentro de la carpeta de trabajo: la
memoria en la raíz del cliente y el resto en la subcarpeta `pre-onboarding/`.

## Cómo se usa

Una sola puerta de entrada: el skill **Pre-onboarding cliente**. Se dispara de
dos maneras (las dos hacen lo mismo):

- Escribiendo `/` y eligiendo **Pre-onboarding cliente**.
- En lenguaje natural: «Prepara este cliente para la reunión de onboarding,
  aquí está la URL y a quién voy a entrevistar».

Lo primero que hace es pedirte los datos del cliente con un formulario fijo
(siempre los mismos campos, incluido **por qué nos contactó el cliente**).
Después te muestra un plan y te pide **confirmar que identificó bien a las
personas** antes de investigar a fondo.

## Cómo trabaja (3 pasos)

1. **Toma de datos** — formulario fijo con los datos del cliente (URL, personas
   a entrevistar, motivo del contacto, etc.).
2. **Investigación** — con checkpoint de identidad antes de profundizar; produce
   un documento de hallazgos con fuentes.
3. **Síntesis y entregables** — produce los 4 archivos.

Siempre hay **revisión humana**: el agente no envía nada al cliente. Un consultor
valida antes.

## Reglas que respeta

Solo fuentes públicas (no se autentica en ninguna plataforma); trazabilidad en
cada afirmación (fuente, confianza, si es hecho/interpretación/hipótesis); no
inventa fuentes; no procesa datos sensibles; anonimiza a terceros. Lo que no
puede verificar lo marca como hueco y lo incluye en el pedido de documentación.

## Investigación de redes (LinkedIn, Instagram, X…)

La búsqueda web por sí sola no basta para redes: LinkedIn pide login y la
mayoría de las redes se renderizan con JavaScript, así que devuelven poco. Para
conseguir el footprint real, el agente:

1. Usa **Claude in Chrome** (si lo tienes conectado) para abrir y leer los
   perfiles reales en tu navegador, donde ya estás logueado. Para que funcione,
   ten la extensión conectada y la sesión de LinkedIn iniciada.
2. Si no hay navegador o el contenido pide login, te pide que **pegues** el
   contenido (posts recientes, «about» de la página).
3. Lo que aun así no consigue, lo marca como hueco y lo suma al pedido de
   documentación, en vez de inventar.

Es contenido público visto desde tu propio navegador (visita asistida), no
scraping automatizado con login de terceros.

## Idioma

Los entregables y el diálogo se redactan en **español de España (peninsular)**,
como en todo el ecosistema. Única excepción: el email al cliente puede
adaptarse a la variante del país del cliente si lo pides explícitamente.

## Nota de compliance

Para un piloto con un cliente conocido bastan las reglas de arriba. Antes de
usarlo con clientes que no sean de confianza, confirma que la agencia tiene su
documentación de tratamiento de datos al día (interés legítimo, aviso de
privacidad, acuerdos de tratamiento).
