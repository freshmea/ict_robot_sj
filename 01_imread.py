import cv2 
import numpy as np 

img = cv2.imread('data/lena.jpg')
img2 = cv2.imread('data/lena.jpg',0)

cv2.imshow('img2', img2)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()