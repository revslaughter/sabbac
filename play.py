from player import Player
from card import Card, Suit
from deck import Deck
from hands import Hand
from pot import Pot
import random

def getPlayerList():
	areYouDone = False
	listToReturn = []
	while not areYouDone:
		thisPlayerName = input("Player Name? ")
		thisPlayerHand = Hand()
		listToReturn.append(Player(thisPlayerName, 20, thisPlayerHand))
		answer = input("Done Adding Players? (y/n)")
		if answer == "y":
			areYouDone = True
		elif answer == "n":
			pass
		else:
			print("Don't understand, assuming you're done...")
			areYouDone = True
	return listToReturn

def dealCards(players, deckOfCards):
	for p in players:
		p.hand.cardGet(deckOfCards.draw())
		p.hand.cardGet(deckOfCards.draw())
		
def bettingPhase(player):
	pass

def callingPhase(player):
	pass

def shiftingPhase(hand, deck):
	cardsToTake = random.randint(0, len(hand.handCards))
	for i in range(cardsToTake):
		goAway = hand.handCards.pop(i)
		hand.cardGet(deck.draw())

def drawingPhase(player):
	pass

def showPlayers(playerList):
	for person in playerList:
		print(person.name + ":")
		for c in person.hand.handCards:
			print("    {0}: {1}".format(c, c.cardValue))
		print("    Score:{0}".format(person.hand.score))
		print("    Pot Amount: {0}".format(person.gold.value))

if (__name__=="__main__"):
	gameOver = False
	playerList = getPlayerList()
	roundPot = Pot()
	sabbacPot = Pot()
	gameDeck = Deck()
	
	dealCards(playerList, gameDeck)

	while not gameOver:
		print("\n".join([repr(p) for p in playerList]))
		gameOver = True #Testing Testing...
