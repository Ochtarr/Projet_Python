class Card:

	def __init__(name, health, attack, cost):
		self.name = name
		self.health = health
		self.attack = attack
		self.cost = cost

	def card_print(self, displayMana):
		if displayMana == True:
			print(self.name+" ("+self.attack+"/"+self.health+") : "+self.cost)
		else:
			print(self.name+" ("+self.attack+"/"+self.health+")")

	def fight(self, Card ennemy):
		#Attaque de la carte
		ennemy.health = ennemy.health - self.attack
		#Défense de la carte
		self.health = self.health = ennemy.attack

	def isAlive(self):
		if self.health > 0:
			return True
		else
			return False

	def loadCardSet(nomFichier):
		fichier = open(nomFichier, "r")
		for line in fichier:
			tabDonneesServiteur = line.split()
			c = Card(tabDonneesServiteur[0],int(tabDonneesServiteur[1]),int(tabDonneesServiteur[2]),int(tabDonneesServiteur[3])
			listServiteur.append(c)
