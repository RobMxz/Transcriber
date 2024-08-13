import os
from datetime import datetime
import pytz
import whisper

# Cargar el modelo [tiny, base, small, medium, large] - Ajustar dependiendo de la capacidad de la máquina
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
            f"Text translated : \"{result_translate['text']}\"\n"  # Asegúrate de que 'result["text"]' es la traducción correcta
            "\n"
        )
        
        # Escribir en el archivo de registro
        with open(log_file_path, "a") as log_file:
            log_file.write(log_message)

