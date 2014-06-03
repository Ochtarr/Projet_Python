#!/usr/bin/python
# -*- coding : utf-8 -*-

from Player import *
from Card import *
from Deck import *

if __name__ == '__main__' :
	deck_j1 = Deck()
	deck_j1.loadCardListSet("deck_j1.txt")
	j1 = Player(deck_j1)
	j1.deploy()