import cv2 
import numpy as np 

src = cv2.imread('data/CornerTest.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

K = 5
corners1 = cv2.goodFeaturesToTrack(gray, K, 0.05, 10, useHarrisDetector=True)
corners2 = cv2.goodFeaturesToTrack(gray, K, 0.05, 10)

corners1 = corners1.reshape(-1, 2)
corners2 = corners2.reshape(-1, 2)

for corner in corners1:
    x, y = corner
    cv2.circle(src, (int(x), int(y)), 5, (0,0,255), -1)
    
for corner in corners2:
    x, y = corner
    cv2.circle(src, (int(x), int(y)), 5, (255,0,), 1)
    
cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()