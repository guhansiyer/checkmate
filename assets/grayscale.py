from PIL import Image
import config


def pickImage(num):
	
	imageName = "Move" + str(num) + ".png"

	img  = Image.open(f"{config.path}\cutPhotos\\{imageName}")
	
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

	img.save(f"{config.path}\\cutPhotos (grayscaled)\\{imageName}")

	print("Image Done")

			


for i in range(35):

	img = pickImage(i)

	convertIntoGrayscale(img, i)

