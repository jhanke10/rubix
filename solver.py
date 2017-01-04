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


#Heuristic Algorithm
def heuristic(cube):
	#Minimum cube displacement
	min_disp = 0
	
	


#Solver Algorithm using A* Search
def rubixSolver(cube):
	return cube

#Reconstructs the path to the solved state
def reconstruct(orig, curr):
	return None

def main():
	cube = Cube("layout.txt")
	print rubixSolver(cube)

if __name__ == "__main__":main()