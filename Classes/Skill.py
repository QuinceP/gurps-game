from abc import ABCMeta, abstractmethod
import math
from Classes import Profession
from Classes import Attribute


class Skill:
    __metaclass__ = ABCMeta

    def __init__(self, name, professional_modifiers):
        self.name = name
        self.level = 0
        self.aptitude = 0
        self.training = 0
        self.professional_modifiers = professional_modifiers

    def set_aptitude(self, aptitude):
        self.aptitude = aptitude

    def set_training(self, training):
        self.training = training

    def calculate_level(self, player):
        base = self.aptitude + self.training
        modifier = 0
        for prof_mod in self.professional_modifiers:
            if player.profession is prof_mod.profession:
                modifier = prof_mod.value
                break

        self.level = base + modifier


class Craft(Skill):
    def __init__(self, name, professional_modifiers):
        super(Craft, self).__init__(name, professional_modifiers)

    def set_attributes(self, player):
        self.aptitude = player.attributes[player.attributes.index(Attribute.DEXTERITY)].value


class Defense(Skill):
    def __init__(self, name, professional_modifiers):
        super(Defense, self).__init__(name, professional_modifiers)

    def set_attributes(self, player):
        self.aptitude = player.attributes[player.attributes.index(Attribute.AGILITY)].value


class Fighting(Skill):
    def __init__(self, name, professional_modifiers):
        super(Fighting, self).__init__(name, professional_modifiers)

    def set_attributes(self, player):
        strength = player.attributes[player.attributes.index(Attribute.STRENGTH)].value
        intellect = player.attributes[player.attributes.index(Attribute.INTELLECT)].value
        self.aptitude = math.floor((strength + intellect) / 2.0)


class Knowledge(Skill):
    def __init__(self, name, professional_modifiers):
        super(Knowledge, self).__init__(name, professional_modifiers)

    def set_attributes(self, player):
        self.aptitude = player.attributes[player.attributes.index(Attribute.INTELLECT)].value


class Manhandle(Skill):
    def __init__(self, name, professional_modifiers):
        super(Manhandle, self).__init__(name, professional_modifiers)

    def set_attributes(self, player):
        self.aptitude = player.attributes[player.attributes.index(Attribute.STRENGTH)].value


class Mobility(Skill):
    def __init__(self, name, professional_modifiers):
        super(Mobility, self).__init__(name, professional_modifiers)

    def set_attributes(self, player):
        strength = player.attributes[player.attributes.index(Attribute.STRENGTH)].value
        agility = player.attributes[player.attributes.index(Attribute.AGILITY)].value
        self.aptitude = math.floor((strength + agility) / 2.0)


class Perception(Skill):
    def __init__(self, name, professional_modifiers):
        super(Perception, self).__init__(name, professional_modifiers)

    def set_attributes(self, player):
        intellect = player.attributes[player.attributes.index(Attribute.INTELLECT)].value
        spirit = player.attributes[player.attributes.index(Attribute.SPIRIT)].value
        self.aptitude = math.floor((intellect + spirit) / 2.0)


class Persuasion(Skill):
    def __init__(self, name, professional_modifiers):
        super(Persuasion, self).__init__(name, professional_modifiers)

    def set_attributes(self, player):
        self.aptitude = player.attributes[player.attributes.index(Attribute.SPIRIT)].value


class Shooting(Skill):
    def __init__(self, name, professional_modifiers):
        super(Shooting, self).__init__(name, professional_modifiers)

    def set_attributes(self, player):
        dexterity = player.attributes[player.attributes.index(Attribute.DEXTERITY)].value
        intellect = player.attributes[player.attributes.index(Attribute.INTELLECT)].value
        self.aptitude = math.floor((dexterity + intellect) / 2.0)


class Stealth(Skill):
    def __init__(self, name, professional_modifiers):
        super(Stealth, self).__init__(name, professional_modifiers)

    def set_attributes(self, player):
        dexterity = player.attributes[player.attributes.index(Attribute.DEXTERITY)].value
        spirit = player.attributes[player.attributes.index(Attribute.SPIRIT)].value
        self.aptitude = math.floor((dexterity + spirit) / 2.0)


class Toughness(Skill):
    def __init__(self, name, professional_modifiers):
        super(Toughness, self).__init__(name, professional_modifiers)

    def set_attributes(self, player):
        strength = player.attributes[player.attributes.index(Attribute.STRENGTH)].value
        spirit = player.attributes[player.attributes.index(Attribute.SPIRIT)].value
        self.aptitude = math.floor((strength + spirit) / 2.0)


CRAFT = Craft(name='craft', professional_modifiers=[
    Profession.ProfessionalModifier(Profession.THIEF, 2)
])
DEFENSE = Defense(name='defense', professional_modifiers=[])
FIGHTING = Fighting(name='fighting', professional_modifiers=[
    Profession.ProfessionalModifier(Profession.FIGHTER, 3),
    Profession.ProfessionalModifier(Profession.MONK, 2),
    Profession.ProfessionalModifier(Profession.AMAZON, 2)
])
KNOWLEDGE = Knowledge(name='knowledge', professional_modifiers=[
    Profession.ProfessionalModifier(Profession.WIZARD, 3)
])
MANHANDLE = Manhandle(name='manhandle', professional_modifiers=[])
MOBILITY = Mobility(name='mobility', professional_modifiers=[
    Profession.ProfessionalModifier(Profession.RANGER, 2),
    Profession.ProfessionalModifier(Profession.MONK, 2)
])
PERCEPTION = Perception(name='perception', professional_modifiers=[])
PERSUASION = Persuasion(name='persuasion', professional_modifiers=[
    Profession.ProfessionalModifier(Profession.PRIEST, 3)
])
SHOOTING = Shooting(name='shooting', professional_modifiers=[
    Profession.ProfessionalModifier(Profession.RANGER, 2),
    Profession.ProfessionalModifier(Profession.AMAZON, 2)
])
STEALTH = Stealth(name='stealth', professional_modifiers=[
    Profession.ProfessionalModifier(Profession.THIEF, 2)
])
TOUGHNESS = Toughness(name='toughness', professional_modifiers=[
    Profession.ProfessionalModifier(Profession.BARBARIAN, 3)
])
