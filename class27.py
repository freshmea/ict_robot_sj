import cv2 
import numpy as np 

img = cv2.imread('data/lena.jpg')
print(img.shape)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray.shape)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(hsv.shape)
yCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
print(yCrCb.shape)

cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.imshow('hsv', hsv)
cv2.imshow('yCrCb', yCrCb)

cv2.waitKey()
cv2.destroyAllWindows()