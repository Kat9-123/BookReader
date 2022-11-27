import cv2
import os

#PATH = r"C:\Users\trist\Desktop\ALB\School\IMG_8483.jpg"#r"C:\Users\trist\Desktop\ALB\School\5V4\Cis\Software\images\1984.jpg"
PATH = r"images\webcam.jpg"
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




def TestCapture():
    focus = 15
    while True:
        camera.set(cv2.CAP_PROP_FOCUS, focus) 
        result, img = camera.read()



        cv2.imwrite("temp\\a" + str(focus) + ".png",img)
        focus += 1

        if(focus == 36): input()
    

def Capture():
    # Read the image

    if READ_FROM_PATH:
        img = cv2.imread(PATH)
    else:

        i = 0
        while i < WAIT_TIME:
            result, img = camera.read()
            i += 1
        cv2.imwrite("temp\\orig.png",img)



    print(img.shape)
    height = img.shape[0]
    width = img.shape[1]

    # Cut the image in half
    width_cutoff = width // 2
    left = img[:, :width_cutoff]
    right = img[:, width_cutoff:]

    cv2.imwrite("temp\\left.png", left)
    cv2.imwrite("temp\\right.png", right)
    
    return (img,left,right)
    

    