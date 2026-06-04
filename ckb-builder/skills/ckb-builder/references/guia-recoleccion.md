# Guía de recolección — CKB Builder

Guía operativa del Paso 1 del flujo (recolección de fuentes). Indica cómo
procesar cada tipo de material que llega al agente, en qué orden, con qué
herramientas y qué guardar en `_fuentes/`.

## Idioma

Recordatorio: todo lo que escribas o produzcas se redacta en español de
España (peninsular). Las citas literales sí se conservan en su idioma
original; lo que tú añades alrededor (síntesis, contexto, notas) va en
peninsular.

## Orden recomendado

1. Memoria del Agente 1 → primero. Marca la línea base y las hipótesis
   abiertas que el resto de fuentes deben validar o desmontar.
2. Transcripciones de entrevistas → segundo. Es el material más rico.
3. Documentación entregada por el cliente → tercero. Complementa y matiza.
4. Web del cliente → cuarto.
5. LinkedIn corporativo + voceros → quinto, después del checkpoint de
   identidad.
6. Apariciones externas → al final.

Trabajar en este orden te permite ir cruzando cada fuente nueva con las
hipótesis acumuladas, en lugar de leerlas en frío.

## 1. Memoria del Agente 1

Es input obligatorio. Si existe el archivo `memoria_[cliente].md`:

- Lo lees completo.
- Lo copias tal cual a `_fuentes/memoria_agente_1.md`.
- Lo trasladas a versión 0 del CKB usando el cuadro de mapeo de
  `esquema-ckb.md`. Cada afirmación trasladada conserva su etiqueta de
  trazabilidad original, reescribiendo la fuente como `memoria-agente-1: §X`.

Si NO existe (cliente que no pasó por el Pre-Onboarding), avisas al
operador y acordáis hacer un pase rápido equivalente antes de continuar.
No procedes sin esa base.

## 2. Transcripciones de entrevistas

Aceptas `.txt`, `.vtt`, `.docx` y `.md`. Procesado:

1. Si la transcripción incluye marcas de hablante (Google Meet suele
   identificar por nombre), conservas la atribución y diferencias
   internamente quién dijo qué.
2. Si la transcripción es un bloque único sin hablantes, la tratas como
   input único y rico; no inventas voces separadas.
3. Extraes citas literales reveladoras con su timestamp en formato
   `mm:ss`.
4. Detectas patrones: contradicciones internas del entrevistado, momentos
   en los que se «abre» tras una pregunta afilada, temas que repite,
   temas que evita.
5. Vinculas con la memoria del Agente 1: ¿qué hipótesis se validan?,
   ¿cuáles se desmontan?, ¿qué hipótesis nuevas emergen?

Output:

- `_fuentes/transcripciones/[rol-o-nombre].md` con el texto procesado y
  las marcas de hablante cuando estén.
- Si hay varias entrevistas separadas (CEO, Marketing, Ventas/CS), un
  archivo por entrevista.
- Si hay una única reunión conjunta,
  `_fuentes/transcripciones/onboarding_conjunto.md`.

## 3. Documentación entregada por el cliente

Llega como PDF, DOCX, PPTX o markdown. Reglas:

- PDFs: Claude los procesa de forma nativa. No necesitas extracción previa.
- DOCX y PPTX: si el operador no los convirtió previamente, puedes pedir su
  conversión a markdown (con pandoc en local) o procesarlos en bruto si el
  contenido es texto plano.
- Markdown plano: se procesa directamente.

Identificas el tipo de cada documento y aplicas extracción específica:

| Tipo de documento     | Qué extraes                                                                |
|-----------------------|----------------------------------------------------------------------------|
| Deck de ventas        | Propuesta declarada, claims, social proof, lenguaje comercial.             |
| Manual de marca       | Tono oficial, vocabulario aprobado, restricciones de comunicación.         |
| Caso de cliente       | Cliente representado, problema, métricas, permiso de publicación.          |
| Estudio propio        | Datos publicables, metodología, conclusiones.                              |
| ICP / buyer persona   | Definición declarada (a contrastar con la evidencia bruta del Módulo 1.3). |
| Transcripción webinar | Tono real del cliente, temas, vocabulario, posturas defendidas.            |

Output: `_fuentes/documentacion_cliente/[nombre-documento].md` con el
resumen estructurado y las citas literales relevantes. Los originales no
se modifican.

## 4. Web del cliente

Método principal: **sitemap + WebFetch**, gratuito y suficiente para los
cinco módulos consolidados.

1. Lees `https://[dominio-cliente]/sitemap.xml` (o sus variantes
   `/sitemap_index.xml`, `/sitemap-pages.xml`). Sacas el listado de URLs
   y sus prioridades si están.
2. Descargas con WebFetch las **páginas estratégicas** (siempre):
   - Home.
   - Producto y páginas de funcionalidades.
   - Pricing (si existe).
   - About / Equipo.
   - Customers / Casos.
   - Industries / Who we serve (si existe).
   - Páginas legales: privacy, terms, DPA, cookies (revelan
     subprocesadores, jurisdicciones, partners).
3. Descargas un **muestreo del blog**:
   - Lista completa de URLs con título, fecha, autor y categorías
     (metadata).
   - Contenido completo de los 10–20 artículos más recientes.
   - Si la fuente permite ordenar por engagement, los 10 más populares.
   - Para el resto, solo metadata.
4. **Escalas a Claude in Chrome** únicamente para páginas concretas donde
   WebFetch devuelva HTML vacío por render con JavaScript. No abandones
   la página en silencio: dejas constancia de que escalaste y por qué.

Reglas de compliance al recoger la web:

- Respetas `robots.txt`.
- Rate limiting prudente: no más de una petición por segundo al sitio del
  cliente.
- User-Agent que identifica a la agencia.
- No sigues enlaces externos: solo dominios del cliente.

Output:

```
_fuentes/web/
├── crawl_summary.json    # índice de páginas con URL, fecha, hash, tamaño
├── paginas_estrategicas/
│   ├── home.md
│   ├── about.md
│   └── ...
├── blog_index.json       # metadata de todos los artículos
└── blog_muestreo/
    ├── articulo_001.md   # solo los 10-20 procesados en profundidad
    └── ...
```

## 5. LinkedIn corporativo y voceros

Es la parte donde más cuidado hace falta y donde aporta más valor.

### 5.1 Checkpoint de identidad (obligatorio)

Antes de tocar LinkedIn a fondo, devuelves al operador:

- La lista de voceros a investigar (los conocidos del input + los
  detectados en la página «About», el blog del cliente o LinkedIn
  corporativo).
- Para cada uno, el perfil de LinkedIn que crees que le corresponde, con
  la URL exacta y tu nivel de certeza.
- La pregunta literal: *«¿Confirmas que estos son los voceros e
  identidades correctos antes de que profundice?»*

Esperas el OK. Si una identidad es dudosa, pides un dato extra (empresa,
foto, URL exacta) en vez de adivinar. Si te equivocas de persona, todo el
trabajo posterior queda contaminado.

### 5.2 LinkedIn corporativo del cliente

Método compliant: solo contenido público indexado.

- Vía Claude in Chrome: navegas a `linkedin.com/company/[empresa]` (donde
  el operador ya está logueado) y lees la página y los posts visibles
  públicamente.
- Captura: últimos 20–30 posts visibles, con texto, fecha aproximada,
  reacciones y comentarios cuando se muestren, hashtags y enlaces
  externos.

Output: `_fuentes/linkedin_corporate/posts.json`.

### 5.3 Voceros

Por cada vocero confirmado en el checkpoint:

1. **Opción A — Claude in Chrome (por defecto).** Navegas al perfil
   personal en el navegador del operador y lees los posts públicos
   visibles. Cubres los últimos 12–18 meses en la medida de lo posible.
   Reportas al operador qué perfil abriste y qué encontraste.

2. **Opción B — Exportación voluntaria del propio vocero (recomendada
   para voceros prioritarios).** Si el operador puede coordinarlo con el
   cliente, el vocero exporta sus propios datos en
   `LinkedIn → Settings → Get a copy of your data`. Tarda 24–48 h. El
   operador entrega el ZIP / CSV al agente, que lo procesa. Compliance
   perfecto y cobertura completa.

3. **NUNCA opción de scraping autenticado.** Ni Sales Navigator, ni
   Phantombuster ni similares. Es violación de los términos de LinkedIn
   y riesgo legal en Europa.

Output: `_fuentes/linkedin_voceros/[slug-nombre].md` con posts, artículos
firmados, posturas defendidas, temas dominantes y comentarios destacados.

## 6. Apariciones externas

Para cada vocero confirmado, búsqueda web con consultas tipo:

```
"[Nombre Vocero]" "[Nombre Empresa]" podcast
"[Nombre Vocero]" "[Nombre Empresa]" keynote OR conferencia
"[Nombre Vocero]" interview OR entrevista
"[Nombre Vocero]" guest article OR artículo firmado
```

Captura por aparición: tipo (podcast / conferencia / prensa / artículo
firmado), nombre del medio, fecha, URL, descripción breve y si hay
transcripción pública.

Si hay transcripción pública (cada vez más habitual), la procesas. Si no,
dejas nota al operador sobre si conviene escuchar el episodio
manualmente.

Output: `_fuentes/apariciones_externas/index.json` más un markdown por
aparición con la transcripción procesada cuando exista.

## Reglas transversales de compliance

- Solo contenido público o material aportado por el cliente con permiso.
- Nada de scraping autenticado.
- Descartar datos sensibles del Art. 9 GDPR (salud, opinión política,
  orientación sexual, religión, sindicación).
- Anonimizar terceros: las reseñas y comentaristas individuales se citan
  por rol y contexto, no por nombre. Los voceros confirmados sí se
  nombran.
- Trazabilidad obligatoria en cada extracto: fuente concreta, fecha de
  acceso, confianza, tipo de hallazgo.
- Si una fuente no es accesible (404, login, render JS), lo dices
  explícitamente. No inventes.

## Cuándo escalar a herramientas adicionales

Si tras varios clientes detectas que necesitas:

- Procesar el blog completo del cliente (40–200 artículos en
  profundidad): considera un servicio de crawling de pago (Firecrawl,
  Tavily). Pendiente para v0.2.
- Voceros con mucha actividad histórica: pide la exportación voluntaria.
- Transcripciones que llegan sin diarización (sin marcas de hablante) y
  la reunión fue conjunta con varias voces: pídele al operador la
  grabación para una transcripción nueva con diarización, o procesa el
  bloque conjunto como input único y deja la diferenciación interna como
  hipótesis abierta.
