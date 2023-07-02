import cv2, sys 

cap = cv2.VideoCapture('data/record1234.mp4')

if not cap:
    sys.exit()
a = 0
while True:
    ret, frame = cap.read()
    a += 1
    print(a)
    # if not ret:
    #     break
    try:
        cv2.imshow('frame', frame)
    except:
        pass
    key =cv2.waitKey(25)
    if key == 27:
        break

if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
