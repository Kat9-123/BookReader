from gtts import gTTS
from pygame import mixer
import time
import os

import parameters



ttsCounter = 0

def Initialise():
    mixer.init()


def IsBusy():
    return mixer.music.get_busy()
        

def PauseWhileBusy():
    while IsBusy():
        time.sleep(0.25)

def Say(path, blocking=False):
    music = mixer.music.load(path)
    mixer.music.play()


    if(not blocking): return

    PauseWhileBusy()


def SayStandard(path, blocking=False):
    Say(os.path.join(parameters.STANDARD_AUDIO_PATH,path), blocking)


def GenerateTTS(text,name=""):
    global ttsCounter

    # Max 4 cached files.
    if name == "":
        if(ttsCounter >= 4): ttsCounter = 0

        path = os.path.join(parameters.TEMP_PATH,"tts" + str(ttsCounter) + ".mp3")

        if(os.path.exists(path)): os.remove(path)
        ttsCounter += 1
    else:
        path = name + ".mp3"
    

    tts = gTTS(text=text, lang="en", tld="co.uk", slow=False)

    tts.save(path)


    return path