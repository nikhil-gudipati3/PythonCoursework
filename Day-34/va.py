import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

#---------------------------------------
# SPEAK FUNCTION
# --------------------------------------
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', 'gmw/en-us')
    engine.setProperty('rate',170)
    engine.setProperty('volume',1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

#--------------------------------------
# LISTEN FUNCTION
# -------------------------------------

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening............')
        recognizer.pause_thereshold = 1
        audio = recognizer.listen(source)
        print('Audio Done')
    try:
        command = recognizer.recognize_google(audio, language='en-in')
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ''
    except sr.RequestError:
        speak('Speech service is unavailable')
        return ''

#------------------------------------------
# PROCESS COMMAND
# -----------------------------------------

speak("Hello Nikhil, I'am your Voice Assistant. How can i help you")


while True:
    command = listen()

    if 'time' in command:
        current_time = datetime.datetime.now().strftime(
            '%I:%M %p'
        )

        speak(
            f'The current time is {current_time}'
        )
    elif 'date' in command:
        today = datetime.datetime.now().strftime('%d %B %Y')
        speak(f"Todays' date is {today}")

    elif 'open google' in command:
        speak('opening google')
        webbrowser.open('https://www.google.com')

    elif 'open youtube' in command:
        speak('opening youtube')
        webbrowser.open('https://www.youtube.com')

    elif 'repati kosam' in command:
        speak('repati kosam')
        break
