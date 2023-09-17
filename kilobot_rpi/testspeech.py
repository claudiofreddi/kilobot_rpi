import pyttsx3
#RPI
import RPi.GPIO as GPIO
import time

pin_ON_OFF_POWER = 6

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_ON_OFF_POWER, GPIO.OUT)

GPIO.output(pin_ON_OFF_POWER , 0)
print('Power On')

engine = pyttsx3.init()
engine.setProperty('rate', 125) 
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
voice_id = 'italian'
engine.setProperty('voice', voice_id)
engine.say('Ciao, sono Kilo bot.')
engine.say('Tu chi sei ?')
engine.say('Lorenzo.')
engine.say('Stai Studiando ?')
# engine.say('Ciao, sono Kilo bot.')
# engine.say('Tu chi sei ?')
# engine.say('Lorenzo.')
# engine.say('Stai Studiando ?')
engine.runAndWait()

#This Turns Relay Off. Brings Voltage to Max GPIO can output ~3.3V
GPIO.output(pin_ON_OFF_POWER , 1)
print('Power Off')
GPIO.cleanup() 