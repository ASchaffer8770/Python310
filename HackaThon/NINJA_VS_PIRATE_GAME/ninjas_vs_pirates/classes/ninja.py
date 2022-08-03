import random

class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.crit = 0.5
        self.crit_chance = 15
        self.stamina = 6
        self.health = 100
        self.special_atk = 2
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nCritical Chance: {self.crit_chance}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        bonus_damage = (self.strength * self.crit) + self.strength
        roll = random.randint(1,20)
        if roll > self.crit_chance:
            damage_done = self.strength + bonus_damage
            pirate.health -= self.strength + bonus_damage
            print(f"{self.name} did a crit attack {damage_done} damage.")
        else:
            damage_done = self.strength
            pirate.health -= self.strength
            print(f"{self.name} attacks for {damage_done} damage.")
        return damage_done

    def special_attack(self, pirate):
        #double the attack at the cost of some health
        if self.special_atk > 0
            print(f"{self.name} did a special attack!")
            self.attack(pirate)
            self.attack(pirate)
            self.health -= self.strength
            return self
        else:
            print(f"No special attack remaining.\n")
            self.attack(pirate)

    def heal(self):
        print(f"{self.name} is healing")
        self.health += self.stamina
        if self.health > 100:
            self.health = 100
        return self