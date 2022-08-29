from types import GeneratorType
import cv2 #computer vision
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=UserWarning) 
image = cv2.imread('/home/hra/Downloads/test.png')#read from image

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#convert image to grayscal

img=gray
sign=img[170:255,570:844] #image cropping
name=img[255:280,570:844]
acc=img[180:210,75:300]
amt=img[135:165,615:775] 

cv2.imshow('gray', gray)#display images
cv2.imshow('Orignal Cheque',image)
cv2.imshow(' Cheque',img)
cv2.imshow('Signature',sign)
cv2.imshow('Name',name)
cv2.imshow('Account Number',acc)
cv2.imshow('Amount',amt)

import easyocr
reader = easyocr.Reader(['en'],gpu = False)
r_easy_ocr=reader.readtext(name,detail=0)
print(r_easy_ocr[0])
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
