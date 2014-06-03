from Deck import *

class Player:

	def __init__(self, deck):
		self.health = 30
		self.mana = 1
		self.hand = deck
		self.field = []

	def pickUp(self, cardList):
		i = random.randint(0,len(cardList))
		return cardList[i]

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

	def setDeck(self, deck):
		self.hand = deck

	def deploy(self):
		print("Vous avez "+str(self.mana)+" points de mana.")
		for card in self.hand.CardList:
			print(card.name)
		print("Quelle carte voulez-vous jouez ? (Nom de carte)")
		reponseUtilisateur = input()
		for card in self.hand.CardList:
			if card.name == reponseUtilisateur:
				print("Vous jouez "+ card.name)







	
