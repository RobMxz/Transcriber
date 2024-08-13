# 🎧 Whisper Translator

¡Bienvenido a **Whisper Translator**! 🚀 Este proyecto es una aplicación simple que utiliza el modelo `whisper` para transcribir y traducir archivos de audio automáticamente. Además, mantiene un registro de todas las transcripciones en un archivo de log. 📜

## 🛠️ Características

- **Transcripción Automática**: Convierte audio en texto utilizando el modelo Whisper.
- **Traducción**: Traduce el contenido del audio al inglés (u otro idioma si lo ajustas).
- **Registro de Logs**: Guarda cada transcripción con una marca de tiempo para futuras referencias.

## 📝 Cómo funciona

1. **Carga del Modelo**: Se carga el modelo pequeño (`small`) de Whisper para realizar la transcripción.
2. **Transcripción y Traducción**: El archivo de audio (`X.ogg`) es procesado para obtener la transcripción y traducción al inglés.
3. **Guardado en Log**: La transcripción se guarda en un archivo `log.txt` con la fecha y hora en que se realizó.

## 🚀 Ejecución del Código

Para ejecutar este código, asegúrate de tener instaladas las dependencias necesarias y simplemente corre el script. Aquí hay un resumen rápido:

```python
import whisper
from datetime import datetime

model = whisper.load_model("small")
result = model.transcribe("X.ogg", task="translate")
print(result["text"])
with open("/workspaces/Translator/log.txt", "a") as log_file:
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    log_message = f"[{current_time}] : {result['text']}\n"
    log_file.write(log_message)
```

## 📁Estructura del proyecto

`📦Translator`  
` ┣ 📂workspace`  
` ┃ ┗ 📜log.txt`  
` ┣ 📜README.md`  
` ┗ 📜X.ogg`  

## 🛠️ Requisitos

- Python 3.8-3.11
- Biblioteca Whisper (`pip install -U openai-whisper`)

## 🌟 ¡Contribuciones!

Las contribuciones son bienvenidas! Siéntete libre de abrir un issue o enviar un pull request. 💡
