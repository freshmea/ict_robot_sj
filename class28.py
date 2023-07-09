import cv2 
import numpy as np 

img = cv2.imread('data/lena.jpg')

dst = cv2.resize(img, (img.shape[0]//2, img.shape[1]//2))
# M1 = np.array([[0, 0],[10, 10],[0, 10]], dtype=np.float32)
# M2 = np.array([[0, 0],[0, 14.414],[5, 5]], dtype=np.float32)

# M = cv2.getAffineTransform(M1, M2)
# print(type(M), M)
# M[0,2] += 100
# M[1,2] += 200
M = cv2.getRotationMatrix2D((img.shape[0]//2, img.shape[1]//2), 45, 1)
print(M)
dst2 = cv2.warpAffine(img, M, (img.shape[0], img.shape[1]))
cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()