import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greeting():
    hour = int(datetime.datetime.now().hour)
    if 10 <= hour < 12:
        speak("Good Morning")

    elif 12 <= hour <= 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

speak("Hello! How may I assist you?")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Try Again")
        return "None"
    return query.lower()

if __name__ == "__main__":
    greeting()
    query = listen()

    if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia ")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com")
    elif 'open google' in query:
        webbrowser.open("https://www.google.com")
    elif 'music' in query:
        speak("Opening Spotify")
        webbrowser.open("https://www.spotify.com")
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"Sir, the time is {strTime}")    
     
    
