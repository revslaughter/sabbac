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
		"""Gives total value of all cards in the hand"""
		runningTotal = 0
		for playingCard in self.handCards:
			runningTotal += playingCard.cardValue
		self.score = runningTotal
	def cardGet(self, incomingCard, desiredIndex = -1):
		"""Recieves a card and adds it to the hand"""
		self.handCards.insert(desiredIndex, incomingCard)
	def cardGive(self, cardIndex):
		"""Returns and removes a card from the hand"""
		return self.handCards.pop(cardIndex)	

