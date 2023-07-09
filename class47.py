import cv2 
import numpy as np 

cap = cv2.VideoCapture('data/vtest.avi')
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

acc_bgr = np.zeros((height, width, 3), dtype=np.float32)

t = 0 
while True:
    ret, frame = cap.read()
    t += 1
    cv2.accumulate(frame, acc_bgr)
    avr_bgr = acc_bgr/t
    dst_bgr = cv2.convertScaleAbs(avr_bgr)
    
    cv2.imshow('frame', frame)
    cv2.imshow('acc', dst_bgr)
    key = cv2.waitKey(20)
    if key == 27:
        break
cap.close()
cv2.destroyAllWindows()