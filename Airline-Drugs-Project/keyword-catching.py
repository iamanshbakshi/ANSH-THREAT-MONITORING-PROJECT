#part-4 running through cmd:-python f:/Airline-Drugs-Project/keyword-catching.py


import speech_recognition as sr
import pyttsx3

# List of alert words
alert_words = ["drugs", "weapons", "hijack", "kill", "threat","narcotic"]

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Function to count alert words in the text
def count_alert_words(text, words):
    word_count = {word: 0 for word in words}
    for word in text.lower().split():
        if word in word_count:
            word_count[word] += 1
    return word_count

with sr.Microphone() as source:
    print("Listening... please start speaking and press enter once done")
    audio = recognizer.listen(source)

try:
    # Recognize speech using Google Speech Recognition
    text = recognizer.recognize_google(audio)
    print("\nYou said:", text)
    
    # Count occurrences of alert words
    word_count = count_alert_words(text, alert_words)
    
    # Check if any alert word is mentioned
    if any(count > 0 for count in word_count.values()):
        engine.say("Alert, alert, alert,alert ,alert ,alert ,pls check")
        engine.runAndWait()
        for word, count in word_count.items():
            if count > 0:
                print(f"The word '{word}' was mentioned {count} times.")
    else:
        print("No alert words mentioned.")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
except Exception as e:
    print(f"An error occurred: {e}")
