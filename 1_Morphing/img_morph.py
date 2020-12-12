import cv2
import numpy as np
img = cv2.imread('Cat21_7.jpg',0)
kernel = np.ones((3,3), np.uint8)
img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=2)
img_final = cv2.erode(img_dilation,kernel,iterations=1)
cv2.imwrite('Cat21_7_res.jpg',img_dilation)

cv2.imshow('Input',img)
#cv2.imshow('Erosion',img_erosion)
cv2.imshow('Dilation',img_dilation)
#cv2.imshow('Final',img_final)

cv2.waitKey(0)
