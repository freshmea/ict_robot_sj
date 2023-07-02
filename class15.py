import cv2 
import numpy as np 

img = np.zeros( (512,512,3), np.uint8) +255
box = (100, 100, 400, 400)
cv2.rectangle(img, box, (0,0,255), 3)

ret, rpt1, rpt2 = cv2.clipLine(box, (15,12), (450,530))
cv2.line(img, (15,12), (450,530), (0,0,255), 2)
print(ret, rpt1, rpt2)
if ret:
    cv2.circle(img, rpt1, radius=5, color=(0,255,0), thickness=-1)
    cv2.circle(img, rpt2, radius=5, color=(0,255,0), thickness=-1)
cv2.imshow('img', img )
key = cv2.waitKey()
cv2.destroyAllWindows()