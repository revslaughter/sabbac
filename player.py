from pot import Pot
from card import Card, Suit
from hands import Hand

class Player:
    """
    Players are objects that play Sabbacc
    """
    def __init__(self, playerName="", startAmt=0):
        self.gold = Pot(startAmt)
        self.name = playerName
    def bet(amount, betCondition):
        if betCondition:
            bufferVal = self.gold.remove(amount)
            return bufferVal
    def newHand(self, startHand):
        self.hand = startHand
    def __repr__(self):
        return (self.name + ":" + "\n"
                 + "\n".join(["    {0}: {1}".format(c, c.cardValue) for c in self.hand.handCards])
                 + "\n    Score:{0}".format(self.hand.score)
                 + "\n    Your Gold:{0}".format(self.gold.value))
