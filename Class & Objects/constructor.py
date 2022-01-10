class Addition:
	first = 0
	second = 0
	answer = 0

	def __init__(self, f, s):
		self.first = f
		self.second = s

	def display(self):
		print(f"First number = {self.first}")
		print(f"Second number = {self.second}")
		print(f"Addition of two numbers = {self.answer}")

	def calculate(self):
		self.answer = self.first + self.second
 
obj = Addition(950, 2999)
obj.calculate()
obj.display()