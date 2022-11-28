import cv2
import numpy as np

import reader
import parameters




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

# Score a piece of text based on the amount of alphabetic characters
def GetCalibrationScore(text):
    nonAlphabeticCount = 0
    for letter in text:
        if not letter.isalpha():
            nonAlphabeticCount += 1
    score = len(text) - nonAlphabeticCount
    return score

# Brute-force sharpness calibration
def CalibrateSharpness(image):
    bestScore = 0
    bestSharpnessValue = -1

    for sharpnessValue in range(parameters.CALIBRATION_START,parameters.CALIBRATION_END):
        score = GetCalibrationScore(reader.Read(Sharpen(image,amount=sharpnessValue/10.0)))
        #print(sharpnessValue,score)
        if(score > bestScore): 
            bestSharpnessValue = sharpnessValue
            bestScore = score

    print("Best:", bestSharpnessValue,bestScore)
    return bestSharpnessValue/10.0
