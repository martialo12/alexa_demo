import sys

import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import random

listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
engine.setProperty("voice", "french")
engine.setProperty("rate", 170)
voices = engine.getProperty('voices')


def talk(text):
    engine.say(text)
    engine.runAndWait()


def greetMe():
    current_hour = int(datetime.datetime.now().hour)
    if 0 <= current_hour < 12:
        talk('Bonjour Martialo Dev')

    if 12 <= current_hour < 18:
        talk('Bon après midi Martialo Dev!')

    if current_hour >= 18 and current_hour != 0:
        talk('Bonsoir Martialo Dev!')

# set french voice
engine.setProperty('voice', voices[3].id)
greetMe()
engine.say('comment vas tu?')
# engine.say('Que puis je faire pour toi?')
engine.runAndWait()


def alexa_command():
    with sr.Microphone() as source:
        print("listening...")
        listener.pause_threshold = 5
        voice = listener.listen(source)
        command = listener.recognize_google(voice, language="fr-FR")
        command = command.lower()
        print(command)
        if 'alexa' in command:
            command = command.replace('alexa', '')
            print(command)
    return command


def run_alexa():
    command = alexa_command()
    if 'musique' in command:
        song = command.replace('musique', '')
        talk('musique en cours....')
        print(song)
        pywhatkit.playonyt(song)
    elif 'heure' in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk('il est actuelement: ' + time)
    elif 'qui est' in command:
        person = command.replace("qui est", "")
        wikipedia.set_lang("fr")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "sortir" in command:
        talk("Désolé, je suis un peu souffrante en ce moment.")
    elif "es-tu en couple" in command:
        talk("non pas encore, mon coeur est encore à conquérir.")
    elif "blague" in command:
        jokes = ["C’est la maîtresse qui demande à Toto « Cite-moi un mammifère qui n’a pas de dents »… « Ma grand-mère ? »",
                 "C’est l’histoire de la maîtresse qui demande à Toto : « Récite-moi le verbe marcher au présent. » Toto répond "
                 "« Je…marche…tu…tu…marches… », mais la maîtresse le presse, allez, plus vite Toto ! "
                 "Ce à quoi il répond « je cours ..…tu cours il court… »",]
        talk(random.choice(jokes))
    elif "et toi" in command:
        msgs = ["Je fais juste mon truc !", "Je vais bien !", "Bien !", "Je suis bien et plein d'énergie."]
        talk(random.choice(msgs))
    elif "désactive toi" in command:
        talk("merci de m'avoir utilisé, Martialo Dev")
        sys.exit()

    else:
        talk("pourrais tu repété? je n'ai pas bien compris.")


if __name__ == '__main__':
    while True:
        run_alexa()
