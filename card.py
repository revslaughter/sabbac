class card():
	'''
	Cards are the atom of the game.
	'''
	def __init__(self, value, suit):
		self.cardValue = value
		self.cardSuit = getSuit(suit)
		
