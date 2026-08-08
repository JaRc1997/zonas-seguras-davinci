# -*- coding: utf-8 -*-
"""
Zona Segura - coloca una guia de zona segura de redes sociales sobre el
timeline vertical (9:16) de DaVinci Resolve.

Se ejecuta desde:  Area de trabajo -> Secuencias de comandos
Es una GUIA para editar: desactiva o borra esa pista antes de exportar.
"""
PLATAFORMA = "YouTube_Shorts"   # nombre del overlay (archivo PNG)

import os
import sys
import json


def obtener_resolve():
    try:
        return resolve
    except NameError:
        pass
    try:
        import DaVinciResolveScript as dvr
        return dvr.scriptapp("Resolve")
    except Exception:
        api = os.environ.get(
            "RESOLVE_SCRIPT_API",
            r"C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting")
        sys.path.append(os.path.join(api, "Modules"))
        import DaVinciResolveScript as dvr
        return dvr.scriptapp("Resolve")


def carpeta_overlays():
    # 1) Overlays JUNTO al script. DaVinci NO define __file__, asi que
    #    obtenemos la ruta del script con inspect (co_filename del lambda).
    try:
        import inspect
        aqui = os.path.dirname(os.path.abspath(inspect.getsourcefile(lambda: 0)))
        if os.path.exists(os.path.join(aqui, PLATAFORMA + ".png")):
            return aqui
    except Exception:
        pass
    # 2) Respaldo: config.json en APPDATA (si existe la variable).
    appdata = os.environ.get("APPDATA") or os.path.expanduser(r"~\AppData\Roaming")
    ruta = os.path.join(appdata, "ZonasSeguras", "config.json")
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8-sig") as f:
            return json.load(f)["overlays"]
    raise RuntimeError("No encuentro la carpeta de overlays (ZonaSegura_assets) "
                       "junto al script ni la configuracion en:\n  " + ruta)


def main():
    resolve = obtener_resolve()
    if resolve is None:
        print("ERROR: No pude conectar con DaVinci Resolve.")
        return
    project = resolve.GetProjectManager().GetCurrentProject()
    if not project:
        print("ERROR: No hay proyecto abierto.")
        return
    timeline = project.GetCurrentTimeline()
    if not timeline:
        print("ERROR: No hay timeline activo. Abre uno en la pagina Edit.")
        return

    png = os.path.join(carpeta_overlays(), PLATAFORMA + ".png")
    if not os.path.exists(png):
        print("ERROR: No encuentro el overlay: " + png)
        return
    print("[guia] Plataforma: " + PLATAFORMA)

    mp = project.GetMediaPool()
    items = mp.ImportMedia([png])
    if not items:
        print("ERROR: No pude importar el overlay al Media Pool.")
        return
    item = items[0]

    timeline.AddTrack("video")
    idx = timeline.GetTrackCount("video")
    try:
        timeline.SetTrackName("video", idx, "GUIA Zona Segura")
    except Exception:
        pass

    inicio = timeline.GetStartFrame()
    dur = timeline.GetEndFrame() - inicio + 1
    clip_info = {
        "mediaPoolItem": item,
        "startFrame": 0,
        "endFrame": max(1, dur - 1),
        "trackIndex": idx,
        "recordFrame": inicio,
    }
    ok = mp.AppendToTimeline([clip_info])

    if ok:
        print("")
        print("[OK] Guia de " + PLATAFORMA + " colocada en la pista de video " + str(idx) + ".")
        print("     - Ajusta tus textos dentro de la zona libre (centro).")
        print("     - IMPORTANTE: apaga (icono del ojo) o borra esa pista antes de exportar.")
    else:
        print("")
        print("[OK] El overlay quedo en el Media Pool, pero no pude colocarlo solo.")
        print("     Arrastralo a una pista nueva ENCIMA de tu video.")


if __name__ == "__main__":
    main()
