from colorama import Fore,Back,Style,init
init(autoreset=True)
import copy
from copy import deepcopy

class Puzzle():
	
	goal = [[1, 2, 3],
	[8, 0, 4],
	[7, 6, 5]]
	
	board_config = [[2, 3, 4],
	[1, 8, 0],
	[7, 6, 5]]
	
	steps = 0
	# Heuristic Value Of Tiles In Place
	def calculate_fOfn(self, cal_config):
	# In BFS f(n) = g(n) + h(n)
	# h(n) = Number Of Misplaced Tiles
	# g(n) = Number Of Steps
		h = 0
		for i in range(0, 3):
			for j in range(0, 3):
				if cal_config[i][j] != self.goal[i][j]:
					h += 1
		return h
	def isSafe(self, x, y):
		return x >= 0 and x < 3 and y >= 0 and y < 3
	def print_board(self, print_config):
		for i in range(0, 3):
			for j in range(0, 3):
				print(" " + str(print_config[i][j]) + " ", end="")
			print()
	# Function To Find All Possible Board Configurations From Given Configurations
	def find_all_configs(self, all_config):
		config_boards = []
		config1 = deepcopy(all_config)
		config2 = deepcopy(all_config)
		config3 = deepcopy(all_config)
		config4 = deepcopy(all_config)
		for i in range(0, 3):
			for j in range(0, 3):
				if all_config[i][j] != 0:
	# Check If We Can Move To The Top
					if self.isSafe(i - 1, j):
						if all_config[i - 1][j] == 0:
	# Move Tile
							config1[i - 1][j] = config1[i][j]
							config1[i][j] = 0
							config_boards.append(config1)
	# Check If We Can Move To The Bottom
					if self.isSafe(i + 1, j):
						if all_config[i + 1][j] == 0:
	# Move Tile
							config2[i + 1][j] = config2[i][j]
							config2[i][j] = 0
							config_boards.append(config2)
	# Check If We Can Move To The Right
					if self.isSafe(i, j + 1):
						if all_config[i][j + 1] == 0:
							config3[i][j + 1] = config3[i][j]
							config3[i][j] = 0
							config_boards.append(config3)
	# Check If We Can Move To The Left
					if self.isSafe(i, j - 1):
						if all_config[i][j - 1] == 0:
							config4[i][j - 1] = config4[i][j]
							config4[i][j] = 0
							config_boards.append(config4)
		return config_boards
	# Hill Climbing Algorithm Function
	def puzzle_start(self, config, goal_heuristic):
		objective_values = []
		new_config = deepcopy(config)
		boards_configs = []
		open_list = []
		closed_list = []
		visited = []
		open_list.append(new_config)
		visited.append(new_config)
		print(Fore.RED+"\t\t\tLIST IS DISPLAYED IN ROW MAJOR ORDER\n\n")
		print("Initially - ")
		# Print Open List
		print("Open List - ")
		print(open_list)
		# Print Closed List
		print("Closed List - ")
		print(closed_list)
		print("\n\n")
		while True:
			self.steps += 1
			boards_configs.clear()
			open_list.remove(new_config)
			closed_list.append(new_config)
			# Calculate Heuristic Value Of New Board Configurations
			heuristic_value = self.calculate_fOfn(new_config)
			if heuristic_value == goal_heuristic:
				print("Solution Reached !!")
				print(f"\nIn {self.steps} Steps\n")
				break
			boards_configs = self.find_all_configs(new_config)
	# Calculating Heuristic Values For All Child Configurations
			for i in boards_configs:
				visited.append(i)
				open_list.append(i)
				h = self.calculate_fOfn(i)
				objective_values.append(h)
			print("Open List - ")
			print(open_list)
			print("Closed List - ")
			print(closed_list)
			print("\n\n")
	# Selecting Minimum Heuristic Value From Child Nodes
			min_value = min(objective_values)
			min_value_index = objective_values.index(min_value)
			new_config = boards_configs[min_value_index]
			print(f"Board Configuration Selected With Heuristic Value - {str(self.steps)} + {str(min_value)}")
			self.print_board(new_config)
			print("\n")
			objective_values.clear()
	def Start_Puzzle(self):
		print("8-Puzzle Problem Using Best First Search\n")
		goal_heuristic = self.calculate_fOfn(self.goal)
		self.puzzle_start(self.board_config, goal_heuristic)	



print(Fore.BLUE+"\t\t\t\t\t\tA* Algorithm - 8 Puzzle Problem\n")
temp = Puzzle()
temp.Start_Puzzle()
