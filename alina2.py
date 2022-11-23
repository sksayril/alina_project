import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os
import smtplib
import pyaudio
import twilio



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[3].id)
engine.setProperty('voice',voices[-1].id)
  

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good, Noon!")
    elif hour>=16 and hour<19:
        speak("Good Afternoon!")
    elif hour>=19 and hour<21:
        speak("Good Evening")
    else:
        speak("Good Night!")    
    speak("Hello Sir, I'm, Alina, How may I help You sir")
def takeCommand():
    #It Take microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("Listenning......")
        r.pause_threshold>=0.001
        r.listen_in_background
        r.non_speaking_duration
        audio=r.listen(source)
    try:
        ("Recognizing")
        query=r.recognize_google(audio,language='en-in')
        print(f"use said:,{query}\n")
    except Exception as e:

        ("say taht again please...")
        return "None"
    return query
if __name__=="__main__":
     
    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query=query.replace("wikipiedia","")
            result=wikipedia.summary(query, sentences=3 )
            speak("According to wikipedia")
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening Youtube")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak("opening facebook")
        elif 'open twitter' in query:
            webbrowser.open("twitter.com")
            speak("opening twitter")
        elif 'who are you' in query:
            speak('''I'm a virtual assistance. My sir is Design for me. I will Improve and my behavior is  Try good
             . I am programed By python language.''')
        elif 'twitter' in query:
            webbrowser.open("twitter.com")
            speak("Opening twitter")
        elif'open my site' in query:
            speak("This Web Site is A, Static Web Page. Web Site is Under Maintainents")
            webbrowser.open("https://webbiscuit.000webhostapp.com/")
            speak("Openinng")
        elif 'open kitpot' in query:
            webbrowser.open("kitpot.in")
            speak("open kitpot")