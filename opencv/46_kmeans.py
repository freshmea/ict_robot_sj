import cv2 
import numpy as np 

src = cv2.imread('data/hand.jpg')
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

data = src.reshape(-1,3).astype(np.float32)
criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret, lables, centers = cv2.kmeans(data, 2, None,criteria, 5, cv2.KMEANS_RANDOM_CENTERS )

centers =np.uint8(centers)
res = centers[lables.flatten()]
dst = res.reshape(src.shape)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
