from collections import deque
###########################################################################################################
# class Search
# This class searches for the best solution
############################################################################################################	
class Search:
	
	###########################################################################################################
# def searching(truth=True, seats = 2)
# This function searches for the best solution
# inputs: truth, seats
# returns: goodBranches
############################################################################################################	
	def searching(truth=True, seats = 2):
		pastBranches = set()
		goodBranches = []
		branchesAvailable= deque()


		root = StateSpace.build_root()
		branchesAvailable.append(root)
		while len(branchesAvailable) != 0:
			branch = branchesAvailable.pop()
			for child in branch.get_children(seats):
				possibility= child.state
				if possibility not in pastBranches:					
					if child.failed() == True:
						continue
					elif child.solved() == True:
						goodBranches.append(child)
						continue					
					if truth == False:
						branchesAvailable.insert(0,child)
					else:
						branchesAvailable.append(child)
					pastBranches.add(possibility)
					
	
		return goodBranches

###########################################################################################################
# class StateSpace
# This class searches for the best solution
############################################################################################################	
class StateSpace:
	
	def __init__(self, state, count=0, parent=None):
		self.parent = parent
		self.count = count
		self.state = state

	#create the first instance of the tree missionary, cannibal, and boat on start side (3, 3, 1) respectively
	@classmethod
	###########################################################################################################
# def searching(truth=True, seats = 2)
# This function builds the root
# inputs: cls
# returns: cls (3, 3, 1) 3 miss, 3 cann, 1 boat
############################################################################################################	
	def build_root(cls):
		return cls((3,3,1))

	
###########################################################################################################
# def get_children(self, seats)
# this function gets the children of the current branch node
# inputs: self,cls
# returns: children
############################################################################################################	
	def get_children(self, seats):
		if seats == 2:
			moves = self.two_person_boat_moves()
		elif seats == 3:
			moves = self.three_person_boat_moves()
		children= []
		startMissionaries, startCannibals, startBoat = self.state
		for move in moves:
			missionariesMoving, cannibalsMoving = move
			if startBoat== 1:  #if on the startside, subtract the values to find number on goal side, else add them
				nextState = (startMissionaries-missionariesMoving, startCannibals-cannibalsMoving, 0)
			else:
				nextState= (startMissionaries + missionariesMoving, startCannibals + cannibalsMoving, 1)
			child = StateSpace(nextState, self.count+1, self)
			if child.allowed():
				children.append(child)

		return children

	
	###########################################################################################################
# def two_person_boat_moves(self)
# this function tests the possible combinations of missionaries/cannibals in 2 seater
# inputs: self
# returns: the possible combinations of missionaries and cannibals in a boat
############################################################################################################	
	def two_person_boat_moves(self):
		return (1, 0), (2, 0), (0, 1), (0, 2), (1, 1)
	###########################################################################################################
# def three_person_boat_moves(self)
# this function tests the possible combinations of missionaries/cannibals in 3 seater
# inputs: self
# returns: the possible combinations of missionaries and cannibals in a boat
############################################################################################################	
	def three_person_boat_moves(self):
		return (1, 0), (2, 0), (3, 0), (0, 1), (0, 2), (0,3), (1, 1), (1, 2), (2, 1)
	#check if making a move breaks our rule that there are 3 missionaries and 3 cannibals total
###########################################################################################################
# def allowed(self)
# This function tests if the number of cannibals/missionaries combo is allowed
# inputs: self
# returns: True/False
############################################################################################################	
	def allowed(self):
		missionaries, cannibals, boatSide = self.state
		if missionaries >= 0 and cannibals >= 0 and missionaries <= 3 and cannibals <= 3: 
			return True
		else:
			return False
	#check if the move made results in 3, 3, 1 on the goal side and 0, 0, 0 on the start side
###########################################################################################################
# def failed(self)
#check if the move made results in 3, 3, 1 on the goal side and 0, 0, 0 on the start side
# inputs: self
# returns: True/False
############################################################################################################	
	def failed(self):
		missionaries, cannibals, boatSide = self.state   
		#If missionary number > 0 and missionaries < cannibals, not done
		if (missionaries > 0 and missionaries < cannibals) or (3 - missionaries > 0 and 3 - missionaries < 3 - cannibals):
			return True
		
		return False
###########################################################################################################
# def solved(self)
# check if the final state on the start side has been achieved
# inputs: self
# returns: True/False
############################################################################################################	
	
	def solved(self):
		if self.state != (0,0,0):
			return False
		else:
			return True
###########################################################################################################
# def print_tree_contents(tree, seats, searchType)
# Print the tree contents by taking each branch in the solution tree, and recursively printing its parents
# inputs: tree, seats, searchType
# returns: Nothing
############################################################################################################	

def print_tree_contents(tree, seats, searchType):
	
	for branch in tree:
		counter = 0
		while branch:
			m, c, b = branch.state
			if b == 1:
				b ="boat on goal side"
			else:
				b = "boat on start side"
			print("depth: " + str(counter+ 1))
			print("start side values:  " + " Missionaries: " + str(3- m) + " Cannibals: " + str(3- c))
			print("goal side values:  " + " Missionaries: " + str(m) + " Cannibals: " + str(c))
			print(b)
			branch =branch.parent
			counter +=1
		print("Number of ", searchType, " solutions with", seats,  " seats: ", len(tree))
		print("Number of steps to solution: ", counter)
		print("\n")

def main():

	depthFirstTree_2Seater = Search.searching(True, 2)
	print_tree_contents(depthFirstTree_2Seater, "2", "depth")
	breadthFirstTree_2Seater = Search.searching(False, 2)
	print_tree_contents(breadthFirstTree_2Seater, "2", "breadth")

	depthFirstTree_3Seater = Search.searching(True, 3)
	print_tree_contents(depthFirstTree_3Seater, "3", "depth")
	breadthFirstTree_3Seater = Search.searching(False, 3)
	print_tree_contents(breadthFirstTree_3Seater, "3", "breadth")

		

if __name__== "__main__":
	main()
