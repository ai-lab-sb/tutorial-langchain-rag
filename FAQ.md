# ❓ Preguntas Frecuentes (FAQ)

## General

### ¿Qué es este proyecto?

Un tutorial completo para aprender a crear un sistema RAG (Retrieval-Augmented Generation) usando LangChain, FAISS y Gemini. Incluye código funcional y explicaciones detalladas.

### ¿Necesito experiencia previa?

Se recomienda conocimientos básicos de:
- Python
- Conceptos básicos de IA/ML (opcional pero útil)

### ¿Cuánto tiempo toma completar el tutorial?

- **Tutorial rápido**: 5-10 minutos
- **Tutorial completo**: 30-45 minutos
- **Experimentación**: Ilimitado 😊

## Instalación y Configuración

### ¿Qué versión de Python necesito?

Python 3.8 o superior. Recomendamos Python 3.10 o 3.11.

```bash
python --version
```

### ¿Necesito una GPU?

No, este tutorial funciona perfectamente con CPU. FAISS tiene versión optimizada para CPU.

### ¿Tengo que pagar por usar Gemini?

Gemini tiene un plan gratuito generoso que es suficiente para este tutorial. Revisa los [límites actuales](https://ai.google.dev/pricing).

### ¿Por qué no usar OpenAI/ChatGPT?

Puedes! El código es fácil de adaptar. Usa:
```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
```

### ¿Puedo usar otros modelos de código abierto?

Sí! Puedes usar modelos locales con Ollama:
```python
from langchain_community.llms import Ollama
llm = Ollama(model="llama2")
```

## Google Sheets

### ¿Por qué Google Sheets y no CSV?

Google Sheets permite:
- ✓ Actualizar datos sin modificar código
- ✓ Colaboración en equipo
- ✓ Acceso desde cualquier lugar
- ✓ Interfaz visual amigable

Pero puedes usar CSV si prefieres (ver "Alternativas a Google Sheets" abajo).

### ¿Cuántos datos puedo poner en Google Sheets?

Google Sheets soporta hasta 10 millones de celdas. Para este tutorial, recomendamos 100-1000 filas para empezar.

### Mi cuenta de servicio no puede acceder a la hoja

Asegúrate de:
1. Haber compartido la hoja con el email de la cuenta de servicio
2. El email está en `credentials.json` → `client_email`
3. Diste al menos permisos de "Lector"

### ¿Puedo usar múltiples hojas/pestañas?

Sí! Modifica `data_loader.py` para iterar sobre múltiples hojas:
```python
for sheet_name in ["Hoja1", "Hoja2", "Hoja3"]:
    sheet = spreadsheet.worksheet(sheet_name)
    # procesar...
```

## FAISS y Vector Store

### ¿Qué es FAISS?

FAISS (Facebook AI Similarity Search) es una biblioteca para búsqueda eficiente de vectores similares. Perfecta para RAG.

### ¿FAISS vs otros vector stores?

| Vector Store | Ventajas | Desventajas |
|--------------|----------|-------------|
| FAISS | Rápido, local, gratis | No persistente por defecto |
| Pinecone | Cloud, escalable | De pago |
| Chroma | Fácil, persistente | Más lento |
| Weaviate | Muy completo | Complejo de configurar |

Para aprender, FAISS es ideal.

### ¿Tengo que recrear el índice cada vez?

No! El código guarda el índice localmente:
```bash
python main.py --use-existing-index
```

### ¿Cómo actualizo los datos?

1. Actualiza tu Google Sheet
2. Elimina la carpeta `faiss_index/`
3. Ejecuta de nuevo para recrear el índice

### ¿Cuántos documentos puede manejar FAISS?

FAISS puede manejar millones de vectores. Para este tutorial:
- < 1,000 documentos: Instantáneo
- 1,000-10,000: Unos segundos
- 10,000+: Minutos (considera usar GPU)

## RAG y Embeddings

### ¿Qué son los embeddings?

Representaciones numéricas (vectores) de texto que capturan el significado semántico. Textos similares tienen embeddings similares.

### ¿Por qué usar embeddings de Google?

- Gratuitos (con límites generosos)
- Alta calidad
- Fácil integración con Gemini
- Sin necesidad de hardware especial

### ¿Puedo usar otros embeddings?

Sí! Opciones:
```python
# OpenAI
from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()

# HuggingFace (local, gratis)
from langchain_community.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
```

### ¿Qué es el parámetro K en top-K?

K es el número de documentos a recuperar. Por defecto: 3.
- K bajo (1-2): Respuestas más enfocadas
- K alto (5-10): Más contexto pero puede ser ruidoso

### Las respuestas no son relevantes

Posibles soluciones:
1. **Agrega más datos** de calidad
2. **Aumenta K**: Recupera más documentos
3. **Mejora tus documentos**: Hazlos más detallados
4. **Ajusta temperature**: Baja para respuestas más deterministas

### ¿Cómo funciona la búsqueda semántica?

```
"¿Qué es Python?" 
   ↓ (embedding)
[0.1, 0.5, 0.3, ...]
   ↓ (FAISS búsqueda)
Documentos más cercanos en espacio vectorial
   ↓
"Tema: Python, Pregunta: ¿Qué es Python?"
```

## Personalización

### ¿Cómo cambio el modelo de Gemini?

En `config.py`:
```python
MODEL_NAME = "gemini-1.5-pro"  # Más potente
# O
MODEL_NAME = "gemini-1.5-flash"  # Más rápido
```

### ¿Qué hace el parámetro temperature?

Controla la "creatividad":
- 0.0: Muy determinista, siempre la misma respuesta
- 0.7: Balance (recomendado para RAG)
- 1.0+: Más creativo pero menos predecible

### ¿Cómo cambio el prompt?

En `rag_system.py`, modifica el `template`:
```python
template = """Eres un asistente experto.
Usa este contexto para responder:

{context}

Pregunta: {question}
Respuesta:"""
```

### ¿Puedo agregar memoria/historial de chat?

Sí! Usa `ConversationBufferMemory`:
```python
from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory()
```

Ver documentación de LangChain para más detalles.

## Alternativas a Google Sheets

### ¿Puedo usar CSV?

Sí! Crea `data_loader_csv.py`:
```python
import pandas as pd
from langchain.schema import Document

def load_from_csv(filepath):
    df = pd.read_csv(filepath)
    documents = []
    for _, row in df.iterrows():
        doc = Document(
            page_content=f"Tema: {row['tema']}\nPregunta: {row['pregunta']}\nRespuesta: {row['respuesta']}",
            metadata={"tema": row['tema'], "pregunta": row['pregunta']}
        )
        documents.append(doc)
    return documents
```

### ¿Puedo cargar PDFs?

Sí! Usa `PyPDFLoader`:
```python
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("documento.pdf")
documents = loader.load()
```

### ¿Puedo scrappear páginas web?

Sí! Usa `WebBaseLoader`:
```python
from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://ejemplo.com")
documents = loader.load()
```

### ¿Bases de datos SQL?

Sí! Usa `SQLDatabaseLoader` o consultas directas con pandas.

## Rendimiento

### El sistema es lento

Optimizaciones:
1. **Usa índice existente**: `--use-existing-index`
2. **Reduce datos**: Empieza con menos documentos
3. **Usa modelos más rápidos**: `gemini-1.5-flash`
4. **Ajusta batch size** en FAISS

### ¿Cómo monitoreo el uso de API?

Ve a [Google AI Studio](https://makersuite.google.com/) para ver tu uso de API.

### ¿Cuántas llamadas hace el sistema por pregunta?

Por pregunta:
- 1 llamada para embedding (pregunta)
- 1 llamada a Gemini (generación)
- Total: 2 llamadas API

## Seguridad

### ¿Es seguro compartir mi código?

**Sí**, siempre que:
- ❌ NO subas `.env`
- ❌ NO subas `credentials.json`
- ✓ Usa `.gitignore` (ya incluido)

### ¿Dónde guardo las credenciales?

- Localmente en `.env` y `credentials.json`
- Nunca en repositorios públicos
- Usa variables de entorno en producción

### ¿Puedo rotar mi API key?

Sí, en Google AI Studio:
1. Genera nueva key
2. Actualiza `.env`
3. Elimina la key antigua

## Despliegue

### ¿Puedo desplegar esto como aplicación web?

¡Sí! Opciones:
1. **Streamlit** (más fácil)
2. **FastAPI** + React
3. **Gradio**

### ¿Cómo escalo esto a producción?

Consideraciones:
- Usa vector stores en cloud (Pinecone, Weaviate)
- Implementa caché de respuestas
- Rate limiting
- Logging y monitoreo
- Manejo de errores robusto

### ¿Dónde hospedar?

- Google Cloud Run (recomendado para Gemini)
- AWS Lambda
- Heroku
- Railway
- Render

## Problemas Comunes

### ImportError: No module named 'X'

```bash
pip install -r requirements.txt
```

### "API key not valid"

1. Verifica que tu key esté correcta en `.env`
2. No debe tener espacios
3. Formato: `GOOGLE_API_KEY=AIzaSy...`

### "Rate limit exceeded"

Estás haciendo demasiadas llamadas. Espera unos minutos o actualiza tu plan.

### Los documentos no se están guardando

- Verifica que `credentials.json` sea válido
- Confirma que compartiste la hoja
- Revisa el SPREADSHEET_ID

### FAISS no se instala

En Windows, podrías necesitar:
```bash
pip install faiss-cpu --no-cache
```

## Aprendizaje

### ¿Dónde aprendo más sobre RAG?

- [LangChain Docs](https://python.langchain.com/)
- [RAG Paper Original](https://arxiv.org/abs/2005.11401)
- [FAISS Documentation](https://faiss.ai/)

### ¿Cursos recomendados?

- DeepLearning.AI - LangChain courses
- YouTube: Sam Witteveen, James Briggs
- Blog: Pinecone Learning Center

### ¿Cómo contribuyo a este proyecto?

Este es un proyecto educativo. Siéntete libre de:
- Mejorar la documentación
- Agregar ejemplos
- Reportar bugs
- Compartir con otros

## Siguiente Nivel

### ¿Qué sigue después de este tutorial?

1. **Agrega más fuentes**: PDFs, URLs, bases de datos
2. **Implementa evaluación**: Mide calidad de respuestas
3. **Agrega memoria**: Conversaciones con contexto
4. **Crea interfaz**: Streamlit/Gradio
5. **Agentes**: Multi-step reasoning
6. **Fine-tuning**: Personaliza embeddings

### Proyectos sugeridos

1. **Chatbot de documentación**: Documentos de tu empresa
2. **Asistente de estudio**: PDFs de tus materias
3. **FAQ automático**: Base de conocimientos
4. **Búsqueda semántica**: Para tu blog/sitio web
5. **Asistente de código**: Documentación técnica

---

## ¿Más preguntas?

Si tu pregunta no está aquí:
1. Revisa el [README.md](README.md) completo
2. Consulta la documentación oficial de LangChain
3. Busca en Stack Overflow
4. Experimenta y aprende! 🚀

---

**Última actualización**: Noviembre 2025


