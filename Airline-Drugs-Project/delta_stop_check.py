#part-5 run through cmd :- python f:/Airline-Drugs-Project/delta_stop_check.py

import speech_recognition as sr
import pyttsx3
import time

alert_words = ["drugs", "illegal weapon", "guns", "kill", "hijack", "narcotics", "bomb"]

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def count_alert_words(text, words):
    word_count = {word: 0 for word in words}
    for word in text.lower().split():
        if word in word_count:
            word_count[word] += 1
    return word_count

def is_stop_command(text):
    return "delta stop" in text.lower()

all_recognized_text = []

print("Listening... (say 'delta stop' to end)")

while True:
    with sr.Microphone() as source:
        try:
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=10)
            
            try:
                text = recognizer.recognize_google(audio)
                print("\nYou said:", text)
                all_recognized_text.append(text)
                
                if is_stop_command(text):
                    print("Stop command received. Processing the results...")
                    break
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

        except Exception as e:
            print(f"An error occurred: {e}")
            break

combined_text = ' '.join(all_recognized_text)

print("\nAll recognized text:")
print(combined_text)

word_count = count_alert_words(combined_text, alert_words)

if any(count > 0 for count in word_count.values()):
    for _ in range(7):
        engine.say("Alert")
    engine.runAndWait()
    for word, count in word_count.items():
        if count > 0:
            print(f"The word '{word}' was mentioned {count} times.")
else:
    print("No alert words mentioned.")



