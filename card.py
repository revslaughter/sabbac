class Suit:
	"""
	Suits right now are little better than a wrapper for
	a list/dict that maps to the string. I dont know what
	else they could be at the moment...
	"""
	def __init__(self, suitChar):
		"""
		init with a suit Char, 0 to 5.
		"0" -> Face cards, no particular suit
		"c" -> Coins
		"f" -> Flasks
		"b" -> Sabres
		"t" -> Staves
		These are used in the Cards object
		"""
		self.suitDict = { 
					"0":"Face",
					"c":"Coins",
					"f":"Flasks",
					"b":"Sabres",
					"t":"Staves"}
		if suitChar not in {"0", "c", "f", "b", "t"}: 
			raise Exception ("Invalid Suit char! See help for details.")
		else:
			self.suitCode = suitChar
	def __repr__(self):
		return self.suitDict[self.suitCode]

class Card:
	"""
	Cards are the atom of the game.
	They will be the body from which decks and hands are built.
	"""
	def __init__(self, value, cardSuit=0, name=""):
		if abs(value) < 23:
			self.cardValue = value
		else:
			raise Exception("Provide a valid value for this card!")
		self.cardSuit = Suit(cardSuit) 
