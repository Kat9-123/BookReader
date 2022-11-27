import pytesseract


def Initialise():
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def Read(image):
    
    s = pytesseract.image_to_string(image, lang="eng")

    s = s.replace("-\n","")
    s = s.replace("\n"," ")
    s = s.replace("|","I")

    return s