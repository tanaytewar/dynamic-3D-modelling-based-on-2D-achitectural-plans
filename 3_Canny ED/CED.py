import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Cat1_1_res.jpg',0)
edges = cv2.Canny(img,100,200)

#plt.subplot(121),plt.imshow(img,cmap = 'gray')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(edges,cmap = 'gray')
#plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

#plt.show()
cv2.imshow('Input',img)
cv2.imshow('Canny',edges)
cv2.imwrite('Cat1_1_morph.jpg',edges)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
