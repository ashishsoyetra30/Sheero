import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #getting details of current voice
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio) 
    # print(voices[1].id)
    engine.runAndWait() #Without this command, speech will not be audible to us.

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")    
    
    else:
        speak("Good Evening!")

    speak("I am Doremon Nobita! I won't help you this time or maybe i will do if you treat me up with doracake...if yes then go on what do you want")    

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)    

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in') 
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Please Say That Again")
        return "None" 
    return query

def sendEmail(do, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #Logic for executing tasks based on query
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results) 


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")


        elif 'open google' in query:
            webbrowser.open("google.com")


        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 



        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'open code' in query:
            codePath = "C:\\Users\\ashis\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        elif 'quit' in query:
            exit(1)
        
        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry my friend ashu bhai. I am not able to send this email")        
