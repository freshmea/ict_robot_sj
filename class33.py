import cv2 
import numpy as np 

src = cv2.imread('data/lena.jpg')

dst1 = cv2.boxFilter(src, ddepth= -1, ksize=(30,30))
dst2 = cv2.bilateralFilter(src, d= -1, sigmaColor=200, sigmaSpace=10)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
