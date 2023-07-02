import cv2 
import numpy as np 

# img = np.zeros( (512,512,3), np.uint8) +255
img = cv2.imread('data/lena.jpg')
text = 'OpenCV Programming'
while True:
    # img = np.zeros( (1024,512,3), np.uint8) +255

    cv2.putText(img, text, (100,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 2)
    size, baseline=cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
    cv2.rectangle(img, (100,100), (100+size[0],100-size[1]), (0,0,255), 1)

    cv2.imshow('img', img )
    key = cv2.waitKey(25)
    if key == 27:
        break
cv2.destroyAllWindows()