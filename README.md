# Documentación del Proyecto

## Descripción

Este proyecto utiliza LangChain y el modelo Ollama (Llama3) para extraer información específica de un texto proporcionado.

## Requisitos

- Python 3.x
- pip (gestor de paquetes de Python)

## Instalación de las Librerías Necesarias

1. Crea un entorno virtual (opcional, pero recomendado):
   ```bash
   python -m venv venv
   ```

2. Activa el entorno virtual:
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Instala las librerías requeridas:
   ```bash
   pip install langchain langchain-community requests
   ```

## Activar el Servidor de Ollama

Para que el script funcione, necesitas tener el servidor de Ollama en ejecución. Utiliza el siguiente comando para iniciar el servidor:

```bash
ollama serve
```

### Cambiar el Puerto

Si el puerto por defecto (`11434`) está ocupado, puedes cambiarlo a un puerto diferente (por ejemplo, `11435`). Para hacerlo, ejecuta el servidor de Ollama con el siguiente comando:

```bash
ollama serve --port 11435
```

### Ajustar el Código para Cambiar el Puerto

Si decides usar un puerto diferente, asegúrate de que el código de tu script apunte al puerto correcto. Modifica la configuración del modelo Ollama en el script de la siguiente manera:

```python
# Configura el modelo de Ollama (Llama3)
llm = Ollama(model='llama3:8b', port=11435)  # Cambia aquí el puerto
```

## Comando para Ejecutar el Código

Una vez que hayas instalado las librerías y tengas el servidor de Ollama en funcionamiento, ejecuta tu script de Python con el siguiente comando:

```bash
python llm_extractor.py
```

Asegúrate de reemplazar `llm_extractor.py` con el nombre real de tu archivo Python.

## Contribuciones

Si deseas contribuir a este proyecto, por favor envía un pull request o abre un issue en este repositorio.

## Licencia

Este proyecto está licenciado bajo la MIT License.
