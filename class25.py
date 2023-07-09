import cv2 
import numpy as np 

img = cv2.imread('data/lena.jpg')

roi = cv2.selectROI('img', img, False, True)

cv2.imshow('img2', img[roi[0]:roi[0]+roi[2], roi[1]: roi[1]+roi[3]] )
cv2.waitKey()
cv2.destroyAllWindows()