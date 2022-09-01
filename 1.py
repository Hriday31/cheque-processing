from types import GeneratorType
import cv2  # computer vision
import numpy as np
from pytesseract import pytesseract  # Tesseract-OCR
from skimage.metrics import structural_similarity as ssim  # SSI
import csv
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

image = cv2.imread('test.png')  # read cheque image
image1 = cv2.imread('sign.jpeg')

# resizing to prevent any mismatch during scanning of cheque
img = cv2.resize(image, (804, 370))

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert image to grayscal
signm1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

sign = img[170:255, 570:804]  # image cropping to extract details
name = img[255:280, 570:800]
acc = img[180:210, 75:300]
amt = img[135:165, 620:775]

# display images
'''cv2.imshow('Orignal Cheque',image)
cv2.imshow('Signature',sign)
cv2.imshow('Name',name)
cv2.imshow('Account Number',acc)
cv2.imshow('Amount',amt)'''


def imgtotext(p):  # extracting text from collected information
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(
        p, lang='eng', config='--psm 6 tessedit_char_whitelist=0123456789')
    return (text[0:-1])


print("Amount:", imgtotext(amt))
print("Account Number:", imgtotext(acc))
print("Payee:", imgtotext(name))


def remove_white_space(image):  # Morpholigal Tranformation
    blur = cv2.GaussianBlur(image, (25, 25), 0)
    thresh = cv2.threshold(
        blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    noise_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening = cv2.morphologyEx(
        thresh, cv2.MORPH_OPEN, noise_kernel, iterations=2)
    close_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    close = cv2.morphologyEx(opening, cv2.MORPH_CLOSE,
                             close_kernel, iterations=3)
    coords = cv2.findNonZero(close)
    x, y, w, h = cv2.boundingRect(coords)
    return image[y:y+h, x:x+w]


sign2 = remove_white_space(signm1)
sign3 = remove_white_space(sign)

cv2.imshow('Recorded signature', sign2)
cv2.imshow('Sign on cheque', sign3)

# Image Matching using structural similarity Index

# unifying dimesions for matching images
cheque_image = cv2.resize(sign3, (100, 100))
original_image = cv2.resize(sign2, (100, 100))

'''cv2.imshow('wrong_image',wrong_image)
cv2.imshow('original_image',original_image)'''

print("Error %-", ssim(cheque_image, original_image)*100)

if ssim(cheque_image, original_image) <= 0.2:
    print("Signatures Matched - Transaction Approved")
else:
    print("Signatures do not Match - Transaction Failed")
f = open('chequeprocessing.csv', 'a', newline='')
a = [imgtotext(amt), imgtotext(acc), imgtotext(name)]
csv.writer(f, delimiter=',').writerow(a)
f.close()

cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image''
