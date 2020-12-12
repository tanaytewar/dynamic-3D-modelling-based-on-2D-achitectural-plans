import cv2
import numpy as np
filename='result-final.jpg'
img=img = cv2.imread(filename)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)

res = cv2.bitwise_and(img,img, mask= mask)

cv2.imshow('image',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.imwrite('result.png',res)    
cv2.waitkey()
cv2.destroyAllWindows()
