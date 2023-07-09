import cv2, sys 

cap = cv2.VideoCapture('data/vtest.avi')

frame_size = ( int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) )
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # ('M', 'P', 'E', 'G')

out1 = cv2.VideoWriter('output/record1234.mp4', fourcc, 20.0, frame_size)

# if cap:
#     sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break
    cv2.imshow('frame', frame)
    out1.write(frame)
    key =cv2.waitKey(25)
    if key == 27:
        break
out1.release()
if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
