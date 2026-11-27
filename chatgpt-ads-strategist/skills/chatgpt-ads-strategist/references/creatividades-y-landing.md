# Creatividades y landing

## 1. Principio: el anuncio continúa la conversación

El anuncio aparece debajo de una respuesta de ChatGPT. El usuario acaba de leer algo útil; el anuncio tiene que parecer el siguiente paso lógico, no una interrupción.

| Conversación | ✅ Coherente | ❌ Desconectado |
|---|---|---|
| "¿Cuánto vale mi piso en Sarrià?" | "Valora tu piso en Sarrià" | "Líderes inmobiliarios desde 1997" |
| "¿Qué agencia GEO me recomiendas?" | "Auditoría GEO de tu marca" | "Agencia de marketing 360" |
| "¿Me conviene alquiler temporal?" | "Calcula tu rentabilidad" | "Gestionamos tu patrimonio" |

## 2. Longitudes

Verifica siempre los límites vigentes en `estado-plataforma.md`. A fecha de la foto: título recomendado 16-24 caracteres y copy 32-48 (🟢), con máximos reportados de 50 y 100 (🟡). Escribe a la recomendación y valida con:

```bash
python3 scripts/calculadora.py anuncios anuncios.json
```

Formato del JSON: lista de objetos `{"ad_group": "...", "titulo": "...", "copy": "..."}`.

## 3. Ángulos creativos

Genera 3-5 variantes por ad group combinando ángulos distintos para poder aprender cuál funciona.

| Ángulo | Cuándo usarlo | Ejemplo (título / copy) |
|---|---|---|
| PROBLEM-LED | Intención PROBLEM o SOLUTION | "¿Tu piso no se vende?" / "Descubre qué frena la venta y cómo corregirlo." |
| SOLUTION-LED | SOLUTION, BUY | "Valora tu piso gratis" / "Estimación con datos reales de tu barrio." |
| COMPARISON-LED | COMPARE | "¿Agencia o por tu cuenta?" / "Compara costes, plazos y riesgos antes de decidir." |
| PROOF-LED | VALIDATE (solo con pruebas reales) | "[Dato real verificable]" / "[Prueba real: reseñas, casos, años]" |
| OFFER-LED | BUY, con oferta real | "Valoración en 48 h" / "Sin compromiso. Te llamamos y te lo explicamos." |
| LOCAL-LED | Servicios locales | "Expertos en Sant Gervasi" / "Conocemos los precios reales de tu calle." |

## 4. Reglas de redacción

- Habla de lo que el usuario quiere conseguir, no de la empresa.
- Beneficio concreto y verbo de acción; nada de superlativos vacíos.
- Refleja el vocabulario de la conversación objetivo (si preguntan "cuánto vale", no escribas "tasación patrimonial").
- Idioma de la conversación objetivo; en España valora castellano y, si procede, catalán en ad groups separados.
- Una sola idea por anuncio.
- Nunca inventes cifras, reseñas, premios, plazos ni ofertas. Los PROOF-LED y OFFER-LED solo con datos que el usuario confirme.
- Revisa las Ads Policies para claims en sectores regulados (salud, finanzas, seguros).
- Imagen: cuadrada, un objeto o escena simple, legible en miniatura; sin texto pequeño.

## 5. Continuidad semántica

Evalúa la cadena completa en cada ad group:

```
CONVERSACIÓN → CONTEXT HINT → ANUNCIO → LANDING → CONVERSIÓN
```

Preguntas de control:
1. ¿El hint describe la misma intención que la conversación objetivo?
2. ¿El anuncio responde a esa intención con las mismas palabras clave de significado?
3. ¿La landing cumple en su primer pantallazo lo que promete el anuncio?
4. ¿La conversión pedida es el siguiente paso natural para ese nivel de intención? (A un usuario en COMPARE quizá le encaje mejor una guía o una calculadora que "pide una demo".)

Si un eslabón se rompe, arréglalo antes de lanzar. Esto además importa para la subasta: 🟢 la landing, el título y el copy son señales del matching.

## 6. Auditoría de landing

Revisa y puntúa (OK / Mejorable / Crítico):

| Elemento | Qué mirar |
|---|---|
| Message match | ¿El H1 repite la promesa del anuncio? |
| Claridad | ¿Se entiende en 5 segundos qué ofrece y para quién? |
| Propuesta de valor | ¿Por qué esta opción y no otra? |
| CTA | ¿Uno principal, visible sin scroll en móvil? |
| Fricción | ¿Pasos, campos o pop-ups innecesarios? |
| Formulario | ¿Pide solo lo necesario para cualificar? |
| Confianza | Reseñas, logos, certificaciones, datos de contacto reales |
| Prueba social | Casos y testimonios reales |
| Velocidad | Core Web Vitals en móvil |
| Mobile | La mayor parte del uso de ChatGPT Free es móvil (🔵 verificar con datos propios) |
| Información solicitada | ¿Coherente con el ticket y la intención? |

Cuando la landing actual no sirva (home genérica, página sin CTA, intención distinta), recomienda una específica.

## 7. Blueprint de landing específica

```
HEADLINE      Promesa del anuncio, con las palabras de la conversación
SUBHEADLINE   Para quién es y qué obtiene, en una frase
PROOF         Pruebas reales (reseñas, cifras verificables, casos)
BENEFITS      3-5 beneficios concretos ligados a la situación del comprador
CTA           Una acción principal, repetida tras cada bloque
FORMULARIO    Mínimos campos; campo de cualificación si el ticket lo exige
FAQ           Las objeciones reales de esa Buyer Situation
```

Añade UTMs a la URL final y verifica que el píxel dispara en la página de gracias o en el evento correspondiente. Si hay que construir la landing a fondo (estructura, copy, schema), la skill `local-landing-architect` puede encargarse.
