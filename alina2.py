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
from AppOpener import run
# run("whatsapp") # Opens whatsapp if installed
# run("whatsapp, telegram")
engine = pyttsx3.init('sapi5')
engine2=pyttsx3
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
            speak("open")
        elif 'open wikipedia'in query:
            webbrowser.open("https://www.wikipedia.org")
            speak("open wikipedia")
        elif 'open excel' in query:
            run("Excel")
            speak("Opening Excel")
        elif 'open visual studio code' in query:
            run('visual Studio Code')
            speak("opening Visual studio code")
        elif 'open MS Word' in query:
            run('Word')
            speak("opening Word")
        elif 'open cortana' in query:
            run("cortana")
            speak("opening cortana")
# while True:
#     # take input
#     print("    CHAT WITH ME WITH YOUR REQUIREMENTS : ", end='')
#     p = input()
#     p = p.upper()
#     print(p)
 
#     if ("DONT" in p) or ("DON'T" in p) or ("NOT" in p):
#         pyttsx3.speak("Type Again")
#         print(".")
#         print(".")
#         continue
 
#     # assignments for different applications in the menu
#     elif ("GOOGLE" in p) or ("SEARCH" in p) or ("WEB BROWSER" in p) or ("CHROME" in p) or ("BROWSER" in p) or ("4" in p):
#         pyttsx3.speak("Opening")
#         pyttsx3.speak("GOOGLE CHROME")
#         print(".")
#         print(".")
#         os.system("chrome")
 
#     elif ("IE" in p) or ("MSEDGE" in p) or ("EDGE" in p) or ("8" in p):
#         pyttsx3.speak("Opening")
#         pyttsx3.speak("MICROSOFT EDGE")
#         print(".")
#         print(".")
#         os.system("msedge")
 
#     elif ("NO" in p) or ("NOTES" in p) or ("NOTEPAD" in p) or ("EDITOR" in p) or ("9" in p):
#         pyttsx3.speak("Opening")
#         pyttsx3.speak("NOTEPAD")
#         print(".")
#         print(".")
#         os.system("Notepad")
 
#     elif ("VLCPLAYER" in p) or ("PLAYER" in p) or ("VIDEO PLAYER" in p) or ("5" in p):
#         pyttsx3.speak("Opening")
#         pyttsx3.speak("VLC PLAYER")
#         print(".")
#         print(".")
#         os.system("VLC")
 
#     elif ("ILLUSTRATOR" in p) or ("AI" in p) or ("6" in p):
#         pyttsx3.speak("Opening")
#         pyttsx3.speak("ADOBE ILLUSTRATOR")
#         print(".")
#         print(".")
#         os.system("illustrator")
 
#     elif ("PHOTOSHOP" in p) or ("PS" in p) or ("PHOTOSHOP CC" in p) or ("7" in p):
#         pyttsx3.speak("Opening")
#         pyttsx3.speak("ADOBE PHOTOSHOP")
#         print(".")
#         print(".")
#         os.system("photoshop")
 
#     elif ("TELEGRAM" in p) or ("TG" in p) or ("10" in p):
#         pyttsx3.speak("Opening")
#         pyttsx3.speak("TELEGRAM")
#         print(".")
#         print(".")
#         os.system("telegram")
 
#     elif ("EXCEL" in p) or ("MSEXCEL" in p) or ("SHEET" in p) or ("WINEXCEL" in p) or ("3" in p):
#         pyttsx3.speak("Opening")
#         pyttsx3.speak("MICROSOFT EXCEL")
#         print(".")
#         print(".")
#         os.system("excel")
 
#     elif ("SLIDE" in p) or ("MSPOWERPOINT" in p) or ("PPT" in p) or ("POWERPNT" in p) or ("2" in p):
#         pyttsx3.speak("Opening")
#         pyttsx3.speak("MICROSOFT POWERPOINT")
#         print(".")
#         print(".")
#         os.system("powerpnt")
 
#     elif ("WORD" in p) or ("MSWORD" in p) or ("1" in p):
#         pyttsx3.speak("Opening")
#         pyttsx3.speak("MICROSOFT WORD")
#         print(".")
#         print(".")
#         os.system("winword")
 
#     # close the program
#     elif ("EXIT" in p) or ("QUIT" in p) or ("CLOSE" in p) or ("0" in p):
#         pyttsx3.speak("Exiting")
#         break
 
#     # for invalid input
#     else:
#         pyttsx3.speak(p)
#         print("Is Invalid,Please Try Again")
#         pyttsx3.speak("is Invalid,Please try again")
#         print(".")
#         print(".")