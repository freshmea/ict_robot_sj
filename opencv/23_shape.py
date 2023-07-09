import cv2 
import numpy as np 

img = cv2.imread('data/lena.jpg')
img2 = cv2.imread('data/lena.jpg', cv2.IMREAD_GRAYSCALE)

print(img.shape)
print(img2.shape)
print(img)
img = img.flatten()
print(img.shape)
img = img.reshape(-1,1024,3)
print(img.shape)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()