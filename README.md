# Zonas Seguras para DaVinci Resolve

Guías con la **interfaz real de cada red social** para editar contenido vertical
(9:16) en **DaVinci Resolve** sin que los botones de la app tapen tus textos.

Coloca sobre tu video una capa transparente que muestra dónde TikTok, Instagram
Reels, YouTube Shorts o Facebook ponen sus botones (like, comentarios, compartir),
la descripción y la barra de estado del teléfono — así sabes exactamente dónde
**sí** y dónde **no** poner tu texto.

Es una guía para editar: la apagas o la borras antes de exportar.

---

## Redes incluidas

- **TikTok**
- **Instagram Reels**
- **YouTube Shorts**
- **Facebook**

---

## Instalación fácil

1. **Descarga el paquete:** [Descargar Zonas Seguras (Windows)](https://drive.google.com/uc?export=download&id=1jERuGHzvnS_UdOY2-MQ7fVeM8L_9_1Mq)
2. Descomprime la carpeta.
3. Doble clic en **`Instalar.bat`**.
4. Cierra y vuelve a abrir DaVinci Resolve.

No necesita instalar nada más. Funciona en la versión gratis.

---

## Cómo usar

1. Abre tu proyecto vertical (9:16, ej. 1080x1920) con el video en la línea de tiempo.
2. Menú **Área de trabajo → Secuencias de comandos** y elige la red:
   `Zona Segura - TikTok` / `Reels` / `Shorts` / `Facebook`.
3. Se crea una pista **"GUIA Zona Segura"** con la interfaz de esa red sobre tu video.
4. Coloca tus textos en la zona libre (el centro), lejos de los iconos.
5. **Apaga o borra esa pista antes de exportar** el video final.

---

## Instalación manual (alternativa)

Copia los archivos `Zona Segura - *.py` y los `.png` a la carpeta:

```
%APPDATA%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Utility
```

(Los `.py` y los `.png` deben quedar en la misma carpeta.)

---

## Estructura

| Archivo | Descripción |
|---|---|
| `Zona Segura - *.py` | Un script por red social |
| `*.png` | Las guías (overlays) a 1080x1920 |
| `Instalar.bat` | Instalador automático |
| `LEEME.txt` | Guía de instalación y uso |

---

## Licencia

MIT. Ver [LICENSE](LICENSE).
