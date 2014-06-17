class Card:

	def __init__(self, name, health, attack, cost):
		self.name = name
		self.health = health
		self.attack = attack
		self.cost = cost

	def __copy__(self, Card):
		self.name = Card.name
		self.health = Card.health
		self.attack = Card.attack
		self.cost = Card.cost

	def card_print(self, displayMana):
		if displayMana == True:
			print(self.name+" ("+self.attack+"/"+self.health+") : "+self.cost)
		else:
			print(self.name+" ("+self.attack+"/"+self.health+")")

	def fight(self, ennemy):
		#Attaque de la carte
		ennemy.health = ennemy.health - self.attack
		#Défense de la carte
		self.health = self.health = ennemy.attack

	def isAlive(self):
		if self.health > 0:
			return True
		else:
			return False

	# def loadCardSet(nomFichier):
	# 	fichier = open(nomFichier,'r')
	# 	for line in fichier:
	# 		tmpTabLine = line.split(";")
	# 		for i in len(tmpTabLine):
	# 			if( isinstance(tmpTabLine, str) ):
	# 				tmpTabLine[i] = tmpTabLine[i].replace("\n","")
	# 				print(tmpTabLine[i])
	# 		c = Card(tmpTabLine[0],int(tmpTabLine[1]),int(tmpTabLine[2]),int(tmpTabLine[3]))
	# 		listServiteur.append(c)
	# 	return listServiteur

	#c = Card(tabDonneesServiteur[0],int(tabDonneesServiteur[1]),int(tabDonneesServiteur[2]),int(tabDonneesServiteur[3])
	#listServiteur.append(c)
