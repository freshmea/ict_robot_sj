import cv2 
import numpy as np 

img = cv2.imread('data/lena.jpg')

b, g, r = cv2.split(img)
zero = np.zeros_like(b)
print(b.shape, zero.shape, img.shape)
original = cv2.merge([b,g,r])
blue_image = cv2.merge([b, zero, zero ])
cv2.imshow('imgb', blue_image)
cv2.imshow('imgg', g)
cv2.imshow('imgr', r)
cv2.waitKey()
cv2.destroyAllWindows()