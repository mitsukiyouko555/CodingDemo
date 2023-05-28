#!/usr/bin/python

from characters import Characters, List

from manacost import *

index = 1
for Characters in List.CharacterList:
	print(index,"-","{}".format(Characters.name))
	index+=1

pickaCharacter = input("\nSelect a character:\n\n")

selectedCharacter = List.CharacterList[int(pickaCharacter)-1]

print("\n")
print("{}".format(selectedCharacter.name),"'s Stats:\n\n",selectedCharacter,"\n", sep='')

index = 1

for i in Spells.listOfSpells:

	print(index,"-",i.spellName,"-",i.spellAttribute)
	index+=1


selectASpell = input("Select a Spell:\n\n")

selectedSpell = Spells.listOfSpells[int(selectASpell)-1]

# I could use a class for this but its so trivial and i proved i know how to use inheritence, abstraction, and polymorphism so im using def for this one :)
def PowerOutput():
	manaOutput = selectedSpell.baseManaCost * selectedCharacter.L_level

	if selectedSpell.spellAttribute == selectedCharacter.overall_Element:
		Output = manaOutput + (manaOutput*0.25) 

	elif selectedSpell.spellAttribute ==  selectedCharacter.secondAttribute:
		Output = (manaOutput * 0.05) + manaOutput

	elif selectedSpell.spellAttribute == selectedCharacter.thirdAttribute:
		Output = (manaOutput * 0.05) + manaOutput

	elif selectedSpell.spellAttribute == selectedCharacter.oppositeAttribute:
		Output = manaOutput

# boost should be (mana cost + the boost if any TIMES the character level)

	print("Power Output:", Output)

def PowerOutput_BaseMana():
	Output = selectedSpell.baseManaCost * selectedCharacter.L_level
	print("Power Output:", Output)


if "Weapons Only User" not in selectedCharacter.overall_Element:

	if selectedSpell.isAbstractSpell == False:

		if selectedSpell.spellAttribute == selectedCharacter.overall_Element:
			manaCostforSpell = selectedSpell.baseManaCost * 0.05
			selectedCharacter.mana = selectedCharacter.mana - manaCostforSpell 

		elif selectedSpell.spellAttribute ==  selectedCharacter.secondAttribute:
			manaCostforSpell = selectedSpell.baseManaCost + (selectedSpell.baseManaCost * 0.10)
			selectedCharacter.mana = selectedCharacter.mana - manaCostforSpell

		elif selectedSpell.spellAttribute == selectedCharacter.thirdAttribute:
			manaCostforSpell = selectedSpell.baseManaCost + (selectedSpell.baseManaCost * 0.15)
			selectedCharacter.mana = selectedCharacter.mana - manaCostforSpell

		elif selectedSpell.spellAttribute == selectedCharacter.oppositeAttribute:
			manaCostforSpell = selectedSpell.baseManaCost + (selectedSpell.baseManaCost * 0.50)
			selectedCharacter.mana = selectedCharacter.mana - manaCostforSpell

	if selectedSpell.isAbstractSpell == True:
		selectedCharacter.mana = selectedCharacter.mana - selectedSpell.baseManaCost



if "Weapons Only User" in selectedCharacter.overall_Element:

	selectedCharacter.mana = selectedCharacter.mana - selectedSpell.baseManaCost

print(selectedCharacter.name,"has",selectedCharacter.mana, "Mana left.")

if "Weapons Only User" not in selectedCharacter.overall_Element and selectedSpell.isAbstractSpell == False:
	PowerOutput()

if "Weapons Only User" in selectedCharacter.overall_Element or "Weapons Only User" not in selectedCharacter.overall_Element and selectedSpell.isAbstractSpell == True:

	PowerOutput_BaseMana()

