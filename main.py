
import cv2
import numpy as np
from PIL import Image

from matplotlib import pyplot as plt





import calibration
import speaker
import reader
import photographer
import time














thresholdValue = -1





print("Initialising...")
speaker.Initialise()
speaker.SayStandard("Initialising.mp3",False)
reader.Initialise()
photographer.Intitialise()





def ProcessImage(image):

    print("Preprocessing...")

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    image = calibration.Sharpen(image,amount=calibration.CalibrateSharpness(image))
    cv2.imwrite("temp\\preprocessed.png",image)






    cv2.destroyAllWindows()
    return image


def Read(image):
    print("Reading...")

    s = reader.Read(image)
    print(s)


    print("Generating TTS...")

    tts = speaker.GenerateTTS(s)
    while(speaker.IsBusy()): time.sleep(0.25)

    print("READING!")
    speaker.Say(tts,False)



while True:
    original, left, right = photographer.Capture()

    left = ProcessImage(left)

    Read(left)

    right = ProcessImage(right)

    Read(right)

    input("Done")