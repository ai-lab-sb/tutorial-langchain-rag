#!/bin/bash

echo "╔══════════════════════════════════════════════════════════════════╗"
echo "║  🚀 Instalador del Tutorial de LangChain RAG                    ║"
echo "╚══════════════════════════════════════════════════════════════════╝"
echo ""

echo "📦 Paso 1: Verificando Python..."
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "❌ Python no está instalado"
        echo "   Por favor, instala Python 3.8+ desde python.org"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

$PYTHON_CMD --version
echo "✅ Python encontrado"
echo ""

echo "📦 Paso 2: Creando entorno virtual..."
if [ ! -d "venv" ]; then
    $PYTHON_CMD -m venv venv
    echo "✅ Entorno virtual creado"
else
    echo "⚠️  Entorno virtual ya existe"
fi
echo ""

echo "📦 Paso 3: Activando entorno virtual..."
source venv/bin/activate
echo "✅ Entorno virtual activado"
echo ""

echo "📦 Paso 4: Instalando dependencias..."
echo "   Esto puede tomar algunos minutos..."
echo ""
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Error al instalar dependencias"
    exit 1
fi

echo "✅ Dependencias instaladas correctamente"
echo ""

echo "📄 Paso 5: Creando archivo .env..."
if [ -f ".env" ]; then
    echo "⚠️  El archivo .env ya existe, no se sobrescribirá"
else
    cp .env.example .env
    echo "✅ Archivo .env creado"
    echo "⚠️  IMPORTANTE: Edita el archivo .env y agrega tu API key de Gemini"
fi
echo ""

echo "🧪 Paso 6: Verificando instalación..."
echo ""
$PYTHON_CMD test_simple.py
echo ""

echo "╔══════════════════════════════════════════════════════════════════╗"
echo "║  ✅ Instalación completada                                       ║"
echo "╚══════════════════════════════════════════════════════════════════╝"
echo ""
echo "📋 PRÓXIMOS PASOS:"
echo ""
echo "   1. Activa el entorno virtual:"
echo "      source venv/bin/activate"
echo ""
echo "   2. Obtén tu API key de Gemini:"
echo "      https://makersuite.google.com/app/apikey"
echo ""
echo "   3. Edita el archivo .env y pega tu API key"
echo ""
echo "   4. Configura Google Sheets siguiendo:"
echo "      INSTRUCCIONES_GOOGLE_SHEETS.md"
echo ""
echo "   5. Ejecuta el tutorial:"
echo "      python tutorial_completo.py"
echo ""
echo "   O ejecuta directamente:"
echo "      python main.py --interactive"
echo ""
echo "📚 Lee EMPEZAR_AQUI.md para más información"
echo ""

