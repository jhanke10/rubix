mid = 0
left = 1
right = 2
back = 3
top = 4
bottom = 5

sides = ['r', 'g', 'b', 'o', 'w', 'y']

class Face:
	side = []
	row = []

	#Initialize for single color
	def __init__(self, color):
		for i in range(3):
			row.append(color)
		side.append(row)
		row = []

	#Set face with array of colors
	def setColors(self, colors):
		for i in range(len(colors)):
			for j in range(len(colors)):
				side[i][j] = colors[i][j]

	#Get face
	def getColors():
		return side

	#Get size of side
	def getNum():
		return len(side)

	def getRow(row):
		return side[row]

	def getCol()

	#Check if face is certain color (for solved state)
	def checkColors(self, color):
		for i in range(len(side)):
			for j in range(len(side)):
				if side[i][j] != color:
					return False
		return True


#Rubix cube
class Cube:
	faces = []

	def __init__(self):
		for i in range(6):
			faces.append(Face(sides[i]))

	def __str__(self):
		for i in range(len(faces[top].getColors())):


