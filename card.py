class Suit:
	"""
	Suits right now are little better than a wrapper for
	a list/dict that maps to the string. I dont know what
	else they could be at the moment...
	"""
	def __init__(self, suitNum):
		"""
		init with a suit Number, 0 to 5.
		0 -> Face cards, no particular suit
		1 -> Coins
		2 -> Flasks
		3 -> Sabres
		4 -> Staves
		These are used in the Cards object
		"""
		self.suitDict = { 
					0:"Face",
					1:"Coins",
					2:"Flasks",
					3:"Sabres",
					4:"Staves"}
		if (suitNum >= 5) or (suitNum < 0):
			raise Exception ("suitNum must be between 0 and 5!")
		else:
			self.suitCode = suitNum
	def __repr__(self):
		return self.suitDict[self.suitCode]

class Card:
	"""
	Cards are the atom of the game.
	"""
	def __init__(self, value, suit=0, name=""):
		if abs(value) < 23:
			self.cardValue = value
		else:
			raise Exception("Provide a valid value for this card!")
		self.cardSuit = getSuit(suit)
	def getSuit(suitNum):
		if (suitNum >= 0 and suitNum <= 5):
			return theSuit = suit(suitNum)
		else:
			raise Exception("Suit must be between 0 and 5!") 
