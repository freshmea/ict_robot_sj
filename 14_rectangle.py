import cv2 
import numpy as np 

img = np.zeros( (512,512,3), np.uint8) +255

cv2.rectangle(img, (100, 100, 200, 200), (0,0,255), 3)

# rectangle overloading
cv2.rectangle(img, (100, 100), (200, 200), (0,255,0), 3)

cv2.imshow('img', img )
key = cv2.waitKey()
cv2.destroyAllWindows()