import difflib


'''
TODO 
-check overlap function overlap numbers should be corresponding to min and max overlap
'''

class Assembler(object):
    
    def __init__(self):
    	self.speed = 5

    def assemble(self, fragments):
    	graph = Graph()
    	for fragment in fragments:
    		newNode = Node(fragment)
    		graph.addNode(newNode)

    	#generate overlap graph
    	graph.bruteForceConnect(1)
    	print("connected")
    	#graph.eliminateWeakPathsOptimized()
    	#print("simplified")
    	#res = graph.getGreedyOverlap()
    	res = graph.getGreedyIntuitiveOverlap();
    	print(len(res))
    	return nodeArrayToString(res)

    	#print(res)

    	#print(nodeArrayToString(res))


class Graph(object):
	def __init__(self):
		self.startingNode = None
		self.nodes = []
		self.connections = [] #stores node a, node b and cost

	def addNode(self,newNode):
		self.startingNode = newNode
		self.nodes += [newNode]

	def addConection(self, indexA,indexB,cost):
		nodeA = self.nodes[indexA]
		nodeB = self.nodes[indexB]
		nodeA.addNeighbor(nodeB, cost)
		#newConection = {"a":nodeA,"b":nodeB,"cost":cost}
		#self.connections += [newConection] 

	#completely conects current graph
	def bruteForceConnect(self,minOverlap):
		cont = 0
		for nodeAindex in range(len(self.nodes)-1):
			for nodeBindex in range(len(self.nodes)-1):
				nodeA = self.nodes[nodeAindex]
				nodeB = self.nodes[nodeBindex]
				sizeA = len(nodeA.data)
				sizeB = len(nodeB.data)
				#print(nodeA.data)
				#print(nodeB.data)
				overlap = overlapMax(nodeA.data,nodeB.data)
				#exists concatenation
				if(overlap >= minOverlap):
					self.addConection(nodeAindex,nodeBindex,overlap)
					cont +=1
					if(cont%2000 == 0):
						print(cont)
				
		print(cont)
	
	def getGreedyIntuitiveOverlap(self):
		result = []
		#use dictionary as cache
		cache = {}
		self.nodes.sort(key=lambda x: x.highestCost, reverse=True)
		for nodeA in self.nodes:
			#visit node if not visited
			if(not nodeA.visited):
				nodeA.visited = True
				#create a copy of current node
				bc = nodeA
				#stores the full path visited by the node
				acc = [bc]
				while(nodeA):
					current = nodeA
					nodeA = None
					for nodeB in current.neighbors:
						if(not nodeB.visited):
							if(nodeB in cache):
								del cache[current]
								acc += cache[nodeB]
							else:
								acc += [nodeB]
							nodeB.visited = True
							nodeA = nodeB
							break
				cache[bc] = acc

		#pn = []
		for node in self.nodes:
			#if(node in cache):
				#print(len(cache[node]))
			if(node in cache and len(cache[node]) > len(result)):
				result = cache[node]

				#pn += [len(cache[node])]
		#print(pn)

		return result


	#does gready aproach to string assembly
	def getGreedyOverlap(self):
		self.eliminateWeakPathsOptimized()
		prin("simplified")
		result = []
		#use dictionary as cache
		cache = {}
		#sort connections by highest value
		self.connections.sort(key=lambda x: x["cost"], reverse=True)
		
		for con in self.connections:
			nodeA = con["a"]
			nodeB = con["b"]
			if(nodeB in cache):
				cache[nodeA] = [nodeA] + cache[nodeB]
			else:
				cache[nodeA] = [nodeA, nodeB]
			#print(cache[nodeA])
			if(len(cache[nodeA]) > len(result)):
				result = cache[nodeA]
		
		pn = []
		for node in self.nodes:
			if(node in cache):
				pn += [len(cache[node])]
		return result

	def nonRepeatingWeakPaths(self):
		self.reset()
		for node in self.nodes:
			node.eliminateWeakPathsOptimized()

		self.reset()
	def eliminateWeakPaths(self):
		for node in self.nodes:
			node.eliminateWeakPaths()
			#add connections to list representation
			if(len(node.neighbors) > 0):
				newConection = {"a":node,"b":node.neighbors[0],"cost":node.cost[0]}
				self.connections += [newConection]

	def eliminateWeakPathsOptimized(self):
		for node in self.nodes:
			node.eliminateWeakPathsOptimized()
			#add connections to list representation
			if(len(node.neighbors) > 0):
				newConection = {"a":node,"b":node.neighbors[0],"cost":node.cost[0]}
				self.connections += [newConection]

	def reset(self):
		for node in self.nodes:
			node.visited = False


class Node(object):
	def __init__(self,data):
		self.neighbors = []
		self.cost = []
		self.data = data
		self.visited = False
		self.highestCost = 0

	#keeps the bigges cost at index 0 
	def addNeighbor(self,newNeightbor, newCost):
		#print(newCost)
		if(len(self.cost) <=0):
			self.cost += [newCost]
			self.neighbors += [newNeightbor]
			return
		#do insertion sort of nodes
		if(newCost > self.cost[0]):
			self.cost = [newCost] + self.cost
			self.neighbors = [newNeightbor] + self.neighbors
		else:
			for i in range(len(self.cost) -1):
				if(self.cost[i] < newCost):
					self.cost = self.cost[:i-1] + [ newCost] + self.cost[i-1:]
					self.neighbors = self.neighbors[:i-1] + [ newNeightbor] + self.neighbors[i-1:]
					break
		#store higest cost value
		self.highestCost = self.cost[0]


	def removeNeighbor(self, target):
		targetIndex = self.neighbors.index(target)
		del cost[targetIndex]
		return newNeightbor.pop(targetIndex)

	def removeNeighborByIndex(self,targetIndex):
		del cost[targetIndex]
		return newNeightbor.pop(targetIndex)

	#removes all nodes but the biggest conection
	def eliminateWeakPaths(self):
		if(len(self.cost) > 0):
			self.cost = [self.cost[0]]
			self.neighbors = [self.neighbors[0]]

	def eliminateWeakPathsOptimized(self):
		
		neighbors = self.neighbors
		cost = self.cost
		self.cost = []
		self.neighbors = []
		if(len(cost) > 0):
			for i in range(len(cost)-1):
				currentCost = cost[i]
				currentNb = neighbors[i]
				if(not currentNb.visited):
					self.cost = [currentCost]
					self.neighbors = [currentNb]
					currentNb.visited = True

# utility function
def get_overlap(s1, s2):
    s = difflib.SequenceMatcher(None, s1, s2)
    pos_a, pos_b, size = s.find_longest_match(0, len(s1), 0, len(s2)) 
    return s1[pos_a:pos_a+size]


def nodeArrayToString(nArr):
	res = nArr[0].data
	for node in nArr[1:]:
		overlap = overlapMax(res,node.data)
		res +=  node.data[overlap:] 
		#print(node.data)
	return res;

#other overlap function
#https://stackoverflow.com/questions/47333771/how-can-i-merge-overlapping-strings-in-python
def overlapMax(a, b):
	values = (i for i in range(len(b)) if b[i-1] == a[-1] and a.endswith(b[:i]))
	return max(values,default = 0)

    
