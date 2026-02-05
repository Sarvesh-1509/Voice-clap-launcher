import speech_recognition as sr

def wait_for_keyword(keyword="jarvis"):
    recognizer = sr.Recognizer()

    with sr.Microphone(device_index=1) as source:
        print(" Microphone active. Say something...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    print(" Audio captured, processing...")

    try:
        text = recognizer.recognize_google(audio).lower()
        print(" Recognized:", text)
        return keyword in text
    except sr.UnknownValueError:
        print(" Could not understand audio")
        return False
    except sr.RequestError as e:
        print(f" API error: {e}")
        return False
