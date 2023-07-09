import cv2 
import numpy as np 

cap = cv2.VideoCapture('data/sample.mp4')
cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, dsize=None, fx= 0.7, fy=0.7)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5, minSize=(20, 20))
    for box in result:
        cv2.rectangle(frame, box, (255,0,0), 2)    
    cv2.imshow('f', frame)
    key = cv2.waitKey(20)
    if key ==27:
        break
