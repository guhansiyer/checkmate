import cv2

path = "/Users/guhaniyer/Documents"


# Read the original image
img = cv2.imread(f'{path}/Move1.png') 
# Display original image

# Convert to graycsale
#img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img, (3,3), 0) 

# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection

cv2.imwrite(f"{path}/Move2.png", edges)

print("Image done.")