import cv2 
import numpy as np 

src = cv2.imread('data/rect.jpg')
edge = cv2.Canny(src, 50, 100)
# lines = cv2.HoughLines(edge, 1, np.pi/180, 100)
# for line in lines:
#     rho, theta = line[0]
#     c = np.cos(theta)
#     s = np.sin(theta)
#     x0 = c * rho
#     y0 = s * rho
#     x1 = int(x0 + 1000*(-s))
#     y1 = int(y0 + 1000*(c))
#     x2 = int(x0 - 1000*(-s))
#     y2 = int(y0 - 1000*(c))
#     cv2.line(src, (x1,y1), (x2,y2), (0,0,255), 2)
lines = cv2.HoughLinesP(edge,1, np.pi/180, 100)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(src, (x1, y1), (x2, y2), (255,0,0), 2)

cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()