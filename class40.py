import cv2 
import numpy as np 

src = cv2.imread('data/chessBoard.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

fastF = cv2.FastFeatureDetector.create(threshold=80)

kp = fastF.detect(gray)
dst = cv2.drawKeypoints(src, kp, None, (255,0,0))

cv2.imshow('a', src)
cv2.imshow('b', dst)

cv2.waitKey()
cv2.destroyAllWindows()