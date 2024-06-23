#part-3  #running through cmd:-python f:/Airline-Drugs-Project/ansh_speech_recognition.py


import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening... pls start speaking and press enter once done ")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("\n you said:", text)
except:
    print('error not recognized pls try once ')

    