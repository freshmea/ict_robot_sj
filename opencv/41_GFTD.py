import cv2 
import numpy as np 

src = cv2.imread('data/chessBoard.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

goodF = cv2.GFTTDetector_create(40, 0.1, 10, useHarrisDetector=True)

kp = goodF.detect(gray)
points = cv2.KeyPoint_convert(kp)
print(points)
print(len(points))

dst = cv2.drawKeypoints(src, kp, None, (0,255,0))

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()