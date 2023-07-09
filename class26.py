import cv2 
import numpy as np 

img = cv2.imread('data/lena.jpg')

roi = img[100:110,200:210].copy()
roi[:,:] = [0, 0, 255]

cv2.imshow('img', img)
cv2.imshow('roi', roi)
cv2.waitKey()
cv2.destroyAllWindows()
