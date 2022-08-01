from PIL import Image
import config

def pickImage(num, folder):
	
	imageName = "Move" + str(num) + ".png"

	img  = Image.open(f"{config.path}\\{folder}\\{imageName}")
	
	return img

def SubtractImage(num):

	img1 = pickImage(num,  "cutPhotos (grayscaled)")
	img2 = pickImage(num+1,"cutPhotos (grayscaled)")
	img  = pickImage(num+1, "cutPhotos (grayscaled)")

	pix = img.load()
	pix1 = img1.load()
	pix2 = img2.load()
	width = img1.width
	height = img1.height

	for x in range(width):

		for y in range(height):

		
			RGBValue1 = pix1[x, y]
			RGBValue2 = pix2[x, y]

			newRGBValue = int(abs(RGBValue1 - RGBValue2))

			pix[x, y] = newRGBValue
			
			

	imageName = "Move" + str(num+1) + ".png"

	img.save(f"{config.path}\\cutPhotos (subtracted)\\{imageName}")

	print("Image Done")

for i in range(36):

	SubtractImage(i)
