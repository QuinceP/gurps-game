class Profession:
    def __init__(self, name, starting_gear, abilities, weapon_types):
        self.name = name
        self.starting_gear = starting_gear
        self.abilities = abilities
        self.weapon_types = weapon_types


class ProfessionalModifier:
    def __init__(self, profession, value):
        self.profession = profession
        self.value = value


BARBARIAN = Profession('barbarian', [], [], [])
FIGHTER = Profession('fighter', [], [], [])
PRIEST = Profession('priest', [], [], [])
RANGER = Profession('ranger', [], [], [])
THIEF = Profession('thief', [], [], [])
WIZARD = Profession('wizard', [], [], [])
MONK = Profession('monk', [], [], [])
AMAZON = Profession('priest', [], [], [])
