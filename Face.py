#A side of the cube
class Face:
	side = []
	row = []

	#Initialize for single color
	def __init__(self, color):
		for i in range(3):
			row.append(color)
		side.append(row)
		row = []

	#Print out string for face, which can add characters
	def __str__(self, char = ''):
		output = ''
		for i in range(len(side)):
			output += char
			for j in range(len(side)):
				output += side[i][j]
			output += '\n'
		return output

	#Get face
	def getColors():
		return side

	#Set face with array of colors
	def setColors(self, colors):
		for i in range(len(colors)):
			for j in range(len(colors)):
				side[i][j] = colors[i][j]

	#Get size of side
	def getNum():
		return len(side)

	#Get Row
	def getRow(row):
		return side[row]

	#Set Row
	def setRow(row, color):
		side[row] = color[:]

	#Get Column
	def getCol(col):
		column = []
		for i in range(len(side)):
			column.append(side[i][col])
		return column

	#Set Column
	def setCol(col, color):
		for i in range(len(side)):
			side[i][col] = color[i]

	#Get Corner Pieces
	def getCorner():
		corner = []
		

	#Rotate Clockwise
	def rotateCW():
		
		

	#Rotate Counter Clockwise
	def rotateCCW():


	#Check if face is certain color (for solved state)
	def checkColors(self, color):
		for i in range(len(side)):
			for j in range(len(side)):
				if side[i][j] != color:
					return False
		return True
