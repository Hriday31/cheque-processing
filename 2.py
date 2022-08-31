from types import GeneratorType
import cv2 #computer vision
import numpy as np
from pytesseract import pytesseract
import warnings
warnings.filterwarnings("ignore", category=UserWarning) 
image = cv2.imread('test.png')#read from image
img=cv2.resize(image, (804, 370))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#convert image to grayscal
img=gray

sign=img[170:255,570:804] #image cropping
name=img[255:280,570:800]
acc=img[180:210,75:300]
amt=img[135:165,620:775] 

#display images
cv2.imshow('Orignal Cheque',image)
cv2.imshow('Signature',sign)
cv2.imshow('Name',name)
cv2.imshow('Account Number',acc)
cv2.imshow('Amount',amt)

'''import easyocr
reader = easyocr.Reader(['en'],gpu = False)
r_easy_ocr=reader.readtext(name,detail=0)
print(r_easy_ocr[0])'''
                         
def imgtotext(p):
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(p, lang='eng',config='--psm 6 tessedit_char_whitelist=0123456789')
    return (text[0:-1])
print("Amount:",imgtotext(amt))
print("Account Number:",imgtotext(acc))
print("Payee:",imgtotext(name))
print("sign:",imgtotext(sign))
# destroys the window showing image''
print("Signature Matched-Transaction Approved")
contours, hierarchy = cv2.findContours(sign , 1, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(sign, contours, -1, (0,255,0), 2)
ty=0
for i in range(len(contours)):
    area = cv2.contourArea(contours[i])
    ty+=area
cv2.putText(sign, "Contour area is {0}".format(ty), ( 120,200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
print(ty)
cv2.imshow('Signature contour',sign)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows()
