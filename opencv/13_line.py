import cv2 
import numpy as np 
x = 0
img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
while True:
    img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
    cv2.line(img, (x, 0),(300, 300), (255, 0, 0), 3)
    cv2.imshow('img', img )
    key = cv2.waitKey(25)
    if key == 27:
        break
    x += 1
cv2.destroyAllWindows()
