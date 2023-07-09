import cv2 

img = cv2.imread('data/lena.jpg')
cv2.imshow('img', img)
cv2.imwrite('output/lena.bmp', img)
cv2.imwrite('output/lena.png', img)
cv2.imwrite('output/lena.png', img, [cv2.IMWRITE_PNG_COMPRESSION,9])
cv2.imwrite('output/lena.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 9])
cv2.imwrite('output/lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])
cv2.waitKey()
cv2.destroyAllWindows()