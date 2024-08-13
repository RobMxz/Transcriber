# 🎧 Whisper Transcriber

¡Bienvenido a **Whisper Transcriber**! 🚀 Este proyecto es una aplicación que utiliza el modelo `whisper` para transcribir y traducir archivos de audio automáticamente. Además, mantiene un registro detallado de todas las transcripciones y traducciones en un archivo de log. 📜

## 🛠️ Características

- **Transcripción Automática**: Convierte audio en texto utilizando el modelo Whisper.
- **Traducción**: Traduce el contenido del audio al inglés (u otro idioma si lo ajustas).
- **Registro de Logs**: Guarda cada transcripción y traducción con una marca de tiempo para futuras referencias.

## 📝 Cómo funciona

1. **Carga del Modelo**: Se carga el modelo `small` de Whisper para realizar la transcripción.
2. **Procesamiento de Archivos de Audio**: Se recorren los archivos `.ogg` en la carpeta `Audios`, y cada uno es procesado para obtener la transcripción y la traducción al inglés.
3. **Guardado en Log**: Tanto la transcripción como la traducción se guardan en un archivo `log.txt` con la fecha y hora en que se realizó.

## 🚀 Ejecución del Código

Para ejecutar este código, asegúrate de tener instaladas las dependencias necesarias y simplemente corre el script. Aquí hay un resumen rápido:

```python
import os
from datetime import datetime
import pytz
import whisper

# Cargar el modelo
model = whisper.load_model("small")

# Ruta del archivo de registro
log_file_path = "/workspaces/Translator/log.txt"

# Ruta de la carpeta de audios
audio_folder = "/workspaces/Translator/Audios"

# Zona horaria de Perú
peru_tz = pytz.timezone('America/Lima')

# Procesar los archivos de audio
for filename in os.listdir(audio_folder):
    if filename.endswith(".ogg"):
        audio_path = os.path.join(audio_folder, filename)
        result_transcribe = model.transcribe(audio_path)
        result_translate = model.transcribe(audio_path, task="translate")
        
        # Obtener la hora actual en la zona horaria de Perú
        current_time = datetime.now(peru_tz).strftime("%d/%m/%Y %H:%M:%S")
        
        # Construir el mensaje de log
        log_message = (
            f"[{datetime.now(peru_tz).strftime('%d/%m/%Y')}][{datetime.now(peru_tz).strftime('%H:%M:%S')}]\n"
            f"Detected language : {result_translate['language']}\n"
            f"Original text: \"{result_transcribe['text']}\"\n"
            f"Text translated : \"{result_translate['text']}\"\n"
            "\n"
        )
        
        # Escribir en el archivo de registro
        with open(log_file_path, "a") as log_file:
            log_file.write(log_message)
```

## 📁Estructura del proyecto

`📦Translator`  
`┣ 📂Audios`  
`┃ ┗ 📜X1.ogg`  
`┃ ┗ 📜X2.ogg`  
`┃ ┗ 📜X3.ogg`  
`┣ 📜log.txt`  
`┣ 📜README.md`  

## 🛠️ Requisitos

- Python 3.8-3.11
- Biblioteca Whisper (`pip install -U openai-whisper`)
- pytz (`pip install pytz`)

## 🌟 ¡Contribuciones!

Las contribuciones son bienvenidas! Siéntete libre de abrir un issue o enviar un pull request. 💡
