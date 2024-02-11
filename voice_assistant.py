import pyttsx3
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Function to convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Function to listen to user's voice input."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        user_input = recognizer.recognize_google(audio)
        print("User:", user_input)
        return user_input.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't get that. Can you please repeat?")
        return listen()
    except sr.RequestError:
        speak("Sorry, there was an error processing your request.")
        return None

def main():
    speak("Hello! I'm your voice assistant. How can I help you today?")
    
    while True:
        user_input = listen()
        
        if user_input is None:
            continue
        
        if "hello" in user_input:
            speak("Hello! How are you?")
        elif "how are you" in user_input:
            speak("I'm doing well, thank you for asking!")
        elif "what is your name" in user_input:
            speak("My name is Python Voice Assistant.")
        elif "goodbye" in user_input or "exit" in user_input:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("Sorry, I'm not sure how to help with that.")

if __name__ == "__main__":
    main()
