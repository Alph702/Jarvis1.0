# importing moduls
import pyttsx3 as p3
import speech_recognition as sr
import os

####### SPEAK #########


def Speak(audio,rate : int = 170):
    engine = p3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',rate)
    print("  ")
    print(f"AI : {audio}")
    print("  ")
    engine.say(audio)
    engine.runAndWait()

###### Take Command #######
def TakeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(" ")
        print(": Listening.....")
        print(" ")
        r.pause_threshold = 1
        audio = r.listen(source,0,6)
    
    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f': Your Command : {query}\n')

    except:
        return ""
    
    return query.lower()

def TakeCommand_hi():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(" ")
        print(": Listening.....")
        print(" ")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='hi')

        print(f': Your Command : {query}\n')

    except:
        return ""
    
    return query.lower()

def TaskExe():
    try:
        os.startfile("DataBase\\Extracode\\Water.pyw") # I open water reminder
    except Exception as e:
        Speak("Sorry I Think The path is not recognised please report the bug.")

    while True:

        query = TakeCommand() # storing the TakeCommand() function on line 21 in varible query

        from Automations import ChromeAuto # for Automation of Chrome
        ChromeAuto(query)
        from Automations import YTAuto # for Automation of Youtube
        YTAuto(query)
        from Automations import winAuto
        winAuto(query)

        try:
            if 'google search' in query: # for google search. I has mane errors
                from Features import GoogleSearch
                GoogleSearch(query)

            elif 'youtube search' in query: # for youtube search
                Query = query.replace("jarvis","")
                query = Query.replace("youtube search","")
                from Features import YouTubeSaerch
                YouTubeSaerch(query)
        except Exception as e:
            Speak("Sorry I Think your internet connection has disturb")

        if 'download' in query: # ToDo: Beter video qolity from youtube (✓)
            from Features import DownloadYouTube
            DownloadYouTube()

        elif 'speed' in query: # Speed Test
            from Features import Speed_Test
            Speed_Test()
        
        elif 'code' in query:
            from Features import Code_Gan # function Code_Gan create a code of any thing in any lang.
            Code_Gan(query)
        
        elif 'quit' in query: # for closeing jarvis 
            break

        else: # if i say Nothing to jarvis it print None
            print(None)


def Jarvis():
     # for password
    Speak("Whats the Password Sir.") 
    Pass_User = "221"
    while Pass_User != "##amanat##":
        Pass_User = input("Whats the Password: ")
        if Pass_User == "##amanat##": # you can change password by changing this
            TaskExe()
        else:
            Speak("Wrong Password Sir.")

Jarvis()