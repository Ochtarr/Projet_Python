from Deck import *

class Player:

	def __init__(self, deck):
		"""
		Constructor
		parameters : Array of Card (deck's player)
		"""
		self.health = 30
		self.mana = 5
		self.hand = deck
		self.field = []

	def pickUp(self):
		"""
		To pick up a random card of hand's player
		No parameters
		Returns Card
		"""
		i = random.randint(0,len(self.hand))
		return self.hand[i]

	def clean(self):
		"""
		To clean hand's player
		No parameters
		No return
		"""
		for i in len(self.hand):
			if self.hand[i].health <= 0:
				del(self.hand[i])

	def isAlive(self):
		"""
		To know if the player is still alive
		No parameters
		Returns boolean
		"""
		if self.health > 0:
			return True
		else:
			return False

	def setMana(self, mana):
		"""
		To set Mana of the specified Player
		parameters : Mana
		No return
		"""
		if mana>0:
			self.mana = mana

	def setDeck(self, deck):
		self.hand = deck

	def deploy(self):
		"""
		Deploy a card on the game's field
		No parameters (except self)
		No return
		"""
		print("Vous avez "+str(self.mana)+" points de mana.")
		for card in self.hand.CardList:
			print(card.name+"     /"+str(card.attack)+"/"+str(card.health)+"/"+str(card.cost))
		print("Quelle carte voulez-vous jouez ? (Nom de carte)")
		carteJouee = False
		while carteJouee != True:
			reponseUtilisateur = input()
			for card in self.hand.CardList:
				if card.name == reponseUtilisateur and self.mana-card.cost>=0:
					#Actions : mettre la carte sur le plateau du jeu / enlever la carte de la main
					carteTemp = Card(card.name,card.health,card.attack,card.cost)
					self.field.append(carteTemp)
					del self.hand.CardList[self.hand.getPositionOfACard(card.name)]
					print("Vous jouez "+ card.name)
					carteJouee = True
				elif self.mana-card.cost<0:
					print("Nécessite " + str(-(self.mana-card.cost)) + " points de mana")
					print("Choisissez une autre carte")
					break
				else:
					print("La carte n'existe pas")
					print("Choisissez une autre carte")
					break

	def clean(self):
		"""
		Function which remove died cards.
		No parameters (except self)
		No return
		"""
		for card in self.hand:
			if card.health <=0 :
				del self.hand[card]
				print("La carte"+card.name+" a ete supprimee")

	def handCardSelect(self):
		"""
		Interactive function which allows user to choose a card from his deck
		No parameters (except self)
		Returns a Card
		"""

	}










	
