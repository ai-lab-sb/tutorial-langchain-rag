@echo off
chcp 65001 >nul
echo ╔══════════════════════════════════════════════════════════════════╗
echo ║  🚀 Instalador del Tutorial de LangChain RAG                    ║
echo ╚══════════════════════════════════════════════════════════════════╝
echo.

echo 📦 Paso 1: Verificando Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python no está instalado o no está en el PATH
    echo    Por favor, instala Python 3.8+ desde python.org
    pause
    exit /b 1
)
python --version
echo ✅ Python encontrado
echo.

echo 📦 Paso 2: Instalando dependencias...
echo    Esto puede tomar algunos minutos...
echo.
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ Error al instalar dependencias
    pause
    exit /b 1
)
echo ✅ Dependencias instaladas correctamente
echo.

echo 📄 Paso 3: Creando archivo .env...
if exist .env (
    echo ⚠️  El archivo .env ya existe, no se sobrescribirá
) else (
    copy .env.example .env >nul
    echo ✅ Archivo .env creado
    echo ⚠️  IMPORTANTE: Edita el archivo .env y agrega tu API key de Gemini
)
echo.

echo 🧪 Paso 4: Verificando instalación...
echo.
python test_simple.py
echo.

echo ╔══════════════════════════════════════════════════════════════════╗
echo ║  ✅ Instalación completada                                       ║
echo ╚══════════════════════════════════════════════════════════════════╝
echo.
echo 📋 PRÓXIMOS PASOS:
echo.
echo    1. Obtén tu API key de Gemini:
echo       https://makersuite.google.com/app/apikey
echo.
echo    2. Edita el archivo .env y pega tu API key
echo.
echo    3. Configura Google Sheets siguiendo:
echo       INSTRUCCIONES_GOOGLE_SHEETS.md
echo.
echo    4. Ejecuta el tutorial:
echo       python tutorial_completo.py
echo.
echo    O ejecuta directamente:
echo       python main.py --interactive
echo.
echo 📚 Lee EMPEZAR_AQUI.md para más información
echo.
pause


