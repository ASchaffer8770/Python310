class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}.")
            self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

class Pet:

    def __init__(self, name, type, tricks, health, energy, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise
    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    def play(self):
        self.health += 5
        return self
    def noise(self):
        print(self.noise)

my_treats = ['cookies', 'snackos', 'socks']
my_pet_food = ['Kibble', 'treats']

rey = Pet("Rey", "Dog", ['sits, stays, barks'], 100, 100, "woof!")
alex = Ninja("Alex", "Schaffer", my_treats, my_pet_food, rey)

alex.walk()
alex.feed()
alex.bathe()