from enum import Enum

class Attribute:
    def __init__(self, name, abbreviation, points):
        self.name = name
        self.abbreviation = abbreviation
        self.points = points

    def add_points(self, points):
        self.points += points

    def subtract_points(self, points):
        self.points -= points

    def set_points(self, points):
        self.points = points


STRENGTH = Attribute('strength', 'STR', 1)
DEXTERITY = Attribute('dexterity', 'DEX', 1)
AGILITY = Attribute('agility', 'AGI', 1)
INTELLECT = Attribute('intellect', 'INT', 1)
SPIRIT = Attribute('spirit', 'SPT', 1)
