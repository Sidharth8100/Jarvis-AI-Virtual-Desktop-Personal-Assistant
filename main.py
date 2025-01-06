import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musicLibrary
import requests
from client import ai

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "9e9828d209194d6dba1efc5a433b4c29"

engine.setProperty('rate', 150)  # Slow down speech rate
engine.setProperty('volume', 0.9)  # Set volume (0.0 to 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    print(c)
    
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    
    elif "open linkedin" in c.lower():
        webbrowser.open("https://tinyurl.com/4x7ub54s")
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=9e9828d209194d6dba1efc5a433b4c29")
        if r.status_code ==200:
            data = r.json()

            articles = data.get('articles', [])

            for article in articles:
                speak(article['title'])
    else:
        #Time for real AI
        ai(c)

if __name__ == "__main__" :
    speak("Initializing Jarvis..... ")
    #listen for the wake word "Jarvis"
    r = sr.Recognizer()

# recognize speech using Sphinx
print("recognizing...")
try:
    flag = True
    cnt = 1
    while(flag):
        with sr.Microphone() as source:
            try:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                word = r.recognize_google(audio)
                if("jarvis" in word.lower()):
                    if cnt==1:
                        speak("Jarvis, at your service")
                        cnt+=1
                    speak("Waiting for command...")
                    
                    #Listen for command
                    with sr.Microphone() as source:
                        print("Jarvis Active...")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)

                        processCommand(command)
            except Exception as e:
                print(e)
except Exception as e:
    print(f"Error; {e}")


