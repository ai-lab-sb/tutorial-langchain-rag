# ⚡ Inicio Rápido - 5 Minutos

Si tienes prisa y quieres empezar rápidamente, sigue estos pasos:

## 1. Instalar Dependencias (2 min)

```bash
cd Documents/PROYECTOS/langchain-rag-tutorial
pip install -r requirements.txt
```

## 2. Configurar Credenciales (2 min)

### Gemini API Key

1. Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Crea una API Key
3. Copia `.env.example` a `.env`:
   ```bash
   copy .env.example .env
   ```
4. Edita `.env` y pega tu API key

### Google Sheets

1. Crea tu hoja siguiendo [INSTRUCCIONES_GOOGLE_SHEETS.md](INSTRUCCIONES_GOOGLE_SHEETS.md)
2. Descarga `credentials.json` de la cuenta de servicio
3. Actualiza `SPREADSHEET_ID` en `config.py`

## 3. Ejecutar (1 min)

```bash
# Tutorial completo paso a paso
python tutorial_completo.py

# O ejecución directa
python main.py

# O modo interactivo
python main.py --interactive
```

## ¿Problemas?

- Revisa el [README.md](README.md) completo
- Sección de Troubleshooting en [INSTRUCCIONES_GOOGLE_SHEETS.md](INSTRUCCIONES_GOOGLE_SHEETS.md)

## Estructura Mínima de Google Sheet

| tema | pregunta | respuesta |
|------|----------|-----------|
| Python | ¿Qué es Python? | Python es un lenguaje... |

**¡Eso es todo! 🚀**


