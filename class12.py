import cv2
from matplotlib import pyplot as plt
import matplotlib.animation as animation

class Video(animation.FuncAnimation):
    def __init__(self, device=0):
        self.fig, self.ax= plt.subplots(1, 2, figsize = (10, 5))
        self.ax[0].set_position([0, 0, 0.5, 1])
        self.ax[1].set_position([0.5, 0, 0.5, 1])
        self.ax[0].axis('off')
        self.ax[1].axis('off')
        self.fig.canvas.manager.set_window_title('Video Capture')
        self.cap = cv2.VideoCapture(device)
        super(Video, self).__init__(self.fig, self.updateFrame, init_func=self.init, interval = 50)

    def init(self):
        self.ret, self.frame = self.cap.read()
        self.im0 = self.ax[0].imshow(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB), aspect = 'auto')
        self.im1 = self.ax[1].imshow(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB), aspect = 'auto')

    def updateFrame(self, k):
        self.ret, self.frame = self.cap.read()
        if self.ret:
            self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            self.im0.set_array(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))
            self.im1.set_array(cv2.merge([self.gray,self.gray,self.gray]))

    def close(self):
        if self.cap.isOpened():
            self.cap.release()

def main():
    camera = Video('data/vtest.avi')
    plt.show()
    camera.close()

if __name__ == '__main__':
    main()
