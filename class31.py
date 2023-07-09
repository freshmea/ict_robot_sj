import cv2 
import numpy as np 
src = cv2.imread('data/srcThreshold.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('src', src)

ret, dst = cv2.threshold(src, 150, 255, cv2.THRESH_BINARY)

dst2 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 101, 7)

cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()