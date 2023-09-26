import googletrans
import speech_recognition

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Speak now...")
    voice = recognizer.listen(source)
    text = recognizer.recognize_google(voice,language='fr')
    print(text)

translator = googletrans.Translator()
translation = translator.translate(text,dest='fr')
print(translation)
