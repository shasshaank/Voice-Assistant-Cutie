import speech_recognition as sr
import pyttsx3   ##
import datetime 
import wikipedia  
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import subprocess
from AppOpener import run
import tkinter as tk


top = tk.Tk()
# Code to add widgets will go here...
greeting = tk.Label(text="Personal AI assisstant - Cutie",
  foreground="white",
  background="green",
  width=40,
  height=20
  )
greeting.pack()

print('Loading your AI personal assistant - Cutie')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',175)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your A I personal assistant Cutie")
wishMe()


if __name__=='__main__':


    while True:
        speak("How can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "goodbye" in statement or "ok bye" in statement or "stop" in statement or 'bye' in statement:
            speak('your personal assistant CUTIE is shutting down,Good bye')
            print('your personal assistant CUTIE is shutting down,Good bye')
            break



        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement,sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail is open now")
            time.sleep(5)

        elif 'open facebook' in statement:
            webbrowser.open_new_tab("https://www.facebook.com/")
            speak("Facebook is open now")
            time.sleep(5)

        elif 'open instagram' in statement:
            webbrowser.open_new_tab("https://www.instagram.com/")
            speak("Instagram is open now")
            time.sleep(5)

        elif 'open twitter' in statement:
            webbrowser.open_new_tab("https://www.twitter.com/")
            speak("TWITTER is open now")
            time.sleep(5)

        elif 'open linked in' in statement or 'open linkedin' in statement:
            webbrowser.open_new_tab("https://www.linkedin.com/")
            speak("Linked In is open now")
            time.sleep(5)

        elif 'open amazon' in statement:
            webbrowser.open_new_tab("https://www.amazon.com/")
            speak("AMAZON is open now")
            time.sleep(5)

        elif 'open flipkart' in statement:
            webbrowser.open_new_tab("https://www.flipkart.com/")
            speak("FLIPKART is open now")
            time.sleep(5)

        elif 'open skype' in statement:
            webbrowser.open_new_tab("https://www.skype.com/")
            speak("SKYPE is open now")
            time.sleep(5)

        elif 'open github' in statement:
            webbrowser.open_new_tab("https://www.github.com/")
            speak("Github is open now")
            time.sleep(5)
            
        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" Pardon,can you repeat it again!")



        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")


        elif 'bennett' in statement:
            webbrowser.open_new_tab("https://www.bennett.edu.in/")
            speak("Bennett University's website is open now")
            time.sleep(5)

        elif 'open teams' in statement:
            run("Microsoft Teams")
            speak("Teams is running now")
            time.sleep(5)


        elif "open settings" in statement:
            run("Settings")
            speak("Setting is open now")
            time.sleep(5)


        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am your Cutie version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather, open calculator,' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!'
                  'opening different social media websites such as facebook, instagram, twitter, linked in, skype, github!'
                  'some of the e-shopping websites such as amazon and flipkart!!')

        elif 'open spotify' in statement:
            run("Spotify")
            speak("Spotify is running now")
            time.sleep(5) 

        elif "do you love me" in statement:
            speak("Obviously, I love you darling")

        elif 'i love you' in statement:
            speak("Awww, I love you too baeby.")


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by FACE BYTE'S TEAM")
            print("I was built by FACE BYTE'S TEAM")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(5)

        elif "camera" in statement or "take a photo" in statement:
            run("Camera")
            speak("Camera is open now")
            time.sleep(5)

        elif "open calculator" in statement:
            subprocess.Popen("C:\Windows\System32\calc.exe")
            speak("Calculator is open now")
            time.sleep(5)

        elif "open zoom" in statement:    
            run("Zoom")
            speak("Zoom is running now")
            time.sleep(5)

        elif "open whatsapp" in statement:
            run("Whatsapp")
            speak("WHATSAPP is open now")
            time.sleep(5)

        elif "open vs code" in statement:
            run("Visual Studio Code")
            speak("VS code is open now")
            time.sleep(5)

        elif "open paint" in statement:
            run("Paint")
            speak("Paint is open now")
            time.sleep(5)

        elif 'search'  in statement:
            statement = statement.replace("search","")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)


        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)
top.mainloop()