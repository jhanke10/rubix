from cube import *
from face import *
from Queue import PriorityQueue
import time

#Altered Priority Queue
#http://stackoverflow.com/questions/9289614/how-to-put-items-into-priority-queues
class PQueue(PriorityQueue):
	def __init__(self):
		PriorityQueue.__init__(self)
		self.counter = 0

	def put(self, item, priority):
		PriorityQueue.put(self, (priority, self.counter, item))
		self.counter += 1

	def get(self, *args, **kwargs):
		_, _, item = PriorityQueue.get(self, *args, **kwargs)
		return item

#Calculate displacement
def calcDisplacement(cube, solved):
	disp = 0
	for i in range(len(cube.faces)):
		disp += solved.faces[i].calcDiff(cube.faces[i])
	return disp

#Get all orientation from a cube state
def getStates(cube):
	#Save current state
	curr = cube.state()

	states = set()
	for i in range(4):
		for j in range(4):
			cube.flipCube(horizontal)
			states.add(cube)
		cube.flipCube(vertical)
		states.add(cube)

	#Return cube to original state
	cube.setState(curr)

	return states

#Heuristic Algorithm 
def heuristic(cube):
	#Calculate the displacement of cubes from each of the different solved states (four of each rotation)
	solved = Cube()

	#Minimum cube displacement
	min_disp = None
	for i in range(4):
		for j in range(4):
			solved.flipCube(horizontal)
			disp = calcDisplacement(cube, solved)
			if min_disp == None or disp < min_disp:
				min_disp = disp
		solved.flipCube(vertical)

	return min_disp

#Solver Algorithm using A* Search
def rubixSolver(cube):
	#All of the different moves possible
	moves = [top, left, front, right, back, bottom]
	moves = [(x, True) for x in moves] + [(x, False) for x in moves]

	#Set for seen states
	closedSet = set()

	#Priority Queue for states that haven't been seen
	openSet = PQueue()
	openSet.put(cube.state(), 0)

	#Parent State
	parent = {}
	parent[cube.state()] = (None, None)

	#Scores
	gscore = {}
	fscore = {}

	#Initialize Scores
	gscore[cube.state()] = 0
	fscore[cube.state()] = heuristic(cube)

	#Algorithm
	while not openSet.empty():
		#Get the node with the lowest fscore
		curr = openSet.get()

		#Set state to current state
		cube.setState(curr)

		#See if the cube is at goal state
		if heuristic(cube) == 0:
			print "Solved"
			return reconstruct(parent, curr)

		#Add the state to seen
		closedSet.add(curr)

		#Go through all possible moves
		for move in moves:
			#Reset cube to current state
			cube.setState(curr)

			#Apply move
			cube.moveHelper(move[0], move[1])

			#Save state
			curr_state = cube.state()

			#Checks if the state has been seen
			if cube.state() in closedSet:
				continue

			#Checks to see if any orientation of the state have been seen
			states = getStates()
			seen = False
			for orientation in states:
				if orientation in closedSet or orientation in gscore:
					seen = True
					break

			#If seen just add to closedSet
			if seen:
				closedSet.add(curr_state)
				continue

			#Calculate the new score
			score = gscore[curr] + 1

			#Updates scores and adds to openSet
			if curr_state not in closedSet or (curr_state in gscore and score < gscore[curr_state]):
				gscore[curr_state] = score
				fscore[curr_state] = score + heuristic(cube)
				openSet.put(curr_state, fscore[curr_state])
				parent[curr_state] = (curr, move)	

#Reconstructs the path to the solved state
def reconstruct(orig, curr):
	moves = []

	while curr is not None:
		moves.append(orig[curr][1])
		if orig[curr][0] is not None:
			curr = orig[curr][0]
		else:
			break

	return moves.reverse()

def main():
	cube = Cube("layout.txt")
	print rubixSolver(cube)

if __name__ == "__main__":main()