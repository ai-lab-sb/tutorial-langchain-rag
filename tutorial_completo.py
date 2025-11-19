"""
Tutorial Completo Paso a Paso de RAG con LangChain
Este script te guía a través de cada componente del sistema RAG
con explicaciones detalladas y ejemplos interactivos.
"""
import time
from typing import List
from langchain.schema import Document
from data_loader import load_data_from_google_sheets
from rag_system import RAGSystem
import config


def print_header(title: str):
    """Imprime un encabezado formateado"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70 + "\n")


def print_step(number: int, title: str):
    """Imprime el número de paso"""
    print(f"\n{'─'*70}")
    print(f"PASO {number}: {title}")
    print(f"{'─'*70}\n")


def pause(message: str = "Presiona Enter para continuar..."):
    """Pausa la ejecución"""
    input(f"\n⏸️  {message}")


def explain_rag():
    """Explica qué es RAG"""
    print_header("🎓 ¿QUÉ ES RAG?")
    
    print("""
RAG (Retrieval-Augmented Generation) es una técnica que mejora las 
respuestas de los modelos de lenguaje grandes (LLMs) combinando dos pasos:

1. 📚 RECUPERACIÓN (Retrieval):
   - Busca información relevante en una base de conocimientos
   - Utiliza búsqueda semántica (por significado, no solo palabras clave)
   - Recupera los documentos más similares a la pregunta

2. ✍️  GENERACIÓN (Generation):
   - El LLM recibe la pregunta + los documentos recuperados
   - Genera una respuesta basada en la información proporcionada
   - Produce respuestas más precisas y actualizadas

🎯 VENTAJAS DE RAG:
   ✓ Respuestas basadas en datos específicos (no alucinaciones)
   ✓ Información actualizada sin reentrenar el modelo
   ✓ Fuentes verificables (sabes de dónde viene la información)
   ✓ Flexible (puedes cambiar la base de conocimientos fácilmente)

📊 FLUJO DE RAG:
   Pregunta → Embedding → Búsqueda en Vector Store → 
   Recuperar Top-K docs → Contexto + Pregunta → LLM → Respuesta
    """)


def explain_embeddings():
    """Explica qué son los embeddings"""
    print_header("🧮 EMBEDDINGS: Convirtiendo Texto en Números")
    
    print("""
Los EMBEDDINGS son representaciones numéricas (vectores) de texto que 
capturan el significado semántico.

🔢 CARACTERÍSTICAS:
   - Vector de números (ej: [0.2, -0.5, 0.8, ...])
   - Dimensión fija (ej: 768 o 1536 dimensiones)
   - Textos similares → vectores cercanos
   - Captura contexto y relaciones

📏 EJEMPLO CONCEPTUAL:
   "perro"     → [0.8, 0.2, 0.1, ...]
   "gato"      → [0.7, 0.3, 0.15, ...] ← Cercano a "perro"
   "auto"      → [0.1, 0.9, 0.8, ...] ← Lejano de "perro"

🎯 EN NUESTRO SISTEMA:
   Usamos el modelo de embeddings de Google (embedding-001)
   que convierte preguntas y documentos en vectores de 768 dimensiones.
    """)


def explain_faiss():
    """Explica qué es FAISS"""
    print_header("⚡ FAISS: Búsqueda Ultrarrápida de Vectores")
    
    print("""
FAISS (Facebook AI Similarity Search) es una biblioteca optimizada
para buscar vectores similares de manera eficiente.

🚀 CARACTERÍSTICAS:
   - Búsquedas extremadamente rápidas (millones de vectores)
   - Algoritmos optimizados (GPU y CPU)
   - Bajo uso de memoria
   - Varios tipos de índices

🔍 CÓMO FUNCIONA:
   1. Indexa todos los embeddings de documentos
   2. Organiza los vectores para búsqueda eficiente
   3. Cuando llega una consulta:
      - Calcula la distancia a todos los vectores
      - Retorna los K vectores más cercanos
      - Todo en milisegundos ⚡

📊 MÉTRICA DE SIMILITUD:
   Usamos "similitud coseno" que mide el ángulo entre vectores:
   - Ángulo pequeño = Alta similitud (vectores apuntan en la misma dirección)
   - Ángulo grande = Baja similitud

💾 EN NUESTRO SISTEMA:
   FAISS indexa los embeddings de Google Sheets y permite
   encontrar rápidamente los documentos más relevantes.
    """)


def explain_langchain():
    """Explica qué es LangChain"""
    print_header("🔗 LANGCHAIN: Orquestando el Sistema RAG")
    
    print("""
LangChain es un framework para construir aplicaciones con LLMs.
Proporciona componentes modulares que se "encadenan" (chain).

🧩 COMPONENTES PRINCIPALES:
   
   1. Documents: Unidades de información con contenido + metadata
   
   2. Embeddings: Interfaz para modelos de embeddings
   
   3. Vector Stores: Almacenamiento de embeddings (FAISS, Pinecone, etc.)
   
   4. Retrievers: Recuperan documentos relevantes
   
   5. LLMs: Modelos de lenguaje (Gemini, GPT, etc.)
   
   6. Chains: Encadenan componentes para flujos complejos
   
   7. Prompts: Templates para estructurar las consultas

🔄 EN NUESTRO SISTEMA:
   LangChain conecta:
   Google Sheets → Documents → Embeddings → FAISS → 
   Retriever → Gemini → Respuesta
    """)


def demonstrate_loading_data():
    """Demuestra la carga de datos"""
    print_step(1, "Cargando Datos desde Google Sheets")
    
    print("""
Vamos a cargar los datos de tu Google Sheet.
El proceso es:
   1. Autenticar con las credenciales de la cuenta de servicio
   2. Conectar con la hoja usando el ID
   3. Leer todas las filas
   4. Convertir cada fila en un Document de LangChain

Cada Document tiene:
   - page_content: El texto del documento
   - metadata: Información adicional (tema, pregunta, etc.)
    """)
    
    pause("¿Listo para cargar los datos?")
    
    print("\n🔄 Cargando datos...\n")
    documents = load_data_from_google_sheets()
    
    if documents:
        print(f"\n✅ ¡Éxito! Se cargaron {len(documents)} documentos")
        
        # Mostrar un ejemplo
        print("\n📄 Ejemplo de documento:")
        print("-" * 70)
        doc = documents[0]
        print(f"Contenido:\n{doc.page_content}\n")
        print(f"Metadata: {doc.metadata}")
        print("-" * 70)
        
        return documents
    else:
        print("\n❌ No se pudieron cargar los datos")
        return None


def demonstrate_embeddings(documents: List[Document]):
    """Demuestra la creación de embeddings"""
    print_step(2, "Creando Embeddings")
    
    print("""
Ahora vamos a convertir el texto en vectores numéricos.

Proceso:
   1. Tomar cada documento
   2. Enviar el texto al modelo de embeddings de Google
   3. Recibir un vector de 768 números
   4. Este vector captura el "significado" del texto

Ejemplo (simplificado):
   Texto: "Python es un lenguaje de programación"
   Embedding: [0.23, -0.45, 0.67, 0.12, ..., 0.89] (768 números)
    """)
    
    pause("¿Listo para crear embeddings?")
    
    print("\n🔄 Creando embeddings...")
    
    rag = RAGSystem()
    if rag.setup_embeddings():
        print("\n✅ Modelo de embeddings configurado")
        print(f"   Modelo: {config.EMBEDDING_MODEL}")
        print("   Dimensión: 768")
        return rag
    else:
        print("\n❌ Error al configurar embeddings")
        return None


def demonstrate_vectorstore(rag: RAGSystem, documents: List[Document]):
    """Demuestra la creación del vector store"""
    print_step(3, "Creando Vector Store con FAISS")
    
    print(f"""
Ahora indexaremos los {len(documents)} documentos en FAISS.

Proceso:
   1. Para cada documento:
      - Calcular su embedding
      - Agregar al índice FAISS
   2. FAISS organiza los vectores para búsqueda eficiente
   3. Guardar el índice localmente para uso futuro

Esto puede tomar unos segundos...
    """)
    
    pause("¿Listo para crear el vector store?")
    
    print("\n🔄 Creando índice FAISS...")
    
    if rag.create_vectorstore(documents, save_local=True):
        print("\n✅ Vector store creado y guardado")
        print(f"   Documentos indexados: {len(documents)}")
        print(f"   Guardado en: {config.FAISS_INDEX_PATH}")
        return True
    else:
        print("\n❌ Error al crear vector store")
        return False


def demonstrate_llm(rag: RAGSystem):
    """Demuestra la configuración del LLM"""
    print_step(4, "Configurando el Modelo de Lenguaje (Gemini)")
    
    print(f"""
Configuraremos Gemini como nuestro modelo de lenguaje.

Configuración:
   - Modelo: {config.MODEL_NAME}
   - Temperature: {config.TEMPERATURE}
     (0 = más determinista, 1 = más creativo)
   - Provider: Google Generative AI

El LLM será el encargado de:
   1. Recibir la pregunta + contexto recuperado
   2. Comprender y razonar sobre la información
   3. Generar una respuesta coherente y útil
    """)
    
    pause("¿Listo para configurar Gemini?")
    
    print("\n🔄 Configurando Gemini...")
    
    if rag.setup_llm():
        print("\n✅ Gemini configurado correctamente")
        return True
    else:
        print("\n❌ Error al configurar Gemini")
        return False


def demonstrate_chain(rag: RAGSystem):
    """Demuestra la creación de la chain"""
    print_step(5, "Creando la Cadena RAG")
    
    print(f"""
Finalmente, conectaremos todos los componentes en una "chain".

La chain incluye:
   1. Retriever: Busca los top-{config.TOP_K_DOCUMENTS} documentos relevantes
   2. Prompt Template: Estructura la pregunta con el contexto
   3. LLM (Gemini): Genera la respuesta
   4. Output Parser: Formatea la salida

Flujo completo:
   Pregunta 
      ↓
   Embedding de la pregunta
      ↓
   Búsqueda en FAISS (retriever)
      ↓
   Recuperar documentos similares
      ↓
   Construir prompt: contexto + pregunta
      ↓
   Enviar a Gemini
      ↓
   Respuesta final
    """)
    
    pause("¿Listo para crear la chain?")
    
    print("\n🔄 Creando chain RAG...")
    
    if rag.setup_qa_chain():
        print("\n✅ Chain RAG lista para usar")
        print(f"   Documentos a recuperar: {config.TOP_K_DOCUMENTS}")
        return True
    else:
        print("\n❌ Error al crear chain")
        return False


def demonstrate_queries(rag: RAGSystem):
    """Demuestra consultas al sistema"""
    print_step(6, "¡Probemos el Sistema RAG!")
    
    print("""
Ahora el sistema está completamente funcional.
Vamos a hacer algunas preguntas y ver cómo funciona.

Para cada pregunta verás:
   1. La pregunta original
   2. La respuesta generada por Gemini
   3. Los documentos fuente que se usaron
    """)
    
    pause("¿Listo para las preguntas de prueba?")
    
    # Preguntas de ejemplo
    questions = [
        "¿Qué es Python?",
        "Explícame qué es RAG y por qué es útil",
        "¿Qué es FAISS y para qué sirve?"
    ]
    
    for i, question in enumerate(questions, 1):
        print(f"\n{'='*70}")
        print(f"PREGUNTA {i}/{len(questions)}")
        print(f"{'='*70}")
        
        print("\n🔍 PROCESO INTERNO:")
        print("   1. Convertir pregunta a embedding...")
        print("   2. Buscar en FAISS los documentos más similares...")
        print("   3. Recuperar contexto relevante...")
        print("   4. Enviar a Gemini con el contexto...")
        print("   5. Generar respuesta...\n")
        
        time.sleep(1)  # Pausa dramática 😄
        
        result = rag.query(question, verbose=True)
        
        if i < len(questions):
            pause("Presiona Enter para la siguiente pregunta...")


def main():
    """Función principal del tutorial"""
    print_header("🎓 TUTORIAL COMPLETO DE RAG CON LANGCHAIN, FAISS Y GEMINI")
    
    print("""
¡Bienvenido al tutorial interactivo!

Este tutorial te llevará paso a paso a través de:
   ✓ Conceptos teóricos de RAG
   ✓ Carga de datos desde Google Sheets
   ✓ Creación de embeddings
   ✓ Uso de FAISS como vector store
   ✓ Configuración de Gemini
   ✓ Consultas al sistema completo

Duración estimada: 10-15 minutos

⚠️  IMPORTANTE: Asegúrate de haber:
   1. Configurado tu API key de Gemini en .env
   2. Creado y configurado tu Google Sheet
   3. Descargado las credenciales de la cuenta de servicio
   4. Instalado todas las dependencias (pip install -r requirements.txt)
    """)
    
    pause("¿Listo para comenzar?")
    
    # Sección 1: Teoría
    explain_rag()
    pause()
    
    explain_embeddings()
    pause()
    
    explain_faiss()
    pause()
    
    explain_langchain()
    pause()
    
    # Sección 2: Práctica
    print_header("💻 PARTE PRÁCTICA: Construyendo el Sistema")
    
    # Paso 1: Cargar datos
    documents = demonstrate_loading_data()
    if not documents:
        print("\n❌ No se puede continuar sin datos")
        return
    pause()
    
    # Paso 2: Embeddings
    rag = demonstrate_embeddings(documents)
    if not rag:
        print("\n❌ No se puede continuar sin embeddings")
        return
    pause()
    
    # Paso 3: Vector Store
    if not demonstrate_vectorstore(rag, documents):
        print("\n❌ No se puede continuar sin vector store")
        return
    pause()
    
    # Paso 4: LLM
    if not demonstrate_llm(rag):
        print("\n❌ No se puede continuar sin LLM")
        return
    pause()
    
    # Paso 5: Chain
    if not demonstrate_chain(rag):
        print("\n❌ No se puede continuar sin chain")
        return
    pause()
    
    # Paso 6: Queries
    demonstrate_queries(rag)
    
    # Conclusión
    print_header("🎉 ¡FELICITACIONES!")
    
    print("""
¡Has completado el tutorial de RAG con LangChain!

🎯 LO QUE APRENDISTE:
   ✓ Conceptos fundamentales de RAG
   ✓ Cómo funcionan los embeddings
   ✓ Uso de FAISS para búsqueda vectorial
   ✓ Integración de componentes con LangChain
   ✓ Uso de Gemini para generación de respuestas

🚀 PRÓXIMOS PASOS:
   1. Agrega más datos a tu Google Sheet
   2. Experimenta con diferentes preguntas
   3. Ajusta los parámetros (temperature, top_k, etc.)
   4. Prueba el modo interactivo: python main.py --interactive
   5. Explora el código fuente para entender los detalles

📚 RECURSOS:
   - README.md: Documentación completa
   - main.py: Modo interactivo
   - rag_system.py: Implementación del sistema
   - data_loader.py: Carga de datos

💡 CONSEJOS:
   - Guarda el índice FAISS para evitar recrearlo cada vez
   - Usa --use-existing-index para cargas más rápidas
   - Experimenta con diferentes modelos de Gemini
   - Monitorea el uso de tu API key

¡Gracias por completar el tutorial!
    """)
    
    print("="*70 + "\n")


if __name__ == "__main__":
    main()


