import pyttsx3


engine = pyttsx3.init()

voices = engine.getProperty('voices')
if voices:
    engine.setProperty('voice', voices[0].id)

engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

text = input("Type: ")

engine.say(text)
engine.runAndWait()