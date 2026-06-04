# Plantilla de input (Paso 0 — toma de datos)

Campos FIJOS que el agente recoge siempre al iniciar, en el mismo orden y con la
misma redaccion. No se improvisan campos distintos en cada ejecucion. Si el
operador ya aporto algunos en su mensaje, se preguntan solo los que falten —
pero los obligatorios y el motivo del contacto se cubren siempre antes de
investigar.

## Campos

```yaml
# --- Obligatorios ---
url_principal: ""                # URL de la web del cliente
personas_a_entrevistar:          # al menos una
  - nombre: ""
    rol: ""
    linkedin_url: ""             # opcional; si no esta, el agente lo busca

# --- Importante (no omitir) ---
motivo_y_contexto_del_contacto: ""
# ¿Por que nos contacto el cliente? ¿Que busca? ¿Como llego
# (referido / inbound / outbound / evento)? Esto orienta toda la preparacion;
# sin esto, el resumen no deberia "preguntar para que nos escribio".

# --- Opcionales (suman si estan) ---
nombre_comercial: ""
pais_hq: ""
mercados_objetivo: []            # ej. ["ES", "IT"]
sector_o_categoria: ""
fecha_objetivo_reunion: ""
quienes_asisten_a_la_reunion: "" # "solo founder" / "founder+mkt+ventas" / "a definir"
notas_libres: ""
```

## Reglas de la toma de datos

- Presentar todos los campos juntos, en un solo paso (formulario o lista clara).
- Minimo para arrancar: `url_principal` + una persona en `personas_a_entrevistar`.
- `motivo_y_contexto_del_contacto` se pregunta SIEMPRE, aunque sea breve.
- Lo opcional que no se aporte no bloquea: se marca como hueco si hace falta.
