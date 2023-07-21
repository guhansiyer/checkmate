import cv2 as cv
import config

# new basis

def Edge(num):
    # Read the original image
    img = cv.imread(f'{config.path}\\PNGs\\cutPhotos\\Move' + str(num) + '.png') 

    # Convert to graycsale
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv.GaussianBlur(img, (3,3), 0) 

    # Canny Edge Detection
    edges = cv.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection

    cv.imwrite(f"{config.path}\\PNGs\\cutPhotos\\Move" + str(num) + ".png", edges)

