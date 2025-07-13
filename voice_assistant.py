import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize recognizer and speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen to voice
def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not catch that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

# Main logic
def run_assistant():
    speak("Hello, how can I help you today?")
    while True:
        command = listen_command()

        if 'hello' in command:
            speak("Hello! Nice to talk to you.")
        
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The current time is {time}")

        elif 'date' in command:
            date = datetime.datetime.now().strftime('%B %d, %Y')
            speak(f"Today's date is {date}")

        elif 'search for' in command:
            search_query = command.replace('search for', '').strip()
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {search_query}")
        
        elif 'exit' in command or 'stop' in command:
            speak("Goodbye!")
            break

        elif command != "":
            speak("I'm not sure how to respond to that yet.")

# Run the assistant
run_assistant()
