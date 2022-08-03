from classes.ninja import Ninja
from classes.pirate import Pirate
import random

# michelangelo = Ninja("Michelanglo")

# jack_sparrow = Pirate("Jack Sparrow")



# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()


# higher dice roll goes first ai or user
# turn base until health is 0

print(f"Welcome to Ninja vs Pirate!")
selection = input(f"Enter 1 for Jack Sparrow or 2 for Snake Eyes \n>")

if selection == "1":
    player1 = Pirate("Jack Sparrow")
    player2 = Ninja("Snake Eyes")
else:
    player1 = Ninja("Snake Eyes")
    player2 = Pirate("Jack Sparrow")

while player1.health > 0 and player2.health > 0:
    #choose action
    action = input("Choose an action \n 1) Basic Attack 2) Special Attack 3) Heal \n >")
    action2 = random.randint(1,3)
    #perfrom action for player 
    if action == "1":
        player1.attack(player2)
    elif action == "2":
        player1.special_attack(player2)
    else:
        player1.heal()
    #perform action for bot
    if action2 == 1:
        player2.attack(player1)
    elif action2 == 2:
        player2.special_attack(player1)
    else:
        player2.heal()
    
#Printing results
    if player1.health <= 0:
        print(f"{player1.name} has died!\n{player2.name} is the winner!!")
    elif player2.health <= 0:
        print(f"{player2.name} has died!\n{player1.name} is the winner!!")
    elif player1.health and player2.health < 0:
        print("We have a tie! Both players are dead! Play Again! This was a small budget game! Sorry!")

    print("Round Complete: \n --------------------------------- \n")
    print("Stats after round \n =================================\n")
    player1.show_stats()
    player2.show_stats()

# player1.show_stats()
# player2.show_stats()