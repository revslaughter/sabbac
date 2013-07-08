class Pot:
    """
    A pot just holds a number, the value of the pot.
    The pot can be sweetened with a beginning value.
    The pot.add(amount) method adds a non-negative amount to the pot.
    The pot.remove(amount) method removes a non-negative amount, if available in the pot, and returns the amount desired.
    This class can be extended for different kinds of pots: Round pots, player pots, and sabbac pots.
    """
    def __init__(self, sweet=0):
        self.value = sweet
    def add(self, amount):
        if (amount < 0):
            raise Exception("Cannot add negative values to the pot!")
        else:
            self.value += amount
    def remove(self, amount):
        """Removes and returns the input value, if available"""
        if (amount < 0):
            raise ValueError("Cannot remove negative values from the pot!")
        elif ((self.value - amount) < 0):
            raise ValueError("Cannot take more than what is in the pot, the pot currently has {0}.".format(self.value))
        else:
            self.value -= amount
            return amount		
