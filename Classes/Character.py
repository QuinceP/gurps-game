from abc import ABCMeta, abstractmethod
import math


class Character:
    __metaclass__ = ABCMeta

    def __init__(self, race, profession, gender, attributes, spirit, health, skills, abilities, armor, right_hand,
                 left_hand, inventory, spells, deity, destiny, money, languages, reputation):
        self.race = race
        self.profession = profession
        self.gender = gender
        self.attributes = attributes
        self.spirit = spirit
        self.health = health
        self.skills = skills
        self.abilities = abilities
        self.armor = armor
        self.right_hand = right_hand
        self.left_hand = left_hand
        self.inventory = inventory
        self.spells = spells
        self.destiny = destiny
        self.deity = deity
        self.money = money
        self.languages = languages
        self.reputation = reputation
