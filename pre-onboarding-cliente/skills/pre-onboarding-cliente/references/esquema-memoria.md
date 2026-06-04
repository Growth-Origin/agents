# Esquema del archivo de memoria del cliente (Knowledge Base)

> Pieza central del agente. NO es un volcado descartable: es el knowledge base
> persistente del cliente, con esquema estable (las secciones no cambian de
> cliente a cliente; cambia el contenido). Sirve a la vez como plantilla a
> rellenar y como contrato que leeran/actualizaran futuras reuniones y agentes.
>
> Nombre al rellenar: `memoria_[slug-cliente].md`.

## Convencion de trazabilidad (leer antes de rellenar)

Toda afirmacion factual lleva una etiqueta:

`‹fuente: URL | acceso: AAAA-MM-DD | confianza: alta/media/baja | tipo: hecho/interpretacion/hipotesis›`

- **confianza:** alta (fuente oficial directa), media (secundaria/indexada),
  baja (inferencia con poca evidencia).
- **tipo:** hecho (verificable en la fuente), interpretacion (lectura del
  agente), hipotesis (a confirmar en la entrevista).
- Lo no verificable NO se afirma: va a la seccion 13 (Huecos).

## Bloque de control (metadata)

```yaml
cliente_slug: ""
nombre_comercial: ""
fecha_creacion: ""            # AAAA-MM-DD
ultima_actualizacion: ""
version_memoria: "0.1"
creado_por: "Pre-Onboarding de Cliente v0.1"
estado: "borrador"            # borrador | revisado-por-humano | en-uso
revisado_por: ""
```

## 1. Identidad del cliente

Nombre legal, comercial, URL, pais HQ, mercados objetivo, idiomas de trabajo,
sector/categoria, descripcion en una frase (neutra, del agente).

- **Motivo y contexto del contacto** (input del operador): por que nos contacto
  el cliente, que busca, como llego (referido / inbound / outbound / evento).

## 2. Personas clave

> Identidad confirmada por humano antes de investigar a fondo.

Por persona: nombre, rol, identidad confirmada (si/no/dudosa), perfil(es)
publico(s) con URL+fecha, a entrevistar (si/no/a definir).

## 3. Posicionamiento y propuesta de valor (version oficial)

- Propuesta de valor y diferenciales declarados (cita literal + trazabilidad).
- ICP declarado: tamano de empresa, sectores, roles compradores, geografias.
- Producto/servicio: categoria, funcionalidades, integraciones, pricing.
- Social proof oficial: logos, casos con metricas, premios, prensa.
- Senales de paginas legales: subprocesadores, jurisdicciones, presencia real.

## 4. Marca y mensaje

- **Tono y estilo** de la comunicacion (formal, cercano, tecnico, provocador...).
- **Narrativa / historia** que cuenta la marca (origen, mision, "por que").
- **Identidad visual** a grandes rasgos (si es observable): estilo, consistencia.
- **Consistencia del mensaje** entre web, redes y materiales.
- **Vocabulario propio / claims que repite.**

## 5. Canales y presencia digital

> El pantallazo de marketing. Cubrir cada canal con: actividad, frecuencia,
> calidad aparente y senales de performance (lo publico). Marcar huecos.

### 5.1 SEO / GEO
- Visibilidad en buscadores para terminos de su categoria (impresion general).
- Visibilidad en LLMs (¿aparece el cliente cuando se pregunta por "best
  [categoria]" en Claude/ChatGPT/Perplexity? ¿antes o despues que competidores?).

### 5.2 Contenido (owned)
- Blog/recursos: temas dominantes, frecuencia, autores, idiomas.
- Newsletter / lead magnets / webinars si hay senales.

### 5.3 Redes sociales
- Plataformas activas (LinkedIn, Instagram, X, TikTok, YouTube, etc.).
- Por plataforma: frecuencia, formato dominante, engagement aparente, tono.
- ¿Donde concentran esfuerzo y donde estan ausentes?

### 5.4 Paid / publicidad (senales publicas)
- Anuncios visibles (display, social, search) si se detectan.
- Bibliotecas de anuncios publicas si aplican.

### 5.5 Email / owned audience (senales)
- Indicios de captura de leads, programas de referidos, comunidad.

## 6. Voz real del mercado

- Volumen y sentimiento en plataformas de resenas (G2, Capterra, Trustpilot...).
- Lenguaje real del mercado vs. jerga oficial.
- Objeciones y fricciones recurrentes (nº de menciones + cita anonimizada).
- Elogios recurrentes / diferenciales percibidos (a menudo distintos de los
  declarados).
- Casos de uso descubiertos fuera del ICP declarado.
- Noticias y prensa relevantes (financiacion, lanzamientos, fichajes).

## 7. Footprint del equipo

Por persona clave: temas dominantes, posturas defendidas, **gap personal vs.
corporate** (lo que defiende y NO esta en la comunicacion oficial — oro para la
entrevista), apariciones publicas destacadas con cita.

## 8. Contexto del nicho y competidores (superficial)

Categoria(s), 5-10 competidores (declarados/implicitos/ambientales) con una
frase de posicionamiento cada uno, dinamicas y vocabulario de la categoria.

## 9. Hipotesis a validar (lista viva)

Por hipotesis: enunciado, evidencia/contraevidencia, confianza, por que importa,
estado (abierta/validada/descartada — se actualiza tras la entrevista).

## 10. Incongruencias detectadas

Contradicciones directas entre la version oficial (sec. 3-5) y otras fuentes
(sec. 6-8): version A (cita+fuente), version B (cita+fuente), por que importa,
pregunta para resolver.

## 11. Diferenciales y oportunidades de marketing no explotados

Lo que el cliente podria destacar/hacer y no hace, apoyado en sec. 4-8. Cada uno
con enunciado, evidencia, implicacion estrategica, pregunta de validacion.

## 12. Riesgos para la relacion cliente-agencia

2-5 riesgos: enunciado, evidencia, implicacion para el trabajo, pregunta de
clarificacion si aplica.

## 13. Huecos de informacion (lo que NO se pudo verificar)

Lo que no se consiguio de fuentes publicas y hay que pedir o preguntar. Alimenta
directamente el pedido de documentacion y accesos.

## 14. Log de actualizaciones

| Fecha | Quien/que agente | Cambio |
|-------|------------------|--------|
| AAAA-MM-DD | Pre-Onboarding de Cliente v0.1 | Creacion inicial |
