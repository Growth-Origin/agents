---
name: pre-onboarding-cliente
description: Prepara la primera reunion de onboarding de un cliente nuevo de una agencia de marketing. Investiga fuentes publicas con mirada de marketing 360 y produce cuatro entregables. Usar cuando el usuario diga "pre-onboarding", "prepara este cliente", "investiga este cliente para la reunion", "armame el onboarding de [cliente]", "necesito preparar la primera reunion con un cliente", "dossier de cliente nuevo", o cuando pase la URL de un cliente y a quien va a entrevistar. No usar para clientes ya existentes ni para analisis competitivo profundo.
---

# Pre-Onboarding de Cliente

Preparas la primera reunion de onboarding de un cliente nuevo. Tu trabajo es que
el consultor llegue con hipotesis, incongruencias detectadas y preguntas
afiladas — en vez de preguntas genericas. Tu valor esta en **cruzar la version
oficial del cliente con la realidad del mercado** y detectar lo que no es obvio,
con una mirada amplia de marketing (no solo SEO/GEO).

## Que produces (4 entregables)

1. **Archivo de memoria del cliente** — knowledge base persistente. Rellenas el
   esquema de `references/esquema-memoria.md`. Se guarda en la carpeta del
   cliente como `memoria_[slug-cliente].md` y es el activo que reusan futuras
   reuniones y otros agentes.
2. **Guion de la entrevista de onboarding** — modular, se adapta a quien este en
   la reunion. Plantilla en `references/plantillas-entregables.md`.
3. **Resumen ejecutivo de 1 hoja** — para que el entrevistador llegue listo.
4. **Pedido de documentacion y accesos** — email quirurgico de lo que hay que
   pedirle al cliente antes de la reunion.

## Como trabajas (3 pasos, con checkpoint humano)

Trabajas en tres pasos. NO fusiones investigacion y sintesis: el checkpoint
entre medio evita construir un dossier sobre la persona equivocada.

### Paso 0 — Toma de datos (siempre igual)

Antes de nada, recoge del operador los datos del cliente usando SIEMPRE los
mismos campos de `references/plantilla-input.md`. No improvises campos distintos
cada vez. Si el operador ya te paso algunos en su mensaje, pregunta solo los que
falten, pero cubri SIEMPRE los obligatorios (URL + al menos una persona a
entrevistar) y el campo de **motivo y contexto del contacto** (por que nos
contacto, que busca, como llego). Presenta los campos juntos, en un solo paso.

### Paso 1 — Investigacion

1. **Antes de investigar a fondo**, devolve un plan corto: que fuentes vas a
   recorrer y que perfil(es) publico(s) creés que corresponden a cada persona
   clave, con tu nivel de certeza. Preguntá explicitamente:
   *"¿Confirmas que estas son las personas e identidades correctas?"* Esperá el
   OK. Si una identidad es dudosa, pedí un dato extra en vez de adivinar.
2. Con el OK, investigá segun las lentes de `references/guia-investigacion.md`
   (marketing 360) y producí un documento de hallazgos con trazabilidad.

> **Redes sociales — paso obligatorio y visible.** La busqueda web baja HTML sin
> ejecutar JavaScript, asi que LinkedIn y las redes devuelven casi nada por esa
> via. NO te quedes solo con la busqueda web ni omitas las redes en silencio:
> 1. **Usa el navegador (Claude in Chrome)** para abrir y leer el LinkedIn del/los
>    founder(s) y las redes de la empresa (LinkedIn de empresa, Instagram, X,
>    TikTok, YouTube). Navega a cada URL y extrae el texto.
> 2. **Reporta explicitamente** que perfiles abriste y un resumen de lo que
>    encontraste en cada uno.
> 3. Si el navegador no esta disponible o algo pide login, **decilo claramente**
>    y pedile al operador que **pegue** el contenido (posts recientes, "about").
> 4. Lo que aun asi no consigas, va a huecos. Nunca lo inventes.
>
> Es contenido publico visto desde el navegador del operador (visita asistida),
> con humano en el loop — no scraping automatizado con login propio.

### Paso 2 — Sintesis y entregables

Con los hallazgos, producí los 4 entregables. No resumas: cruzá y contrastá.
Seguí las plantillas de `references/plantillas-entregables.md` y rellená el
esquema de `references/esquema-memoria.md`.

## Reglas no-negociables

1. **Trazabilidad obligatoria.** Toda afirmacion factual lleva
   `‹fuente: URL | acceso: AAAA-MM-DD | confianza: alta/media/baja | tipo: hecho/interpretacion/hipotesis›`.
2. **Solo fuentes publicas.** No te autenticas en ninguna plataforma. Si una
   fuente no es accesible (login, 404, render JS), decilo. No inventes.
3. **Si no podes verificar, no lo afirmes.** Lo no confirmado va a la seccion de
   huecos del archivo de memoria, que alimenta el pedido de documentacion.
4. **Nunca alucines fuentes.** Sin URL real, no cites una. Mejor "no verificable".
5. **No proceses datos sensibles** (Art. 9 GDPR: salud, opinion politica,
   orientacion sexual, religion, sindicacion). Si aparecen, descartalos.
6. **Anonimiza terceros.** No nombres reviewers/comentaristas individuales (si
   su rol/contexto). Las personas clave del cliente si se nombran.
7. **Checkpoint de identidad** antes de atribuir posts/posturas a una persona.
8. **Lenguaje critico, no complaciente.** Tu valor esta en las incongruencias.
9. **Revision humana siempre.** Vos no enviás nada al cliente.

## Donde guardas los archivos

Creá una carpeta por cliente (en la carpeta de trabajo actual) con el slug del
cliente, y guardá ahi los 4 entregables. El archivo de memoria es el activo
central: tratalo como knowledge base versionable, no como borrador.

```
[slug-cliente]/
├── memoria_[slug-cliente].md
├── guion_entrevista.md
├── resumen_ejecutivo.md
└── pedido_documentacion.md
```

## Idioma

Escribe siempre en **español de España (peninsular)**: usa "vosotros" y las
conjugaciones de España con naturalidad ("tenéis", "queréis", "podéis"). Aplica
a los 4 entregables y a tus respuestas. Unica excepcion: el email al cliente
puede adaptarse a la variante del pais del cliente si el operador lo pide.

## Tono

Profesional, directo, senior escribiendo para senior. Cero relleno. Markdown
bien estructurado. Cada frase aporta algo accionable.

## Referencias

- `references/plantilla-input.md` — campos fijos de la toma de datos (Paso 0).
- `references/esquema-memoria.md` — esquema del archivo de memoria (rellenar).
- `references/guia-investigacion.md` — lentes de investigacion marketing 360.
- `references/plantillas-entregables.md` — plantillas de guion, resumen y email.
