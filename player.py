from pot import Pot
from card import Card, Suit
from hands import Hand

class Player:
	"""
	Players are objects that play Sabbacc
	"""
	def __init__(self, playerName="", startAmt=0, startHand=Hand()):
		self.gold = Pot(startAmt)
		self.name = playerName
		self.hand = startHand
	def bet(amount, betCondition):
		if betCondition:
			bufferVal = self.gold.remove(amount)
			return bufferVal
	
