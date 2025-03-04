import datetime
from email import message
import webbrowser
from numpy import tile
import pyttsx3
import speech_recognition 
import requests
from bs4 import BeautifulSoup
import os
import pyautogui
import random

from plyer import notification
import getpass




for i in range(3):
    # a = input("Enter Password to open Jarvis :- ")
    a = getpass.getpass("Enter Password to open Jarvis : ") 
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):       
        print("Try Again")

from INTRO import play_gif
play_gif
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again"+str(e))
        return "None"
    return query




def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


if __name__ == "__main__":
    from GreetMe import greetMe
    greetMe()
    b=1
    while True:
        query = takeCommand().lower()
        if True:
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    break 
                
                
                elif "change password" in query:


                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")

        

                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("translate","")
                    translategl(query)

                


                elif "open" in query:   
                    query = query.replace("open","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")                       
                     
                

                
              
                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     dtime = datetime.datetime.now().strftime("%H:%M:%S")
                     dtime=dtime.replace(":",".")
                     output_path=f'{dtime}.jpg'
                     print(output_path)                    
                     im = pyautogui.screenshot()  
                     im.save(output_path)

                     exit()

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE Dastagir")
                    pyautogui.press("enter")

                
                

                ############################################################
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you"  in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")

                    a = (2,3,4)
                    
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                        b = random.choice(a)
                    elif b==2:
                        speak(b)


                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                


                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)


                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    if "search on" in query:
                        query=query.replace("search on","")
                    if "search" in query:
                        query=query.replace("search","")
                    from SearchNow import searchYoutube
                    

                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)

                elif "whatsapp" in query:
                    # from Whatsapp import sendMessage
                    # sendMessage()
                    speak("in progress")

                

                elif "temperature" in query:
                    if "current" in query:
                        query=query.replace("current","")
                    
                    search = "current"+ query + "in Ramanagara"
                    if "in" in query:
                        search = "current"+ query

                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"{search} is {temp}")
                elif "weather" in query:
                    if "current" in query:
                        query=query.replace("current","")
                    
                    search = "current"+ query + "in Ramanagara"
                    if "in" in query:
                        search = "current"+ query

                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"{search} is {temp}")

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
                           
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    exit()

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to "+rememberMessage)
                    remember = open("Remember.txt","w")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to " + remember.read())


                elif "shutdown system" in query:
                    speak("available soon")
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break

                




                


 