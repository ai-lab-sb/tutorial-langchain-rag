"""
Sistema RAG (Retrieval-Augmented Generation) con FAISS y Gemini
"""
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.schema import Document
from typing import List, Dict
import config
import os


class RAGSystem:
    """
    Sistema RAG completo que integra:
    - Embeddings de Google
    - FAISS como vector store
    - Gemini como LLM
    - Chain de recuperación y generación
    """
    
    def __init__(self):
        """Inicializa el sistema RAG"""
        self.embeddings = None
        self.vectorstore = None
        self.llm = None
        self.qa_chain = None
        
    def setup_embeddings(self):
        """Configura el modelo de embeddings"""
        print("🔧 Configurando embeddings de Google...")
        
        try:
            self.embeddings = GoogleGenerativeAIEmbeddings(
                model=config.EMBEDDING_MODEL,
                google_api_key=config.GOOGLE_API_KEY
            )
            print("✅ Embeddings configurados correctamente")
            return True
        except Exception as e:
            print(f"❌ Error al configurar embeddings: {str(e)}")
            return False
    
    def create_vectorstore(self, documents: List[Document], save_local: bool = True):
        """
        Crea el vector store con FAISS a partir de los documentos.
        
        Args:
            documents: Lista de documentos a indexar
            save_local: Si True, guarda el índice localmente
        """
        print(f"🔨 Creando vector store con {len(documents)} documentos...")
        
        try:
            # Crear el vector store con FAISS
            self.vectorstore = FAISS.from_documents(
                documents=documents,
                embedding=self.embeddings
            )
            
            print("✅ Vector store creado correctamente")
            
            # Guardar localmente si se solicita
            if save_local:
                self.save_vectorstore()
            
            return True
        except Exception as e:
            print(f"❌ Error al crear vector store: {str(e)}")
            return False
    
    def save_vectorstore(self):
        """Guarda el vector store localmente"""
        try:
            if self.vectorstore:
                self.vectorstore.save_local(config.FAISS_INDEX_PATH)
                print(f"💾 Vector store guardado en: {config.FAISS_INDEX_PATH}")
        except Exception as e:
            print(f"⚠️  Advertencia al guardar vector store: {str(e)}")
    
    def load_vectorstore(self):
        """Carga un vector store previamente guardado"""
        try:
            if os.path.exists(config.FAISS_INDEX_PATH):
                print("📂 Cargando vector store existente...")
                self.vectorstore = FAISS.load_local(
                    config.FAISS_INDEX_PATH,
                    self.embeddings,
                    allow_dangerous_deserialization=True
                )
                print("✅ Vector store cargado correctamente")
                return True
            else:
                print(f"⚠️  No se encontró vector store en: {config.FAISS_INDEX_PATH}")
                return False
        except Exception as e:
            print(f"❌ Error al cargar vector store: {str(e)}")
            return False
    
    def setup_llm(self):
        """Configura el modelo de lenguaje Gemini"""
        print("🤖 Configurando modelo Gemini...")
        
        try:
            self.llm = ChatGoogleGenerativeAI(
                model=config.MODEL_NAME,
                temperature=config.TEMPERATURE,
                google_api_key=config.GOOGLE_API_KEY
            )
            print("✅ Modelo Gemini configurado correctamente")
            return True
        except Exception as e:
            print(f"❌ Error al configurar Gemini: {str(e)}")
            return False
    
    def setup_qa_chain(self):
        """Configura la cadena de pregunta-respuesta"""
        print("🔗 Configurando cadena RAG...")
        
        # Crear el prompt template personalizado
        template = """Usa el siguiente contexto para responder la pregunta al final.
Si no sabes la respuesta, simplemente di que no lo sabes, no intentes inventar una respuesta.
Responde de manera clara, concisa y útil.

Contexto:
{context}

Pregunta: {question}

Respuesta útil:"""
        
        PROMPT = PromptTemplate(
            template=template,
            input_variables=["context", "question"]
        )
        
        try:
            # Crear el retriever
            retriever = self.vectorstore.as_retriever(
                search_kwargs={"k": config.TOP_K_DOCUMENTS}
            )
            
            # Crear la cadena de QA
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                chain_type="stuff",
                retriever=retriever,
                return_source_documents=True,
                chain_type_kwargs={"prompt": PROMPT}
            )
            
            print("✅ Cadena RAG configurada correctamente")
            return True
        except Exception as e:
            print(f"❌ Error al configurar cadena: {str(e)}")
            return False
    
    def query(self, question: str, verbose: bool = True) -> Dict:
        """
        Realiza una consulta al sistema RAG.
        
        Args:
            question: Pregunta a realizar
            verbose: Si True, muestra información detallada
            
        Returns:
            Diccionario con la respuesta y documentos fuente
        """
        if not self.qa_chain:
            return {
                "error": "El sistema RAG no está inicializado correctamente"
            }
        
        try:
            if verbose:
                print(f"\n❓ Pregunta: {question}")
                print("🔍 Buscando información relevante...")
            
            # Ejecutar la consulta
            result = self.qa_chain.invoke({"query": question})
            
            if verbose:
                print("✅ Respuesta generada\n")
                self.print_result(result)
            
            return result
            
        except Exception as e:
            print(f"❌ Error al procesar consulta: {str(e)}")
            return {"error": str(e)}
    
    def print_result(self, result: Dict):
        """
        Imprime el resultado de una consulta de manera formateada.
        
        Args:
            result: Resultado de la consulta
        """
        print("="*70)
        print("💡 RESPUESTA:")
        print("="*70)
        print(result.get("result", "No se generó respuesta"))
        
        # Mostrar documentos fuente
        source_docs = result.get("source_documents", [])
        if source_docs:
            print("\n" + "="*70)
            print("📚 DOCUMENTOS FUENTE UTILIZADOS:")
            print("="*70)
            for i, doc in enumerate(source_docs, 1):
                print(f"\n📄 Documento {i}:")
                print(f"   Tema: {doc.metadata.get('tema', 'N/A')}")
                print(f"   Pregunta: {doc.metadata.get('pregunta', 'N/A')}")
                print(f"   Contenido: {doc.page_content[:200]}...")
        print("="*70 + "\n")
    
    def initialize(self, documents: List[Document] = None, use_existing_index: bool = False):
        """
        Inicializa todo el sistema RAG.
        
        Args:
            documents: Documentos para crear el vector store (si no se usa índice existente)
            use_existing_index: Si True, intenta cargar un índice existente
            
        Returns:
            True si la inicialización fue exitosa
        """
        print("\n" + "="*70)
        print("🚀 INICIALIZANDO SISTEMA RAG")
        print("="*70 + "\n")
        
        # 1. Configurar embeddings
        if not self.setup_embeddings():
            return False
        
        # 2. Crear o cargar vector store
        if use_existing_index and self.load_vectorstore():
            print("✅ Usando vector store existente")
        elif documents:
            if not self.create_vectorstore(documents):
                return False
        else:
            print("❌ No se proporcionaron documentos ni existe un índice previo")
            return False
        
        # 3. Configurar LLM
        if not self.setup_llm():
            return False
        
        # 4. Configurar cadena
        if not self.setup_qa_chain():
            return False
        
        print("\n" + "="*70)
        print("✅ SISTEMA RAG INICIALIZADO CORRECTAMENTE")
        print("="*70 + "\n")
        
        return True


if __name__ == "__main__":
    """
    Script de prueba del sistema RAG
    """
    print("🧪 Probando sistema RAG...\n")
    
    # Crear documentos de prueba
    test_docs = [
        Document(
            page_content="Python es un lenguaje de programación de alto nivel.",
            metadata={"tema": "Python", "pregunta": "¿Qué es Python?"}
        ),
        Document(
            page_content="RAG combina recuperación de información con generación de texto.",
            metadata={"tema": "RAG", "pregunta": "¿Qué es RAG?"}
        )
    ]
    
    # Inicializar sistema
    rag = RAGSystem()
    if rag.initialize(documents=test_docs):
        # Hacer una consulta de prueba
        rag.query("¿Qué es Python?")


