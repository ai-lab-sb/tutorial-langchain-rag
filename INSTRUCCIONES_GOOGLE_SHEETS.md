# 📊 Guía Completa para Configurar Google Sheets

Esta guía te llevará paso a paso en la configuración de Google Sheets para el tutorial de RAG.

## 🎯 Objetivo

Crear una hoja de Google Sheets con datos de conocimiento que nuestro sistema RAG utilizará para responder preguntas.

## 📝 Paso 1: Crear la Hoja de Cálculo

1. **Accede a Google Sheets**
   - Ve a [sheets.google.com](https://sheets.google.com)
   - Inicia sesión con tu cuenta de Google

2. **Crea una nueva hoja**
   - Haz clic en el botón "+" (Hoja de cálculo en blanco)
   - O usa este atajo: [sheets.new](https://sheets.new)

3. **Nombra tu hoja**
   - Haz clic en "Hoja de cálculo sin título" en la esquina superior izquierda
   - Escribe: **"Conocimientos RAG Tutorial"**
   - Presiona Enter

## 📋 Paso 2: Estructurar los Datos

### Crear las Columnas

En la primera fila, crea estos encabezados:

| A1 | B1 | C1 |
|----|----|----|
| tema | pregunta | respuesta |

### Agregar Datos de Ejemplo

Copia y pega los siguientes datos (desde la fila 2):

```
Python	¿Qué es Python?	Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Creado por Guido van Rossum en 1991, se caracteriza por su sintaxis clara y legible, lo que lo hace ideal para principiantes y profesionales.

Python	¿Para qué se usa Python?	Python se utiliza en múltiples ámbitos: desarrollo web (Django, Flask), análisis de datos (Pandas, NumPy), inteligencia artificial y machine learning (TensorFlow, PyTorch), automatización, scripting, desarrollo de juegos, aplicaciones de escritorio y mucho más.

Python	¿Cuáles son las características principales de Python?	Python es interpretado, tiene tipado dinámico, es multiplataforma, cuenta con una gran biblioteca estándar, soporta múltiples paradigmas de programación (orientado a objetos, funcional, procedural) y tiene una comunidad muy activa.

LangChain	¿Qué es LangChain?	LangChain es un framework de código abierto para desarrollar aplicaciones potenciadas por modelos de lenguaje. Facilita la creación de cadenas de procesamiento complejas, agentes inteligentes y aplicaciones RAG (Retrieval-Augmented Generation).

LangChain	¿Cuáles son los componentes principales de LangChain?	Los componentes principales incluyen: Documents (documentos), Embeddings (representaciones vectoriales), Vector Stores (almacenamiento vectorial), Retrievers (recuperadores), LLMs (modelos de lenguaje), Chains (cadenas) y Prompts (plantillas de consulta).

RAG	¿Qué es RAG?	RAG (Retrieval-Augmented Generation) es una técnica que combina recuperación de información con generación de texto usando LLMs. Primero recupera documentos relevantes de una base de conocimientos y luego usa esa información como contexto para generar respuestas más precisas y fundamentadas.

RAG	¿Por qué usar RAG?	RAG permite que los LLMs accedan a información actualizada sin necesidad de reentrenamiento, reduce las alucinaciones al proporcionar contexto verificable, permite respuestas específicas del dominio y proporciona fuentes para las respuestas generadas.

RAG	¿Cómo funciona el proceso RAG?	El proceso consta de varias etapas: 1) El usuario hace una pregunta, 2) La pregunta se convierte en embedding, 3) Se buscan documentos similares en el vector store, 4) Se recuperan los documentos más relevantes, 5) Se construye un prompt con el contexto, 6) El LLM genera una respuesta basada en ese contexto.

FAISS	¿Qué es FAISS?	FAISS (Facebook AI Similarity Search) es una biblioteca desarrollada por Meta/Facebook para búsqueda eficiente de similitud y clustering de vectores densos. Es extremadamente rápida y puede manejar miles de millones de vectores.

FAISS	¿Por qué usar FAISS para RAG?	FAISS es ideal para RAG porque: ofrece búsquedas muy rápidas (milisegundos), soporta grandes volúmenes de datos, tiene bajo consumo de memoria, ofrece múltiples algoritmos de indexación y está altamente optimizado para CPU y GPU.

FAISS	¿Cómo funciona FAISS?	FAISS indexa vectores de embeddings en estructuras de datos optimizadas. Cuando llega una consulta, calcula la distancia (generalmente coseno o euclidiana) entre el vector de consulta y los vectores indexados, y retorna los K vectores más cercanos de manera eficiente.

Embeddings	¿Qué son los embeddings?	Los embeddings son representaciones vectoriales numéricas de texto (o cualquier dato) que capturan el significado semántico en un espacio multidimensional. Textos con significados similares tienen embeddings cercanos en este espacio.

Embeddings	¿Cómo se generan los embeddings?	Los embeddings se generan usando modelos de redes neuronales entrenados en grandes cantidades de texto. Estos modelos aprenden a convertir palabras, frases o documentos en vectores de números que preservan las relaciones semánticas.

Embeddings	¿Por qué son importantes los embeddings en RAG?	Los embeddings permiten la búsqueda semántica: encontrar documentos relevantes basándose en el significado, no solo en palabras clave exactas. Esto hace que RAG sea mucho más efectivo que búsquedas tradicionales basadas en texto.

Gemini	¿Qué es Gemini?	Gemini es la familia de modelos de lenguaje de última generación desarrollada por Google. Son modelos multimodales, diseñados para ser altamente capaces y eficientes, disponibles en diferentes tamaños: Nano, Pro, Ultra y versiones 1.5.

Gemini	¿Qué versiones de Gemini existen?	Existen varias versiones: Gemini Nano (dispositivos móviles), Gemini Pro (uso general), Gemini Ultra (tareas más complejas), y las versiones mejoradas como Gemini 1.5 Pro y 1.5 Flash que ofrecen ventanas de contexto más grandes.

Gemini	¿Cómo usar Gemini con LangChain?	Para usar Gemini con LangChain necesitas: 1) Obtener una API key de Google AI Studio, 2) Instalar langchain-google-genai, 3) Importar ChatGoogleGenerativeAI, 4) Inicializar el modelo con tu API key y configuración deseada.

Machine Learning	¿Qué es el aprendizaje automático?	El aprendizaje automático (Machine Learning) es una rama de la inteligencia artificial que permite a las computadoras aprender de datos y mejorar su rendimiento sin ser programadas explícitamente para cada tarea específica.

Machine Learning	¿Cuáles son los tipos de aprendizaje automático?	Los principales tipos son: Aprendizaje Supervisado (con datos etiquetados), Aprendizaje No Supervisado (sin etiquetas), Aprendizaje por Refuerzo (basado en recompensas) y Aprendizaje Semi-supervisado (combinación de etiquetados y no etiquetados).

IA	¿Qué es la Inteligencia Artificial?	La Inteligencia Artificial (IA) es el campo de la informática que se enfoca en crear sistemas capaces de realizar tareas que normalmente requieren inteligencia humana, como el razonamiento, el aprendizaje, la percepción y el procesamiento del lenguaje natural.

Vector Store	¿Qué es un Vector Store?	Un Vector Store (almacén de vectores) es una base de datos especializada en almacenar y buscar embeddings. Está optimizado para operaciones de similitud y puede recuperar rápidamente los vectores más cercanos a una consulta dada.

Vector Store	¿Qué diferencia hay entre Vector Store y base de datos tradicional?	Las bases de datos tradicionales buscan coincidencias exactas, mientras que los Vector Stores realizan búsquedas por similitud semántica. Los Vector Stores usan métricas de distancia (coseno, euclidiana) para encontrar vectores "cercanos" en el espacio multidimensional.
```

**Nota:** Los datos están separados por tabulaciones (TAB). Si tienes problemas al pegar, puedes:
1. Crear un archivo CSV con estos datos
2. Importarlo en Google Sheets: Archivo > Importar
3. O escribir los datos manualmente siguiendo la estructura

### Vista Final de tu Hoja

Tu hoja debería verse así:

![Ejemplo de estructura](ejemplo-estructura.png)

| tema | pregunta | respuesta |
|------|----------|-----------|
| Python | ¿Qué es Python? | Python es un lenguaje de programación... |
| Python | ¿Para qué se usa Python? | Python se utiliza en múltiples ámbitos... |
| ... | ... | ... |

## 🔑 Paso 3: Obtener el ID de la Hoja

1. **Observa la URL de tu hoja**
   
   La URL tiene este formato:
   ```
   https://docs.google.com/spreadsheets/d/[ESTE_ES_EL_ID]/edit#gid=0
   ```

2. **Copia el ID**
   
   Por ejemplo, si tu URL es:
   ```
   https://docs.google.com/spreadsheets/d/1a2b3c4d5e6f7g8h9i0j/edit#gid=0
   ```
   
   El ID es: `1a2b3c4d5e6f7g8h9i0j`

3. **Guarda este ID**
   
   Lo necesitarás para el archivo `config.py`

## 🔐 Paso 4: Configurar Permisos (Cuenta de Servicio)

### ¿Por qué necesitamos una cuenta de servicio?

Para que nuestro script de Python pueda acceder a Google Sheets automáticamente sin intervención del usuario.

### Crear la Cuenta de Servicio

1. **Ve a Google Cloud Console**
   - Accede a [console.cloud.google.com](https://console.cloud.google.com)
   - Inicia sesión con tu cuenta de Google

2. **Crear o seleccionar proyecto**
   - Haz clic en el selector de proyectos (parte superior)
   - Haz clic en "Nuevo proyecto"
   - Nombre: "LangChain RAG Tutorial"
   - Haz clic en "Crear"
   - Espera unos segundos y selecciona el proyecto

3. **Habilitar Google Sheets API**
   - En el menú lateral (☰), ve a "APIs y servicios" > "Biblioteca"
   - Busca "Google Sheets API"
   - Haz clic en el resultado
   - Haz clic en "Habilitar"
   - Espera a que se habilite

4. **Crear Cuenta de Servicio**
   - Ve a "APIs y servicios" > "Credenciales"
   - Haz clic en "+ CREAR CREDENCIALES"
   - Selecciona "Cuenta de servicio"
   - Completa los campos:
     - Nombre: `langchain-rag-service`
     - ID: se genera automáticamente
     - Descripción: "Cuenta para acceder a Google Sheets en el tutorial RAG"
   - Haz clic en "Crear y continuar"
   - Omite los pasos opcionales (rol y acceso)
   - Haz clic en "Listo"

5. **Descargar Credenciales JSON**
   - En la lista de cuentas de servicio, haz clic en la que acabas de crear
   - Ve a la pestaña "Claves"
   - Haz clic en "Agregar clave" > "Crear clave nueva"
   - Selecciona formato "JSON"
   - Haz clic en "Crear"
   - Se descargará un archivo JSON automáticamente

6. **Guardar el archivo JSON**
   - Mueve el archivo descargado a tu proyecto
   - Renómbralo a: `credentials.json`
   - Colócalo en: `Documents/PROYECTOS/langchain-rag-tutorial/`

### Compartir la Hoja con la Cuenta de Servicio

1. **Obtener el email de la cuenta de servicio**
   - Abre el archivo `credentials.json`
   - Busca el campo `"client_email"`
   - Copia el email (se ve algo como: `langchain-rag-service@proyecto-xxxxx.iam.gserviceaccount.com`)

2. **Compartir tu Google Sheet**
   - Abre tu hoja de Google Sheets
   - Haz clic en "Compartir" (esquina superior derecha)
   - Pega el email de la cuenta de servicio
   - Selecciona rol: **"Lector"** (es suficiente para este tutorial)
   - **Desmarca** "Notificar a las personas" (no es necesario)
   - Haz clic en "Compartir" o "Enviar"

3. **Verificar**
   - Deberías ver el email de la cuenta de servicio en la lista de personas con acceso

## ✅ Paso 5: Actualizar la Configuración

### Editar config.py

1. Abre el archivo `config.py` en tu editor
2. Encuentra esta línea:
   ```python
   SPREADSHEET_ID = "TU_SPREADSHEET_ID_AQUI"
   ```
3. Reemplázala con tu ID real:
   ```python
   SPREADSHEET_ID = "1a2b3c4d5e6f7g8h9i0j"  # Tu ID aquí
   ```
4. Si tu hoja no se llama "Hoja 1", actualiza también:
   ```python
   SHEET_NAME = "Nombre de tu hoja"
   ```
5. Guarda el archivo

## 🧪 Paso 6: Probar la Conexión

Ejecuta este comando para verificar que todo funciona:

```bash
python data_loader.py
```

Deberías ver algo como:

```
📊 Conectando con Google Sheets...
✅ Se encontraron 22 filas de datos
✅ Se crearon 22 documentos

=====================================================================
📚 RESUMEN DE DOCUMENTOS CARGADOS
=====================================================================
...
```

Si ves errores, revisa la sección de Troubleshooting abajo.

## ❗ Troubleshooting

### Error: "No such file or directory: 'credentials.json'"

**Solución:**
- Verifica que el archivo `credentials.json` esté en la carpeta del proyecto
- Asegúrate de que el nombre sea exactamente `credentials.json` (sin espacios)

### Error: "Insufficient authentication scopes"

**Solución:**
- Verifica que hayas habilitado Google Sheets API en Google Cloud Console
- Regenera el archivo `credentials.json` y vuelve a descargarlo

### Error: "The caller does not have permission"

**Solución:**
- Asegúrate de haber compartido la hoja con el email de la cuenta de servicio
- Verifica que el SPREADSHEET_ID en `config.py` sea correcto

### Error: "Unable to find worksheet"

**Solución:**
- Verifica que el nombre de la hoja en `config.py` (SHEET_NAME) coincida con el nombre de la pestaña
- Por defecto es "Hoja 1" en español

### No se encuentran datos

**Solución:**
- Verifica que los nombres de las columnas sean exactamente: `tema`, `pregunta`, `respuesta`
- Asegúrate de que haya datos en las filas (no solo encabezados)
- Verifica que no haya espacios extra en los nombres de las columnas

## 📚 Recursos Adicionales

- [Documentación de Google Sheets API](https://developers.google.com/sheets/api)
- [Guía de Cuentas de Servicio](https://cloud.google.com/iam/docs/service-accounts)
- [Biblioteca gspread (Python)](https://docs.gspread.org/)

## 💡 Consejos

1. **Seguridad:**
   - **NUNCA** subas `credentials.json` a Git o repositorios públicos
   - El archivo `.gitignore` ya está configurado para ignorarlo

2. **Organización:**
   - Mantén tus datos organizados por tema
   - Usa respuestas completas y detalladas
   - Incluye múltiples preguntas sobre el mismo tema

3. **Escalabilidad:**
   - Puedes agregar miles de filas sin problema
   - FAISS puede manejar grandes volúmenes de datos
   - Considera dividir en múltiples hojas si tienes muchos datos

4. **Actualización:**
   - Puedes actualizar los datos en Google Sheets en cualquier momento
   - Solo necesitas recrear el índice FAISS (elimina la carpeta `faiss_index`)

---

¡Listo! Ahora tu Google Sheet está correctamente configurada para el tutorial de RAG. 🎉

Continúa con el [README.md](README.md) principal para seguir con el tutorial.


