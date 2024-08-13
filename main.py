import whisper
from datetime import datetime

model = whisper.load_model("small")
result = model.transcribe("X.ogg", task="translate")
print(result["text"])
with open("/workspaces/Translator/log.txt", "a") as log_file:
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    log_message = f"[{current_time}] : {result['text']}\n"
    log_file.write(log_message)