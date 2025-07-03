import speech_recognition as sr
r = sr.Recognizer()
while True:
    try:
        with sr.Microphone() as source:
            print("Please say something:")
            audio = r.listen(source)
            text = r.recognize_google(audio, language='en-US')
            text = text.lower()
            print(f"You said: {text}")
    except:
        print("you did not say anything or I did not understand you.")
        r = sr.Recognizer()
        continue
