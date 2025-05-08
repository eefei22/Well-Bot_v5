import pyttsx3

def speak_text(text, rate=180, voice=None):
    engine = pyttsx3.init()

    # Optional: Set speaking rate
    engine.setProperty('rate', rate)

    # Optional: Set voice (male/female)
    if voice:
        voices = engine.getProperty('voices')
        for v in voices:
            if voice.lower() in v.name.lower():
                engine.setProperty('voice', v.id)
                break

    engine.say(text)
    engine.runAndWait()
