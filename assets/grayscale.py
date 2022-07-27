import numpy as np
from PIL import Image
import pyautogui

path = "C:\\Users\\Antonio\\Desktop\\Python Programs\\Chess"


def pickImage(num):
	
	imageName = "Move" + str(num) + ".png"

	img  = Image.open(f"{path}\\ChessPNGs2 (Coloured)\\{imageName}")
	
	return img

def convertIntoGrayscale(img, num):

	pix = img.load()
	width = img.width
	height = img.height


	for x in range(width):

		for y in range(height):

			RGBValue = pix[x, y]

			newRGBValue = int(RGBValue[0]*0.2989 + RGBValue[1]*0.5870 + RGBValue[2]*0.1140)

			pix[x,y] = (newRGBValue, newRGBValue, newRGBValue)

	imageName = "Move" + str(num) + ".png"

	img.save(f"{path}\\ChessPNGs2 (Gray Scale)\\{imageName}")

	print("Image Done")

			


for i in range(6):

	img = pickImage(i+1)

	convertIntoGrayscale(img, i+1)

