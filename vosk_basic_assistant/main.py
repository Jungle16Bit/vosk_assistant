from vosk import Model, KaldiRecognizer
from datetime import datetime 
import pyaudio
import json
import os

# pasta do modelo
model_path = "models/vosk-model-small-pt-0.3" # aqui você deverá substituir pelo local do seu modelo

# inicializar o modelo
model = Model(model_path)
rec = KaldiRecognizer(model, 16000)

#nome do usuario que está conversando
username = ""

#nome do assistente
assistant_name = "Jungle_Assistant"

# inicializar pyaudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1,
                rate=16000, input=True, frames_per_buffer=4096)

stream.start_stream()

print("Fale algo: ")

while True:
    data = stream.read(4096, exception_on_overflow=False)
    if rec.AcceptWaveform(data):
        result = json.loads(rec.Result())
        os.system("cls")
        response =  result.get("text", "").strip()

        print(f"Você disse: ", response)
        word = "meu nome é "

        if word in response:
            username =  response.replace(word, "")
        
        match response:
            case "desligar":
                break
            case "data":
                date_now = datetime.now()
                date_now =  date_now.strftime("[%H:%M:%S - %d/%m/%Y]")
                print(date_now)
            case "seu nome":
                print(f"Pode me chamar de {assistant_name}!")
            case "meu nome":
                print(f"Você se chama {username}!")
            case "tudo bem" | "como vai" | "tudo legal":
                print("Tudo bem sim, e com voçê?")
                