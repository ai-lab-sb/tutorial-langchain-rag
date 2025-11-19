#!/bin/bash

echo "╔══════════════════════════════════════════════════════════════════╗"
echo "║  🚀 Tutorial de LangChain RAG - Menú de Ejecución               ║"
echo "╚══════════════════════════════════════════════════════════════════╝"
echo ""
echo "Selecciona una opción:"
echo ""
echo "  1. 🎓 Tutorial completo paso a paso (Recomendado para principiantes)"
echo "  2. 💬 Modo interactivo (Hacer preguntas al sistema)"
echo "  3. 📋 Ejemplos predefinidos"
echo "  4. 🧪 Verificar configuración"
echo "  5. ⚡ Modo interactivo rápido (con índice existente)"
echo "  6. ❌ Salir"
echo ""
read -p "Tu elección (1-6): " opcion

# Activar entorno virtual si existe
if [ -d "venv" ]; then
    source venv/bin/activate
fi

case $opcion in
    1)
        echo ""
        echo "🎓 Ejecutando tutorial completo..."
        echo ""
        python tutorial_completo.py
        ;;
    2)
        echo ""
        echo "💬 Iniciando modo interactivo..."
        echo ""
        python main.py --interactive
        ;;
    3)
        echo ""
        echo "📋 Ejecutando ejemplos..."
        echo ""
        python main.py
        ;;
    4)
        echo ""
        echo "🧪 Verificando configuración..."
        echo ""
        python test_simple.py
        ;;
    5)
        echo ""
        echo "⚡ Modo interactivo rápido..."
        echo ""
        python main.py --use-existing-index --interactive
        ;;
    6)
        echo ""
        echo "👋 ¡Hasta luego!"
        exit 0
        ;;
    *)
        echo ""
        echo "❌ Opción no válida"
        echo ""
        ;;
esac

echo ""
echo "╔══════════════════════════════════════════════════════════════════╗"
echo "║  ✅ Ejecución completada                                         ║"
echo "╚══════════════════════════════════════════════════════════════════╝"
echo ""

