"""
Script simple para probar la instalación y configuración básica
"""
import sys

def test_imports():
    """Prueba que todas las librerías necesarias estén instaladas"""
    print("🧪 Probando importaciones...\n")
    
    tests = {
        "langchain": "LangChain",
        "langchain_google_genai": "LangChain Google GenAI",
        "langchain_community": "LangChain Community",
        "faiss": "FAISS",
        "gspread": "gspread (Google Sheets)",
        "google.generativeai": "Google Generative AI",
        "dotenv": "python-dotenv",
        "pandas": "Pandas",
        "numpy": "NumPy"
    }
    
    failed = []
    passed = []
    
    for module, name in tests.items():
        try:
            __import__(module)
            print(f"✅ {name}")
            passed.append(name)
        except ImportError as e:
            print(f"❌ {name} - Error: {e}")
            failed.append(name)
    
    print(f"\n📊 Resultado: {len(passed)}/{len(tests)} módulos instalados correctamente")
    
    if failed:
        print(f"\n⚠️  Módulos faltantes: {', '.join(failed)}")
        print("\n💡 Para instalar:")
        print("   pip install -r requirements.txt")
        return False
    
    return True


def test_env():
    """Prueba la configuración del archivo .env"""
    print("\n🔑 Probando variables de entorno...\n")
    
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        print("❌ GOOGLE_API_KEY no encontrada en .env")
        print("\n💡 Pasos para configurar:")
        print("   1. Copia .env.example a .env")
        print("   2. Obtén tu API key en: https://makersuite.google.com/app/apikey")
        print("   3. Agrega la key al archivo .env")
        return False
    
    if api_key == "tu_api_key_de_gemini_aqui":
        print("⚠️  GOOGLE_API_KEY no ha sido actualizada")
        print("   Por favor, actualiza el archivo .env con tu API key real")
        return False
    
    print(f"✅ GOOGLE_API_KEY encontrada ({api_key[:10]}...)")
    return True


def test_credentials():
    """Prueba que exista el archivo credentials.json"""
    print("\n📄 Probando credenciales de Google...\n")
    
    import os
    import json
    
    if not os.path.exists("credentials.json"):
        print("❌ credentials.json no encontrado")
        print("\n💡 Pasos para configurar:")
        print("   1. Crea una cuenta de servicio en Google Cloud Console")
        print("   2. Descarga el archivo JSON de credenciales")
        print("   3. Guárdalo como 'credentials.json' en esta carpeta")
        print("   Ver: INSTRUCCIONES_GOOGLE_SHEETS.md")
        return False
    
    try:
        with open("credentials.json", 'r') as f:
            creds = json.load(f)
        
        if "client_email" in creds:
            print(f"✅ credentials.json válido")
            print(f"   Email cuenta servicio: {creds['client_email']}")
            return True
        else:
            print("⚠️  credentials.json no parece válido")
            return False
    except Exception as e:
        print(f"❌ Error al leer credentials.json: {e}")
        return False


def test_config():
    """Prueba la configuración del proyecto"""
    print("\n⚙️  Probando configuración del proyecto...\n")
    
    try:
        import config
        
        if config.SPREADSHEET_ID == "TU_SPREADSHEET_ID_AQUI":
            print("⚠️  SPREADSHEET_ID no ha sido configurado")
            print("   Por favor, actualiza SPREADSHEET_ID en config.py")
            print("   con el ID de tu Google Sheet")
            return False
        
        print(f"✅ SPREADSHEET_ID configurado")
        print(f"   ID: {config.SPREADSHEET_ID}")
        print(f"   Hoja: {config.SHEET_NAME}")
        print(f"   Modelo: {config.MODEL_NAME}")
        return True
        
    except Exception as e:
        print(f"❌ Error al cargar config.py: {e}")
        return False


def test_google_sheets_connection():
    """Prueba la conexión con Google Sheets"""
    print("\n📊 Probando conexión con Google Sheets...\n")
    
    try:
        from data_loader import load_data_from_google_sheets
        
        documents = load_data_from_google_sheets()
        
        if documents:
            print(f"✅ Conexión exitosa - {len(documents)} documentos cargados")
            return True
        else:
            print("❌ No se pudieron cargar documentos")
            return False
            
    except Exception as e:
        print(f"❌ Error al conectar con Google Sheets: {e}")
        print("\n💡 Verifica que:")
        print("   1. El SPREADSHEET_ID sea correcto")
        print("   2. Hayas compartido la hoja con la cuenta de servicio")
        print("   3. La hoja tenga datos")
        return False


def main():
    """Ejecuta todas las pruebas"""
    print("="*70)
    print("  🔍 VERIFICACIÓN DE INSTALACIÓN Y CONFIGURACIÓN")
    print("="*70 + "\n")
    
    results = {
        "Importaciones": test_imports(),
        "Variables de entorno": test_env(),
        "Credenciales Google": test_credentials(),
        "Configuración": test_config()
    }
    
    # Solo probar Google Sheets si las anteriores pasaron
    if all(results.values()):
        results["Conexión Google Sheets"] = test_google_sheets_connection()
    
    print("\n" + "="*70)
    print("  📊 RESUMEN")
    print("="*70 + "\n")
    
    for test_name, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{status} - {test_name}")
    
    total = len(results)
    passed_count = sum(results.values())
    
    print(f"\n🎯 Total: {passed_count}/{total} pruebas pasadas")
    
    if all(results.values()):
        print("\n🎉 ¡Todo está configurado correctamente!")
        print("   Puedes ejecutar: python main.py")
    else:
        print("\n⚠️  Hay configuraciones pendientes")
        print("   Revisa los errores arriba y el README.md")
    
    print("="*70 + "\n")
    
    return all(results.values())


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)


