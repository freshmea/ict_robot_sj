import cv2
import numpy as np 

# def findlocalMaxium(src):
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, ksize= (11,11))
#     dilate = cv2.dilate(src, kernel)
#     localMax = (src == dilate)
    
#     erode = cv2.erode(src, kernel)
#     localMax2 = src > erode
    
#     localMax &= localMax2
#     points = np.argwhere(localMax == True)
#     points[:,[0,1]] = points[:,[1,0]]
#     return points
    
src = cv2.imread('data/CornerTest.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

res = cv2.cornerHarris(gray, 5, 3, 0.01)
ret, res = cv2.threshold(np.abs(res), 0.02, 0, cv2.THRESH_TOZERO)
res8 = cv2.normalize(res, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8S)

# corners = findlocalMaxium(res8)
print(corners)

cv2.imshow('src', src)
cv2.imshow('res', res)
cv2.waitKey()
cv2.destroyAllWindows()