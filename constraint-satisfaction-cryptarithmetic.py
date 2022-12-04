from colorama import Fore, Back, Style, init
init(strip=False)
init(autoreset=True)

class cryptarithmetic():
	solved = False
	count = 0
	def start(self):
		word1 = input("Enter First Word - ").upper()
		word2 = input("Enter Second Word - ").upper()
		result = input("Enter Result - ").upper()
		values = []
		visited = [False for x in range(10)]
		equation = [word1, word2, result]
		# Get Unique Words
		set = []
		for c in word1:
			if c not in set:
				set.append(c)
		for c in word2:
			if c not in set:
				set.append(c)
		for c in result:
			if c not in set:
				set.append(c)
		if len(set) > 10:
			print("\nNo Solution (as values will repeat)\n")
			exit()
		print("Solution Is - ")
		print(f" \t{word1}\n+\t{word2}\n-------------\n\t{result}\n\n")
		self.solve(set, values, visited, equation)
	def solve(self, letters, values, visited, equation):
		if len(letters) == len(values):
			map = {}
			for letter, val in zip(letters, values):
				map[letter] = val
			if map[equation[0][0]] == 0 or map[equation[1][0]] == 0 or map[equation[2][0]] == 0:
				return
			word1, word2, res = "", "", ""
			for c in equation[0]:
				word1 += str(map[c])
			for c in equation[1]:
				word2 += str(map[c])
			for c in equation[2]:
				res += str(map[c])
			if int(word1) + int(word2) == int(res):
				self.count += 1
				print(Fore.GREEN+f"Result {self.count} = {word1} + {word2} = {res}\n")
				solved = True
			return
		for i in range(10):
			if not visited[i]:
				visited[i] = True
				values.append(i)
				self.solve(letters, values, visited, equation)
				values.pop()
				visited[i] = False

print(Fore.GREEN+"\t\t\t\tConstraint Satisfaction - CryptArithmetic")

temp = cryptarithmetic()
temp.start()

