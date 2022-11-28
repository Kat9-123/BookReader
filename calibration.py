import cv2
import reader
import numpy as np


CALIBRATION_START = 45#5
CALIBRATION_END = 60#50


# https://stackoverflow.com/questions/4993082/how-can-i-sharpen-an-image-in-opencv
def Sharpen(image, kernel_size=(5, 5), sigma=1.0, amount=2.5, threshold=1):
    blurred = cv2.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    return sharpened

def GetCalibrationScore(text):
    x = 0
    for i in text:
        if not i.isalpha():
            x += 1
    score = len(text) - x
    return score


def CalibrateSharpness(image):
    bestScore = 0
    bestSharpnessValue = -1

    for sharpnessValue in range(CALIBRATION_START,CALIBRATION_END):


        score = GetCalibrationScore(reader.Read(Sharpen(image,amount=sharpnessValue/10.0)))
        #print(sharpnessValue,score)
        if(score > bestScore): 
            bestSharpnessValue = sharpnessValue
            bestScore = score

    print("Best:", bestSharpnessValue,bestScore)
    return bestSharpnessValue/10.0
       

# Depricated
"""
def Calibrate(image):


    bestScore = 0
    bestThresholdValue = -1

    calibrationCount = (CALIBRATION_END - CALIBRATION_START) // CALIBRATION_STEP
    print(calibrationCount)
    for thresholdValue in range(CALIBRATION_START,CALIBRATION_END,CALIBRATION_STEP):

    #    percentage = str(int(((i)/calibrationCount) * 100)) + "%"
     #   print("Calibrating... " + percentage + "           ", end="\r")

       # speaker.Say(speaker.GenerateTTS(percentage), True)

        score = GetCalibrationScore(reader.Read(Threshold(image,thresholdValue)))
        print(thresholdValue,score)
        if(score > bestScore): 
            bestThresholdValue = thresholdValue
            bestScore = score

    print("Best:", bestThresholdValue,bestScore)
    return bestThresholdValue
    



def Threshold(image,i):
    ret,thresh = cv2.threshold(image,i,255,cv2.THRESH_BINARY)

    return thresh
"""