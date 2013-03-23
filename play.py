from player import Player
from card import Card, Suit
from deck import Deck
from hands import Hand
from pot import Pot

def getPlayerList():
	areYouDone = False
	listToReturn = []
	while not areYouDone:
		thisPlayerName = input("Player Name? ")
		listToReturn.append(Player(thisPlayerName, 20))
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
		
if (__name__=="__main__"):
	gameOver = False
	playerList = getPlayerList()
	roundPot = Pot()
	sabbacPot = Pot()
	gameDeck = Deck()
	
	dealCards(playerList, gameDeck)

	while not gameOver:
		for person in playerList:
			print(person.name + ":")
			print(person.hand.score)
		gameOver = True #Testing Testing...
			
		
