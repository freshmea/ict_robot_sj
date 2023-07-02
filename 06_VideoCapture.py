import cv2, sys 

cap = cv2.VideoCapture('data/record123.avi')

while True:
    ret, frame = cap.read()

    if not ret:
        break
    cv2.imshow('frame', frame)

    key =cv2.waitKey(25)
    if key == 27:
        break

if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
