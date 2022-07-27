import numpy as np
from PIL import Image
import pyautogui

path = "C:\\Users\\Antonio\\Desktop\\Python Programs\\Chess"

def pickImage(num, folder):
	
	imageName = "Move" + str(num) + ".png"

	img  = Image.open(f"{path}\\{folder}\\{imageName}")
	
	return img

def SubtractImage(num):

	img1 = pickImage(num,  "ChessPNGs2 (Gray Scale)")
	img2 = pickImage(num+1,"ChessPNGs2 (Gray Scale)")
	img = pickImage(num+1, "ChessPNGs2")

	pix = img.load()
	pix1 = img1.load()
	pix2 = img2.load()
	width = img1.width
	height = img1.height

	for x in range(width):

		for y in range(height):

			try:
				RGBValue1 = pix1[x, y]
				RGBValue2 = pix2[x, y]

				newRGBValue = abs(RGBValue1[0] - RGBValue2[0])

				pix[x, y] = (newRGBValue,newRGBValue,newRGBValue)
			except:
				pass

	imageName = "Move" + str(num+1) + ".png"

	img.save(f"{path}\\ChessPNGs2\\{imageName}")

	print("Image Done")

for i in range(37):

	SubtractImage(i)
