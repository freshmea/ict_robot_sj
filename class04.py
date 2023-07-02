import cv2 
from matplotlib import pyplot as plt 

img = cv2.imread('data/lena.jpg', cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.show()