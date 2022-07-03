import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
# creating the object

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print((voices[1].id))


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# speak("let us watch code with harry")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak(" good morning sir")
    elif(hour>12 and hour <= 18):
        speak("good afternoon sir")
    elif(hour>18 and hour< 20):
        speak("good evening sir")
    else:
        speak("good night sir")

    speak(" i am a bot. How may i help you bro ? ")

wishMe()

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognising.......")
        query = r.recognize_google(audio,language='en-in')
        print("user said " + str(query))

    except Exception as e:
        # print(e)
        print("sorry, i coudn't hear you, say that again please.. ")
        return "None"
    return query

while True:
    query = takeCommand().lower()

    #  logic for executing tasks in query

    # task 1 = wikipedia
    if 'wikipedia' in query:
        speak("searching wikipedia.....")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences = 2)
        speak("according to wikipedia....")
        speak(results)

    # task 2 : search a website on the web
    elif 'youtube' in query:
        webbrowser.open("https://youtu.be")
    elif 'google' in query:
        webbrowser.open("https://google.com")
    elif 'amazon' in query:
        webbrowser.open("https://amazon.in")
    elif 'github' in query:
        webbrowser.open("https://github.com/atharva100")
    elif 'stackoverflow' in query:
        webbrowser.open("https://stackoverflow.com")
    elif 'thankyou' in query:
        speak(" welcome, im glad i helped you")
    elif 'shape of you' in query:
        webbrowser.open("https://www.youtube.com/watch?v=4_cnVRbZEqI")
    elif 'top' or 'end' or 'finish' in query:
        speak("well,im going to sleep now, thank you for being such a patient guest!")
        print("exiting the loop..")
        break
    # task : tell the current time
    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak("the current time is " + str(strTime))

    #  to open an application on your pc
    # elif 'spotify' in query:
    #     codepath = "C:\\Users\HP\AppData\Roaming\Spotify\Spotify.exe"
    #     os.startfile(codepath)
