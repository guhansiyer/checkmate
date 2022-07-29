import cv2 as cv
import numpy as np 


img = cv.imread()
rsz_img = cv.resize(img, None, fx=0.20, fy=0.20)
gray = cv.cvtColor(rsz_img, cv.COLOR_BGR2GRAY)

cv.imshow("Grayscale", gray)
cv.waitKey(0)

cv.destroyAllWindows()