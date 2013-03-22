from pot import Pot
from card import Card, Suit
from hands import Hand

class Player:
	"""
	Players are objects that play Sabbacc
	"""
	def __init__(self, startAmt=0, playerName="", startHand):
		self.gold = Pot(startAmt)
		self.name = playerName
		self.hand = startHand
	def bet(amount, betCondition):
		bufferVal = self.gold.remove(amount)
		return bufferVal
	
