from card import Card, Suit

class Deck:
	def __init__(self):
		"""
		Initializes a sabbac deck with all the cards in the deck
		"""
		self.sabbacDeck = set() #initializes empty set
		for suit in ["c", "f", "b", "t"]: #each suit, no face cards
			for value in range(1,12):#add the normal cards. note that range(1,12) goes only up to 11
				self.sabbacDeck.add(Card(value, suit))
			
			#using a dictionary here is easier than using a list
			dicCommonFaces = {12:"Commander",
							  13:"Mistress",
							  14:"Master",
							  15:"Ace"}
			
			for value in range(12,16): #add the minor face cards
				self.sabbacDeck.add(Card(value,suit,dicCommonFaces[value]))
		self.putTheFaceCards()
		self.putTheFaceCards()
		#This happens twice so that there are 2 copies of each face card

	def putTheFaceCards(self):
		self.sabbacDeck.add(Card(-2, "0", "Queen of Air and Darkness"))
		self.sabbacDeck.add(Card(-8, "0", "Endurance"))
		self.sabbacDeck.add(Card(-11, "0", "Balance"))
		self.sabbacDeck.add(Card(-13, "0", "Demise"))
		self.sabbacDeck.add(Card(-14, "0", "Moderation"))
		self.sabbacDeck.add(Card(-15, "0", "The Evil One"))
		self.sabbacDeck.add(Card(-17, "0", "The Star"))
		self.sabbacDeck.add(Card(0, "0", "The Idiot"))

	def draw(self):
		"""
		Since the sabbacDeck object is a set, the pop method
		will return a random card. This just wraps that.
		"""
		return self.sabbacDeck.pop()
	def cardPut(self, returningCard):
	 	"""
		Places a card into the deck
	 	"""
	 	self.sabbacDeck.add(returningCard)
