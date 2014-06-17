from Card import *
#on pourrait rajouter des propriétés sur un deck pour faire des decks spéciaux à voir ...

class Deck:

	def __init__(self):
		self.CardList = []

	def deck_print(self):
		for element in self.CardList:
			print(self.CardList[i])

	def loadCardListSet(self, nomFichier):
		fichier = open(nomFichier,'r')
		for line in fichier:
			tmpTabLine = line.split(";")
			del tmpTabLine[1]
			for element in tmpTabLine:
				tmpTabElement = element.split(",")
				c = Card(tmpTabElement[0],int(tmpTabElement[1]),int(tmpTabElement[2]),int(tmpTabElement[3]))
				self.CardList.append(c)

	def getPositionOfACard(self, nomCarte):
		for element in self.CardList:
			if element.name == nomCarte:
				return element
		print("Impossible de trouver la carte dans le deck")

