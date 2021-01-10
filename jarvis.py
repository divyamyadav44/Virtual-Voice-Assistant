import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import datetime
engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[0].id) 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12: 
        speak("Good Moring Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    elif hour>=18 and hour<22:
        speak("Good Evenig Sir")
    elif hour>=22 and hour<=24:
        speak("Good Night Sir")
    speak("I am your Assistant How may i help you")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio =r.listen(source)
    try:      
        print("Recongnizing")
        query= r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)

        print("Say that again ")
        return "None"
    return query

if __name__ == "__main__":
    #speak("divyam  is good")
    wishme()
    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia..")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("Accoring to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query: 
            music_dir='C:\\Users\\divyam\\Desktop\\music'
            songs=os.listdir(music_dir)
            x=int(random.randrange(1,10))
            #print(songs)
            os.startfile(os.path.join(music_dir,songs[x]))
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is{strTime}")