class Player:

	def __init__(self, deck):
		self.health = 30
		self.mana = 1
		self.hand = deck
		self.field = []

	def pickUp(self, cardList):
		i = random.randint(0,len(cardList))
		return cardList[i]

	def deploy(self):


	def clean(self):
		for i in len(self.hand):
			if self.hand[i].health <= 0:
				del(self.hand[i])

	def isAlive(self):
		if self.health > 0:
			return True
		else:
			return False

	def setMana(self, mana):
		if mana>0:
			self.mana = mana

	def playTurn(j1, j2):







	
