@echo off
chcp 65001 >nul
title Instalador - Zonas Seguras para DaVinci Resolve

set "BASE=%~dp0"
set "UTIL=%APPDATA%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Utility"

echo ============================================================
echo    ZONAS SEGURAS para DaVinci Resolve
echo    Instalacion automatica
echo ============================================================
echo.

if not exist "%UTIL%" mkdir "%UTIL%"

copy /Y "%BASE%Zona Segura - *.py" "%UTIL%\" >nul
copy /Y "%BASE%*.png" "%UTIL%\" >nul

echo  [OK] Guias instaladas en DaVinci Resolve.
echo.
echo ============================================================
echo    LISTO. Cierra y vuelve a abrir DaVinci Resolve, luego:
echo.
echo    Area de trabajo -^> Secuencias de comandos -^>
echo        Zona Segura - TikTok
echo        Zona Segura - Reels
echo        Zona Segura - Shorts
echo        Zona Segura - Facebook
echo ============================================================
echo.
pause
