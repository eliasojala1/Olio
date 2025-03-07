import random

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.name} ({self.value} gold)"

class Player:
    def __init__(self, name):
        self.name = name
        self.backpack = []
        self.gold = 100

    def buy(self, shop, item_name):
        item = shop.items.get(item_name)
        if item and self.gold >= item.value:
            self.gold -= item.value
            self.backpack.append(shop.items.pop(item_name))
            print(f"Bought {item.name}")
        else:
            print("Not enough gold or item not found")

    def sell(self, shop, item_name):
        for item in self.backpack:
            if item.name == item_name:
                self.gold += item.value // 2
                self.backpack.remove(item)
                shop.items[item_name] = item
                print(f"Sold {item.name}")
                return
        print("Item not in backpack")

    def gamble(self, shop, desired_item):
        if desired_item in shop.items and self.backpack and random.random() < 0.5:
            lost_item = random.choice(self.backpack)
            self.backpack.remove(lost_item)
            shop.items[lost_item.name] = lost_item
            self.backpack.append(shop.items.pop(desired_item))
            print(f"Gamble won! Lost {lost_item.name}, gained {desired_item}")
        else:
            print("Gamble lost or conditions not met")

    def __repr__(self):
        return f"{self.name}: {self.gold} gold, Backpack: {self.backpack}"

class Shop:
    def __init__(self, name):
        self.name = name
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def __repr__(self):
        return f"{self.name} Inventory: {list(self.items.values())}"

if __name__ == "__main__":
    shop = Shop("StoneAge Market")
    player = Player("Caveman Joe")
    
    shop.add_item(Item("Stone Axe", 50))
    shop.add_item(Item("Mammoth Hide", 30))
    
    print(shop)
    player.buy(shop, "Stone Axe")
    player.sell(shop, "Stone Axe")
    player.gamble(shop, "Mammoth Hide")
    
    print(player)
    print(shop)