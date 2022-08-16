import config
import cv2 as cv 
import numpy as np 

def crop(num):
    image = cv.imread(f"C:\\Users\\guhan\\Desktop\\chess\\realChessPNGs (coloured)\\Move" + str(num) + ".png")
    
  