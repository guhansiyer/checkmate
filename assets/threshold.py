import cv2 as cv
import numpy as np 

path = "/Users/guhaniyer/Documents"


img = cv.imread("/Users/guhaniyer/Documents/Move0.png")
rsz_img = cv.resize(img, None, fx=0.20, fy=0.20)
gray = cv.cvtColor(rsz_img, cv.COLOR_BGR2GRAY)

#Standard Thresholding
#ret, thresh_gray = cv.threshold(gray, 150, 55, cv.THRESH_BINARY+cv.THRESH_OTSU)

#Adaptive Mean Thresholding
#thresh_gray = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, \
           #cv.THRESH_BINARY, 11, 2) 

#Adaptive Gaussian Thresholding 
thresh_gray = cv.adaptiveThreshold(gray, 100, cv.ADAPTIVE_THRESH_GAUSSIAN_C, \
           cv.THRESH_BINARY, 11, 2)


#Otsu's Method
#ret, thresh_gray = cv.threshold(gray, 150, 55, cv.THRESH_BINARY+cv.THRESH_OTSU)

cv.imwrite(f"{path}/Move1.png", thresh_gray)
cv.imshow("Thresholded", thresh_gray)
cv.waitKey(0)

cv.destroyAllWindows()