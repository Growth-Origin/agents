"""Evalúa un Excel de keywords con Jev (typesafe-ai/jev) vía Vercel AI Gateway.

Modos:
  --inspeccionar   Muestra hojas, columnas y filas de ejemplo (no gasta créditos).
  --dry-run        Construye los states y estima el tamaño/coste (no gasta créditos).
  (por defecto)    Evalúa cada fila y guarda <excel>_jev.xlsx con columnas nuevas.

Requiere AI_GATEWAY_API_KEY en el entorno (proceso o variable de usuario de Windows).
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import openpyxl
import openpyxl.styles
import openpyxl.utils

ENDPOINT = "https://ai-gateway.vercel.sh/typesafe/v1/systemone"
CREDITS = "https://ai-gateway.vercel.sh/v1/credits"
MODEL = "typesafe-ai/jev"
KEYWORD_COL = re.compile(r"^(keyword|keywords|kw|palabra[s]? clave|query|t[ée]rmino|b[úu]squeda)$", re.I)
DEFAULT_QUESTIONS = Path(__file__).resolve().parent.parent / "preguntas.json"

sys.stdout.reconfigure(encoding="utf-8")


def api_key():
    key = os.environ.get("AI_GATEWAY_API_KEY")
    if not key and os.name == "nt":
        import winreg

        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as k:
                key = winreg.QueryValueEx(k, "AI_GATEWAY_API_KEY")[0]
        except OSError:
            pass
    if not key:
        sys.exit("Falta AI_GATEWAY_API_KEY (ni en el proceso ni en las variables de usuario).")
    return key


def read_rows(path, sheet):
    wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
    ws = wb[sheet] if sheet else wb.worksheets[0]
    rows = list(ws.iter_rows(values_only=True))
    wb.close()
    if not rows:
        sys.exit("La hoja está vacía.")
    headers = [str(h).strip() if h is not None else f"col_{i + 1}" for i, h in enumerate(rows[0])]
    return ws.title, headers, rows[1:]


def find_keyword_col(headers, forced):
    if forced:
        if forced not in headers:
            sys.exit(f"No existe la columna '{forced}'. Columnas: {headers}")
        return headers.index(forced)
    for i, h in enumerate(headers):
        if KEYWORD_COL.match(h):
            return i
    return 0


def inspect(path):
    wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
    for ws in wb.worksheets:
        rows = list(ws.iter_rows(values_only=True))
        print(f"\n=== Hoja '{ws.title}': {max(len(rows) - 1, 0)} filas de datos ===")
        if not rows:
            continue
        headers = [str(h) if h is not None else f"col_{i + 1}" for i, h in enumerate(rows[0])]
        body = rows[1:]
        for i, h in enumerate(headers):
            values = [r[i] for r in body if i < len(r) and r[i] not in (None, "")]
            distinct = list(dict.fromkeys(str(v) for v in values))
            nums = [v for v in values if isinstance(v, (int, float))]
            line = f"- {h}: {len(values)} con valor, {len(distinct)} distintos"
            if nums:
                line += f", rango {min(nums)}–{max(nums)}"
            if len(distinct) <= 12:
                line += f", valores: {distinct}"
            else:
                line += f", ejemplos: {distinct[:5]}"
            print(line)
        print("Primeras filas:")
        for r in body[:5]:
            print("  ", dict(zip(headers, r)))
    wb.close()


def build_state(context, headers, row, kw_idx):
    data = "\n".join(
        f"- {h}: {v}" for i, (h, v) in enumerate(zip(headers, row)) if i != kw_idx and v not in (None, "")
    )
    return f"{context.strip()}\n\n## Keyword a evaluar\n{row[kw_idx]}\n\n## Datos de esta keyword en el Excel\n{data or '- (sin datos)'}"


def call_jev(key, state, questions, retries=4):
    body = json.dumps({"model": MODEL, "state": state, "questions": questions}).encode()
    for attempt in range(retries):
        req = urllib.request.Request(
            ENDPOINT,
            data=body,
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            detail = e.read().decode(errors="replace")
            if e.code in (429, 500, 502, 503, 504) and attempt < retries - 1:
                time.sleep(2**attempt)
                continue
            raise RuntimeError(f"HTTP {e.code}: {detail[:300]}")
        except urllib.error.URLError as e:
            if attempt < retries - 1:
                time.sleep(2**attempt)
                continue
            raise RuntimeError(f"Red: {e.reason}")


def confidence(a, qtype):
    """Seguridad de Jev en una respuesta (0–1), derivada de sus probabilidades."""
    if qtype == "noul":
        return max(a["noul"], 1 - a["noul"]) if "noul" in a else None
    probs = a.get("probabilities") or {}
    return max(probs.values()) if probs else None


def flatten(answers, questions):
    """Convierte las respuestas de Jev en valores planos: {pregunta: valor} + '_precision'."""
    out, confs = {}, []
    for name, q in questions.items():
        a = answers.get(name, {})
        if q["type"] == "choice":
            out[name] = a.get("choice")
        elif q["type"] == "score":
            out[name] = round(a["score"], 2) if "score" in a else None
        else:  # noul
            out[name] = round(a["noul"], 3) if "noul" in a else None
        c = confidence(a, q["type"])
        if c is not None:
            confs.append(c)
    out["_precision"] = round(sum(confs) / len(confs), 3) if confs else None
    return out


def veredicto(v):
    """Etiqueta final: priorizar / revisar / descartar. El potencial GEO puede rescatar keywords."""
    rel, prio, geo, prec = (v.get(k) for k in ("relevancia", "prioridad", "potencial_geo", "_precision"))
    if rel is None or prio is None:
        return None
    geo = geo or 0
    if rel < 1.5:
        label = "descartar"  # no encaja con el negocio: el GEO no la salva
    elif prio >= 2.5 or (prio >= 1.5 and geo >= 0.7):
        label = "priorizar"
    elif prio < 1 and geo < 0.5:
        label = "descartar"
    else:
        label = "revisar"
    if label == "priorizar" and prec is not None and prec < 0.6:
        label = "revisar"  # Jev duda: que lo confirme una persona
    return label


# Columnas de salida: (clave interna, cabecera en el Excel, formato)
OUTPUT_COLUMNS = [
    ("relevancia", "Jev · Relevancia (0-4)", "0.0"),
    ("intencion", "Jev · Intención", None),
    ("funnel", "Jev · Funnel", None),
    ("potencial_geo", "Jev · Potencial GEO", "0%"),
    ("prioridad", "Jev · Prioridad (0-3)", "0.0"),
    ("veredicto", "Jev · Veredicto", None),
    ("_precision", "Jev · Precisión", "0%"),
    ("_error", "Jev · Error", None),
]


def evaluate(args, questions):
    key = api_key()
    context = Path(args.contexto).read_text(encoding="utf-8-sig")
    sheet, headers, rows = read_rows(args.excel, args.hoja)
    kw_idx = find_keyword_col(headers, args.col_keyword)
    targets = [(i, r) for i, r in enumerate(rows) if kw_idx < len(r) and r[kw_idx] not in (None, "")]
    if args.limite:
        targets = targets[: args.limite]

    states = [(i, build_state(context, headers, r, kw_idx)) for i, r in targets]
    print(f"Hoja '{sheet}', columna keyword: '{headers[kw_idx]}', filas a evaluar: {len(states)}")

    if args.dry_run:
        chars = sum(len(s) for _, s in states)
        print(f"Tamaño aprox.: {chars // 4:,} tokens de entrada en total (~{chars // 4 // max(len(states), 1)} por keyword)")
        print("\n--- State de ejemplo (fila 1) ---\n" + states[0][1] if states else "Sin filas.")
        print("\n--- Preguntas ---\n" + ", ".join(f"{k} ({q['type']})" for k, q in questions.items()))
        return

    def work(item):
        i, state = item
        try:
            res = call_jev(key, state, questions)
            cost = float(res.get("provider_metadata", {}).get("gateway", {}).get("cost", 0) or 0)
            return i, flatten(res.get("answers", {}), questions), cost, None
        except Exception as e:  # noqa: BLE001 — se registra por fila y se sigue
            return i, {}, 0.0, str(e)

    results, total_cost, done = {}, 0.0, 0
    with ThreadPoolExecutor(max_workers=args.concurrencia) as pool:
        for i, cols, cost, err in pool.map(work, states):
            if cols:
                cols["veredicto"] = veredicto(cols)
            cols["_error"] = err
            results[i] = cols
            total_cost += cost
            done += 1
            if done % 25 == 0 or done == len(states):
                print(f"  {done}/{len(states)} evaluadas")

    # Escribe sobre una copia que conserva formato y fórmulas del original.
    wb = openpyxl.load_workbook(args.excel)
    ws = wb[sheet]
    base = ws.max_column
    header_fill = openpyxl.styles.PatternFill("solid", fgColor="E8E0FF")
    for j, (_, title, _) in enumerate(OUTPUT_COLUMNS, start=1):
        cell = ws.cell(row=1, column=base + j, value=title)
        cell.font = openpyxl.styles.Font(bold=True)
        cell.fill = header_fill
        ws.column_dimensions[openpyxl.utils.get_column_letter(base + j)].width = max(14, len(title) + 2)
    for i, cols in results.items():
        for j, (key_, _, fmt) in enumerate(OUTPUT_COLUMNS, start=1):
            cell = ws.cell(row=i + 2, column=base + j, value=cols.get(key_))
            if fmt:
                cell.number_format = fmt
    out = Path(args.salida) if args.salida else Path(args.excel).with_name(Path(args.excel).stem + "_jev.xlsx")
    wb.save(out)

    ok = [c for c in results.values() if not c.get("_error")]
    errors = len(results) - len(ok)
    print(f"\nGuardado: {out}")
    print(f"Evaluadas OK: {len(ok)} · Errores: {errors} · Coste: ${total_cost:.6f}")
    if ok:
        counts = {}
        for c in ok:
            counts[c.get("veredicto")] = counts.get(c.get("veredicto"), 0) + 1
        precs = [c["_precision"] for c in ok if c.get("_precision") is not None]
        print("Veredictos:", ", ".join(f"{k}: {n}" for k, n in counts.items()))
        if precs:
            print(f"Precisión media de Jev: {sum(precs) / len(precs):.0%}")
    if errors:
        first = next(c["_error"] for c in results.values() if c.get("_error"))
        print(f"Primer error: {first}")


def credits():
    req = urllib.request.Request(CREDITS, headers={"Authorization": f"Bearer {api_key()}"})
    with urllib.request.urlopen(req, timeout=30) as r:
        print("Créditos AI Gateway:", r.read().decode())


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("excel", nargs="?")
    p.add_argument("--contexto", help="Archivo .md con el contexto del cliente y del Excel")
    p.add_argument("--preguntas", default=str(DEFAULT_QUESTIONS))
    p.add_argument("--hoja")
    p.add_argument("--col-keyword")
    p.add_argument("--salida")
    p.add_argument("--limite", type=int)
    p.add_argument("--concurrencia", type=int, default=5)
    p.add_argument("--inspeccionar", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--creditos", action="store_true")
    args = p.parse_args()

    if args.creditos:
        return credits()
    if not args.excel:
        p.error("falta la ruta del Excel")
    if args.inspeccionar:
        return inspect(args.excel)
    if not args.contexto:
        p.error("falta --contexto")
    questions = json.loads(Path(args.preguntas).read_text(encoding="utf-8"))
    evaluate(args, questions)


if __name__ == "__main__":
    main()
