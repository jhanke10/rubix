#Row/Col
row = 0
col = 1

#A side of the cube
class Face:
	side = []

	#Initialize for single color
	def __init__(self, color):
		self.side = []
		row = []
		for i in range(3):
			for j in range(3):
				row.append(color)
			self.side.append(row)
			row = []

	#Print out string for face
	def __str__(self):
		output = ''
		for i in range(len(self.side)):
			for j in range(len(self.side)):
				output += self.side[i][j] + ' '
			output += '\n'
		return output

	#Set face with array of colors
	def setColors(self, colors):
		for i in range(len(colors)):
			for j in range(len(colors)):
				self.side[i][j] = colors[i][j]

	#Determines if function is a getter of row or col
	def getFunc(self, part, num):
		if part == row:
			return self.side[num]
		else:
			column = []
			for i in range(len(self.side)):
				column.append(self.side[i][num])
			return column

	#Determines if function is a setter of row or col
	def setFunc(self, part, num, color):
		if part == row:
			self.side[num] = color[:]
		else:
			for i in range(len(self.side)):
				self.side[i][num] = color[i]


	#Get Corner Pieces
	def getCorner(self):
		corner = [self.side[0][0], self.side[0][2], self.side[2][2], self.side[2][0]]
		return corner

	#Set Corner Pieces
	def setCorner(self, corners):
		self.side[0][0] = corners[0]
		self.side[0][2] = corners[1]
		self.side[2][2] = corners[2]
		self.side[2][0] = corners[3]

	#Get Cross Edge Pieces
	def getCross(self):
		cross = [self.side[0][1], self.side[1][2], self.side[2][1], self.side[1][0]]
		return cross

	#Set Cross Pieces
	def setCross(self, crosses):
		self.side[0][1] = crosses[0]
		self.side[1][2] = crosses[1]
		self.side[2][1] = crosses[2]
		self.side[1][0] = crosses[3]

	#Rotate list
	def rotate(self, lists, num):
		return lists[num:] + lists[:num]

	#Rotate Clockwise or Counter Clockwise
	def rotateFace(self, cw):
		if cw:
			corner = self.getCorner()
			cross = self.getCross()
			self.setCorner(self.rotate(corner, 1))
			self.setCross(self.rotate(cross, 1))
		else:
			corner = self.getCorner()
			cross = self.getCross()
			self.setCorner(self.rotate(corner, 3))
			self.setCross(self.rotate(cross, 3))

	#Check if face is certain color (for solved state)
	def checkColors(self, color):
		for i in range(len(self.side)):
			for j in range(len(self.side)):
				if self.side[i][j] != color:
					return False
		return True