import config
import cv2 as cv 
import numpy as np 

def crop(num):
    img_rgb = cv.imread(f"C:\\Users\\guhan\\Desktop\\chess\\realChessPNGs (coloured)\\Move" + str(num) + ".png")
    
    # Convert it to grayscale
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    
    # Read the template
    template = cv.imread('template', 0)
    
    # Store width and height of template in w and h
    w, h = template.shape[::-1]
    

    resize = imutils.resize(img_gray, width=int(shape[0]), height=int(img_gray.shape[1]*scale))
    

    if resized.shape[0] < h or resized.shape[1] < w:
            break
    found=(maxVal, maxLoc, r)
    

    (__, maxLoc, r)=found
    (startX, startY)=(int(maxLoc[0]*r), int maxLoc[1]*r)
    (endX, endY)=(int((maxLoc[0]+tw)*r), int(maxLoc[1]+tH)*r)
    
    cv2.rectangle(img_rgb, (startX, startY), (endX, endY), (0, 0, 255), 2)
    cv2.imshow("Image", img_rgb)
    cv2.waitKey(0)