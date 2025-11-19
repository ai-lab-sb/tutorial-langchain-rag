# 🤝 Guía de Contribución

¡Gracias por tu interés en contribuir a este tutorial de LangChain RAG! Este es un proyecto educativo y todas las contribuciones son bienvenidas.

## 📋 Tipos de Contribuciones

### 1. Reportar Errores
- Usa el sistema de Issues de GitHub
- Describe claramente el problema
- Incluye pasos para reproducir el error
- Menciona tu sistema operativo y versión de Python

### 2. Mejorar Documentación
- Corregir typos o errores gramaticales
- Aclarar explicaciones confusas
- Agregar ejemplos adicionales
- Traducir a otros idiomas

### 3. Agregar Ejemplos
- Casos de uso prácticos
- Integraciones con otras herramientas
- Optimizaciones de rendimiento
- Nuevas fuentes de datos

### 4. Mejorar Código
- Optimizaciones
- Mejores prácticas
- Nuevas características
- Tests adicionales

## 🚀 Cómo Contribuir

### Paso 1: Fork el Repositorio
```bash
# Haz fork del repo en GitHub
# Luego clona tu fork
git clone https://github.com/TU-USUARIO/tutorial-langchain-rag.git
cd tutorial-langchain-rag
```

### Paso 2: Crear una Rama
```bash
git checkout -b feature/mi-contribucion
# o
git checkout -b fix/correccion-error
```

### Paso 3: Hacer tus Cambios
- Mantén el código limpio y comentado
- Sigue el estilo de código existente
- Actualiza la documentación si es necesario

### Paso 4: Probar tus Cambios
```bash
# Verifica que todo funcione
python test_simple.py

# Prueba manualmente
python main.py
```

### Paso 5: Commit y Push
```bash
git add .
git commit -m "Descripción clara de los cambios"
git push origin feature/mi-contribucion
```

### Paso 6: Crear Pull Request
- Ve a GitHub
- Crea un Pull Request desde tu rama
- Describe claramente qué cambios hiciste y por qué
- Referencia issues relacionados si aplica

## 📝 Estándares de Código

### Python
- Sigue PEP 8
- Usa nombres descriptivos para variables y funciones
- Agrega docstrings a funciones y clases
- Comenta código complejo

```python
def mi_funcion(parametro: str) -> dict:
    """
    Descripción breve de la función.
    
    Args:
        parametro: Descripción del parámetro
        
    Returns:
        Descripción de lo que retorna
    """
    # Tu código aquí
    pass
```

### Documentación
- Usa Markdown para todos los documentos
- Mantén el formato consistente
- Incluye ejemplos cuando sea posible
- Usa emojis de manera apropiada (como en otros docs)

## 🎯 Áreas que Necesitan Ayuda

### Prioritarias
- [ ] Tests unitarios más completos
- [ ] Ejemplos con otras fuentes de datos (PDFs, URLs)
- [ ] Interfaz web con Streamlit/Gradio
- [ ] Documentación en inglés
- [ ] Scripts para más sistemas operativos

### Deseables
- [ ] Integración con otros LLMs (OpenAI, Anthropic)
- [ ] Otros vector stores (Chroma, Pinecone)
- [ ] Evaluación automatizada de respuestas
- [ ] Docker container
- [ ] CI/CD pipeline

## 🐛 Reportar Issues

### Información a Incluir
- **Descripción**: Qué esperabas vs qué obtuviste
- **Pasos para reproducir**: Cómo reproducir el error
- **Sistema**: SO, versión de Python, versiones de librerías
- **Logs**: Mensajes de error completos

### Plantilla de Issue
```markdown
## Descripción
[Descripción clara del problema o sugerencia]

## Pasos para Reproducir
1. Paso 1
2. Paso 2
3. Paso 3

## Comportamiento Esperado
[Lo que esperabas que pasara]

## Comportamiento Actual
[Lo que realmente pasó]

## Entorno
- SO: [Windows/Mac/Linux]
- Python: [versión]
- Código de error: [si aplica]
```

## 💡 Sugerencias

### Buenas Ideas de Contribución
- Agregar más preguntas al FAQ basadas en problemas comunes
- Crear tutoriales en video y linkearlos
- Escribir posts de blog sobre el proyecto
- Compartir casos de uso reales
- Mejorar los mensajes de error

### NO Recomendado
- Cambios que rompan la compatibilidad sin discusión previa
- Agregar dependencias pesadas sin justificación
- Cambiar la estructura del proyecto sin consenso
- Eliminar documentación existente

## ✅ Checklist para Pull Requests

Antes de crear un PR, verifica:

- [ ] El código funciona correctamente
- [ ] He probado los cambios localmente
- [ ] La documentación está actualizada
- [ ] Los comentarios están claros
- [ ] No hay errores de linting
- [ ] El commit message es descriptivo
- [ ] He referenciado issues relacionados

## 📞 Contacto

Si tienes preguntas sobre cómo contribuir:
- Abre un Issue de discusión
- Revisa Issues existentes
- Consulta la documentación existente

## 🙏 Reconocimiento

Todos los contribuidores serán reconocidos en el README principal del proyecto.

---

**¡Gracias por contribuir a este proyecto educativo! 🚀**

Tu contribución ayuda a más personas a aprender sobre RAG y LangChain.

