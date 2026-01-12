import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:  # works if sounddevice is installed
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")

    try:
        print("Text: " + r.recognize_google(audio_text))
    except sr.RequestError:
        print("API unavailable")
    except sr.UnknownValueError:
        print("Sorry, I did not get that")