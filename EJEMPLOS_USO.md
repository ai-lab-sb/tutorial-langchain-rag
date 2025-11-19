# 💡 Ejemplos de Uso

Esta guía muestra diferentes formas de usar el sistema RAG.

## 🎯 Casos de Uso Básicos

### 1. Ejecución Simple

```bash
python main.py
```

**Resultado**: Ejecuta 5 preguntas de ejemplo y muestra las respuestas.

### 2. Modo Interactivo

```bash
python main.py --interactive
```

**Resultado**: Puedes hacer preguntas ilimitadas hasta que escribas "salir".

**Ejemplo de sesión:**
```
❓ Tu pregunta: ¿Qué es Python?
💡 RESPUESTA:
Python es un lenguaje de programación de alto nivel...

❓ Tu pregunta: ¿Y para qué sirve?
💡 RESPUESTA:
Python se utiliza en múltiples ámbitos...

❓ Tu pregunta: salir
👋 ¡Hasta luego!
```

### 3. Usar Índice Existente (Más Rápido)

```bash
python main.py --use-existing-index
```

**Resultado**: Carga el índice FAISS guardado en lugar de recrearlo. Mucho más rápido en ejecuciones posteriores.

### 4. Tutorial Completo Paso a Paso

```bash
python tutorial_completo.py
```

**Resultado**: Tutorial interactivo con explicaciones detalladas de cada componente.

## 🔧 Uso Programático

### Ejemplo 1: Sistema RAG Básico

```python
from data_loader import load_data_from_google_sheets
from rag_system import RAGSystem

# Cargar datos
documents = load_data_from_google_sheets()

# Inicializar sistema
rag = RAGSystem()
rag.initialize(documents=documents)

# Hacer pregunta
result = rag.query("¿Qué es Python?")
print(result['result'])
```

### Ejemplo 2: Múltiples Preguntas

```python
from rag_system import RAGSystem
from data_loader import load_data_from_google_sheets

# Setup
documents = load_data_from_google_sheets()
rag = RAGSystem()
rag.initialize(documents=documents)

# Lista de preguntas
questions = [
    "¿Qué es Python?",
    "¿Qué es RAG?",
    "¿Cómo funcionan los embeddings?"
]

# Procesar todas
for question in questions:
    print(f"\n❓ {question}")
    result = rag.query(question, verbose=False)
    print(f"💡 {result['result']}\n")
```

### Ejemplo 3: Con Metadata y Fuentes

```python
from rag_system import RAGSystem
from data_loader import load_data_from_google_sheets

documents = load_data_from_google_sheets()
rag = RAGSystem()
rag.initialize(documents=documents)

result = rag.query("¿Qué es FAISS?", verbose=False)

# Respuesta
print("RESPUESTA:", result['result'])

# Fuentes utilizadas
print("\nFUENTES:")
for i, doc in enumerate(result['source_documents'], 1):
    print(f"{i}. Tema: {doc.metadata['tema']}")
    print(f"   Pregunta: {doc.metadata['pregunta']}")
```

### Ejemplo 4: Personalizar Configuración

```python
from rag_system import RAGSystem
from langchain_google_genai import ChatGoogleGenerativeAI
from data_loader import load_data_from_google_sheets
import config

# Cargar datos
documents = load_data_from_google_sheets()

# Crear sistema con configuración personalizada
rag = RAGSystem()

# Embeddings
rag.setup_embeddings()

# Vector store
rag.create_vectorstore(documents)

# LLM personalizado (más creativo)
rag.llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0.9,  # Más creativo
    google_api_key=config.GOOGLE_API_KEY
)

# Chain con más documentos
rag.vectorstore
retriever = rag.vectorstore.as_retriever(
    search_kwargs={"k": 5}  # Recuperar 5 documentos en lugar de 3
)

rag.setup_qa_chain()

# Usar
result = rag.query("Explica creativamente qué es RAG")
```

### Ejemplo 5: Guardar Respuestas a Archivo

```python
from rag_system import RAGSystem
from data_loader import load_data_from_google_sheets
import json
from datetime import datetime

documents = load_data_from_google_sheets()
rag = RAGSystem()
rag.initialize(documents=documents)

questions = [
    "¿Qué es Python?",
    "¿Qué es RAG?",
    "¿Qué es FAISS?"
]

results = []

for question in questions:
    result = rag.query(question, verbose=False)
    
    results.append({
        "timestamp": datetime.now().isoformat(),
        "question": question,
        "answer": result['result'],
        "sources": [
            {
                "tema": doc.metadata['tema'],
                "pregunta": doc.metadata['pregunta']
            }
            for doc in result['source_documents']
        ]
    })

# Guardar a JSON
with open('respuestas.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("✅ Respuestas guardadas en respuestas.json")
```

## 🎨 Integración con Streamlit

Crea `app_streamlit.py`:

```python
import streamlit as st
from rag_system import RAGSystem
from data_loader import load_data_from_google_sheets

@st.cache_resource
def load_rag_system():
    """Cargar sistema RAG (se cachea para no recargar)"""
    documents = load_data_from_google_sheets()
    rag = RAGSystem()
    rag.initialize(documents=documents)
    return rag

# Configurar página
st.set_page_config(
    page_title="Sistema RAG",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Sistema RAG con LangChain")
st.markdown("Pregunta cualquier cosa sobre los temas en la base de conocimientos")

# Cargar sistema
rag = load_rag_system()

# Input del usuario
question = st.text_input("Tu pregunta:", placeholder="¿Qué es Python?")

if st.button("Buscar Respuesta") and question:
    with st.spinner("Buscando información relevante..."):
        result = rag.query(question, verbose=False)
    
    # Mostrar respuesta
    st.success("Respuesta:")
    st.write(result['result'])
    
    # Mostrar fuentes
    st.info("📚 Fuentes:")
    for i, doc in enumerate(result['source_documents'], 1):
        with st.expander(f"Fuente {i}: {doc.metadata['tema']}"):
            st.write(f"**Pregunta:** {doc.metadata['pregunta']}")
            st.write(f"**Contenido:** {doc.page_content}")

# Sidebar con información
with st.sidebar:
    st.header("ℹ️ Información")
    st.write("Sistema RAG usando:")
    st.write("- 🧠 LangChain")
    st.write("- ⚡ FAISS")
    st.write("- 🤖 Gemini")
    st.write("- 📊 Google Sheets")
```

**Ejecutar:**
```bash
pip install streamlit
streamlit run app_streamlit.py
```

## 🌐 API REST con FastAPI

Crea `api.py`:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag_system import RAGSystem
from data_loader import load_data_from_google_sheets

# Inicializar FastAPI
app = FastAPI(title="RAG API")

# Cargar sistema RAG al inicio
print("Cargando sistema RAG...")
documents = load_data_from_google_sheets()
rag = RAGSystem()
rag.initialize(documents=documents)
print("✅ Sistema RAG listo")

class Question(BaseModel):
    question: str
    return_sources: bool = True

class Answer(BaseModel):
    question: str
    answer: str
    sources: list = []

@app.get("/")
def root():
    return {"message": "RAG API está funcionando"}

@app.post("/query", response_model=Answer)
def query(q: Question):
    """Endpoint para hacer preguntas"""
    try:
        result = rag.query(q.question, verbose=False)
        
        sources = []
        if q.return_sources and 'source_documents' in result:
            sources = [
                {
                    "tema": doc.metadata['tema'],
                    "pregunta": doc.metadata['pregunta'],
                    "contenido": doc.page_content[:200]
                }
                for doc in result['source_documents']
            ]
        
        return Answer(
            question=q.question,
            answer=result['result'],
            sources=sources
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "healthy"}
```

**Instalar y ejecutar:**
```bash
pip install fastapi uvicorn
uvicorn api:app --reload
```

**Probar:**
```bash
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"question": "¿Qué es Python?"}'
```

## 📊 Evaluación de Respuestas

Crea `evaluate.py`:

```python
from rag_system import RAGSystem
from data_loader import load_data_from_google_sheets

# Casos de prueba
test_cases = [
    {
        "question": "¿Qué es Python?",
        "expected_keywords": ["lenguaje", "programación", "alto nivel"]
    },
    {
        "question": "¿Qué es RAG?",
        "expected_keywords": ["retrieval", "generation", "documentos"]
    },
    {
        "question": "¿Qué es FAISS?",
        "expected_keywords": ["facebook", "búsqueda", "vectores"]
    }
]

# Inicializar sistema
documents = load_data_from_google_sheets()
rag = RAGSystem()
rag.initialize(documents=documents)

print("🧪 Evaluando sistema RAG...\n")

total = len(test_cases)
passed = 0

for i, test in enumerate(test_cases, 1):
    print(f"Test {i}/{total}: {test['question']}")
    
    result = rag.query(test['question'], verbose=False)
    answer = result['result'].lower()
    
    # Verificar keywords
    found = [kw for kw in test['expected_keywords'] if kw in answer]
    
    if len(found) >= 2:  # Al menos 2 keywords
        print(f"  ✅ PASSED - Keywords encontradas: {found}")
        passed += 1
    else:
        print(f"  ❌ FAILED - Solo encontró: {found}")
    
    print()

print(f"\n📊 Resultado: {passed}/{total} tests pasados ({passed/total*100:.1f}%)")
```

## 🔄 Actualización Automática de Índice

Crea `auto_update.py`:

```python
import os
import time
import hashlib
from data_loader import load_data_from_google_sheets
from rag_system import RAGSystem
import config

def get_data_hash(documents):
    """Genera hash de los datos para detectar cambios"""
    content = "".join([doc.page_content for doc in documents])
    return hashlib.md5(content.encode()).hexdigest()

def update_if_changed():
    """Actualiza índice si los datos cambiaron"""
    print("🔍 Verificando si hay cambios...")
    
    # Cargar datos actuales
    documents = load_data_from_google_sheets()
    current_hash = get_data_hash(documents)
    
    # Leer hash anterior
    hash_file = "data_hash.txt"
    previous_hash = None
    if os.path.exists(hash_file):
        with open(hash_file, 'r') as f:
            previous_hash = f.read().strip()
    
    # Comparar
    if current_hash != previous_hash:
        print("🔄 Cambios detectados, actualizando índice...")
        
        # Recrear índice
        rag = RAGSystem()
        rag.setup_embeddings()
        rag.create_vectorstore(documents, save_local=True)
        
        # Guardar nuevo hash
        with open(hash_file, 'w') as f:
            f.write(current_hash)
        
        print("✅ Índice actualizado")
    else:
        print("✓ No hay cambios")

if __name__ == "__main__":
    # Ejecutar cada 5 minutos
    while True:
        try:
            update_if_changed()
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print("⏰ Esperando 5 minutos...\n")
        time.sleep(300)  # 5 minutos
```

## 📈 Métricas y Logging

Crea `rag_with_logging.py`:

```python
import logging
import time
from rag_system import RAGSystem
from data_loader import load_data_from_google_sheets

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('rag_system.log'),
        logging.StreamHandler()
    ]
)

class RAGWithLogging(RAGSystem):
    """RAG System con logging y métricas"""
    
    def query(self, question, verbose=True):
        start_time = time.time()
        logging.info(f"Nueva consulta: {question}")
        
        try:
            result = super().query(question, verbose)
            
            elapsed = time.time() - start_time
            num_sources = len(result.get('source_documents', []))
            
            logging.info(f"Consulta exitosa en {elapsed:.2f}s con {num_sources} fuentes")
            
            return result
            
        except Exception as e:
            logging.error(f"Error en consulta: {str(e)}")
            raise

# Usar
if __name__ == "__main__":
    documents = load_data_from_google_sheets()
    rag = RAGWithLogging()
    rag.initialize(documents=documents)
    
    questions = [
        "¿Qué es Python?",
        "¿Qué es RAG?",
        "¿Qué es FAISS?"
    ]
    
    for q in questions:
        rag.query(q, verbose=False)
```

---

## 🎓 Consejos para Mejores Resultados

1. **Preguntas claras**: Sé específico en tus preguntas
2. **Datos de calidad**: Agrega información completa y precisa
3. **Ajusta K**: Experimenta con diferentes valores de documentos a recuperar
4. **Temperature**: Ajusta según necesites respuestas deterministas o creativas
5. **Prompt engineering**: Personaliza el prompt template para tu caso de uso

---

**¡Explora y experimenta! 🚀**


