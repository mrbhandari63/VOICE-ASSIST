import pyttsx3
import speech_recognition as sr
import pywhatkit
import wikipedia
import webbrowser
import requests
from hugchat import hugchat
from bs4 import BeautifulSoup


# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set properties for the voice engine
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 180)

def speak(audio):
    try:
        engine.say(audio)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in speak function: {e}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, timeout=4, phrase_time_limit=4)
        
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

def searchGoogle(query):
    query = query.replace("jarvis", "").replace("google search", "").replace("google", "").strip()
    speak("This is what I found on Google.")
    try:
        pywhatkit.search(query)
        result = wikipedia.summary(query, sentences=1)
        speak(result)
    except Exception as e:
        print(f"Error: {e}")
        speak("No speakable output is available.")

def searchYoutube(query):
    query = query.replace("youtube search", "").replace("youtube", "").replace("jarvis", "").strip()
    speak("This is what I found for your search!")
    web = "https://www.youtube.com/results?search_query=" + query
    webbrowser.open(web)
    pywhatkit.playonyt(query)
    speak("Done, sir!")

def searchWikipedia(query):
    query = query.replace("wikipedia", "").replace("search wikipedia", "").replace("jarvis", "").strip()
    speak("Searching from Wikipedia...")
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia...")
        print(results)
        speak(results)
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Error: {e}")
        speak("The query is ambiguous, please be more specific.")
    except Exception as e:
        print(f"Error: {e}")
        speak("An error occurred while searching Wikipedia.")
def chatBot(query):
    user_input= query.lower();
    chatbot=hugchat.ChatBot(cookie_path=r"C:\Users\ADMIN\OneDrive - Graphic Era University\Desktop\pro\cookies.json")
    id= chatbot.new_conversation()
    chatbot.change_conversation(id)
    response=chatbot.chat(user_input)
    speak(response)
    print(response)    
