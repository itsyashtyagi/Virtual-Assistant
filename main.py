import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
       with sr.Microphone() as source:
        print('Listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa', '')
            print(command) 
    except:
      pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        topic = command.replace('who the heck is', '')
        info = wikipedia.summary(topic, 1)
        print(info)
        talk(info)
    elif 'can we go on a date' in command:
        print("i am sorry i have to complete my work we can go next time")
        talk("i am sorry i have to complete my work we can go next time")
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    else:
        talk("i did not understand the command please repeat it")

while True:
    run_alexa()
