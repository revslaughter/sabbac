from deck import Deck
from card import Card, Suit

class Hand:
	"""
	A hand is a list of sabbac cards that can be evaluated.
	"""
	def __init__(self):
		"""
		Hands init to an empty list.
		Through the other methods, cards can be added or shifted
		and hands can be evaluated.
		"""
		self.handCards = []
		self.score = 0
	def updateScore(self):
		runningTotal = 0
		for playingCard in self.handCards:
			runningTotal += playingCard.cardValue
		self.score = runningTotal
	def cardGet(self, incomingCard, desiredIndex = -1):
		self.handCards.insert(desiredIndex, incomingCard)
	def cardGive(self, cardIndex):
		return self.handCards.pop(cardIndex)	

