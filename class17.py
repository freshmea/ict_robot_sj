import cv2 
import numpy as np 

img = np.zeros( (512,512,3), np.uint8) +255

pts1 = np.array([[100, 120],[130, 140],[300, 340],[350, 200],[100, 50]])

while True:
    img = np.zeros( (1024,512,3), np.uint8) +255

    cv2.polylines(img, [pts1], True, (0,0,255))
    cv2.imshow('img', img )
    key = cv2.waitKey(25)
    if key == 27:
        break
cv2.destroyAllWindows()