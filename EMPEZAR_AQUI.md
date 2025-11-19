# 👋 ¡Bienvenido! Empieza Aquí

## 🎯 ¿Qué es este proyecto?

Este es un **tutorial completo de RAG (Retrieval-Augmented Generation)** con:
- 🧠 **LangChain** - Framework para aplicaciones con LLMs
- ⚡ **FAISS** - Base de datos vectorial ultrarrápida
- 🤖 **Gemini** - Modelo de lenguaje de Google
- 📊 **Google Sheets** - Tu base de conocimientos

## 🚦 Tres Caminos para Empezar

### 🏃‍♂️ Camino Rápido (5 minutos)

**Para quién**: Usuarios con experiencia que quieren empezar ya

```bash
# 1. Instalar
pip install -r requirements.txt

# 2. Configurar (ver INICIO_RAPIDO.md)
copy .env.example .env
# Editar .env con tu API key

# 3. Ejecutar
python main.py --interactive
```

📖 **Lee**: [INICIO_RAPIDO.md](INICIO_RAPIDO.md)

---

### 🎓 Camino Tutorial (30-45 minutos)

**Para quién**: Principiantes que quieren entender cada paso

**Orden recomendado**:

1. **📖 Lee el README completo**
   - Archivo: [README.md](README.md)
   - Qué aprenderás: Conceptos de RAG, arquitectura, instalación

2. **🔧 Configura tu entorno**
   - Instala dependencias: `pip install -r requirements.txt`
   - Configura Gemini API
   - Sigue: [INSTRUCCIONES_GOOGLE_SHEETS.md](INSTRUCCIONES_GOOGLE_SHEETS.md)

3. **✅ Verifica tu configuración**
   - Ejecuta: `python test_simple.py`
   - Debe pasar todas las pruebas

4. **🎓 Tutorial interactivo**
   - Ejecuta: `python tutorial_completo.py`
   - Aprende cada componente paso a paso

5. **🔬 Experimenta**
   - Ejecuta: `python main.py --interactive`
   - Haz tus propias preguntas

---

### 📚 Camino Explorador (Flexible)

**Para quién**: Desarrolladores que quieren explorar y personalizar

**Navega según tus intereses**:

- 🤔 **¿Tienes dudas?** → [FAQ.md](FAQ.md)
- 💡 **¿Quieres ejemplos?** → [EJEMPLOS_USO.md](EJEMPLOS_USO.md)
- 📊 **¿Problemas con Google Sheets?** → [INSTRUCCIONES_GOOGLE_SHEETS.md](INSTRUCCIONES_GOOGLE_SHEETS.md)
- 🗺️ **¿Ver estructura del proyecto?** → [RESUMEN_PROYECTO.md](RESUMEN_PROYECTO.md)

---

## 📂 Navegación de Archivos

### 📖 Documentación (Léeme)

```
EMPEZAR_AQUI.md              ← Estás aquí
├── README.md                ← Documentación principal ⭐
├── INICIO_RAPIDO.md         ← Guía express
├── RESUMEN_PROYECTO.md      ← Vista general del proyecto
├── INSTRUCCIONES_GOOGLE_SHEETS.md  ← Configurar Google Sheets
├── FAQ.md                   ← Preguntas frecuentes
└── EJEMPLOS_USO.md          ← Casos de uso prácticos
```

### 🐍 Código (Ejecútame)

```
main.py                      ← Script principal ⭐
├── tutorial_completo.py     ← Tutorial interactivo
├── test_simple.py           ← Verificar instalación
├── config.py                ← Configuración
├── data_loader.py           ← Carga de datos
└── rag_system.py            ← Sistema RAG
```

### ⚙️ Configuración (Configúrame)

```
requirements.txt             ← Dependencias
├── .env.example             ← Plantilla de variables
├── .env                     ← Tu configuración (crear)
├── credentials.json         ← Credenciales Google (descargar)
└── .gitignore               ← Ya configurado
```

## ✅ Checklist de Configuración

Antes de ejecutar el tutorial, asegúrate de tener:

- [ ] Python 3.8+ instalado
- [ ] Dependencias instaladas (`pip install -r requirements.txt`)
- [ ] API key de Gemini obtenida
- [ ] Archivo `.env` creado y configurado
- [ ] Cuenta de servicio de Google creada
- [ ] Archivo `credentials.json` descargado
- [ ] Google Sheet creada con datos
- [ ] Google Sheet compartida con cuenta de servicio
- [ ] `SPREADSHEET_ID` actualizado en `config.py`

**Verificar todo**: `python test_simple.py`

## 🎯 Comandos Principales

```bash
# Verificar instalación
python test_simple.py

# Tutorial completo interactivo
python tutorial_completo.py

# Ejecutar con ejemplos
python main.py

# Modo interactivo (recomendado)
python main.py --interactive

# Usar índice existente (más rápido)
python main.py --use-existing-index --interactive
```

## 🆘 ¿Problemas?

### Error en instalación
```bash
pip install -r requirements.txt --upgrade
```

### Error de API key
- Verifica `.env`
- La API key debe empezar con `AIzaSy...`

### Error de Google Sheets
- Ejecuta: `python test_simple.py`
- Sigue los mensajes de error
- Consulta: [INSTRUCCIONES_GOOGLE_SHEETS.md](INSTRUCCIONES_GOOGLE_SHEETS.md)

### Otros problemas
- 📖 [FAQ.md](FAQ.md) - Problemas comunes
- 🔍 Lee los mensajes de error cuidadosamente
- ✅ Verifica el checklist arriba

## 💡 Consejos Rápidos

1. **Primera vez**: Sigue el "Camino Tutorial"
2. **Lee los comentarios**: El código está bien documentado
3. **Experimenta**: Cambia parámetros en `config.py`
4. **Agrega datos**: Más datos = Mejores respuestas
5. **Pregunta**: Usa `--interactive` para explorar

## 🎉 ¿Listo?

### Si tienes 5 minutos:
```bash
python main.py --interactive
```

### Si tienes 30 minutos:
```bash
python tutorial_completo.py
```

### Si tienes dudas:
Lee [README.md](README.md) primero

---

## 📚 Recursos Adicionales

- [Documentación de LangChain](https://python.langchain.com/)
- [Google AI Studio](https://makersuite.google.com/)
- [FAISS Documentation](https://faiss.ai/)

---

**🚀 ¡Que disfrutes aprendiendo sobre RAG!**

---

*Última actualización: Noviembre 2025*  
*Licencia: MIT - Ver [LICENCIA.txt](LICENCIA.txt)*


