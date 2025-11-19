"""
Script principal para ejecutar el sistema RAG
"""
import argparse
from data_loader import load_data_from_google_sheets, print_documents_summary
from rag_system import RAGSystem


def run_example_queries(rag_system: RAGSystem):
    """
    Ejecuta consultas de ejemplo para demostrar el sistema.
    
    Args:
        rag_system: Sistema RAG inicializado
    """
    print("\n" + "="*70)
    print("🎯 EJECUTANDO CONSULTAS DE EJEMPLO")
    print("="*70 + "\n")
    
    # Lista de preguntas de ejemplo
    example_questions = [
        "¿Qué es Python y para qué se utiliza?",
        "Explícame qué es RAG",
        "¿Qué es FAISS?",
        "¿Cómo funcionan los embeddings?",
        "Háblame sobre Gemini"
    ]
    
    for i, question in enumerate(example_questions, 1):
        print(f"\n{'='*70}")
        print(f"Ejemplo {i}/{len(example_questions)}")
        print(f"{'='*70}")
        
        rag_system.query(question, verbose=True)
        
        if i < len(example_questions):
            input("\n⏸️  Presiona Enter para continuar con el siguiente ejemplo...")


def run_interactive_mode(rag_system: RAGSystem):
    """
    Modo interactivo para hacer preguntas al sistema.
    
    Args:
        rag_system: Sistema RAG inicializado
    """
    print("\n" + "="*70)
    print("💬 MODO INTERACTIVO")
    print("="*70)
    print("\nEscribe tus preguntas (o 'salir' para terminar)")
    print("-"*70 + "\n")
    
    while True:
        try:
            question = input("\n❓ Tu pregunta: ").strip()
            
            if not question:
                continue
            
            if question.lower() in ['salir', 'exit', 'quit', 'q']:
                print("\n👋 ¡Hasta luego!")
                break
            
            # Procesar la pregunta
            rag_system.query(question, verbose=True)
            
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")


def main():
    """Función principal"""
    # Configurar argumentos de línea de comandos
    parser = argparse.ArgumentParser(
        description="Sistema RAG con LangChain, FAISS y Gemini"
    )
    parser.add_argument(
        "--interactive",
        "-i",
        action="store_true",
        help="Ejecutar en modo interactivo"
    )
    parser.add_argument(
        "--use-existing-index",
        "-e",
        action="store_true",
        help="Usar índice FAISS existente en lugar de crear uno nuevo"
    )
    
    args = parser.parse_args()
    
    print("\n" + "="*70)
    print("🎓 TUTORIAL DE LANGCHAIN CON RAG")
    print("   Usando FAISS como Vector Store y Gemini como LLM")
    print("="*70 + "\n")
    
    # Paso 1: Cargar datos
    print("PASO 1: Cargando datos desde Google Sheets")
    print("-"*70)
    documents = load_data_from_google_sheets()
    
    if not documents:
        print("\n❌ No se pudieron cargar los datos. Verifica la configuración.")
        print("   Revisa el README.md para más información sobre cómo configurar Google Sheets.")
        return
    
    # Mostrar resumen de documentos
    print_documents_summary(documents)
    
    # Paso 2: Inicializar sistema RAG
    print("\nPASO 2: Inicializando sistema RAG")
    print("-"*70)
    
    rag = RAGSystem()
    
    # Intentar usar índice existente si se solicita
    if args.use_existing_index:
        success = rag.initialize(use_existing_index=True)
        if not success:
            print("\n⚠️  No se pudo cargar índice existente. Creando uno nuevo...")
            success = rag.initialize(documents=documents)
    else:
        success = rag.initialize(documents=documents)
    
    if not success:
        print("\n❌ No se pudo inicializar el sistema RAG")
        return
    
    # Paso 3: Ejecutar consultas
    print("\nPASO 3: Realizando consultas")
    print("-"*70)
    
    if args.interactive:
        run_interactive_mode(rag)
    else:
        run_example_queries(rag)
    
    print("\n" + "="*70)
    print("✅ TUTORIAL COMPLETADO")
    print("="*70)
    print("\n💡 Consejos:")
    print("   - Ejecuta con --interactive para modo interactivo")
    print("   - Ejecuta con --use-existing-index para usar el índice guardado")
    print("   - Agrega más datos a tu Google Sheet para mejores resultados")
    print("   - Revisa el README.md para más información\n")


if __name__ == "__main__":
    main()


