# part-6 run through cmd :- python f:/Airline-Drugs-Project/final_ansh.py

import speech_recognition as sr
import pyttsx3
from datetime import datetime

alert_words = ["drugs", "weapons", "hijack", "kill", "threat", "narcotic"]

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def count_alert_words(text, words):
    word_count = {word: 0 for word in words}
    for word in text.lower().split():
        if word in word_count:
            word_count[word] += 1
    return word_count

def save_results(timestamp, text, word_count):
    with open("threat.txt", "a") as file:
        file.write(f"Timestamp: {timestamp}\n")
        file.write(f"Text: {text}\n")
        for word, count in word_count.items():
            file.write(f"{word}: {count} times\n")
        file.write("\n")

all_recognized_text = []

print("Listening... (say 'delta stop' to end)")

while True:
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print("\nYou said:", text)
        all_recognized_text.append(text)
        
        if "delta stop" in text.lower():
            print("Stop command received. Processing the results...")
            break
    
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

combined_text = ' '.join(all_recognized_text)
word_count = count_alert_words(combined_text, alert_words)
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if any(count > 0 for count in word_count.values()):
    engine.say("Alert, alert, alert, alert")
    engine.runAndWait()
    for word, count in word_count.items():
        if count > 0:
            print(f"The word '{word}' was mentioned {count} times.")
    save_results(timestamp, combined_text, word_count)
else:
    print("No alert words mentioned.")

