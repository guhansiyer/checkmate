import cv2 as cv
import numpy as np 
import config

img = cv.imread("C:\\Users\\guhan\\Desktop\\checkmate\\newChessPNGs\\realChessPNGs (coloured)\\Move2.png")
rsz_img = cv.resize(img, None, fx=0.20, fy=0.20)
mask = np.zeros(rsz_img.shape[:2], dtype = "uint8")
mask = cv.rectangle(mask, (115,225), (500, 600), (255,255,255), -1)

result = cv.bitwise_and(rsz_img, rsz_img, mask = mask)
#Standard Thresholding
#ret, thresh_gray = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)

#Inverted Thresholding
#ret, thresh_gray = cv.threshold(gray, 150, 55, cv.THRESH_BINARY_INV)

#Otsu's Method
#ret, thresh_gray = cv.threshold(gray, 150, 55, cv.THRESH_BINARY+cv.THRESH_OTSU)

#Adaptive Mean Thresholding
#thresh_gray = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, \
           #cv.THRESH_BINARY, 11, 2) 

#Adaptive Gaussian Thresholding 
#thresh_gray = cv.adaptiveThreshold(gray, 220, cv.ADAPTIVE_THRESH_GAUSSIAN_C, \
           #cv.THRESH_BINARY, 11, 2)

print(rsz_img.shape)
cv.imshow("Masked", result)
cv.waitKey(0)

cv.destroyAllWindows()