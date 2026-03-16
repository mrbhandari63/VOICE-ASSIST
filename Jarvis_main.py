import pyttsx3
import speech_recognition as sr
import pyaudio
import requests
from bs4 import BeautifulSoup
import datetime


# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set properties for the voice engine
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 220)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.energy_threshold = 300
        audio = r.listen(source, timeout=3, phrase_time_limit=3)
    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that. Can you please repeat?")
        return "None"
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service; check your network connection.")
        return "None"
    return query

def normalize_text(text):
    # Normalize common variations
    text = text.lower()
    replacements = {
        "how r u": "how are you",
        "i m fine": "i am fine",
        "thank u": "thank you"
    }
    for original, replacement in replacements.items():
        text = text.replace(original, replacement)
    return text

if __name__ == "__main__":
    engine.say("Hello sir, my name is Jarvis")
    engine.runAndWait()

    while True:
        query = takeCommand().lower()
        if query is None:
            continue
        
        query = normalize_text(query)
        
        if "wake up" in query:
            try:
                from Greet_me import greetMe
                greetMe()
            except ImportError:
                print("Module Greet_me not found. Please ensure it is available.")
                speak("Module Greet_me not found. Please ensure it is available.")

            while True:
                query = takeCommand().lower()
                if query is None:
                    continue
                
                query = normalize_text(query)
                
                if "go to sleep" in query:
                    speak("Ok sir, You can call me anytime")
                    break

                elif "hello" in query:
                    speak("Hello sir, how are you?")

                elif "i am fine" in query:
                    speak("That is great, sir")

                elif "how are you" in query:
                    speak("Perfect, sir")

                elif "thank you" in query:
                    speak("You are welcome, sir")
                
                # elif "open" in query:
                    
                
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                elif "temperature" in query or "weather" in query:
                    search = "temprature in Nainital(Uttarakhand)"
                    url = f"https://www.google.com/search?q={search}"
                    r=requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp= data.find("div",class_= "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "time" in query:
                    strTime= datetime.datetime.now().strftime("%H:%M")
                    speak(f"sir, the time is{strTime}")
                
                elif "finally sleep" in query:
                    speak("I am going to sleep")
                    exit()
                else:
                    from SearchNow import chatBot
                    chatBot(query)
                
                    
