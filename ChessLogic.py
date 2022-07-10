# import cv2 as cv
import numpy as np
from PIL import Image
import pyautogui
from time import sleep
import requests
import json


# print("Hello Python")

# print(f"OpenCV {cv.__version__}")

# print(f"Numpy {np.__version__}")


# path = "C:\\Users\\Antonio\\Desktop\\Python Programs\\Chess"
path = "C:\\Users\\guhan\\Desktop\\chess"

# path = input("Enter your system path.")


def differenceFinder(oldSquares, newSquares):

	missingPiece = []
	unknownPiece = None

	# checking for castling king side white
	if oldSquares[4] == ["e1", "K", "White"] and oldSquares[5] == ["f1", "None", "Blank"] and oldSquares[6] == ["g1", "None", "Blank"] and oldSquares[7] == ["h1", "R", "White"] and newSquares[5] == ["f1", "None", "White"] and newSquares[6] == ["g1", "None", "White"]: 

		newSquares = oldSquares
		newSquares[4] = ["e1", "None", "Blank"]
		newSquares[5] = ["f1", "R", "White"]
		newSquares[6] = ["g1", "K", "White"]
		newSquares[7] = ["h1", "None", "Blank"]

		move = "O-O"

		values = [newSquares, move]

	# checking for castling king side black
	elif oldSquares[60] == ["e8", "K", "Black"] and oldSquares[61] == ["f8", "None", "Blank"] and oldSquares[62] == ["g8", "None", "Blank"] and oldSquares[63] == ["h8", "R", "Black"] and newSquares[61] == ["f8", "None", "Black"] and newSquares[62] == ["g8", "None", "Black"]:
	
		newSquares = oldSquares
		newSquares[60] = ["e8", "None", "Blank"]
		newSquares[61] = ["f8", "R", "Black"]
		newSquares[62] = ["g8", "K", "Black"]
		newSquares[63] = ["h8", "None", "Blank"]

		move = "O-O"

		values = [newSquares, move]

	# checking for castling queen side white
	elif oldSquares[0] == ["a1", "R", "White"] and oldSquares[1] == ["b1", "None", "Blank"] and oldSquares[2] == ["c1", "None", "Blank"] and oldSquares[3] == ["d1", "None", "Blank"] and oldSquares[4] == ["e1", "K", "White"] and newSquares[2] == ["c1", "None", "White"] and newSquares[3] == ["d1", "None", "White"]:

		newSquares = oldSquares
		newSquares[0] = ["a1", "None", "Blank"]
		newSquares[1] = ["b1", "None", "Blank"]
		newSquares[2] = ["c1", "K", "White"]
		newSquares[3] = ["d1", "R", "White"]
		newSquares[4] = ["e1", "None", "Blank"]

		move = "O-O-O"

		values = [newSquares, move]

	#checking for castling queen side black
	elif oldSquares[56] == ["a8", "R", "Black"] and oldSquares[57] == ["b8", "None", "Blank"] and oldSquares[58] == ["c8", "None", "Blank"] and oldSquares[59] == ["d8", "None", "Blank"] and oldSquares[60] == ["e8", "K", "Black"] and newSquares[58] == ["c8", "None", "Black"] and newSquares[59] == ["d8", "None", "Black"]:

		newSquares = oldSquares
		newSquares[56] = ["a8", "None", "Blank"]
		newSquares[57] = ["b8", "None", "Blank"]
		newSquares[58] = ["c8", "K", "Black"]
		newSquares[59] = ["d8", "R", "Black"]
		newSquares[60] = ["e8", "None", "Blank"]

		move = "O-O-O"

		values = [newSquares, move]

	else:

		for i in range(64):
			

			squareOld = oldSquares[i]
			squareNew = newSquares[i]


			# checks if there was a change
			if squareOld[2] == squareNew[2]:
				# no change
				squareNew[1] = squareOld[1]
			# change
			else:

				# a piece should be there but isn't
				if squareNew[2] == "Blank":
					
					squareNew[1] = "None"
					missingPiece.append(squareOld)

				# was one colour but is a new one now
				elif  (squareOld[2] == "White" and squareNew[2] == "Black") or (squareOld[2] == "Black" and squareNew[2] == "White"):

					missingPiece.append(squareOld)
					unknownPiece = i
				# was blank but now has a piece
				else:

					unknownPiece = i

		if unknownPiece != None:

			changedSquare = newSquares[unknownPiece]

			if len(missingPiece) == 1:

				# piece movement message return
				move = f"{missingPiece[0][1]}{changedSquare[0]}"
				changedSquare[1] = missingPiece[0][1]

			else:

				missingPiece1 = missingPiece[0]
				missingPiece2 = missingPiece[1]

				if changedSquare[2] == missingPiece1[2]:
					# piece killed another piece return
					changedSquare[1] = missingPiece1[1]
					if missingPiece1[1] == "":
						move = f"{missingPiece1[0][0]}x{changedSquare[0]}"
					else:
						move = f"{missingPiece1[1]}x{changedSquare[0]}"

				else:
					# piece killed another piece return
					changedSquare[1] = missingPiece2[1]
					if missingPiece2[1] == "":
						move = f"{missingPiece2[0][0]}x{changedSquare[0]}"
					else:
						move = f"{missingPiece2[1]}x{changedSquare[0]}"


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

	squares = [
	# 1st Row
	["a1", "R", "White"],
	["b1", "N", "White"],
	["c1", "B", "White"],
	["d1", "Q", "White"],
	["e1", "K", "White"],
	["f1", "B", "White"],
	["g1", "N", "White"],
	["h1", "R", "White"],

	# 2nd Row
	["a2", "", "White"],
	["b2", "", "White"],
	["c2", "", "White"],
	["d2", "", "White"],
	["e2", "", "White"],
	["f2", "", "White"],
	["g2", "", "White"],
	["h2", "", "White"],

	# 3rd Row
	["a3", "None", "Blank"],
	["b3", "None", "Blank"],
	["c3", "None", "Blank"],
	["d3", "None", "Blank"],
	["e3", "None", "Blank"],
	["f3", "None", "Blank"],
	["g3", "None", "Blank"],
	["h3", "None", "Blank"],

	# 4th Row
	["a4", "None", "Blank"],
	["b4", "None", "Blank"],
	["c4", "None", "Blank"],
	["d4", "None", "Blank"],
	["e4", "None", "Blank"],
	["f4", "None", "Blank"],
	["g4", "None", "Blank"],
	["h4", "None", "Blank"],


	# 5th Row
	["a5", "None", "Blank"],
	["b5", "None", "Blank"],
	["c5", "None", "Blank"],
	["d5", "None", "Blank"],
	["e5", "None", "Blank"],
	["f5", "None", "Blank"],
	["g5", "None", "Blank"],
	["h5", "None", "Blank"],

	# 6th Row
	["a6", "None", "Blank"],
	["b6", "None", "Blank"],
	["c6", "None", "Blank"],
	["d6", "None", "Blank"],
	["e6", "None", "Blank"],
	["f6", "None", "Blank"],
	["g6", "None", "Blank"],
	["h6", "None", "Blank"],

	# 7th Row
	["a7", "", "Black"],
	["b7", "", "Black"],
	["c7", "", "Black"],
	["d7", "", "Black"],
	["e7", "", "Black"],
	["f7", "", "Black"],
	["g7", "", "Black"],
	["h7", "", "Black"],

	# 8th Row
	["a8", "R", "Black"],
	["b8", "N", "Black"],
	["c8", "B", "Black"],
	["d8", "Q", "Black"],
	["e8", "K", "Black"],
	["f8", "B", "Black"],
	["g8", "N", "Black"],
	["h8", "R", "Black"],

	]

	return squares


squaresOld = startPositions()

# sleep(5000)

moves = []

for x in range(37):

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

# for i in range(len(moves)):

# 	print(f"{i+1}. {moves[i]} ")

with open(f"{path}\\Chess Moves.pgn", "w") as fileChess:

	for i in range(len(moves)):

		fileChess.write(f"{i+1}. {moves[i]} ")

with open(f"{path}\\Chess Moves.txt", "w") as fileChess:

	for i in range(len(moves)):

		fileChess.write(f"{i+1}. {moves[i]} ")

file = open(f"{path}\\Chess Moves.pgn", "r")

read = file.read()

file.close()

response = requests.post("https://lichess.org/api/import",  
    data = {"pgn": read}
)

print(response.json()["url"])
