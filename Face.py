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
		corner = [side[0][0], side[0][2], side[2][2], side[2][0]]
		return corner

	#Set Corner Pieces
	def setCorner(corners):
		side[0][0] = corners[0]
		side[0][2] = corners[1]
		side[2][2] = corners[2]
		side[2][0] = corners[3]

	#Get Cross Edge Pieces
	def getCross():
		cross = [side[0][1], side[1][2], side[2][1], side[1][0]]
		return cross

	#Set Cross Pieces
	def setCross(crosses):
		side[0][1] = crosses[0]
		side[1][2] = crosses[1]
		side[2][1] = crosses[2]
		side[1][0] = crosses[3]

	#Rotate Clockwise
	def rotateCW():
		corner = getCorner()
		cross = getCross()
		setCorner(corner.rotate(1))
		setCross(cross.rotate(1))

	#Rotate Counter Clockwise
	def rotateCCW():
		corner = getCorner()
		cross = getCross()
		setCorner(corner.rotate(3))
		setCross(cross.rotate(3))

	#Check if face is certain color (for solved state)
	def checkColors(self, color):
		for i in range(len(side)):
			for j in range(len(side)):
				if side[i][j] != color:
					return False
		return True
