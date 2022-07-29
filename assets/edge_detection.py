import cv2
import config
import numpy as np

# Read the original image
img = cv2.imread(f'{config.path}\\Move0.png') 
rsz_img = cv2.resize(img, None, fx=0.20, fy=0.20)
# Display original image

# Convert to graycsale
#img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(rsz_img, (3,3), 0) 

# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection

## find the non-zero min-max coords of canny
pts = np.argwhere(edges>0)
y1,x1 = pts.min(axis=0)
y2,x2 = pts.max(axis=0)

## crop the region
cropped = rsz_img[y1:y2, x1:x2]

tagged = cv2.rectangle(rsz_img.copy(), (x1,y1), (x2,y2), (0,255,0), 3, cv2.LINE_AA)

cv2.imshow("Canny", tagged)
cv2.waitKey(0)
#cv2.imwrite(f"{config.path}\\Move4.png", edges)

print("Image done.")

cv2.destroyAllWindows()