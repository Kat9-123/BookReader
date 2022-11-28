import cv2
import os

import calibration
import speaker
import reader
import photographer
import parameters





def ProcessImage(image):

    # Greyscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    # Sharpen
    sharpnessValue = calibration.CalibrateSharpness(image)
    image = calibration.Sharpen(image,amount=sharpnessValue)

    cv2.imwrite(os.path.join(parameters.TEMP_PATH,"preprocessed.png"),image)

    return image


def Read(image):

    # Preprocessing
    print("Preprocessing...")
    if not speaker.IsBusy(): speaker.SayStandard("Preprocessing.mp3",False)

    image = ProcessImage(image)


    # Reading
    print("Reading...")
    if not speaker.IsBusy(): speaker.SayStandard("Reading.mp3", False)

    text = reader.Read(image)
    print("Text:")
    print(text)


    # TTS Generation
    if not speaker.IsBusy(): speaker.SayStandard("GeneratingTTS.mp3", False)
    print("Generating TTS...")

    tts = speaker.GenerateTTS(text)
    print("Done generating.")


    # Wait if the speaker is still busy with the previous page...
    speaker.PauseWhileBusy()


    # Speak
    print("Speaking...")
    speaker.Say(tts,False)



print("Initialising...")
speaker.Initialise()
reader.Initialise()
photographer.Intitialise()

speaker.SayStandard("FirstImage.mp3",False)

input("Press enter to capture an image.")

while True:

    left, right = photographer.Capture()

    Read(left)

    Read(right)

    speaker.PauseWhileBusy()
    speaker.SayStandard("DoneReading.mp3",False)
    input("Done reading.")
