class Shop:
    def __init__(self, items):
        self.items = items

    def buy(self, item, player):
        if item in self.items:
            player.backpack.append(item)
            self.items.remove(item)

    def sell(self, item, player):
        if item in player.backpack:
            player.backpack.remove(item)
            self.items.append(item)

    def gamble(self, player):
        import random
        if player.backpack and self.items:
            lost = random.choice(player.backpack)
            gained = random.choice(self.items)
            player.backpack.remove(lost)
            self.items.remove(gained)
            player.backpack.append(gained)

class Player:
    def __init__(self, name):
        self.name = name
        self.backpack = []

if __name__ == "__main__":
    p = Player("Rock")
    s = Shop(["Spear", "Axe", "Bone Necklace"])
    
    s.buy("Spear", p)
    print(p.backpack)
    
    s.gamble(p)
    print(p.backpack)