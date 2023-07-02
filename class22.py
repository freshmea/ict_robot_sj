import cv2 
import numpy as np 

img = cv2.imread('data/lena.jpg')

print(img.ndim)
print(img.shape)
print(img.dtype)

img = img.astype(np.int32)

print(img.dtype)
# img = img.astype(np.uint8)
img = np.uint8(img)

img= img.flatten()
print(img.shape)
img = img.reshape((-1,512,3))
print(img.shape)

roi = cv2.selectROI(img)
# # ROI 복사, 참조.
# a = img[100:200,100:200,:].copy()
# a[::] =100
# cv2.imshow('a', a)
print(type(roi))
cv2.imshow('roi', roi)
cv2.imshow('img', img )
cv2.waitKey()
cv2.destroyAllWindows()