# File:        coin.py
# Source:      Tony Gaddis: Starting out with Python, fourth edition
# Modified by: Sanna Maatta & Anne Jumppanen
# Description: Coin object and tossing

import random

# Class definition

import random

class Coin:
    def __init__(self):
        self.sideup = "Heads"

    def toss_the_coin(self):
        chance = random.randint(1, 100)

        if chance <= 40:
            self.sideup = "Heads"
        elif chance <= 80:
            self.sideup = "Tails"
        elif chance <= 90:
            self.sideup = "Upright"
        elif chance <= 97:
            self.sideup = "Lost in rabbit hole"
        else:
            self.sideup = "Lost in space"

    def get_sideup(self):
        return self.sideup

def main():
    my_coin = Coin()
    print("This side is up:", my_coin.get_sideup())

    print("Tossing the coin...")
    my_coin.toss_the_coin()

    print("Now this side is up:", my_coin.get_sideup())

main()
