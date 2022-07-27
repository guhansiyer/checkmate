import cv2

path = "C:\\Users\\guhan\\Desktop\\chess"

for i in range(36):
    # Read the original image
    img = cv2.imread(f'{path}\\realChessPNGs (coloured)\\Move{i}.png') 
    # Display original image

    # Convert to graycsale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

    # Canny Edge Detection
    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
    # Display Canny Edge Detection Image

    cv2.imwrite(f"{path}\\realChessPNGs (grayscaled)\\Move{i}.png", edges)

    print("image done")