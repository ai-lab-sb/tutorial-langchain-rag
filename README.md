# Tutorial de LangChain con RAG usando FAISS y Gemini

Este tutorial te guiará paso a paso en la creación de un sistema RAG (Retrieval-Augmented Generation) utilizando LangChain, FAISS como base de datos vectorial, y Gemini como modelo de lenguaje.

## 📋 Tabla de Contenidos

1. [¿Qué es RAG?](#qué-es-rag)
2. [Requisitos Previos](#requisitos-previos)
3. [Instalación](#instalación)
4. [Configuración de Credenciales](#configuración-de-credenciales)
5. [Preparación de Datos](#preparación-de-datos)
6. [Estructura del Proyecto](#estructura-del-proyecto)
7. [Ejecución del Tutorial](#ejecución-del-tutorial)
8. [Explicación del Código](#explicación-del-código)

## 🤔 ¿Qué es RAG?

RAG (Retrieval-Augmented Generation) es una técnica que combina:
- **Recuperación de información**: Busca documentos relevantes en una base de datos
- **Generación**: Utiliza un LLM para generar respuestas basadas en los documentos recuperados

Esto permite que el modelo responda preguntas con información actualizada y específica de tu dominio.

## 📦 Requisitos Previos

- Python 3.8 o superior
- Una cuenta de Google (para Google Sheets y Gemini API)
- Conocimientos básicos de Python

## 🔧 Instalación

1. **Clona o navega al directorio del proyecto**

```bash
cd Documents/PROYECTOS/langchain-rag-tutorial
```

2. **Crea un entorno virtual (recomendado)**

```bash
python -m venv venv

# En Windows
venv\Scripts\activate

# En Linux/Mac
source venv/bin/activate
```

3. **Instala las dependencias**

```bash
pip install -r requirements.txt
```

## 🔑 Configuración de Credenciales

### 1. Obtener API Key de Gemini

1. Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Inicia sesión con tu cuenta de Google
3. Haz clic en "Create API Key"
4. Copia la API Key generada

### 2. Configurar Google Sheets API (para acceder a la hoja de datos)

1. Ve a [Google Cloud Console](https://console.cloud.google.com/)
2. Crea un nuevo proyecto o selecciona uno existente
3. Habilita la API de Google Sheets:
   - En el menú lateral, ve a "APIs y servicios" > "Biblioteca"
   - Busca "Google Sheets API"
   - Haz clic en "Habilitar"
4. Crea credenciales de cuenta de servicio:
   - Ve a "APIs y servicios" > "Credenciales"
   - Haz clic en "Crear credenciales" > "Cuenta de servicio"
   - Dale un nombre (ej: "langchain-rag-service")
   - Haz clic en "Crear y continuar"
   - Omite los permisos opcionales y haz clic en "Listo"
5. Descarga las credenciales:
   - Haz clic en la cuenta de servicio que acabas de crear
   - Ve a la pestaña "Claves"
   - Haz clic en "Agregar clave" > "Crear clave nueva"
   - Selecciona "JSON" y haz clic en "Crear"
   - Se descargará un archivo JSON - guárdalo como `credentials.json` en el directorio del proyecto

### 3. Configurar variables de entorno

1. Copia el archivo de ejemplo:

```bash
cp .env.example .env
```

2. Edita el archivo `.env` y agrega tu API Key de Gemini:

```
GOOGLE_API_KEY=tu_api_key_aqui
```

## 📊 Preparación de Datos

### Crear la Hoja de Google Sheets

1. Ve a [Google Sheets](https://sheets.google.com/)
2. Crea una nueva hoja de cálculo
3. Nómbrala: **"Conocimientos RAG Tutorial"**
4. Crea las siguientes columnas en la primera fila:
   - A1: `tema`
   - B1: `pregunta`
   - C1: `respuesta`

5. Agrega datos de ejemplo (puedes agregar más filas):

| tema | pregunta | respuesta |
|------|----------|-----------|
| Python | ¿Qué es Python? | Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Creado por Guido van Rossum en 1991. |
| Python | ¿Para qué se usa Python? | Python se utiliza para desarrollo web, análisis de datos, inteligencia artificial, automatización, scripting y mucho más. |
| LangChain | ¿Qué es LangChain? | LangChain es un framework para desarrollar aplicaciones potenciadas por modelos de lenguaje. Facilita la creación de cadenas de procesamiento y agentes. |
| RAG | ¿Qué es RAG? | RAG (Retrieval-Augmented Generation) es una técnica que combina recuperación de información con generación de texto usando LLMs. |
| FAISS | ¿Qué es FAISS? | FAISS (Facebook AI Similarity Search) es una biblioteca para búsqueda eficiente de similitud y clustering de vectores densos. |
| Embeddings | ¿Qué son los embeddings? | Los embeddings son representaciones vectoriales de texto que capturan el significado semántico en un espacio multidimensional. |
| Gemini | ¿Qué es Gemini? | Gemini es la familia de modelos de lenguaje de Google, diseñados para ser multimodales y altamente capaces. |
| Machine Learning | ¿Qué es el aprendizaje automático? | El aprendizaje automático es una rama de la IA que permite a las computadoras aprender de datos sin ser programadas explícitamente. |

6. Comparte la hoja con la cuenta de servicio:
   - Haz clic en "Compartir" en la esquina superior derecha
   - Pega el email de la cuenta de servicio (lo encuentras en `credentials.json` en el campo `client_email`)
   - Dale permisos de "Lector"
   - Haz clic en "Enviar"

7. Copia el ID de la hoja:
   - El ID está en la URL: `https://docs.google.com/spreadsheets/d/[ESTE_ES_EL_ID]/edit`
   - Guárdalo, lo necesitarás en el código

8. Edita el archivo `config.py` y actualiza el `SPREADSHEET_ID` con el ID de tu hoja.

## 📁 Estructura del Proyecto

```
langchain-rag-tutorial/
├── README.md                 # Este archivo
├── requirements.txt          # Dependencias del proyecto
├── .env.example             # Plantilla de variables de entorno
├── .env                     # Variables de entorno (NO subir a Git)
├── credentials.json         # Credenciales de Google (NO subir a Git)
├── .gitignore              # Archivos a ignorar en Git
├── config.py               # Configuración del proyecto
├── data_loader.py          # Carga de datos desde Google Sheets
├── rag_system.py           # Sistema RAG con FAISS
├── main.py                 # Script principal con ejemplos
└── tutorial_completo.py    # Tutorial paso a paso con explicaciones
```

## 🚀 Ejecución del Tutorial

### Opción 1: Tutorial Interactivo Completo

```bash
python tutorial_completo.py
```

Este script te guiará paso a paso por todo el proceso con explicaciones detalladas.

### Opción 2: Ejecutar el Sistema RAG Directamente

```bash
python main.py
```

Este script ejecuta el sistema RAG con ejemplos predefinidos.

### Opción 3: Modo Interactivo

```bash
python main.py --interactive
```

Esto te permitirá hacer preguntas al sistema en tiempo real.

## 📚 Explicación del Código

### 1. Carga de Datos (`data_loader.py`)

Este módulo se encarga de:
- Conectarse a Google Sheets usando las credenciales
- Leer los datos de la hoja
- Convertir los datos en documentos de LangChain

```python
# Conecta con Google Sheets
# Lee los datos
# Crea documentos con metadata
```

### 2. Sistema RAG (`rag_system.py`)

El sistema RAG incluye:
- **Embeddings**: Convierte texto a vectores usando Google Generative AI Embeddings
- **Vector Store (FAISS)**: Almacena y busca vectores similares eficientemente
- **Retriever**: Recupera los documentos más relevantes
- **LLM (Gemini)**: Genera respuestas basadas en el contexto recuperado
- **Chain**: Encadena todo el proceso

### 3. Flujo de RAG

```
Pregunta del Usuario
    ↓
Convertir a Embedding
    ↓
Buscar en FAISS (vectores similares)
    ↓
Recuperar Top-K documentos relevantes
    ↓
Construir prompt con contexto
    ↓
Enviar a Gemini
    ↓
Respuesta generada
```

## 🎯 Conceptos Clave

### Embeddings
Los embeddings convierten texto en vectores numéricos que representan el significado semántico. Textos con significados similares tienen vectores cercanos en el espacio vectorial.

### FAISS (Facebook AI Similarity Search)
FAISS es una biblioteca altamente optimizada para búsqueda de similitud. Permite:
- Indexar millones de vectores
- Búsquedas extremadamente rápidas
- Varios algoritmos de indexación

### Vector Store
Almacena los embeddings de tus documentos y permite búsquedas por similitud semántica.

### Retriever
Componente que recupera los documentos más relevantes basándose en la consulta del usuario.

### Chain
En LangChain, una chain conecta múltiples componentes para crear un flujo de procesamiento.

## 🔍 Personalización

### Cambiar el número de documentos recuperados

En `rag_system.py`, modifica:

```python
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})  # Cambia 3 por el número deseado
```

### Usar diferentes modelos de Gemini

```python
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",  # o "gemini-pro", "gemini-1.5-flash"
    temperature=0.7
)
```

### Agregar más fuentes de datos

Puedes extender `data_loader.py` para cargar desde:
- Archivos CSV
- PDFs
- Páginas web
- Bases de datos

## ⚠️ Troubleshooting

### Error: "API key not valid"
- Verifica que tu API key de Gemini esté correcta en el archivo `.env`
- Asegúrate de que la API key esté activa

### Error: "Permission denied" en Google Sheets
- Verifica que hayas compartido la hoja con el email de la cuenta de servicio
- Confirma que el SPREADSHEET_ID sea correcto

### Error: "Module not found"
- Asegúrate de haber instalado todas las dependencias: `pip install -r requirements.txt`
- Verifica que el entorno virtual esté activado

### Las respuestas no son relevantes
- Agrega más datos a tu Google Sheet
- Aumenta el número de documentos recuperados (parámetro `k`)
- Mejora la calidad de los documentos en tu base de conocimientos

## 📖 Recursos Adicionales

- [Documentación de LangChain](https://python.langchain.com/)
- [Documentación de FAISS](https://faiss.ai/)
- [Google AI Studio](https://makersuite.google.com/)
- [Google Sheets API](https://developers.google.com/sheets/api)

## 🎓 Próximos Pasos

1. Agrega más documentos a tu base de conocimientos
2. Experimenta con diferentes modelos de Gemini
3. Implementa un sistema de chat con memoria
4. Crea una interfaz web con Streamlit o Gradio
5. Implementa evaluación de respuestas
6. Agrega logging y monitoreo

## 📝 Notas Importantes

- **NO subas** el archivo `.env` ni `credentials.json` a Git
- El archivo `.gitignore` ya está configurado para ignorar estos archivos
- Mantén tus API keys seguras
- Revisa los límites de uso de la API de Gemini

## 🤝 Contribuciones

Si encuentras errores o tienes sugerencias, siéntete libre de mejorar este tutorial.

## 📄 Licencia

Este tutorial es de uso libre para fines educativos.

---

**¡Feliz aprendizaje! 🚀**


