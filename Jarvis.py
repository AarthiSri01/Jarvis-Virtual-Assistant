import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_to_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said: " + command)  # Debugging statement
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, there was a problem with the speech recognition service.")
            speak("Sorry, there was a problem with the speech recognition service.")
            return None

def execute_command(command):
    print(f"Command received: {command}")  # Debugging statement
    if 'open notepad' in command:
        os.system('notepad')
        speak("Opening Notepad.")
    elif 'open calculator' in command:
        os.system('calc')
        speak("Opening Calculator.")
    elif 'search for' in command:
        query = command.replace('search for', '').strip()
        webbrowser.open(f'https://www.google.com/search?q={query}')
        speak(f"Searching for {query}.")
    elif 'what time is it' in command:
        now = datetime.datetime.now()
        current_time = now.strftime('%H:%M:%S')
        speak(f"The time is {current_time}.")
    elif 'open google' in command:
        webbrowser.open('https://www.google.com')
        speak("Opening Google.")
    elif 'open youtube' in command:
        webbrowser.open('https://www.youtube.com')
        speak("Opening YouTube.")
    elif 'open gmail' in command:
        webbrowser.open('https://mail.google.com')
        speak("Opening Gmail.")
    elif 'open facebook' in command:
        webbrowser.open('https://www.facebook.com')
        speak("Opening Facebook.")
    elif 'open twitter' in command:
        webbrowser.open('https://www.twitter.com')
        speak("Opening Twitter.")
    elif 'open instagram' in command:
        webbrowser.open('https://www.instagram.com')
        speak("Opening Instagram.")
    elif 'exit' in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I don't understand that command.")

def main():
    speak("How can I assist you?")
    while True:
        command = listen_to_command()
        if command:
            execute_command(command)

if __name__ == "__main__":
    main()
