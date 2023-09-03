# importing the pyttsx library
# pip install pyttsx3
# https://www.codespeedy.com/how-to-install-pyttsx3-in-python-and-convert-text-into-speech-offline/#google_vignette


import pyttsx3
  
# initialisation
engine = pyttsx3.init()
  


class KilobotSpeechClass():
    def __init__(self):
        engine.init()
        self.EnableSpeech = True

    # Commands
    def say_hello(self):
        # testing
        engine.say("My first code on text-to-speech")
        engine.say("Thank you, Geeksforgeeks")
        engine.runAndWait()

def main():
    MySpeechClass = KilobotSpeechClass()
    print("speech enabled")
    MySpeechClass.say_hello()


# Main
if __name__ == "__main__":
    main()

