#!/usr/bin/python

class Characters:
	def __init__(self, name, dominant_Hand, L_level, mana, overall_Element):

		self.name = name
		self.dominant_Hand = dominant_Hand
		# self.will_Power_Boost = will_Power_Boost
		self.L_level = L_level
		self.mana = mana
		self.overall_Element = overall_Element

	def __str__(self):
		return f"Name: {self.name}\nDominant Hand?: {self.dominant_Hand}\nAttribute: {self.overall_Element}\nL-Level: {self.L_level}\nMana: {self.mana}"


class CharactersWithAttributes(Characters):
	def __init__ (self, name, dominant_Hand,  L_level, mana, overall_Element,secondAttribute, thirdAttribute, oppositeAttribute):
		super().__init__(name, dominant_Hand, L_level, mana, overall_Element)
		self.secondAttribute = secondAttribute
		self.thirdAttribute = thirdAttribute
		self.oppositeAttribute = oppositeAttribute
	def UserType(self):
			return("""This character is a {} Attribute User.
If they use a {} spell, it will only cost them 5% of the spell's base mana and they will get a 25% boost in power output.
If they use a {} spell, it will cost them the Base Mana cost + an extra 10% mana drain and they will only get a 5% power output boost.
If they use a {} spell,it will cost them the Base Mana cost + an extra 15% mana drain and they will only get a 10% power output boost.
If they use a {} spell,it will cost them the Base Mana cost + an extra 50% mana drain and they will get a 0% power output boost.
If they use an Abstract Spell, it will cost them the base mana of the abstract spell only.
""").format(self.overall_Element,self.overall_Element, self.secondAttribute, self.thirdAttribute, self.oppositeAttribute)

class FireAttrCharas(CharactersWithAttributes):
	def __init__ (self, name, dominant_Hand, L_level, mana):
		super().__init__(name, dominant_Hand,L_level, mana, "Fire",  "Wind", "Earth", "Water")


class WindAttrCharas(CharactersWithAttributes):
	def __init__ (self, name, dominant_Hand, L_level, mana):
		super().__init__(name, dominant_Hand,L_level, mana, "Wind", "Earth", "Water", "Fire")


class EarthAttrCharas(CharactersWithAttributes):
	def __init__ (self, name, dominant_Hand, L_level, mana):
		super().__init__(name, dominant_Hand,L_level, mana, "Earth", "Water", "Fire",  "Wind")

	
class WaterAttrCharas(CharactersWithAttributes):
	def __init__ (self, name, dominant_Hand, L_level, mana):
		super().__init__(name, dominant_Hand,L_level, mana, "Water", "Fire",  "Wind", "Earth")


class WeaponsOnlyCharacters(CharactersWithAttributes):
	def __init__ (self, name, dominant_Hand, L_level, mana):
		super().__init__(name, dominant_Hand,L_level, mana, "Weapons Only User", "None",  "None", "None")

	def UserType(self):
		return("This character is a {}.\nAll spells cost the base mana cost with no extra mana drain or boosts for this character.").format(self.overall_Element)

class List:
	CharacterList = []


List.CharacterList.append(FireAttrCharas("Maxus", "Yes", 50, 800))
List.CharacterList.append(WindAttrCharas("Hydra", "Yes", 45, 300))
List.CharacterList.append(EarthAttrCharas("Mouse", "Yes", 23, 750))
List.CharacterList.append(WeaponsOnlyCharacters("Alis", "Yes",15, 400))
List.CharacterList.append(FireAttrCharas("Mal", "Yes", 67, 850))


for Characters in List.CharacterList:
	print(Characters,"\nOpposite Attribute: ",Characters.oppositeAttribute,"\n\n",Characters.UserType(),"\n\n", sep = "")

