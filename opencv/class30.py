import cv2 
import numpy as np 

src1 = cv2.imread('data/lena.jpg')
src2 = cv2.imread('data/opencv_logo.png')

rows, cols, channels =  src2.shape
roi = src1[:rows,:cols]


print(cv2.bitwise_or(np.array([1]), np.array([1])))
print(cv2.bitwise_or(np.array([1]), np.array([2])))
print(cv2.bitwise_or(np.array([0]), np.array([1])))
print(cv2.bitwise_or(np.array([1]), np.array([0])))

print(cv2.bitwise_and(np.array([1]), np.array([1])))
print(cv2.bitwise_and(np.array([0]), np.array([1])))
print(cv2.bitwise_and(np.array([1]), np.array([0])))
print(cv2.bitwise_and(np.array([1]), np.array([2])))

gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

src1_bg = cv2.bitwise_and(roi, roi, mask= mask)
src2_fg = cv2.bitwise_and(src2, src2, mask= mask_inv)
dst = cv2.bitwise_or(src1_bg, src2_fg)
roi[:,:] = dst
# src1[:rows,:cols] = dst
cv2.imshow('a', src1_bg)
cv2.imshow('b', src2_fg)
cv2.imshow('c', roi)
cv2.imshow('d', src1)
cv2.waitKey()
cv2.destroyAllWindows()


