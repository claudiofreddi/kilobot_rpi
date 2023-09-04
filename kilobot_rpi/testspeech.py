import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 125) 
voice_id = 'italian'
engine.setProperty('voice', voice_id)
engine.say('Ciao, sono Kilo bot')
engine.runAndWait()