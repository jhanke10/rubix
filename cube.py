from face import *

#Sides of the cube
top = 0
left = 1
front = 2
right = 3
back = 4
bottom = 5

#Vertically/Horizontally
vertical = 0
horizontal = 1

#Rubix cube
class Cube:
	#Faces of the cube
	faces = []

	#Color of all of the sides of the rubix cube
	colors = ['w', 'g', 'r', 'b', 'o', 'y']

	#Holds the faces that are affected by the move
	moves = {
		front : [[left, col, 2], [top, row, 2], [right, col, 0], [bottom, row, 0]],
		back : [[left, col, 0], [top, row, 0], [right, col, 2], [bottom, row, 2]],
		left : [[back, col, 2], [top, col, 0], [front, col, 0], [bottom, col, 0]],
		right : [[back, col, 0], [top, col, 2], [front, col, 2], [bottom, col, 2]],
		top : [[left, row, 0], [back, row, 0], [right, row, 0], [front, row, 0]],
		bottom : [[left, row, 2], [back, row, 2], [right, row, 2], [front, row, 2]]
	}

	flips = {
		vertical : [front, bottom, back, top],
		horizontal : [front, right, back, left]
	}

	#Initialize a solved cube if no file-read, else make the layout in file
	def __init__(self, files = None):
		self.faces = []
		for i in range(6):
			self.faces.append(Face(self.colors[i]))
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

	#Flips cube in two directions: vertically towards you or horizontally right
	def flipCube(self, direction):
		flip = self.flips[direction]
		next = self.faces[flip[0]].side[:]
		for i in range(len(flip)):
			curr = next[:]
			next = self.faces[flip[(i + 1) % 4]].side[:]
			self.faces[flip[(i + 1) % 4]].setColors(curr)
		for i in range(len(self.faces)):
			self.colors[i] = self.faces[i].getCenter()

	#Creates a string for the cube state
	def state(self):
		curr = ''
		for i in range(len(self.faces)):
			curr += self.faces[i].state()
		return curr

	#Sets the state of the cube from string
	def setState(self, state):
		states = state.strip()
		state_faces = []
		count = 0
		for i in range(6):
			face = []
			for x in range(3):
				row = []
				for y in range(3):
					row.append(states[count])
					count += 1
				face.append(row)
			state_faces.append(face)
		for i in range(len(self.faces)):
			self.faces[i].setColors(state_faces[i])

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
