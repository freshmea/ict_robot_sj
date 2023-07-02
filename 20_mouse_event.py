import cv2 
import numpy as np 

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(param[0], (x,y), 5, (255,0,0), -1)
        if flags & cv2.EVENT_FLAG_CTRLKEY:
            cv2.circle(param[0], (x,y), 20, (0,255,0), -1)
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(param[0], (x,y),(x+5,y+5), (0,0,255), -1)
    cv2.imshow('img', param[0])

def main():
    img = np.zeros((512,512,3), np.uint8)+255
    cv2.imshow('img', img)
    cv2.setMouseCallback('img', onMouse, [img])
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
