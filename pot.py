class Pot:
	def __init__(self, sweet=0):
		self.value = sweet
	def add(self, amount):
		self.value += amount
	def remove(self, amount):
		self.value -= amount
		return amount		
