from card import Suit, Card

def cardTry(val, su="0", name=""):
	try:
		aCard = Card(val, su, name)
		return True
	except:
		return False 

print("Value 1 and suit t")
print(cardTry(1, "t"))
print("Value -1 and suit t")
print(cardTry(-1, "t"))
print("Value 100 and suit t")
print(cardTry(100, "a"))
print("Value 5 and suit c, Name")
print(cardTry(5, "c", "Name"))
print("Value 4 and suit U")
print(cardTry(4, "U"))
