import cv2 
import numpy as np 

def onChange(pos):
    r = cv2.getTrackbarPos('R', 'img')
    b = cv2.getTrackbarPos('B', 'img')
    g = cv2.getTrackbarPos('G', 'img')
    img[:] =(b,g,r)
    cv2.imshow('img', img)

img = np.zeros((512,512,3), np.uint8) + 255
cv2.imshow('img', img)
cv2.createTrackbar('R', 'img', 0, 255, onChange)
cv2.createTrackbar('G', 'img', 0, 255, onChange)
cv2.createTrackbar('B', 'img', 0, 255, onChange)

cv2.waitKey()
cv2.destroyAllWindows()