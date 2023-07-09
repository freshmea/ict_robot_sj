import cv2 
img = cv2.imread('data/lena.jpg')

print(img[100,200])
print(img[100:110,200:210])
img[100,200] = [0, 0, 0]
img[100:110,200:210, 0] = [0]
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()