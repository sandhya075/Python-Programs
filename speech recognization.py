
'''
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
engine = pyttsx3.init()
def speak(text):
    print('Assistant:',text)
    engine.say(text)
    engine.runAndWait()
          
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = take_command()
        print("YOU", command)
        return command.lower()
        
        speak("Sorry, I could not understand you.")
        return ""
    except sr.RequestError:
        speak('Speech recognition service is unavailable.')
        return ""
def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I help you?")
def run_assistant():
    wish_user()
    while True:
        command = take_command()
        if "hello" in command:
            speak("Hello HOw can I help you?")
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")
        elif 'open youtube' in command:
            speak("Opening Youtube")
            webbrowser.open("https://wwww.youtube.com")
        elif "open google" in command:
            speak("Opening  Google")
            webbrowser.open("https://www.google.com")
        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break
        else:
            speak("I don't know that command yet.")
run_assistant()
'''

import speech_recognition as sr
print("1. Program started")
print("2. Checking microphones...")
microphones = sr.Microphone.list_microphone_names()
print("3. Microphones found:", len(microphones))
for index, name in enumerate(microphones):
    print(index, name)
print("4. Creating microphone...")
mic = sr.Microphone()
print("5. Microphone created")
with mic as source:
    print("6. Microphone opened")
    print("7. Speak now...")
    recognizer = sr.Recognizer()
    audio = recognizer.listen(
        source,
        timeout=5,
        phrase_time_limit=5
    )
print("8. Recording completed")
print("9. Recognizing...")
text = recognizer.recognize_google(audio)
print("10. You said:", text)
    

