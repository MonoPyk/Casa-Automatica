import speech_recognition as sr

recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=1)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio).lower()
            print(f"Reconhecido: {text}")

            if text == "prepare":
                print("1")


    except sr.UnknownValueError:
        print("Não entendi o áudio.")
        continue

    except sr.RequestError as e:
        print(f"Erro de solicitação ao serviço do Google: {e}")
        break
