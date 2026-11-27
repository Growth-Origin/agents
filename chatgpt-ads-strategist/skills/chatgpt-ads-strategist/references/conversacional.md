# Método conversacional: de ICP a context hints

## Índice
1. ICP situacional
2. Buyer Situations
3. Conversation Map
4. Intent Classification
5. Opportunity Score
6. Context hints
7. Framework BROAD / MEDIUM / HIGH
8. Arquitectura de campañas
9. Ejemplo completo (inmobiliaria en Barcelona)

---

## 1. ICP situacional

Un ICP demográfico ("hombre de 45 años, empresario de Barcelona") no sirve para ChatGPT Ads porque el sistema no empareja por perfil: empareja por conversación. Completa siempre estas preguntas:

| Dimensión | Pregunta |
|---|---|
| Situación | ¿Qué está pasando en su vida o negocio? |
| Necesidad | ¿Qué necesita conseguir? |
| Problema | ¿Qué le frena o le preocupa? |
| Trigger | ¿Qué evento ha disparado la búsqueda? (herencia, ronda de inversión, cambio normativo, avería, mudanza…) |
| Urgencia | ¿Tiene fecha límite? |
| Alternativas | ¿Qué otras opciones está valorando? (competidores, hacerlo solo, no hacer nada) |
| Momento de compra | ¿Está aprendiendo, comparando o a punto de decidir? |

## 2. Buyer Situations

Una Buyer Situation describe lo que está ocurriendo y hace relevante la solución.

- ❌ "Propietarios de pisos de Barcelona."
- ✅ "Propietario de un piso en Barcelona que está pensando en venderlo y quiere saber cuánto podría obtener hoy."
- ✅ "Propietario que duda entre alquiler tradicional y temporal y quiere saber qué opción da más rentabilidad con menos riesgo."

Genera entre 5 y 15. Formato recomendado para cada una:

`[Quién] + [qué le pasa / qué ha ocurrido] + [qué quiere saber o conseguir]`

Fuentes para descubrirlas: la web del cliente (FAQs, casos de éxito, objeciones), el equipo comercial ("¿qué te preguntan en la primera llamada?"), el CRM (motivos de contacto), Search Console (consultas largas), estudios de prompts GEO y foros o Reddit del sector.

## 3. Conversation Map

Para cada situación, escribe 5-10 conversaciones naturales que esa persona tendría con ChatGPT. Piensa en cómo habla la gente con un asistente: frases completas, contexto personal, dudas encadenadas.

Ejemplo — situación "propietario que piensa vender":

- "¿Cuánto vale ahora un piso de 120 m² en el Eixample?"
- "¿Es buen momento para vender vivienda en Barcelona?"
- "¿Qué comisión suele cobrar una inmobiliaria?"
- "¿Me conviene vender por mi cuenta o con agencia?"
- "¿Qué inmobiliarias son buenas para vender un piso en Barcelona?"
- "¿Cómo vendo mi piso sin tener que bajar mucho el precio?"
- "¿Cuánto se tarda en vender un piso en Sarrià?"

Recuerda que la conversación puede empezar lejos (una duda fiscal, una herencia) y acercarse a la compra varios turnos después. Incluye esos recorridos cuando sean típicos del sector.

## 4. Intent Classification

| Nivel | Estado | Señal típica en la conversación |
|---|---|---|
| EXPLORE | Aprende | "qué es", "cómo funciona", "tendencias" |
| PROBLEM | Reconoce un problema | "no consigo…", "tengo un problema con…" |
| SOLUTION | Busca cómo resolverlo | "cómo puedo…", "qué opciones hay para…" |
| COMPARE | Compara alternativas | "X o Y", "mejor opción para…", "diferencias entre…" |
| VALIDATE | Verifica proveedor o decisión | "¿es fiable X?", "opiniones de…", "¿merece la pena?" |
| BUY | Cerca de actuar | "precio", "presupuesto", "contratar", "cerca de mí", "dónde reservar" |

Simplificación: EXPLORE/PROBLEM = LOW · SOLUTION/COMPARE = MEDIUM · VALIDATE/BUY = HIGH.

Con objetivo de performance, empieza por HIGH y MEDIUM. Reserva LOW para awareness o para cuando HIGH no tenga volumen suficiente.

## 5. Opportunity Score

Puntúa cada Buyer Situation de 1 a 5:

| Criterio | 1 | 5 |
|---|---|---|
| Intención | Curiosidad | A punto de contratar |
| Volumen | Situación rara | Situación muy frecuente |
| Fit | Encaje parcial con la oferta | Encaje exacto |
| Valor | Ticket bajo | Ticket o LTV alto |
| Facilidad de conversión | Requiere mucha educación | Conversión directa con la landing actual |

Opportunity Score = media ponderada (por defecto: intención ×1,5, valor ×1,2, resto ×1). Calcúlalo con `scripts/calculadora.py score`. El volumen es estimación cualitativa (🔵): no existe hoy un dato público de volumen de conversaciones por tema.

Arranca con las 2-4 situaciones con mejor puntuación que además tengan landing coherente o una fácil de crear.

## 6. Context hints

### Qué son (🟢)
Descripciones a nivel de ad group de las conversaciones, temas o keywords donde la oferta es relevante. Orientan el matching, pero no son concordancia exacta ni garantizan la entrega.

### Fórmula de referencia
**WHO + SITUATION + PROBLEM + INTENT + SOLUTION FIT**. No hace falta incluir los cinco literalmente; sí que el conjunto describa un momento de compra reconocible.

### Buenos ejemplos
- "Propietarios de viviendas en Barcelona que están valorando vender su inmueble y quieren saber su valor actual, cuánto podrían obtener y si les compensa trabajar con una agencia inmobiliaria."
- "Propietarios de Barcelona que comparan alquiler tradicional y alquiler temporal para decidir qué modalidad les da más rentabilidad y encaja mejor con su situación."
- "Responsables de marketing de empresas B2B españolas que quieren que su marca aparezca recomendada en ChatGPT, Perplexity o Gemini y buscan una agencia especializada en GEO."

### Antipatrones
- ❌ Listas de keywords: "inmobiliaria barcelona, vender piso, tasación".
- ❌ Hints genéricos: "gente interesada en el mercado inmobiliario" (🟡 causa frecuente de baja entrega: pierden la subasta frente a hints mejor acotados).
- ❌ Párrafos sobreoptimizados con diez intenciones distintas: diluyen el ad group.
- ❌ Instrucciones de segmentación o exclusión dentro del hint ("no mostrar a…").
- ❌ Características personales sensibles (salud, religión, orientación, situación financiera delicada).
- ❌ Claims no respaldados por la web o por el usuario.

### Reglas prácticas
- Un tema o intención coherente por ad group; varios hints dentro del grupo pueden describir la misma intención con matices distintos (🔵 el número óptimo no está demostrado; empieza con 3-5).
- Aporta información que no esté ya en el copy: la situación, el caso de uso, la razón de encaje.
- Deja margen semántico: la gente expresa la misma necesidad con palabras distintas.
- Escribe en el idioma de las conversaciones objetivo.
- Si la información no basta para un hint útil, pregunta antes de inventar.

### Checklist por hint
- [ ] ¿Describe un comprador en un momento, no una palabra clave?
- [ ] ¿Se entiende qué problema tiene y qué quiere hacer?
- [ ] ¿Encaja con el anuncio y la landing del mismo ad group?
- [ ] ¿Todo lo que afirma es cierto para esta oferta?
- [ ] ¿Es lo bastante específico para ganar relevancia y lo bastante abierto para recibir volumen?

## 7. Framework BROAD / MEDIUM / HIGH

| Nivel | Contenido del hint | Ejemplo |
|---|---|---|
| BROAD | Situación general | "Propietarios interesados en entender el mercado inmobiliario de Barcelona." |
| MEDIUM | Problema + solución | "Propietarios de Barcelona que estudian cuánto podrían obtener vendiendo o alquilando su vivienda." |
| HIGH | Problema + intención comercial clara + solución | "Propietarios de viviendas en Barcelona que buscan una agencia inmobiliaria para valorar y vender su propiedad." |

Reparto orientativo (🔵) con objetivo de leads: HIGH 50-60 %, MEDIUM 30-40 %, BROAD 0-10 % (solo si hay presupuesto de sobra o HIGH no entrega). Con objetivo awareness, invierte el peso. Pruébalos como ad groups separados con el mismo anuncio y la misma landing para aislar el efecto del hint.

## 8. Arquitectura de campañas

```
CAMPAIGN (objetivo, país, presupuesto)
└── AD GROUP (una hipótesis conversacional, una puja)
    ├── CONTEXT HINTS (3-5 sobre la misma intención)
    ├── ADS (3-5 variantes de ángulo)
    └── LANDING (una, coherente con la intención)
```

Separa **campañas** cuando cambia: objetivo, producto, mercado/país, economía (ticket muy distinto) o tipo de conversión.
Separa **ad groups** por hipótesis conversacional.

Regla de presupuesto: cada ad group necesita volumen suficiente para aprender (ver `scripts/calculadora.py presupuesto`). Si el cálculo da menos grupos de los que querías, fusiona hipótesis cercanas o deja las de menor score para la segunda ola.

Nomenclatura recomendada: `[País]_[Producto]_[Objetivo]` para campañas y `AG[nº]_[Situación]_[Nivel intención]` para ad groups. Ejemplo: `ES_ValoracionVivienda_Leads` / `AG01_ValorarPiso_HIGH`.

## 9. Ejemplo completo (inmobiliaria en Barcelona, objetivo leads)

CAMPAIGN `ES_Propietarios_Leads`

| Ad group | Hipótesis | Intención | Landing |
|---|---|---|---|
| AG01 Valoración vivienda | Quien pregunta por el valor de su piso convierte mejor que quien pregunta por el mercado | HIGH | /valoracion-vivienda-barcelona |
| AG02 Vender vivienda | Quien duda entre vender solo o con agencia está cerca de contactar | HIGH | /vender-piso-barcelona |
| AG03 Comparar inmobiliarias | Quien compara agencias necesita prueba y diferenciación | VALIDATE | /por-que-elegirnos |
| AG04 Alquiler tradicional vs temporal | Quien compara modalidades valora asesoramiento | COMPARE | /gestion-alquiler |

Con presupuesto ajustado, lanza solo AG01 y AG02 y deja AG03-AG04 para cuando haya datos.
