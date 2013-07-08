from player import Player
from card import Card, Suit
from deck import Deck
from hands import Hand
from pot import Pot
import random

gameDeck = Deck()
roundPot = Pot()
sabbacPot = Pot()

def getPlayerList():
    areYouDone = False
    listToReturn = []
    firsPlayerName = input("Player Name? ")
    listToReturn.append(Player(firsPlayerName, 20))
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
        thisHand = Hand()
        thisHand.cardGet(deckOfCards.draw())
        thisHand.cardGet(deckOfCards.draw())
        p.newHand(thisHand)

def bettingPhase(player, roundPlaying):
    keepGoing = True
    while keepGoing:
        playerBet = int(input("What is your bet? Enter 0 to check. "))
        try:
            roundPot.add(player.gold.remove(playerBet))
            keepGoing = False
        except ValueError:
            print("You can't do that! Try again.\n")
    otherPlayers = roundPlaying.copy() #If we remove player from allPlayers, source list is altered
    otherPlayers.remove(player)
    for other in otherPlayers:
        print(other)
        decision = input("{0}, do you [s]ee or [f]old? ".format(other.name))
        if decision == "s":
            try:
                roundPot.add(other.gold.remove(playerBet))
            except ValueError:
                print("You're no good for it!\n")
                decision = "f"
        if decision == "f":
            print("You fold.")
            roundPlaying.remove(other)
        if (decision != "f" and decision != "s"):
            print("I don't understand, forefit your turn...")

def callingPhase(player):
    pass

def shiftingPhase(players):
    for p in players:
        thisHand = p.hand
        chance = random.randint(0,10)
        if chance == 7:
            print("A shift pulse sends out a wave of shifty energy!")
            cardsToTake = random.randint(0, len(thisHand.handCards))
            for i in range(cardsToTake):
                goAway = thisHand.handCards.pop(i)
                thisHand.cardGet(gameDeck.draw())

def drawingPhase(player):
    yesOrNo = {"y":True, "n":False}
    if yesOrNo[input("Hit? (y/n)")]:
        theCard = gameDeck.draw()
        print(theCard)
        player.hand.cardGet(theCard)
        print(player)
    else:
        pass

def showPlayers(playerList):
    for person in playerList:
        print(person)

def determineRoundWinner(players):
    inTheRunning = players[0]
    for per in players:
        if per.hand.score > inTheRunning.hand.score:
            inTheRunning = per
    return inTheRunning

def auntieUp(players):
    for p in players:
        try:
            roundPot.add(p.gold.remove(1))
            sabbacPot.add(p.gold.remove(1))
        except ValueError:
            print("{0} is no good for it!\nYou're out!\n".format(p.name)) 
            players.remove(p)

def doARound(roundPlayers):
    auntieUp(roundPlayers)
    for person in roundPlayers:
        print("{0}, your turn. Here's your stats:\n".format(person.name))
        print(person)
        drawingPhase(person)
        bettingPhase(person, roundPlayers)
        shiftingPhase(roundPlayers)
        callingPhase(person)
    showPlayers(roundPlayers)
    winner = determineRoundWinner(roundPlayers)
    winner.gold.add(roundPot.remove(roundPot.value)) #The winner takes the round Pot!
    print("{0} wins this round!\n".format(winner.name)) 

if (__name__=="__main__"):
    playerList = getPlayerList()

    dealCards(playerList, gameDeck)
    for round in range(int(input("How many Rounds? "))):
        doARound(playerList)
