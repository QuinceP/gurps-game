from abc import ABCMeta, abstractmethod
import math


class Character:
    __metaclass__ = ABCMeta

    def __init__(self, gender, points, strength, dexterity, intelligence, health, image, social, advantages,
                 disadvantages, quirks, skills, armor, shield, weapon, inventory, height, weight):
        self.points = points
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.health = health
        self.image = image
        self.social = social
        self.advantages = advantages
        self.disadvantages = disadvantages
        self.quirks = quirks
        self.skills = skills
        self.armor = armor
        self.shield = shield
        self.weapon = weapon
        self.inventory = inventory
        self.gender = gender
        self.height = height
        self.weight = weight

        def speed(self):
            speed = (self.health + self.dex) / 4.0
            return round(speed, 2)

        def encumbrance(self):
            enc = 0
            for item in range(0, len(self.inventory)):
                enc += self.inventory[item].weight
            return enc

        def encumbrance_level(self):
            enc = encumbrance(self)
            if enc < 2 * self.strength:
                return 0
            elif enc < 4 * self.strength:
                return 1
            elif enc < 6 * self.strength:
                return 2
            elif enc < 12 * self.strength:
                return 3
            elif enc < 20 * self.strength:
                return 4
            elif enc < 30 * self.strength:
                return 5
            else:
                return 6

        def move(self):
            enc_lvl = encumbrance_level(self)
            # TODO: if character has Running skill, add 1/8 speed to base speed.
            move_distance = self.speed - enc_lvl
            if enc_lvl >= 6:
                move_distance = 0
            return math.floor(move_distance)
