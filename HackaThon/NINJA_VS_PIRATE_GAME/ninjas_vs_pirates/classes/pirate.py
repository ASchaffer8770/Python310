import random

class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.crit = 0.3
        self.crit_chance = 18
        self.stamina = 4
        self.health = 100
        self.special_atk = 2

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nCritical Chance: {self.crit_chance}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        bonus_damage = (self.strength * self.crit) + self.strength
        roll = random.randint(1,20)
        if roll > self.crit_chance:
            damage_done = self.strength + bonus_damage
            ninja.health -= self.strength + bonus_damage
            print(f"{self.name} did a crit attack for {damage_done} damage.")
        else:
            damage_done = self.strength
            ninja.health -= self.strength
            print(f"{self.name} attacks for {damage_done}.")
        return damage_done

    def special_attack(self, ninja):
        # beserker attack at cost of health
        print(f"{self.name} goes Beserk!")
        ninja.health -= self.strength * 2
        self.health -= self.strength
        return self

    def heal(self):
        print(f"{self.name} is healing")
        self.health += self.stamina
        if self.health > 100:
            self.health = 100
        return self
# each character needs to have three actions
# each chr wont do action until both have inputs
# calc each turn
#show result
#attack / defense/ special

