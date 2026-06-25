# Guía de dimensionado — Fase 1 (ICP Definer, Agente 3)

> Cómo decides **cuántos** ICP/personas hacen falta antes de construir, con criterio
> explícito de cuándo separar y cuándo fusionar, y la persona negativa obligatoria.
> Idioma: español de España (peninsular).

## Principio

Más no es mejor. El objetivo es el **mínimo conjunto que cubra el grueso del valor**.
Regla de referencia: **3–5 personas suelen cubrir el ~80%** de la audiencia objetivo;
y si el ticket es bajo o el negocio es simple, **1 ICP + 1 persona ligera** supera a un
deck de 30 páginas que nadie usa. **La complejidad es enemiga de la ejecución.**

El agente **propone** el número y lo **justifica**; el consultor valida (checkpoint de
la Fase 1). No se construye ningún perfil hasta tener ese OK.

## Las cinco preguntas para dimensionar

Se responden cruzando el CKB, el Agente 2.1 (mercado), el 2.2 (competidores) y el
input del cliente:

1. **¿Cuántos segmentos de demanda distintos hay?** (del Agente 2.1) — segmentos con
   lenguaje, intención o necesidad claramente diferentes justifican personas separadas.
2. **¿Cuántos modelos de negocio sirve el cliente?** (del CKB) — B2B y B2C simultáneos
   = al menos un perfil por cada uno.
3. **¿Hay comité de compra?** (B2B) — varios roles que deciden juntos = una persona por
   rol relevante (decisor, influenciador, usuario, bloqueador).
4. **¿Los JTBD son distintos entre segmentos?** — si dos grupos «contratan» el producto
   para progresos distintos, son personas distintas. Si es el mismo job, quizá es una
   sola.
5. **¿El cliente tiene capacidad de producir contenido para N perfiles?** — restricción
   operativa real: mejor **2 personas bien servidas que 5 desatendidas**.

## Criterio de decisión: separar o fusionar

Dos perfiles merecen **separarse solo si difieren en al menos uno** de estos cuatro
ejes:

- el **job principal** (JTBD),
- el **lenguaje de búsqueda/prompt**,
- las **objeciones clave**,
- la **etapa de madurez**.

Si comparten los cuatro, **se fusionan**. El agente expone, por cada par de perfiles
candidatos, en cuál de los cuatro ejes difieren (o que no difieren en ninguno) para
justificar la decisión.

## La persona negativa (obligatoria)

El agente **siempre** define al menos una **persona negativa**: a quién **NO** nos
dirigimos. En SEO/GEO es crítico, no opcional: sin ella, el equipo persigue todas las
keywords de alto volumen y atrae tráfico que no convierte (el clásico «rankear para
‹qué es un CRM› y recibir estudiantes, no compradores»). La persona negativa es lo que
permite **descartar keywords y prompts** que traen volumen pero no valor, y alimenta el
**filtro anti-persona** de la Fase 3.

La persona negativa se describe con lo mínimo para reconocerla: quién es, por qué
parece encajar pero no encaja, y las señales/keywords que la delatan.

## Salida de la Fase 1 (`propuesta_perfiles.md`)

```markdown
# Propuesta de perfiles — [Cliente]

**Modelo:** B2B / B2C / B2B2C
**Nº de perfiles propuesto:** [N] + 1 persona negativa

## Perfiles propuestos (ordenados por prioridad)
1. [Nombre del perfil] — primario — [una línea: a quién representa y por qué primario]
2. [Nombre del perfil] — [una línea]
...

## Persona negativa
- [Nombre] — [por qué parece encajar y por qué se descarta]

## Justificación del número
- Segmentos de demanda (2.1): ...
- Modelos de negocio (CKB): ...
- Comité de compra (B2B): ...
- JTBD distintos: ...
- Capacidad de producción del cliente: ...
- Pares fusionados y por qué: ...

## Checkpoint
¿Validas o ajustas este número de perfiles antes de construir?
```

Tras mostrarla, el agente pregunta *«¿Validas o ajustas este número de perfiles antes
de construir?»* y **espera el OK**. El consultor puede añadir/quitar; el agente acata y
lo registra en `audit/execution_log.json`.
