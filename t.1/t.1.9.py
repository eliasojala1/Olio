import random

def dice():
    rollDice = random.randint(1, 6)
    return rollDice

roll = dice()
print(roll)