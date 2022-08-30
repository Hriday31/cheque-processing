from types import GeneratorType
import cv2 #computer vision
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=UserWarning) 
image = cv2.imread('test.png')#read from image
gray=cv2.resize(image, (804, 370))
img = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)#convert image to grayscal


sign=img[170:255,570:844] #image cropping
name=img[255:280,570:844]
acc=img[180:210,75:300]
amt=img[135:165,615:775] 

cv2.imshow('gray', img)#display images
cv2.imshow('Orignal Cheque',image)
cv2.imshow(' Cheque',gray)
cv2.imshow('Signature',sign)
cv2.imshow('Name',name)
cv2.imshow('Account Number',acc)
cv2.imshow('Amount',amt)

'''import easyocr
reader = easyocr.Reader(['en'],gpu = False)
r_easy_ocr=reader.readtext(name,detail=0)
print(r_easy_ocr[0])'''
                         
#from PIL import Image
from pytesseract import pytesseract

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#Extract text from image
text = pytesseract.image_to_string(amt, lang='eng',config='--psm 6 tessedit_char_whitelist=0123456789')

print(text[1:-1])

cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image''
