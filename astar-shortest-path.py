from colorama import Fore,Back,Style,init
init(autoreset=True)
import copy
from copy import deepcopy

class City_Distance():
	class Graph:
		def __init__(self, graph_dict=None, directed=True):
			self.graph_dict = graph_dict or {}
			self.directed = directed
			if not directed:
				self.make_undirected()
		# Create An Undirected Graph By Adding Symmetric Edges
		def make_undirected(self):
			for a in list(self.graph_dict.keys()):
				for (b, dist) in self.graph_dict[a].items():
					self.graph_dict.setdefault(b, {})[a] = dist
		# Add a link from A and B of given distance, and also add the inverse link if the graph is undirected
		def connect(self, A, B, distance=1):
			self.graph_dict.setdefault(A, {})[B] = distance
			if not self.directed:
				self.graph_dict.setdefault(B, {})[A] = distance
		# Get Neighbors Or A Neighbor
		def get(self, a, b=None):
			links = self.graph_dict.setdefault(a, {})
			if b is None:
				return links
			else:
				return links.get(b)
		# Return A List Of Nodes In The Graph
		def nodes(self):
			s1 = set([k for k in self.graph_dict.keys()])
			s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
			nodes = s1.union(s2)
			return list(nodes)
		def display_graph(self):
			print(Fore.YELLOW+"\n\t\t\tTHE GRAPH IS - \n")
			for key in self.graph_dict:
				print(Fore.CYAN+key, Fore.WHITE+' -> ', self.graph_dict[key])
# This class represent a node
	class Node:
	# Initialize the class
		def __init__(self, name: str, parent: str):
			self.name = name
			self.parent = parent
			self.g = 0 # Distance to start node
			self.h = 0 # Distance to goal node
			self.f = 0 # Total cost
		# Compare nodes
		def __eq__(self, other):
			return self.name == other.name
		# Sort nodes
		def __lt__(self, other):
			return self.f < other.f
		# Print node
		def __repr__(self):
			return ('({0},{1})'.format(self.position, self.f))
# Best-first search
	def best_first_search(self, graph, heuristics, start, end):
	# Create lists for open nodes and closed nodes
		open = []
		closed = []
		# Create a start node and an goal node
		start_node = self.Node(start, None)
		goal_node = self.Node(end, None)
		# Add the start node
		open.append(start_node)
		# Loop until the open list is empty
		while len(open) > 0:
			print(Fore.BLUE+"\n\nOpen List - ")
			for i in open:
				print(i.name, end=" | ")
			print()
			print(Fore.BLUE+"Closed List - ")
			for i in closed:
				print(i.name, end=" | ")
			# Sort the open list to get the node with the lowest cost first
			open.sort()
			# Get the node with the lowest cost
			current_node = open.pop(0)
			# Add the current node to the closed list
			closed.append(current_node)
			# Check if we have reached the goal, return the path
			if current_node == goal_node:
				path = []
				while current_node != start_node:
					path.append(current_node.name)
					current_node = current_node.parent
				path.append(start_node.name)
		# Return reversed path
				return path[::-1]
		# Get neighbours
			neighbors = graph.get(current_node.name)
		# Loop neighbors
			for key, value in neighbors.items():
		# Create a neighbor node
				neighbor = self.Node(key, current_node)
		# Check if the neighbor is in the closed list
				if (neighbor in closed):
					continue
		# Calculate cost to goal
				neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
				neighbor.h = heuristics.get(neighbor.name)
				neighbor.f = neighbor.g + neighbor.h
		# Check if neighbor is in open list and if it has a lower f value
				if (self.add_to_open(open, neighbor) == True):
				# Everything is green, add neighbor to open list
					open.append(neighbor)
		# Return None, no path is found
		return None
	# Check If A Neighbor Should Be Added To Open List
	def add_to_open(self, open, neighbor):
		for node in open:
			if (neighbor == node and neighbor.f >= node.f):
				return False
		return True
	def start(self):
	# Create a graph
		graph = self.Graph()
		# Create graph connections (Actual distance)
		graph.connect('Oradea', 'Zerind', 71)
		graph.connect('Oradea', 'Sibiu', 151)
		graph.connect('Zerind', 'Arad', 75)
		graph.connect('Arad', 'Sibiu', 140)
		graph.connect('Arad', 'Timisoara', 118)
		graph.connect('Timisoara', 'Lugoj', 111)
		graph.connect('Lugoj', 'Mehadia', 70)
		graph.connect('Mehadia', 'Drobeta', 75)
		graph.connect('Drobeta', 'Craiova', 120)
		graph.connect('Craiova', 'Pitesti', 138)
		graph.connect('Craiova', 'Rimnicu Vilcea', 146)
		graph.connect('Sibiu', 'Fagaras', 99)
		graph.connect('Fagaras', 'Bucharest', 211)
		graph.connect('Sibiu', 'Rimnicu Vilcea', 80)
		graph.connect('Rimnicu Vilcea', 'Pitesti', 97)
		graph.connect('Pitesti', 'Bucharest', 101)
		graph.connect('Bucharest', 'Giurgui', 90)
		# Make graph undirected, create symmetric connections
		graph.make_undirected()
		graph.display_graph()
		# Create heuristics (straight-line distance, air-travel distance)
		heuristics = {}
		heuristics['Arad'] = 366
		heuristics['Bucharest'] = 0
		heuristics['Craiova'] = 160
		heuristics['Drobeta'] = 242
		heuristics['Fagaras'] = 176
		heuristics['Guirgiu'] = 77
		heuristics['Lugoj'] = 244
		heuristics['Mehadia'] = 241
		heuristics['Oradea'] = 380
		heuristics['Pitesti'] = 100
		heuristics['Rimnicu Vilcea'] = 193
		heuristics['Sibiu'] = 253
		heuristics['Timisoara'] = 329
		heuristics['Zerind'] = 800
	# Run search algorithm
		path = self.best_first_search(graph, heuristics, 'Arad', 'Bucharest')
		print(Fore.GREEN+"\n\nThe Path Is - ")
		if path is not None:
			for i in range(len(path)):
				print(path[i])

print(Fore.BLUE+"\t\t\t\t\t\tA* Algorithm - City Distance Problem\n")

temp = City_Distance()
temp.start()