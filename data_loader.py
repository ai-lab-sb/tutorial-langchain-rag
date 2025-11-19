"""
Módulo para cargar datos desde Google Sheets
"""
import gspread
from google.oauth2.service_account import Credentials
from langchain.schema import Document
from typing import List
import config


def load_data_from_google_sheets() -> List[Document]:
    """
    Carga datos desde Google Sheets y los convierte en documentos de LangChain.
    
    Returns:
        List[Document]: Lista de documentos con contenido y metadata
    """
    print("📊 Conectando con Google Sheets...")
    
    # Definir los scopes necesarios
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets.readonly",
        "https://www.googleapis.com/auth/drive.readonly"
    ]
    
    try:
        # Autenticar con las credenciales
        credentials = Credentials.from_service_account_file(
            config.CREDENTIALS_PATH,
            scopes=scopes
        )
        
        # Conectar con Google Sheets
        client = gspread.authorize(credentials)
        
        # Abrir la hoja por ID
        spreadsheet = client.open_by_key(config.SPREADSHEET_ID)
        sheet = spreadsheet.worksheet(config.SHEET_NAME)
        
        # Obtener todos los datos
        data = sheet.get_all_records()
        
        print(f"✅ Se encontraron {len(data)} filas de datos")
        
        # Convertir a documentos de LangChain
        documents = []
        for row in data:
            # Crear el contenido del documento
            # Combinamos pregunta y respuesta para tener contexto completo
            content = f"Tema: {row.get('tema', 'N/A')}\n"
            content += f"Pregunta: {row.get('pregunta', 'N/A')}\n"
            content += f"Respuesta: {row.get('respuesta', 'N/A')}"
            
            # Crear metadata
            metadata = {
                "tema": row.get('tema', 'N/A'),
                "pregunta": row.get('pregunta', 'N/A'),
                "source": "Google Sheets"
            }
            
            # Crear documento
            doc = Document(
                page_content=content,
                metadata=metadata
            )
            documents.append(doc)
        
        print(f"✅ Se crearon {len(documents)} documentos")
        return documents
        
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo {config.CREDENTIALS_PATH}")
        print("   Asegúrate de haber descargado las credenciales de la cuenta de servicio")
        return []
    except Exception as e:
        print(f"❌ Error al cargar datos: {str(e)}")
        print("   Verifica que:")
        print("   1. El SPREADSHEET_ID en config.py sea correcto")
        print("   2. Hayas compartido la hoja con el email de la cuenta de servicio")
        print("   3. El nombre de la hoja sea correcto (por defecto 'Hoja 1')")
        return []


def print_documents_summary(documents: List[Document]):
    """
    Imprime un resumen de los documentos cargados.
    
    Args:
        documents: Lista de documentos
    """
    print("\n" + "="*70)
    print("📚 RESUMEN DE DOCUMENTOS CARGADOS")
    print("="*70)
    
    if not documents:
        print("No hay documentos para mostrar")
        return
    
    # Contar temas únicos
    temas = set(doc.metadata.get('tema', 'N/A') for doc in documents)
    print(f"\n📊 Total de documentos: {len(documents)}")
    print(f"📑 Temas únicos: {len(temas)}")
    print(f"🏷️  Temas: {', '.join(sorted(temas))}")
    
    # Mostrar algunos ejemplos
    print("\n📝 Ejemplos de documentos:")
    print("-" * 70)
    for i, doc in enumerate(documents[:3], 1):
        print(f"\nDocumento {i}:")
        print(f"  Tema: {doc.metadata.get('tema', 'N/A')}")
        print(f"  Pregunta: {doc.metadata.get('pregunta', 'N/A')}")
        print(f"  Contenido (primeros 100 caracteres):")
        print(f"  {doc.page_content[:100]}...")
    
    if len(documents) > 3:
        print(f"\n... y {len(documents) - 3} documentos más")
    
    print("="*70 + "\n")


if __name__ == "__main__":
    """
    Script de prueba para verificar la carga de datos
    """
    print("🧪 Probando carga de datos desde Google Sheets...\n")
    
    documents = load_data_from_google_sheets()
    print_documents_summary(documents)


