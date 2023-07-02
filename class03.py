import cv2 
from matplotlib import pyplot as plt 

imgBGR = cv2.imread('data/lena.jpg')
imgRBG = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
print(type(imgBGR))
print(type(imgRBG))
plt.axis('off')
plt.imshow(imgRBG)
plt.show()