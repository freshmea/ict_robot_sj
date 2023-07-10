import cv2 
from matplotlib import pyplot as plt 
import matplotlib.animation as animation

class Video:
    def __init__(self, device=0):
        self.cap = cv2.VideoCapture(device)
        self.ret, self.frame = self.cap.read()
        self.im = plt.imshow(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))

    def updateFrame(self, k):
        self.ret, self.frame = self.cap.read()
        self.im.set_array(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))

    def close(self):
        if self.cap.isOpened():
            self.cap.release()

def main():
    fig = plt.figure(figsize = (10, 6))
    plt.axis('off')
    fig.canvas.manager.set_window_title('Video Capture')

    camera = Video('data/vtest.avi')
    ani = animation.FuncAnimation(fig, camera.updateFrame, interval = 50)
    plt.show()
    camera.close()

if __name__ == '__main__':
    main()
