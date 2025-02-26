import speech_recognition as sr
import webbrowser
import pyttsx3
import music
from openai import OpenAI
from gtts import gTTS
import pygame
import os
import requests
import time 
import impweb
# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init() 


def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(api_key="<Your Key Here>",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named sachin skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    if  "start" in c.lower():
        app_name = c[5:].strip()  
        try:
            os.system(f'start {app_name}')
        except Exception as e:
             speak("App Not Find in system ", e)
    elif "search " in c.lower():
        query = c.lower().replace("search ", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        time.sleep(10) 
        if "click first  " in c.lower():
            webbrowser.open(f"https://www.google.com/search?q={query}&btnI") 
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "video " in c.lower():
        query = c.lower().replace("Video ", "").strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("open"):
         web=c.lower().split(" ")[1]
         webbrowser.open(impweb[web])
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music.music[song]
        webbrowser.open(link)

         
    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output) 
    
        
if __name__ == "__main__":
    speak("Initializing sachin....")
    while True:
  
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "sachin"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("sachin Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))