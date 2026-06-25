# Plantillas de outputs accionables — Fase 3 (ICP Definer, Agente 3)

> La **capa puente**: no entregas «fichas de persona bonitas», entregas un artefacto
> con el que se trabaja. Cada output nombra su **agente destino**. Idioma: español de
> España (peninsular). Todo va en `outputs_accionables.md`.

## 5.1 Mapa de priorización de perfiles

Tabla con los N perfiles ordenados por valor (**encaje x tamaño x accesibilidad**),
señalando el **primario** (donde se concentra el esfuerzo inicial). Incluye la persona
negativa.

```markdown
| Perfil | Tipo | Encaje | Tamaño | Accesibilidad | Prioridad | Notas |
|--------|------|--------|--------|---------------|-----------|-------|
| [Nombre] | primario | alta | medio | alta | 1 | ... |
| [Nombre] | secundario | media-alta | grande | media | 2 | ... |
| [Nombre negativo] | NEGATIVO | — | — | — | descartar | a quién no perseguir |
```

«Encaje», «tamaño» y «accesibilidad» se puntúan con criterio cualitativo (alta /
media / baja) anclado en datos; si una columna depende de un dato Nivel 2+ no
disponible, se marca y se nota qué herramienta la completaría.

## 5.2 Matriz persona x etapa x intención → contenido/prompt (el entregable más accionable)

Por cada persona (no la negativa) y cada etapa del funnel:

```markdown
| Persona | Etapa | Intención | Firma de prompt / keyword | Tipo de contenido | Agente destino |
|---------|-------|-----------|---------------------------|-------------------|----------------|
| [primaria] | Descubrimiento | Informacional | "cómo formula el problema" | guía / explicativo | Contenido (3) |
| [primaria] | Consideración | Comparativa | "X vs Y para [caso]" | comparativa / tabla | Contenido (3) |
| [primaria] | Decisión | Transaccional | "mejor [solución] para [contexto]" | landing / caso | Estrategia (2) |
```

Es lo que el agente de Contenido y el de Estrategia consumen para **priorizar y
calibrar** cada pieza. La columna «Firma de prompt / keyword» usa el lenguaje real de
la persona, no etiquetas genéricas.

## 5.3 Filtro de descalificación (keyword/prompt anti-persona)

Lista **explícita** de keywords/prompts a **evitar** porque atraen a la persona
negativa: alto volumen, baja conversión. Va directo a Estrategia para depurar el
pipeline de keywords.

```markdown
| Keyword / prompt a evitar | Por qué atrae a la persona negativa | Señal de que es trampa de volumen |
|---------------------------|--------------------------------------|-----------------------------------|
| "qué es [término genérico]" | trae estudiantes/curiosos, no compradores | volumen alto, intención informacional pura |
```

## 5.4 Conclusiones accionables → agentes downstream

Cada conclusión es **afirmación verificable y autocontenida**, no observación vaga.
«La persona primaria formula sus prompts pidiendo comparativas para su sector concreto;
priorizar contenido comparativo» es accionable; «conocer al cliente» no lo es.

```markdown
| Conclusión accionable | Agente destino |
|-----------------------|----------------|
| Perfil primario y orden de prioridad | Estrategia (Capa 2) |
| Matriz persona x etapa x intención | Contenido (Capa 3) |
| Firmas de prompt por persona | Prompts GEO · Contenido |
| Lenguaje real / vocabulario por persona | Contenido (Capa 3) |
| Objeciones a resolver en contenido | Contenido (Capa 3) |
| JTBD y disparadores por persona | Estrategia · Contenido |
| Filtro anti-persona (keywords a evitar) | Estrategia (Capa 2) |
| Canales/plataformas por persona | Estrategia (Capa 2) |
```

Cada fila debe poder leerse sin abrir el resto del documento. Si una fila depende de un
dato Nivel 2+ aún no disponible, se incluye igual con la nota de qué herramienta la
completará.

## ICP estructurado (JSON) — recomendado en Nivel 2

Para consumo automático de Estrategia y Contenido. Esquema orientativo:

```json
{
  "cliente": "slug",
  "version": "0.1",
  "fecha": "AAAA-MM-DD",
  "modelo": "B2B|B2C|B2B2C",
  "perfil_primario": "nombre",
  "perfiles": [
    {
      "nombre": "...",
      "tipo": "primario|secundario|negativo",
      "icp": { "firmograficos_o_segmento": "...", "trigger_events": ["..."], "descalificacion": ["..."] },
      "persona": { "rol": "...", "rol_decision": "...", "objeciones": ["..."], "lenguaje_real": ["..."] },
      "jtbd": { "statement": "...", "funcional": "...", "emocional": "...", "social": "...", "outcome": "..." },
      "geo_seo": { "firma_prompt": ["..."], "funnel": "...", "intencion": "...", "canales": ["..."], "temas_alto_valor": ["..."] }
    }
  ],
  "filtro_anti_persona": ["keyword/prompt a evitar"]
}
```
