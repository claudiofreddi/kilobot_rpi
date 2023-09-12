import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 125) 
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
voice_id = 'italian'
engine.setProperty('voice', voice_id)
engine.say('Ciao, sono Kilo bot.')
engine.say('Tu chi sei ?')
#engine.say('Lorenzo.')
#engine.say('Stai Studiando ?')
engine.runAndWait()