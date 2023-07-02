import cv2 
import numpy as np 
theta = 0
img = np.zeros( (512,512,3), np.uint8) +255
while True:
    img = np.zeros( (512,512,3), np.uint8) +255
    cv2.ellipse(img , (256,256), (200, 100), 0, 0, 360, (255,0,0))
    cv2.ellipse(img , (256,256), (200, 100), 45, 0, 360, (0,0,255))
    cv2.ellipse(img , (256,256), (200, 100), 60, theta, theta+10, (0,0,255), thickness=3)
    cv2.imshow('img', img )
    theta += 5
    key = cv2.waitKey(25)
    if key == 27:
        break
cv2.destroyAllWindows()