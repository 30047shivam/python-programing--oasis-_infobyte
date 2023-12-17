import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime

def speak(text):
    """
    Function to convert text to speech.

    Parameters:
    - text: The text to be spoken.
    """
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech

    # Convert the text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

def take_command():
    """
    Function to capture user speech input.

    Returns:
    - str: The recognized speech as text.
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Error connecting to Google API: {e}")
        return None

def wishes():
    """
    Function to provide different greetings based on the time of day.
    """
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if 0 <= hour < 12:
        speak("Good morning! How can I assist you?")
    elif 12 <= hour < 18:
        speak("Good afternoon! How may I assist you?")
    else:
        speak("Good evening! How can I help you now?")

# Example usage
wishes()
speak("Hello, I am Jarvis. How can I assist you today?")

# Continuously listen for commands and execute tasks
while True:
    query = take_command()
    if query:
        speak(f"You said: {query}")

        # Execute tasks based on user's query
        if "wikipedia" in query:
            search_query = query.replace("wikipedia", "").strip()
            result = wikipedia.summary(search_query, sentences=2)
            speak(f"According to Wikipedia, {result}")
        elif "open google" in query:
            webbrowser.open("https://www.google.com")
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
        elif "open stackoverflow" in query:
            webbrowser.open("https://stackoverflow.com")
        elif "open quora" in query:
            webbrowser.open("https://www.quora.com")
        elif "open linkedin" in query:
            webbrowser.open("https://www.linkedin.com")
        elif "the time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {current_time}")
        elif "open code" in query:
            os.system("code")  # Assuming "code" is the command to open Visual Studio Code
        else:
            speak("I'm sorry, I didn't understand that.")
