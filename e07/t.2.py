import random

class Player:
    def __init__(self, name):
        self.name = name
        self.pet = None

    def roll_dice(self):
        return random.randint(1, 6) + random.randint(1, 6)

class Mammal:
    def __init__(self, species, weight):
        self.species = species
        self.weight = weight

    def __str__(self):
        return f"{self.species} weighing {self.weight} kg"

def choose_pet(dice_sum):
    if dice_sum <= 6:
        return Mammal("Mouse", 0.5)
    elif dice_sum <= 9:
        return Mammal("Cat", 4)
    elif dice_sum <= 12:
        return Mammal("Dog", 20)
    else:
        return Mammal("Elephant", 100)

def main():
    num_players = int(input("How many players? "))
    
    for i in range(num_players):
        name = input(f"Enter name for Player {i + 1}: ")
        player = Player(name)

        dice_sum = player.roll_dice()
        print(f"{name} rolled {dice_sum}!")

        pet = choose_pet(dice_sum)
        player.pet = pet

        print(f"{name}'s Pet: {player.pet}\n")

if __name__ == "__main__":
    main()
