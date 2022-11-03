import bs4
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
from fastapi import requests

audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt')
            comando = comando.lower()
            if 'tina' in comando:
                comando = comando.replace('tina', '')
                maquina.say(comando)
                maquina.runAndWait()

    except:
        print('Microfone não está ok')

    return comando


