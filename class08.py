import cv2 
from matplotlib import pyplot as plt 

def handle_key_press(event):
    if event.key == 'escape':
        cap.release()
        plt.close()
        
def handle_close(event):
    print('Close figure!')
    cap.release()


cap = cv2.VideoCapture('data/vtest.avi')

plt.ion()
fig = plt.figure(figsize = (10, 6))
plt.axis('off')

fig.canvas.manager.set_window_title('Video Capture')
fig.canvas.mpl_connect('key_press_event', handle_key_press)
fig.canvas.mpl_connect('close_evnet', handle_close)

ret, frame = cap.read()
im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    fig.canvas.draw()
    fig.canvas.flush_events()

if cap.isOpened():
    cap.release()