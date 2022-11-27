from gtts import gTTS
from pygame import mixer
import time
import random
import os


TEMP = "temp"
STANDARD = "standard"


ttsCounter = 0

def Initialise():
    mixer.init()



def IsBusy():
    return mixer.music.get_busy()
        


def Say(path, blocking=False):
    music = mixer.music.load(path)
    mixer.music.play()
    if(not blocking): return


    while mixer.music.get_busy():
        time.sleep(0.1)


def SayStandard(path, blocking=False):
    Say(os.path.join(STANDARD,path), blocking)


def GenerateTTS(text,name=""):
    global ttsCounter

    if name == "":
        if(ttsCounter >= 4): ttsCounter = 0

        path = os.path.join(TEMP,"tts" + str(ttsCounter) + ".mp3")

        if(os.path.exists(path)): os.remove(path)
    else:
        path = name + ".mp3"
    

    tts = gTTS(text=text, lang="en", tld="co.uk", slow=False)
    name = os.path.join(path)
    tts.save(name)


    ttsCounter += 1


    return name