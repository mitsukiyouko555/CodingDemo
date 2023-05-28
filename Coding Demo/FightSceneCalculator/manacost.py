#!/usr/bin/python

from characters import Characters

class baseManaCost:
	def __init__ (self, spellName,baseManaCost, isAbstractSpell, spellAttribute):
		self.spellName = spellName
		self.baseManaCost = baseManaCost
		self.isAbstractSpell = isAbstractSpell
		self.spellAttribute = spellAttribute
	def __str__(self):
		return f"Base Mana Cost: {self.baseManaCost}\nIs Abstract Spell?: {self.isAbstractSpell}\nSpell Attribute: {self.spellAttribute}"
	
class Spells():
	listOfSpells = []


Spells.listOfSpells.append(baseManaCost("Kalion",50, False, "Fire"))
Spells.listOfSpells.append(baseManaCost("Tazz", 200, True, "Fire"))

Spells.listOfSpells.append(baseManaCost("Barillion",50, False, "Wind"))
Spells.listOfSpells.append(baseManaCost("Warshroom",200, True, "Wind"))

Spells.listOfSpells.append(baseManaCost("Elk",50, False, "Earth"))
Spells.listOfSpells.append(baseManaCost("Vero",200, True, "Earth"))

Spells.listOfSpells.append(baseManaCost("Blort", 50, False, "Water"))
Spells.listOfSpells.append(baseManaCost("Zurk", 200, True, "Water"))


