# Pre-Onboarding de Cliente

Plugin para preparar la primera reunion de onboarding de un cliente nuevo.
A partir de la URL del cliente y de quien va a la reunion, investiga fuentes
publicas con una mirada de **marketing 360** y deja todo listo para que el
consultor llegue con hipotesis y preguntas afiladas en vez de preguntas
genericas.

Hecho por **Growth Origin**. Uso interno del equipo.

## Que hace

Investiga al cliente cubriendo: posicionamiento y propuesta de valor, marca y
mensaje, canales y presencia digital (SEO/GEO, contenido, redes sociales, paid,
email), voz real del mercado, footprint del equipo fundador y contexto del
nicho/competencia. Despues cruza la version oficial del cliente con la realidad
del mercado y detecta lo que no es obvio.

## Que entrega (4 archivos por cliente)

1. **Archivo de memoria del cliente** — un knowledge base que queda guardado y
   crece con el tiempo; lo reusan futuras reuniones.
2. **Guion de entrevista de onboarding** — modular, se adapta a quien este en la
   reunion (founder, marketing, ventas).
3. **Resumen ejecutivo de 1 hoja** — para llegar listo de un vistazo.
4. **Pedido de documentacion y accesos** — email para pedirle al cliente lo
   justo y necesario antes de la reunion.

Se guardan en una carpeta con el nombre del cliente, dentro de la carpeta de
trabajo.

## Como se usa

Una sola puerta de entrada: el skill **Pre-onboarding cliente**. Se dispara de
dos maneras (las dos hacen lo mismo):

- Escribiendo `/` y eligiendo **Pre-onboarding cliente**.
- En lenguaje natural: "Prepará este cliente para la reunion de onboarding,
  aca esta la URL y a quien voy a entrevistar".

Lo primero que hace es pedirte los datos del cliente con un formulario fijo
(siempre los mismos campos, incluido **por que nos contacto el cliente**).
Despues te muestra un plan y te pide **confirmar que identifico bien a las
personas** antes de investigar a fondo.

## Como trabaja (3 pasos)

1. **Toma de datos** — formulario fijo con los datos del cliente (URL, personas
   a entrevistar, motivo del contacto, etc.).
2. **Investigacion** — con checkpoint de identidad antes de profundizar; produce
   un documento de hallazgos con fuentes.
3. **Sintesis y entregables** — produce los 4 archivos.

Siempre hay **revision humana**: el agente no envia nada al cliente. Un consultor
valida antes.

## Reglas que respeta

Solo fuentes publicas (no se autentica en ninguna plataforma); trazabilidad en
cada afirmacion (fuente, confianza, si es hecho/interpretacion/hipotesis); no
inventa fuentes; no procesa datos sensibles; anonimiza a terceros. Lo que no
puede verificar lo marca como hueco y lo incluye en el pedido de documentacion.

## Investigacion de redes (LinkedIn, Instagram, X...)

La busqueda web por si sola no alcanza para redes: LinkedIn pide login y la
mayoria de las redes se renderizan con JavaScript, asi que devuelven poco. Para
conseguir el footprint real, el agente:

1. Usa **Claude in Chrome** (si lo tenes conectado) para abrir y leer los
   perfiles reales en tu navegador, donde ya estas logueado. Para que funcione,
   tene la extension conectada y la sesion de LinkedIn iniciada.
2. Si no hay navegador o el contenido pide login, te pide que **pegues** el
   contenido (posts recientes, "about" de la pagina).
3. Lo que aun asi no consigue, lo marca como hueco y lo suma al pedido de
   documentacion, en vez de inventar.

Es contenido publico visto desde tu propio navegador (visita asistida), no
scraping automatizado con login de terceros.

## Idioma

Los entregables se redactan en **español de España**.

## Nota de compliance

Para un piloto con un cliente conocido alcanza con las reglas de arriba. Antes de
usarlo con clientes que no sean de confianza, confirmá que la agencia tiene su
documentacion de tratamiento de datos al dia (interes legitimo, aviso de
privacidad, acuerdos de tratamiento).
