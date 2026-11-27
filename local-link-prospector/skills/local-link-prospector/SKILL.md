---
name: local-link-prospector
description: "Prospector de enlaces y citaciones (citations) gratuitas para SEO y GEO local en España y LATAM. Úsala cuando el usuario aporte la URL de una ficha de Google Business Profile (Google My Business) o de una web local y quiera un mapa accionable de oportunidades gratuitas donde dar de alta el negocio: directorios generalistas, sectoriales, citaciones NAP y backlinks no-directorio (asociaciones, prensa local, patrocinios, listicles, gremios). Triggers: \"dónde doy de alta este negocio\", \"directorios para esta ficha\", \"links gratuitos para SEO local\", \"citations para Google My Business\", \"auditoría de citaciones\", \"link building local gratis\", \"qué directorios sectoriales aplican\". También cuando pegue una URL de GBP o web local y pida oportunidades de enlace. Output: análisis del negocio (sector, zona, NAP), tabla priorizada por capas diferenciando citations (ficha) vs backlinks (web), gap vs competencia, monitorización y un Excel checklist con branding Growth Origin.\n"
---

# Skill: Prospector de Enlaces y Citaciones Locales (SEO + GEO)

## Qué hace esta skill
A partir de **un solo input** (URL de ficha de Google Business Profile **o** URL de
una web local), genera un **mapa completo y priorizado** de todas las oportunidades
gratuitas (o de alta básica gratuita) donde el negocio debería aparecer para mejorar
su SEO local y su visibilidad en motores generativos (GEO). No da una lista genérica:
analiza **qué sector y qué zona** es el negocio y recomienda directorios generalistas,
**sectoriales**, citaciones NAP y oportunidades creativas de enlace, cruza con dónde
está la competencia, y entrega un **Excel accionable** tipo checklist.

### Decisión clave ya tomada (no volver a preguntar): ficha vs web
En SEO local hay **dos cosas distintas** y la skill SIEMPRE las separa:

1. **CITATIONS (citaciones NAP) → refuerzan la FICHA / la entidad.**
   Son menciones consistentes de Nombre + Dirección + Teléfono (+ Web) en directorios
   y plataformas. Pueden llevar enlace o no. Lo que importa es la **consistencia**.
   No se "enlaza a la ficha de GBP": se replica el NAP idéntico en muchos sitios para
   que Google confirme la entidad. Esto sube la **prominencia** en el Local Pack/Maps.

2. **BACKLINKS → refuerzan la WEB / la autoridad de dominio.**
   Enlaces reales hacia la URL del sitio (o landing local). Suben autoridad orgánica
   y ayudan a búsquedas fuera del Local Pack.

→ Por tanto el input GBP se usa para **extraer el NAP/sector/zona** y proponer sobre
todo **citations**; el input web se usa para proponer **citations + backlinks**.
La skill produce ambos bloques siempre, etiquetando cada fila con **DESTINO**
(`ficha` / `web` / `ambos`).

### Por qué también GEO, no solo SEO
Los motores generativos (ChatGPT, Gemini, Perplexity, AI Overviews) cruzan menciones
de marca en múltiples fuentes para decidir si eres una entidad fiable y citarte.
NAP consistente + presencia en directorios de autoridad + menciones en prensa/listicles
= más probabilidad de ser **citado** por una IA cuando alguien pregunta por ese
servicio en esa zona. La skill marca las oportunidades con alto valor GEO.

---

## FASE 0 — Briefing de Inputs

### Input OBLIGATORIO (uno de los dos basta)
```
<input_negocio>
  UNA de estas dos:
  - URL de la ficha de Google Business Profile / Google Maps del negocio, O
  - URL de la web local del negocio.
</input_negocio>
```

### Inputs OPCIONALES (mejoran mucho el resultado)
```
<competidores>      1-5 URLs (web o ficha) de competidores que ya rankean bien.
<pais_zona>         País + ciudad/provincia/barrio (si no se deduce del input).
<sector_detalle>    Subnicho concreto si el genérico no basta.
<nap_oficial>       NAP canónico exacto si el usuario lo tiene fijado.
<idioma>            es / ca / pt… (default es).
```

Si falta el input obligatorio, **pídelo**. Si solo falta opcional, sigue y dedúcelo.

---

## FASE 1 — Análisis del negocio (extracción)

Objetivo: saber **quién es, dónde está y a qué sector pertenece**.

1. **Lee el input.**
   - Si es URL de web → `web_fetch` de la home + páginas de contacto/servicios.
     Extrae: nombre, NAP, sector, servicios, ciudades/zonas que cubre, idioma,
     si tiene varias sedes.
   - Si es URL de ficha GBP/Maps → `web_fetch` y/o `web_search` del nombre del
     negocio para extraer NAP, categoría principal y secundarias, zona.
     (Si la ficha no es fetchable directamente, busca el nombre + ciudad.)

2. **Determina el NAP canónico.** Si el usuario lo dio, úsalo. Si no, propón uno y
   avisa de que la consistencia exacta (mismo formato de calle, mismo teléfono) es
   crítica: una sola variación reduce la señal de confianza de Google.

3. **Clasifica el sector** en una de las categorías de la base sectorial
   (`references/directory-database.md`, Capa 3) + subnicho. Detecta si es:
   B2C local puro / B2B / con e-commerce / multisede / YMYL (salud, legal,
   finanzas → exige más E-E-A-T).

4. **Determina país + zona** (España o país LATAM concreto + ciudad/provincia).
   Esto filtra qué generalistas y qué directorios locales aplican.

5. **Resume el perfil** en 4-6 líneas antes de prospectar. Confirma con el usuario
   solo si algo crítico es ambiguo (p. ej. sector dudoso); si no, continúa.

---

## FASE 2 — Prospección por capas (núcleo de la skill)

Carga `references/directory-database.md`. Construye candidatas combinando la base
curada **filtrada** por sector + país + zona, MÁS búsqueda en vivo para ampliar.

### 2.1 — Filtra la base curada
Selecciona de cada capa lo que aplica:
- **Capa 1 (universal)**: casi siempre todas.
- **Capa 2 / 2b (generalistas ES o LATAM según país)**.
- **Capa 3 (sectoriales)**: SOLO las del sector del negocio. **Máxima prioridad.**
- **Capa 4 (oportunidades creativas)**: las que encajen con el modelo de negocio.

### 2.2 — Amplía en vivo (búsqueda)
Haz búsquedas dirigidas para descubrir lo que NO está en la base (directorios
locales de ese municipio, sectoriales de nicho, listicles donde quieres estar):
- `[tipo de negocio] directorio [ciudad/país]`
- `mejores [tipo de negocio] [ciudad]`  → los listicles que rankean = donde quieres aparecer (pitch)
- `[sector] asociación / gremio / colegio profesional [país]`
- `directorio empresas [municipio]` / `ayuntamiento [municipio] empresas`
- `[sector] prensa local [ciudad]` para oportunidades de mención
Escala: 5-12 búsquedas según riqueza del nicho. Para nichos ricos, más.

### 2.3 — Gap competitivo (si hay competidores)
Para cada competidor aportado:
- `[nombre competidor] [ciudad]` y revisa en qué directorios/listicles aparece.
- Busca su marca para detectar citaciones que el cliente NO tiene → **gap = prioridad alta**.
Regla: si la competencia que rankea está en un sitio, el cliente debería estar.

---

## FASE 3 — Puntuación y priorización

Puntúa cada oportunidad (0-100) combinando:
- **Relevancia sectorial/geográfica** (peso alto)
- **Autoridad** del dominio (orientativa)
- **¿Trae tráfico real?** (si no, penaliza fuerte)
- **Tipo de enlace** (dofollow suma; nofollow no penaliza, es natural)
- **Esfuerzo de alta** vs valor (ratio)
- **Gap competitivo** (si la competencia está y el cliente no → +)
- **Valor GEO** (¿lo citan/indexan los LLMs? prensa, listicles, Wikipedia)

Asigna a cada fila:
- **PRIORIDAD**: 🔴 Imprescindible / 🟠 Recomendado / 🟡 Oportunista
- **DESTINO**: ficha / web / ambos
- **TIPO**: citation / backlink / mixto
- **FASE DE EJECUCIÓN**: Semana 1 (universal + NAP) → Mes 1 (sectoriales + gap) →
  Mes 2-3 (creativas: prensa, patrocinios, listicles).

Aplica los **ANTI-PATRONES** de la base: descarta granjas, PBNs y directorios sin
tráfico, y avisa de que esto NO es una fábrica de enlaces (riesgo de spam de Google).

---

## FASE 4 — Verificación en vivo (HÍBRIDO)

No se verifica todo (lento). Se verifica **solo las candidatas TOP** (las 🔴 y las
🟠 de mayor puntuación, ~15-25 fuentes):

Para cada una, `web_fetch` o `web_search` para confirmar:
1. **Sigue existiendo** y funciona.
2. **Permite alta gratuita** (o freemium con perfil base gratis).
3. Tiene **versión del país correcto** (LATAM: cada país su dominio).
4. Localiza la **URL exacta de alta** ("añadir empresa / anuncia tu negocio").

Marca el resultado de verificación en el Excel (✅ verificado / ⚠️ revisar / ❌ caído).
Las no verificadas quedan como "candidata sin verificar" con nota.

---

## FASE 5 — Plan de monitorización

Define cómo se mantiene vivo (el usuario pidió "trabajo de monitorización"):
- **Consistencia NAP**: revisar trimestralmente que el NAP sigue idéntico en las altas
  hechas (herramientas: Moz Local free check, BrightLocal trial, DinoRank/Localo si
  los tiene). Recomiéndalas como opciones, no como obligación.
- **Nuevas citaciones de la competencia**: re-ejecutar el gap competitivo cada 2-3 meses.
- **Estado de altas**: columna en el Excel para marcar Pendiente / Solicitada / Publicada / Indexada.
- **Menciones de marca (GEO)**: sugerir Brand24/Mention/Google Alerts y comprobar
  manualmente en Perplexity/ChatGPT si el negocio ya aparece para sus prompts clave.
- Propón un **ciclo de revisión** (p. ej. cada 60-90 días) y qué mirar en cada uno.

---

## FASE 6 — Entregable: Excel accionable (checklist)

El entregable principal es un **Excel** con branding Growth Origin. Antes de generarlo,
**lee la skill de xlsx** (`/mnt/skills/public/xlsx/SKILL.md`) y síguela.

Estructura del Excel:

**Hoja 1 — "Resumen"**
- Datos del negocio (nombre, NAP canónico, sector, zona, país).
- GEO Local Readiness: nº de oportunidades por prioridad y por destino (ficha/web).
- Leyenda de prioridades, tipos y destinos.
- Roadmap por fases (Semana 1 / Mes 1 / Mes 2-3).

**Hoja 2 — "Plan de altas" (la checklist accionable)** — columnas:
Prioridad | Fuente | URL de alta | Tipo (citation/backlink/mixto) | Destino (ficha/web/ambos) | Capa | Sector/Geo | Dofollow? | Coste | Valor GEO | Verificado | Estado | Notas/anchor sugerido

Una fila por oportunidad, ordenadas por prioridad. La columna **Estado** con validación
de datos (Pendiente / Solicitada / Publicada / Indexada) para que sea un checklist real.

**Hoja 3 — "Gap competidores"** (si hubo competidores)
- Dónde está cada competidor, dónde NO está el cliente, acción.

**Hoja 4 — "Monitorización"**
- Calendario de revisión, qué comprobar, herramientas sugeridas.

**Hoja 5 — "NAP canónico"**
- El NAP exacto a copiar/pegar IDÉNTICO en todas las altas (la regla de consistencia).

Branding Growth Origin: paleta navy/coral (o navy/indigo), nombre en cabecera de
Resumen, pie con "Growth Origin · GEO & SEO Local". Reusa el patrón de las otras
skills de la cuenta.

Guarda en `/mnt/user-data/outputs/` y preséntalo con `present_files`.

---

## Resumen del flujo
1. Recibe URL (GBP o web). 2. Extrae NAP + sector + zona. 3. Filtra base curada +
amplía en vivo + gap competitivo. 4. Puntúa y prioriza (ficha vs web). 5. Verifica
en vivo solo las top. 6. Define monitorización. 7. Entrega Excel checklist Growth Origin.

## Principios
- **Citations → ficha; backlinks → web.** Siempre separados y etiquetados.
- **Sectorial > generalista.** El mayor valor está en estar donde el usuario espera.
- **Calidad > cantidad.** 10-20 altas buenas. Esto NO es una fábrica de enlaces.
- **NAP idéntico** en todas partes. Una variación rompe la señal.
- **Adaptar a país** (ES vs LATAM: dominios distintos por país).
- **Valor GEO**: prensa, listicles y menciones que los LLMs citan cuentan doble.
