class suit():
	def __init__(self, suitNum):
		self.suitDict = { 
					0:"Face",
					1:"Coins",
					2:"Flasks",
					3:"Sabres",
					4:"Staves"}
	def __repr__(self):

class card():
	"""
	Cards are the atom of the game.
	"""
	def __init__(self, value, suit):
		if abs(value) < 23:
			self.cardValue = value
		self.cardSuit = getSuit(suit)
	def getSuit(suitNum):
		if (suitNum >= 0 and suitNum <= 5):
			return theSuit = suit(suitNum)
		else:
			#throw error
