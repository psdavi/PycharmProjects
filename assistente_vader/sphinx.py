import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Ouvindo...")
    audio = r.listen(source)

try:
    texto = r.recognize_google(audio, language="pt-BR")
    if str(texto).lower() == 'cerveja gelada':
        print("Entendi")
    else:
        print("não entendi")
except sr.UnknownValueError:
    print("Sphinx não conseguiu entender")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))


