import cv2

PATH = "temp\\orig.png"
CAMERA_PORT = 1

READ_FROM_PATH = True

WAIT_TIME = 100

camera = None


def Intitialise():
    global camera

    if READ_FROM_PATH: return

    camera = cv2.VideoCapture(CAMERA_PORT, cv2.CAP_DSHOW)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)


    

def Capture():

    # Either read cached image or capture a new one
    if READ_FROM_PATH:
        img = cv2.imread(PATH)
    else:

        i = 0
        while i < WAIT_TIME:
            result, img = camera.read()
            i += 1
        cv2.imwrite("temp\\orig.png",img)


    # Cut the image in half
    width = img.shape[1]
    width_cutoff = width // 2
    left = img[:, :width_cutoff]
    right = img[:, width_cutoff:]

    cv2.imwrite("temp\\left.png", left)
    cv2.imwrite("temp\\right.png", right)
    
    return (left,right)
    

    