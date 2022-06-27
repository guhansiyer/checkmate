# import cv2 as cv
import numpy as np
from PIL import Image
import pyautogui
from time import sleep


# print("Hello Python")

# print(f"OpenCV {cv.__version__}")

# print(f"Numpy {np.__version__}")


#path = "C:\\Users\\Antonio\\Desktop\\Python Programs\\Chess"
path = "C:\\Users\\guhan\Desktop\\chess"


def differenceFinder(oldSquares, newSquares):

	missingPiece = []
	unknownPiece = None

	for i in range(64):
		

		squareOld = oldSquares[i]
		squareNew = newSquares[i]


		if squareOld[2] == squareNew[2]:

			squareNew[1] = squareOld[1]

		else:

			if squareNew[2] == "Blank":
				
				squareNew[1] = "None"
				missingPiece.append(squareOld[1])

			elif  (squareOld[2] == "White" and squareNew[2] == "Black") or (squareOld[2] == "Black" and squareNew[2] == "White"):

				missingPiece.append(squareOld[1])
				unknownPiece = i

			else:

				unknownPiece = i

	if unknownPiece != None:

		changedSquare = newSquares[unknownPiece]

		if len(missingPiece) == 1:

			# pice movement message return
			move = f"{missingPiece[0]}{changedSquare[0]}"
			changedSquare[1] = missingPiece[0]

		else:

			missingPiece1 = missingPiece[0]
			missingPiece2 = missingPiece[1]

			if changedSquare[2] == missingPiece1:
				# piece killed another piece return
				changedSquare[1] = missingPiece1
				move = f"{missingPiece1} to {changedSquare[0]} and {missingPiece2} was taken out of the game"

			else:
				# piece killed another piece return
				changedSquare[1] = missingPiece2
				move = f"{missingPiece2} to {changedSquare[0]} and {missingPiece1} was taken out of the game"


		newSquares[unknownPiece] = changedSquare

		values = [newSquares, move]

	else:
		values = [newSquares]

	return values

def getHex (x):
	
	hexNum = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
	xHex = ""
	
	while x >= 1:
	
		rem = int(x%16)
		xHex = hexNum[rem] + xHex
		x = int(x/16)

	if xHex == "":

		xHex = "0"

	if len(xHex) == 1:
	
		xHex = "0" + xHex

	
	return xHex


def getColour(r, g, b):

	rHex = getHex(r)
	gHex = getHex(g)
	bHex = getHex(b)

	colourHex = "#" + rHex + gHex + bHex

	return colourHex

def pickImage(num):
	
	imageName = "Move" + str(num) + ".png"

	img  = Image.open(f"{path}\\ChessPNGs\\{imageName}")
	
	return img


def getColours(img):

	sqr = startPositions()
	height = img.height
	width = img.width

	xStep = int(width/8)
	yStep = int(height/8)

	y = height
	x = 0
	
	colour = "Blank"

	sqrNum = 0
	pix = img.load()

	for h in range(8):

		for g in range(8):


			# get all the colours of the square
			colour = "Blank"
			y = height - yStep*h - 1
			square = sqr[sqrNum]

			for f in range(yStep-1):

				x = 0 + xStep*g + 1

				for i in range(xStep-1):			

					RGBValue = pix[x,y]

					hexValue = getColour(RGBValue[0], RGBValue[1], RGBValue[2])

					if hexValue == "#565352":

						colour = "Black"

					elif hexValue == "#F8F8F8" :

						colour = "White"

					else:
						pass


					x = x + 1

				y = y - 1

			square[2] = colour
			square[1] = "None"

			sqr[sqrNum] = square
			sqrNum = sqrNum + 1

	return sqr

def takeScreenshot(num):

	imageName = "Move" + str(num) + ".png"

	myScreenshot = pyautogui.screenshot()
	myScreenshot.save(f"{path}\\ChessPNGs\\{imageName}")

def startPositions():
	# setting up the original positions

	# 1st Row
	square1 = ["a1", "R", "White"]
	square2 = ["b1", "N", "White"]
	square3 = ["c1", "B", "White"]
	square4 = ["d1", "Q", "White"]
	square5 = ["e1", "K", "White"]
	square6 = ["f1", "B", "White"]
	square7 = ["g1", "N", "White"]
	square8 = ["h1", "R", "White"]

	# 2nd Row
	square9  = ["a2", "", "White"]
	square10 = ["b2", "", "White"]
	square11 = ["c2", "", "White"]
	square12 = ["d2", "", "White"]
	square13 = ["e2", "", "White"]
	square14 = ["f2", "", "White"]
	square15 = ["g2", "", "White"]
	square16 = ["h2", "", "White"]

	# 3rd Row
	square17 = ["a3", "None", "Blank"]
	square18 = ["b3", "None", "Blank"]
	square19 = ["c3", "None", "Blank"]
	square20 = ["d3", "None", "Blank"]
	square21 = ["e3", "None", "Blank"]
	square22 = ["f3", "None", "Blank"]
	square23 = ["g3", "None", "Blank"]
	square24 = ["h3", "None", "Blank"]

	# 4th Row
	square25 = ["a4", "None", "Blank"]
	square26 = ["b4", "None", "Blank"]
	square27 = ["c4", "None", "Blank"]
	square28 = ["d4", "None", "Blank"]
	square29 = ["e4", "None", "Blank"]
	square30 = ["f4", "None", "Blank"]
	square31 = ["g4", "None", "Blank"]
	square32 = ["h4", "None", "Blank"]


	# 5th Row
	square33 = ["a5", "None", "Blank"]
	square34 = ["b5", "None", "Blank"]
	square35 = ["c5", "None", "Blank"]
	square36 = ["d5", "None", "Blank"]
	square37 = ["e5", "None", "Blank"]
	square38 = ["f5", "None", "Blank"]
	square39 = ["g5", "None", "Blank"]
	square40 = ["h5", "None", "Blank"]

	# 6th Row
	square41 = ["a6", "None", "Blank"]
	square42 = ["b6", "None", "Blank"]
	square43 = ["c6", "None", "Blank"]
	square44 = ["d6", "None", "Blank"]
	square45 = ["e6", "None", "Blank"]
	square46 = ["f6", "None", "Blank"]
	square47 = ["g6", "None", "Blank"]
	square48 = ["h6", "None", "Blank"] 

	# 7th Row
	square49 = ["a7", "", "Black"]
	square50 = ["b7", "", "Black"]
	square51 = ["c7", "", "Black"]
	square52 = ["d7", "", "Black"]
	square53 = ["e7", "", "Black"]
	square54 = ["f7", "", "Black"]
	square55 = ["g7", "", "Black"]
	square56 = ["h7", "", "Black"]

	# 8th Row
	square57 = ["a8", "R", "Black"]
	square58 = ["b8", "N", "Black"]
	square59 = ["c8", "B", "Black"]
	square60 = ["d8", "Q", "Black"]
	square61 = ["e8", "K", "Black"]
	square62 = ["f8", "B", "Black"]
	square63 = ["g8", "N", "Black"]
	square64 = ["h8", "R", "Black"]

	squares = [square1, square2, square3, square4, square5, square6, square7, square8, square9, square10, square11, square12, square13, square14, square15, square16, square17, square18, square19, square20, square21, square22, square23, square24, square25, square26, square27, square28, square29, square30, square31, square32, square33, square34, square35, square36, square37, square38, square39, square40, square41, square42, square43, square44, square45, square46, square47, square48, square49, square50, square51, square52, square53, square54, square55, square56, square57, square58, square59, square60, square61, square62, square63, square64]

	return squares


squaresOld = startPositions()

# sleep(5000)

moves = []

for x in range(7):

	# takeScreenshot(x)
	img = pickImage(x+1)
	squaresNew = getColours(img)

	difference = differenceFinder(squaresOld, squaresNew)

	squaresOld = difference[0]

	try:
		move = difference[1]
		moves.append(move)
	except:
		pass

with open(f"{path}\\Chess Moves.txt", "w") as fileChess:

	for i in range(len(moves)):

		fileChess.write('\n'.join(['{}.{}'.format(i+1, moves[i])]))
