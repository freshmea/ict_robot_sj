import cv2 
import numpy as np 

src = np.zeros((512,512,3), np.uint8)
cv2.rectangle(src, (50, 100, 400, 300), (255,255,255), -1)
cv2.rectangle(src, (100, 150, 300, 200), (0,0,0), -1)
cv2.rectangle(src, (200, 200, 100, 100), (255,255,255), -1)

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(src, contours, -1, (0,0,255), 3)

cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()