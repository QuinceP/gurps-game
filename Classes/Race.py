from Classes import Attribute
from Classes import Profession


class AttributeModifier:
    def __init__(self, attribute, value):
        self.attribute = attribute
        self.value = value


class Race:
    def __init__(self, name, attribute_modifier, professions, weapon_training):
        self.name = name
        self.attribute_modifier = attribute_modifier
        self.professions = professions
        self.weapon_training = weapon_training


HUMAN = Race('human', AttributeModifier(Attribute.SPIRIT, 1),
             [Profession.BARBARIAN, Profession.FIGHTER, Profession.PRIEST, Profession.RANGER, Profession.THIEF,
              Profession.WIZARD, Profession.MONK, Profession.AMAZON], [])

ELF = Race('elf', AttributeModifier(Attribute.INTELLECT, 1),
           [Profession.FIGHTER, Profession.MONK, Profession.RANGER, Profession.WIZARD], [])

DWARF = Race('dwarf', AttributeModifier(Attribute.STRENGTH, 1),
             [Profession.FIGHTER, Profession.THIEF, Profession.PRIEST], [])

GNOME = Race('gnome', AttributeModifier(Attribute.DEXTERITY, 1),
             [Profession.PRIEST, Profession.THIEF, Profession.WIZARD], [])

HALF_ORC = Race('half-orc', AttributeModifier(Attribute.STRENGTH, 2),
                [Profession.FIGHTER, Profession.BARBARIAN, Profession.MONK], [])

HOBBIT = Race('hobbit', AttributeModifier(Attribute.AGILITY, 1),
              [Profession.AMAZON, Profession.BARBARIAN, Profession.THIEF], [])
