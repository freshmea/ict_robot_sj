import cv2 
import numpy as np 
from matplotlib import pyplot as plt 

src = cv2.imread('data/lena.jpg')
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

hist1 = cv2.calcHist(v, [0], None, [256], [0,255])
plt.plot(hist1, color='b')

v = cv2.equalizeHist(v)

hist2 = cv2.calcHist(v, [0], None, [256], [0,255])
plt.plot(hist2, color='r')

hsv = cv2.merge([h, s, v])
src1 = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

cv2.imshow('a', src)
cv2.imshow('b', src1)

# plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
