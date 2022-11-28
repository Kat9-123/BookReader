import cv2
import os

import parameters




camera = None


def Intitialise():
    global camera

    if parameters.READ_FROM_CACHE: return

    camera = cv2.VideoCapture(parameters.CAMERA_PORT, cv2.CAP_DSHOW)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)


    

def Capture():

    # Either read cached image or capture a new one
    imagePath = os.path.join(parameters.TEMP_PATH, "original.png")

    if parameters.READ_FROM_CACHE:
        image = cv2.imread(imagePath)
    else:

        i = 0
        while i < parameters.CAMERA_WAIT_FRAMES:
            result, imgage = camera.read()
            i += 1
        cv2.imwrite(imagePath,image)


    # Cut the image in half
    width = image.shape[1]
    width_cutoff = width // 2
    left = image[:, :width_cutoff]
    right = image[:, width_cutoff:]

    cv2.imwrite(os.path.join(parameters.TEMP_PATH, "left.png"), left)
    cv2.imwrite(os.path.join(parameters.TEMP_PATH, "right.png"), right)
    
    return (left,right)
    

    