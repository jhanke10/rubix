from face import *

#Sides of the cube
top = 0
left = 1
front = 2
right = 3
back = 4
bottom = 5

#Row/Col
row = 0
col = 1

#Color of all of the sides of the rubix cube
colors = ['w', 'g', 'r', 'b', 'o', 'y']

#Rubix cube
class Cube:
	#Faces of the cube
	faces = []

	#Holds the faces that are affected by the move
	moves = {
		front : [[left, col, 2], [top, row, 2], [right, col, 0], [bottom, row, 0]],
		back : [[left, col, 0], [top, row, 0], [right, col, 2], [bottom, row, 2]],
		left : [[back, col, 2], [top, col, 0], [front, col, 0], [bottom, col, 0]],
		right : [[back, col, 0], [top, col, 2], [front, col, 2], [bottom, col, 2]],
		top : [[left, row, 0], [back, row, 0], [right, row, 0], [front, row, 0]],
		bottom : [[left, row, 2], [back, row, 2], [right, row, 2], [front, row, 2]]
	}

	#Initialize a solved cube if no file-read, else make the layout in file
	def __init__(self, files = None):
		for i in range(6):
			self.faces.append(Face(colors[i]))
		if files != None:
			layout = open(files, 'r')
			count = 0
			layout_faces = []

			#Parsing the input file layout
			face = []
			for tiles in layout:
				tiles = tiles.split()
				if count < 3: 
					face.append(tiles)
				if count == 3:
					layout_faces.append(face)
					face = []
				if count > 2 and count < 6:
					face.append(tiles)
				if count == 5:
					face = self.getFaces(face)
					for i in range(len(face)):
						layout_faces.append(face[i])
					face = []
				if count > 5 and count < 9:
					face.append(tiles)
				if count == 8:
					layout_faces.append(face)
				count += 1

			#Set the cube's faces to the layout color
			for i in range(len(layout_faces)):
				self.faces[i].setColors(layout_faces[i])

	#Breaks up the list into faces
	def getFaces(self, lists):
		layout_faces = []
		lists_face = []
		for i in range(len(lists)):
			layout = lists[i]
			face = [layout[x:x+3] for x in xrange(0, len(layout), 3)]
			lists_face.append(face)
		face = []
		for i in range(4):
			for j in range(3):
				face.append(lists_face[j][i])
			layout_faces.append(face)
			face = []
		return layout_faces

	#Returns a string for the cube
	#Output Format:      
	#      w w w
	#      w w w
	#      w w w
	# g g g r r r b b b o o o
	# g g g r r r b b b o o o
	# g g g r r r b b b o o o
	#      y y y
	#      y y y
	#      y y y
	def __str__(self):
		output = ''
		face = self.faces[top].side
		#Adds the top face
		for i in range(len(face)):
			output += '      '
			for j in range(len(face)):
				output += face[i][j] + ' '
			output += '\n'

		#Adds the middle four faces
		for i in range(len(face)):
			for k in range(4):
				face = self.faces[k+1].side
				for j in range(len(face)):
					output += face[i][j] + ' '
			output += '\n'

		#Adds the bottom face
		face = self.faces[bottom].side
		for i in range(len(face)):
			output += '      '
			for j in range(len(face)):
				output += face[i][j] + ' '
			output += '\n'
		return output

	#Checks if the cube have been solved by checking each sides correct color
	def haveSolved(self):
		for i in range(len(self.faces)):
			if not self.faces[i].checkColors(colors[i]):
				return False
		return True

	#Get Move
	def getMove(self, move):
		return move[0], move[1], move[2]

	#Takes a move and changes the configuration of the cube
	def moveHelper(self, move, cw = True):
		sides = self.moves[move]

		#Alter order if CCW
		if not cw:
			sides.reverse()

		#Set next to first one
		face, part, num = self.getMove(sides[0])
		next = self.faces[face].getFunc(part, num)[:]

		for i in range(len(sides)):
			#Get the first side and the next side
			face, part, num = self.getMove(sides[i])
			face2, part2, num2 = self.getMove(sides[(i+1)%4])

			#Set the temp variables
			curr = next[:]
			next = self.faces[face2].getFunc(part2, num2)[:]

			#Set the next side to curr
			self.faces[face2].setFunc(part2, num2, curr)

		#Rotate face
		self.faces[move].rotateFace(cw)