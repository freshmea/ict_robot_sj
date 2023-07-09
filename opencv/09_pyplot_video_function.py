import cv2 
from matplotlib import pyplot as plt 
import matplotlib.animation as animation

cap = cv2.VideoCapture('data/vtest.avi')

fig = plt.figure(figsize = (10, 6))
plt.axis('off')
fig.canvas.manager.set_window_title('Video Capture')

def init():
    global im
    ret, frame = cap.read()
    im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

def updateFrame(k):
    ret, frame = cap.read()
    im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

ani = animation.FuncAnimation(fig, updateFrame, init_func=init, interval = 50)
plt.show()

if cap.isOpened():
    cap.release()