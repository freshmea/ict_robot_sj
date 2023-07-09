import cv2 
import numpy as np 

src = cv2.imread('data/lena.jpg', cv2.IMREAD_GRAYSCALE)

src = cv2.GaussianBlur(src,(7,7), 0.0)
lap = cv2.Laplacian(src, ddepth=cv2.CV_32F)
dst = cv2.convertScaleAbs(lap)
dst = cv2.normalize(dst, None, 0, 255, cv2.NORM_MINMAX)

cv2.imshow('dst', dst)
# cv2.imshow('dstY', dstY)
# cv2.imshow('mag', mag)
cv2.waitKey()
cv2.destroyAllWindows()
