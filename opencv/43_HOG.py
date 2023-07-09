import cv2 
import numpy as np 

src = cv2.imread('data/people.png')
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

loc1, weights1 = hog.detectMultiScale(src)
print(len(loc1))
dst1 = src.copy()
w, h =hog.winSize
for rectangle in loc1:
    cv2.rectangle(dst1, rectangle, (255,0,0), 2)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.waitKey()
cv2.destroyAllWindows()