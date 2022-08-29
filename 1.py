import cv2
import numpy as np
 
image = cv2.imread('/home/hra/Downloads/test.png')
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_sharp = cv2.filter2D(src=gray, ddepth=-1, kernel=kernel)
cv2.imshow('gray', gray)
img=gray
sign=img[170:255,570:844] 
name=img[255:280,570:844]
acc=img[180:210,75:300]
amt=img[135:165,615:775] 
cv2.imshow('Orignal Cheque',image)
cv2.imshow(' Cheque',img)
cv2.imshow('Signature',sign)
cv2.imshow('Name',name)
cv2.imshow('Account Number',acc)
cv2.imshow('Amount',amt)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image