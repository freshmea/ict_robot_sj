import cv2 
import numpy as np 

img = np.zeros( (512,512,3), np.uint8) +255
text = 'Moving Text'
x = 100
y = 100
while True:
    img = np.zeros( (1024,512,3), np.uint8) +255
    cv2.putText(img, text, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
    cv2.imshow('img', img )
    
    key = cv2.waitKeyEx(30)
    print(key)
    if key == 97: # left
        x -= 10
    elif key == 119: # up
        y -= 10
    elif key == 100: # right 
        x += 10
    elif key == 115: # down
        y += 10
    elif key == 27:
        break
    
cv2.destroyAllWindows()