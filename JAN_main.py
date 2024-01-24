import pyttsx3
import speech_recognition
import webbrowser
import random
import requests
from bs4 import BeautifulSoup
import datetime
import os
from plyer import notification
from pygame import mixer
import pyautogui

############################################################################################################################
for i in range(3):
    a = input("Enter Password to open Jans :- ")
    pw_file = open("password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if (a == pw):
        print("WELCOME SIR ! PLZ SPEAK [[[WAKE UP]]] TO LOAD ME UP")
        break
    elif (i == 2 and a != pw):
        exit()

    elif (a != pw):
        print("Try Again")

############################################################################################################################

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
rate = engine.setProperty("rate", 170)
print(voices[0])
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening............")
        r.pause_threshold = 1
        r.energy_threshold = 300  # according ki aap kitna jor sa chila raho ho ya ki dhira sa bol raha ho
        audio = r.listen(source,0,4)  #har 4 sec ma listening kara ga 
    try:
           print("Understanding......")
           query = r.recognize_google(audio,language='en-in') 
           print(f"you Said: {query}\n")
    except Exception as e:
        print("pls sir, say that again")   
        return "None"    
    return query      ## just link loop chala diya try(if ) nahi to except default speek kar da gi 



def alarm(query):
    timehere = open("AlarmTXT.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


if __name__== "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import GreetMe
            GreetMe()
            while True:
                query = takeCommand().lower() 
                if"go to sleep" in query:
                    speak("ok sir, you can call me any time")
                    break

                elif "finally sleep" in query:
                    speak("Going to sleep, sir")
                    exit()  

                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input(
                        "Do you wish to shutdown your computer? (yes/no): ")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break    

############################################### Jan 2.0 password manager ##########################################

                elif "change password" in query:      # 08/07/23
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt", "w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is: {new_pw}")
##################################################################################################################

                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great sir")
                elif "and you" in query:
                    speak("Always perfect, sir")
                elif "thank u" in query:
                    speak("you are welcome, sir")
                elif "who i am" in query:
                    speak("it's a suraj account, yes i am talking to suraj")


                elif "i am tired" in query:
                    speak("ok,  can i playing your favourite song, sir")
                    a = (1, 2, 3,4,5)
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open(
                            "https://www.youtube.com/watch?v=AHAl1R2YIr0&ab_channel=ForTheRecordMusic")
                    elif b == 2:
                        webbrowser.open(
                            "https://www.youtube.com/watch?v=k6eyzRda9zU&ab_channel=sukoon")
                    elif b == 3:
                        webbrowser.open(
                            "https://www.youtube.com/watch?v=BN0bQ6DXD4g&ab_channel=T-Series")
                    elif b == 4:
                        webbrowser.open(
                            "https://music.youtube.com/search?q=aziyat"
                        )
                    elif b == 5:
                        webbrowser.open(
                            "https://music.youtube.com/watch?v=W4sHmzMCo8s"
                        )     


                elif "open" in query:
                    from OpeningTabs import openappweb
                    openappweb(query)
                elif "close" in query:
                    from OpeningTabs import closeappweb
                    closeappweb(query)    



                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)   


                elif "temperature" in query: 
                    search = "tempertaure"
                    url = f"https://www.google.com/search?client=firefox-b-d&q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current {search} is {temp}")    
                elif "weather" in query:
                    search = "weather"
                    url = f"https://www.google.com/search?client=firefox-b-d&q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current {search} is {temp}")    



                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"sir, the time is {strTime}")         


                elif "set an alarm" in query:
                    print("input time example: 10 and 10 and 10")
                    speak("set the time")
                    a = input("please tell me the time sir :--")
                    alarm(a)
                    speak("Done, sir")  



                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "")
                    rememberMessage = query.replace("jan", "")
                    speak("You told me to "+rememberMessage)
                    remember = open("Remember.txt", "a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    rememberMessage = query.replace("remember that", "")
                    remember = open("Remember.txt","r")
                    speak("you told me " + remember.read())



                elif "news" in query:
                    from News import latestnews
                    latestnews()   


                elif "calculate" in query:
                    from calculator import WolfRamAlpha
                    from calculator import Calc
                    query = query.replace("calculate", "")
                    query = query.replace("jan", "")
                    Calc(query) 
                

                elif "schedule my day" in query:
                    tasks = []  # Empty list1
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("DaysList.txt", "w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("DaysList.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("DaysList.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                 
                #  show my schedule using desktop notification
                elif "show my schedule" in query:
                    file = open("DaysList.txt", "r")
                    content = file.read()
                    file.close()
                    mixer.init()  
                    mixer.music.load("Notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title="My schedule :-",
                        message=content,
                        timeout=15
                    )  


                elif "play a game" in query:
                    from game import game_play
                    game_play()      

 
                
                elif "screenshot" in query:
                     import pyautogui 
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")


                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE PLEASE ")
                    pyautogui.press("enter")

                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO] "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("C:\\Users\\suraj\\OneDrive\\Desktop\\Project_Strart\\FocusMode.py")
                        exit()
                    
                    else:
                        pass


