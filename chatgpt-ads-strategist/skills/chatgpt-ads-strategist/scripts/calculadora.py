#!/usr/bin/env python3
"""Calculadora del estratega de ChatGPT Ads.

Subcomandos:
  presupuesto  Presupuesto de aprendizaje y nº máximo de ad groups viables.
  score        Opportunity Score de Buyer Situations (JSON de entrada).
  anuncios     Valida longitudes de título y copy (JSON de entrada).

Las cifras por defecto son orientativas (hipótesis): ajústalas a los datos
reales del proyecto y verifica los límites vigentes de la plataforma.
"""
import argparse
import json
import math
import sys

# Límites de anuncio (verificar en references/estado-plataforma.md)
TITULO_REC = (16, 24)
TITULO_MAX = 50
COPY_REC = (32, 48)
COPY_MAX = 100

PESOS_DEFECTO = {
    "intencion": 1.5,
    "volumen": 1.0,
    "fit": 1.0,
    "valor": 1.2,
    "facilidad": 1.0,
}


def cmd_presupuesto(a):
    if a.cvr <= 0 or a.cvr >= 100:
        sys.exit("La CVR debe estar entre 0 y 100 (en %).")
    cvr = a.cvr / 100
    clics_por_grupo = max(math.ceil(a.conversiones / cvr), a.clics_min)
    coste_grupo = clics_por_grupo * a.cpc
    diario_grupo = coste_grupo / a.dias

    print("=== PRESUPUESTO DE APRENDIZAJE (orientativo) ===")
    print(f"CPC estimado:               {a.cpc:.2f}")
    print(f"CVR estimada:               {a.cvr:.2f} %")
    print(f"Conversiones objetivo/grupo: {a.conversiones}")
    print(f"Clics necesarios/grupo:     {clics_por_grupo}")
    print(f"Coste por ad group:         {coste_grupo:,.0f} en {a.dias} días")
    print(f"Diario por ad group:        {diario_grupo:,.2f}")
    print(f"CPA implícito:              {a.cpc / cvr:,.2f}")

    if a.cpa_objetivo:
        cpa = a.cpc / cvr
        estado = "OK" if cpa <= a.cpa_objetivo else "POR ENCIMA DEL OBJETIVO"
        print(f"CPA objetivo:               {a.cpa_objetivo:,.2f} -> {estado}")

    if a.grupos:
        total = coste_grupo * a.grupos
        print(f"\nPara {a.grupos} ad groups: {total:,.0f} en {a.dias} días "
              f"({total / a.dias:,.2f}/día)")

    if a.presupuesto:
        prorrateado = a.presupuesto * a.dias / 30
        viables = int(prorrateado // coste_grupo)
        print(f"\nPresupuesto mensual:        {a.presupuesto:,.0f} "
              f"(≈ {prorrateado:,.0f} en {a.dias} días)")
        print(f"Ad groups viables:          {viables}")
        if viables == 0:
            print("AVISO: no alcanza ni para un ad group con este criterio. "
                  "Reduce el objetivo de conversiones, alarga el test, "
                  "optimiza a microconversión o replantea el canal.")
        elif a.grupos and viables < a.grupos:
            print(f"AVISO: el plan de {a.grupos} ad groups fragmenta la señal. "
                  f"Concentra en {viables} y deja el resto para la segunda ola.")
    if a.minimo_diario and a.presupuesto:
        diario = a.presupuesto / 30
        if diario < a.minimo_diario:
            print(f"\nAVISO: {diario:,.2f}/día no llega al mínimo de plataforma "
                  f"indicado ({a.minimo_diario:,.2f}/día por campaña).")
        else:
            print(f"\nMínimo de plataforma ({a.minimo_diario:,.2f}/día por campaña): cubierto.")


def cmd_score(a):
    with open(a.archivo, encoding="utf-8") as f:
        items = json.load(f)
    pesos = dict(PESOS_DEFECTO)
    if a.pesos:
        pesos.update(json.loads(a.pesos))
    resultados = []
    for it in items:
        faltan = [k for k in pesos if k not in it]
        if faltan:
            sys.exit(f"Faltan criterios {faltan} en: {it.get('situacion', it)}")
        for k in pesos:
            if not 1 <= it[k] <= 5:
                sys.exit(f"'{k}' debe estar entre 1 y 5 en: {it.get('situacion')}")
        total = sum(it[k] * w for k, w in pesos.items()) / sum(pesos.values())
        resultados.append((round(total, 2), it))
    resultados.sort(key=lambda x: x[0], reverse=True)
    print("=== OPPORTUNITY SCORE (1-5) ===")
    print("Pesos: " + ", ".join(f"{k}={v}" for k, v in pesos.items()))
    for i, (s, it) in enumerate(resultados, 1):
        print(f"{i:>2}. {s:.2f}  {it.get('situacion', '(sin nombre)')}"
              f"  [intent: {it.get('intent', '-')}]")


def estado(n, rec, maximo):
    if n > maximo:
        return "ERROR >máx"
    if n < rec[0]:
        return "corto"
    if n > rec[1]:
        return "largo (puede truncarse)"
    return "OK"


def cmd_anuncios(a):
    with open(a.archivo, encoding="utf-8") as f:
        ads = json.load(f)
    errores = 0
    print("=== VALIDACIÓN DE ANUNCIOS ===")
    print(f"Título rec {TITULO_REC[0]}-{TITULO_REC[1]} (máx {TITULO_MAX}) · "
          f"Copy rec {COPY_REC[0]}-{COPY_REC[1]} (máx {COPY_MAX})\n")
    for i, ad in enumerate(ads, 1):
        t, c = ad.get("titulo", ""), ad.get("copy", "")
        et, ec = estado(len(t), TITULO_REC, TITULO_MAX), estado(len(c), COPY_REC, COPY_MAX)
        errores += et.startswith("ERROR") + ec.startswith("ERROR")
        print(f"{i:>2}. [{ad.get('ad_group', '-')}]")
        print(f"    Título ({len(t):>3}) {et:<24} {t}")
        print(f"    Copy   ({len(c):>3}) {ec:<24} {c}")
    print(f"\nAnuncios: {len(ads)} · errores bloqueantes: {errores}")
    sys.exit(1 if errores else 0)


def main():
    # La consola de Windows (cp1252) no puede imprimir '≈' y otros símbolos
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    b = sub.add_parser("presupuesto", help="Presupuesto de aprendizaje")
    b.add_argument("--cpc", type=float, required=True, help="CPC estimado")
    b.add_argument("--cvr", type=float, required=True, help="CVR estimada en %%")
    b.add_argument("--conversiones", type=int, default=15,
                   help="Conversiones objetivo por ad group (defecto 15)")
    b.add_argument("--clics-min", type=int, default=100,
                   help="Clics mínimos por ad group (defecto 100)")
    b.add_argument("--dias", type=int, default=30, help="Duración del test (defecto 30)")
    b.add_argument("--grupos", type=int, help="Nº de ad groups planeados")
    b.add_argument("--presupuesto", type=float, help="Presupuesto mensual disponible")
    b.add_argument("--cpa-objetivo", type=float, help="CPA/CPL objetivo")
    b.add_argument("--minimo-diario", type=float, help="Mínimo diario de plataforma")
    b.set_defaults(func=cmd_presupuesto)

    s = sub.add_parser("score", help="Opportunity Score")
    s.add_argument("archivo", help="JSON: [{situacion, intent, intencion, volumen, "
                                   "fit, valor, facilidad}]")
    s.add_argument("--pesos", help='JSON de pesos, p. ej. \'{"valor": 2}\'')
    s.set_defaults(func=cmd_score)

    v = sub.add_parser("anuncios", help="Validar longitudes")
    v.add_argument("archivo", help="JSON: [{ad_group, titulo, copy}]")
    v.set_defaults(func=cmd_anuncios)

    a = p.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
