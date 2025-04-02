class Card:
    def __init__(self, money):
        self.money = money

    def __str__(self):
        return f"Balance: {self.money:.1f}€"

    def pay(self, amount):
        if self.money >= amount:
            self.money -= amount

    def add(self, amount):
        if amount > 0:
            self.money += amount

p = Card(20)
g = Card(30)

p.pay(5.90)
g.pay(2.95)
print("Peter:", p)
print("Grace:", g)

p.add(20)
g.pay(5.90)
print("Peter:", p)
print("Grace:", g)

p.pay(2.95)
p.pay(2.95)
g.add(50)
print("Peter:", p)
print("Grace:", g)
