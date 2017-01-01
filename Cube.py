import Face from *

mid = 0
left = 1
right = 2
back = 3
top = 4
bottom = 5

sides = ['r', 'g', 'b', 'o', 'w', 'y']

#Rubix cube
class Cube:
	faces = []

	def __init__(self):
		for i in range(6):
			faces.append(Face(sides[i]))

	def __str__(self):
		for i in range(len(faces[top].getColors())):


