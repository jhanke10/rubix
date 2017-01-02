from Face import *

front = 0
left = 1
right = 2
back = 3
top = 4
bottom = 5

sides = ['r', 'g', 'b', 'o', 'w', 'y']

#Rubix cube
class Cube:
	#Faces of the cube
	global faces
	faces = []

	#Holds the faces that are affected by the move
	moves = {
		front : [left, top, right, bottom],
		back : [right, top, left, bottom],
		left : [back, top, front, bottom],
		right : [front, top, back, bottom],
		top : [left, back, right, front],
		bottom : [left, front, right, back]
	}

	#Initialize a solved cube
	def __init__(self):
		for i in range(6):
			faces.append(Face(sides[i]))

	#Returns a string for the cube
	#Output Format:      
	#      w w w
	#      w w w
	#      w w w
	#g g g r r r b b b o o o
	#g g g r r r b b b o o o
	#g g g r r r b b b o o o
	#      y y y
	#      y y y
	#      y y y
	def __str__(self):
		output = ''
		face = faces[top].getColors()
		print face
		#Adds the top face
		for i in range(len(face)):
			output += '      '
			for j in range(len(face)):
				output += face[i][j] + ' '
			ouput += '\n'

		#Adds the middle four faces
		mid = [left, front, right, back]
		for i in range(len(face)):
			for k in range(4):
				face = faces[mid[k]].getColors()
				for j in range(len(face)):
					output += face[i][j] + ' '
			output += '\n'

		#Adds the bottom face
		face = faces[bottom].getColors()
		for i in range(len(face)):
			output += '      '
			for j in range(len(face)):
				output += face[i][j] + ' '
			ouput += '\n'

		return output

print Cube()