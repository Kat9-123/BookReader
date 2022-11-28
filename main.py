import cv2



import calibration
import speaker
import reader
import photographer








# Initialisation
print("Initialising...")
speaker.Initialise()
reader.Initialise()
photographer.Intitialise()





def ProcessImage(image):

    # Greyscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Sharpen
    image = calibration.Sharpen(image,amount=calibration.CalibrateSharpness(image))

    cv2.imwrite("temp\\preprocessed.png",image)



    return image


def Read(image):

    print("Preprocessing...")
    if not speaker.IsBusy(): speaker.SayStandard("Preprocessing.mp3",False)
    image = ProcessImage(image)

    print("Reading...")
    if not speaker.IsBusy(): speaker.SayStandard("Reading.mp3", False)

    text = reader.Read(image)

    print(text)

    if not speaker.IsBusy(): speaker.SayStandard("GeneratingTTS.mp3", False)
    print("Generating TTS...")

    tts = speaker.GenerateTTS(text)
    print("Done generating.")
    speaker.PauseWhileBusy()

    print("Speaking")
    speaker.Say(tts,False)




speaker.SayStandard("FirstImage.mp3",False)
input("Press enter to capture an image.")


while True:

    left, right = photographer.Capture()

    Read(left)

    Read(right)

    speaker.PauseWhileBusy()
    speaker.SayStandard("DoneReading.mp3",False)
    input("Done reading.")
