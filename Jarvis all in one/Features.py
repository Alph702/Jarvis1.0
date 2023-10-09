import pywhatkit
import wikipedia
from pywikihow import search_wikihow
import os
import pyttsx3 as p3
import webbrowser as web
from time import sleep

####### SPEAK #########
engine = p3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',180)
def Speak(audio):
    print("  ")
    print(f"AI : {audio}")
    print("  ")
    engine.say(audio)
    engine.runAndWait()

def GoogleSearch(term):
    query = term.replace("jarvis","")
    query = query.replace("what is","")
    query = query.replace("google search","")
    query = query.replace("how to","")
    query = query.replace("What do you mean by","")
    writeab = str(query)

    oooooo = open("Jarvis all in one\\Data.txt",'a')
    oooooo.write(writeab)
    oooooo.close()


    Query = str(term)
    os.startfile('Jarvis all in one\\DataBase\\Extracode\\start.py')
    pywhatkit.search(Query)

    if 'how to' in Query:
        max_result = 1
        how_to_func = search_wikihow(query=Query,max_results=max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print()
        Speak(how_to_func[0].summary)

    else:
        try:
            search = wikipedia.summary(Query,2)
            Speak(f"According To Your Search : {search}")
        except Exception as e:
            Speak('Error ...Error...Sorry form Jarvis sir')
            return e

def YouTubeSaerch(term):
    result = f"https://www.youtube.com/results?search_query={term}"
    web.open(result)
    Speak("This is What I found For Your Search.")
    try:
        pywhatkit.playonyt(term)
        Speak("This May Also Help you Sir.")
    except Exception as e:
        Speak("Error...Sorry from Jarvis sir.")
        return e

def Alarm(query): # Not integrated to Main file

    TimeHere = open("Jarvis all in one\\Data.txt",'a')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("Jarvis all in one\\DataBase\\Extracode\\Alarm.py")

def DownloadYouTube():
    os.startfile("Jarvis all in one\\DataBase\\Extracode\\Yt.py")


def Speed_Test():
    os.startfile("Jarvis all in one\\DataBase\\Gui Program\\SpeedTestGui.py")

def Wolfram(query): # It not work in Pakistan
    import wolframalpha
    api_key = "KHYKUV-6XX57V3VTP"
    client = wolframalpha.Client(api_key)
    res = client.query(query)
    
    try:
        Ans = next(res.result).text
        return Ans
    except:
        Speak("An String Velue Is Not Answerable, sir.")

def Colculater(query): # It not work in Pakistan
    Term = str(query)
    Term = Term.replace("jarvis","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divided by","/")
    Final = str(Term)
    
    try:
        result = Wolfram(Final)
        Speak(result)
    except Exception as e:
        Speak('Error...Error...Sorry form Jarvis sir')
        return e

def Code_Gan(query:str):
    a = open("Jarvis all in one\\Data.txt",'w')
    a.write(query)
    a.close()
    os.startfile("Jarvis all in one\\DataBase\\Extracode\\Code_Gan.py")


