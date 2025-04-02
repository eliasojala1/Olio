class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return self.name + " (" + str(self.weight) + "g)"

class Suitcase:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.items = []

    def add_item(self, item):
        total_weight = 0
        for i in self.items:
            total_weight += i.weight
        if total_weight + item.weight <= self.max_weight:
            self.itepms.append(item)

    def weight(self):
        total_weight = 0
        for i in self.items:
            total_weight += i.weight
        return total_weight

    def __str__(self):
        total_weight = self.weight()
        return str(len(self.items)) + " item" + ("s" if len(self.items) != 1 else "") + " (" + str(total_weight) + "g)"

class CargoHold:
    def __init__(self, max_weight):
        self.max_weight = max_weight * 1000
        self.suitcases = []

    def add_suitcase(self, suitcase):
        total_weight = 0
        for s in self.suitcases:
            total_weight += s.weight()
        if total_weight + suitcase.weight() <= self.max_weight:
            self.suitcases.append(suitcase)

    def print_items(self):
        for suitcase in self.suitcases:
            for item in suitcase.items:
                print(item)

    def __str__(self):
        total_weight = 0
        for suitcase in self.suitcases:
            total_weight += suitcase.weight()
        remaining_space = (self.max_weight - total_weight) / 1000
        return str(len(self.suitcases)) + " suitcase" + ("s" if len(self.suitcases) != 1 else "") + ", space for " + str(round(remaining_space, 1)) + " kg"

book = Item("ABC Book", 200)
phone = Item("Nokia 3210", 100)
brick = Item("Brick", 400)

adas_suitcase = Suitcase(1000)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)

peters_suitcase = Suitcase(1000)
peters_suitcase.add_item(brick)

cargo_hold = CargoHold(100)
cargo_hold.add_suitcase(adas_suitcase)
cargo_hold.add_suitcase(peters_suitcase)

print("The suitcases contains:")
cargo_hold.print_items()
