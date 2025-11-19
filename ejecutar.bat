@echo off
chcp 65001 >nul
echo ╔══════════════════════════════════════════════════════════════════╗
echo ║  🚀 Tutorial de LangChain RAG - Menú de Ejecución               ║
echo ╚══════════════════════════════════════════════════════════════════╝
echo.
echo Selecciona una opción:
echo.
echo   1. 🎓 Tutorial completo paso a paso (Recomendado para principiantes)
echo   2. 💬 Modo interactivo (Hacer preguntas al sistema)
echo   3. 📋 Ejemplos predefinidos
echo   4. 🧪 Verificar configuración
echo   5. ⚡ Modo interactivo rápido (con índice existente)
echo   6. ❌ Salir
echo.
set /p opcion="Tu elección (1-6): "

if "%opcion%"=="1" (
    echo.
    echo 🎓 Ejecutando tutorial completo...
    echo.
    python tutorial_completo.py
    goto fin
)

if "%opcion%"=="2" (
    echo.
    echo 💬 Iniciando modo interactivo...
    echo.
    python main.py --interactive
    goto fin
)

if "%opcion%"=="3" (
    echo.
    echo 📋 Ejecutando ejemplos...
    echo.
    python main.py
    goto fin
)

if "%opcion%"=="4" (
    echo.
    echo 🧪 Verificando configuración...
    echo.
    python test_simple.py
    goto fin
)

if "%opcion%"=="5" (
    echo.
    echo ⚡ Modo interactivo rápido...
    echo.
    python main.py --use-existing-index --interactive
    goto fin
)

if "%opcion%"=="6" (
    echo.
    echo 👋 ¡Hasta luego!
    exit /b 0
)

echo.
echo ❌ Opción no válida
echo.

:fin
echo.
echo ╔══════════════════════════════════════════════════════════════════╗
echo ║  ✅ Ejecución completada                                         ║
echo ╚══════════════════════════════════════════════════════════════════╝
echo.
pause


