import cv2 

src1 = cv2.imread('data/hand.jpg')
hsv = cv2.cvtColor(src1, cv2.COLOR_BGR2HSV)

lower = (0, 40, 0)
upper = (20, 180, 255)
dst1 = cv2.inRange(hsv, lower, upper)
print(type(dst1), dst1.shape, dst1.dtype)
cv2.imshow('a', src1)
cv2.imshow('inRange', dst1)
cv2.waitKey()
cv2.destroyAllWindows()