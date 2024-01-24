import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
rate = engine.setProperty("rate", 170)
print(voices[0])

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def GreetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning,sir")
    elif hour>12 and hour<=18:
        speak("Good Afternoon,sir")
    else:
        speak("Good Evening,sir")

    speak("Please tell me sir, How can I help you ?") 