"""
Configuración del proyecto RAG con LangChain
"""
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# API Keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configuración de Google Sheets
# IMPORTANTE: Reemplaza este ID con el ID de tu hoja de Google Sheets
# El ID está en la URL: https://docs.google.com/spreadsheets/d/[ESTE_ES_EL_ID]/edit
SPREADSHEET_ID = "TU_SPREADSHEET_ID_AQUI"
SHEET_NAME = "Hoja 1"  # Nombre de la pestaña en tu Google Sheet

# Configuración del modelo
MODEL_NAME = "gemini-1.5-flash"  # O "gemini-pro" o "gemini-1.5-pro"
TEMPERATURE = 0.7  # Entre 0 (más determinista) y 1 (más creativo)

# Configuración de RAG
CHUNK_SIZE = 1000  # Tamaño de los chunks de texto
CHUNK_OVERLAP = 200  # Superposición entre chunks
TOP_K_DOCUMENTS = 3  # Número de documentos a recuperar

# Configuración de embeddings
EMBEDDING_MODEL = "models/embedding-001"  # Modelo de embeddings de Google

# Rutas
CREDENTIALS_PATH = "credentials.json"
FAISS_INDEX_PATH = "faiss_index"  # Ruta donde se guardará el índice FAISS

# Validación
if not GOOGLE_API_KEY or GOOGLE_API_KEY == "tu_api_key_de_gemini_aqui":
    print("⚠️  ADVERTENCIA: No se ha configurado GOOGLE_API_KEY en el archivo .env")
    print("   Por favor, copia .env.example a .env y agrega tu API key")

if SPREADSHEET_ID == "TU_SPREADSHEET_ID_AQUI":
    print("⚠️  ADVERTENCIA: No se ha configurado SPREADSHEET_ID en config.py")
    print("   Por favor, actualiza el SPREADSHEET_ID con el ID de tu Google Sheet")


