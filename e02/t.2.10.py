class Property:
    def __init__(self, rooms, size, price):
        self.rooms = rooms
        self.size = size
        self.price = price

    def bigger(self, other):
        return self.size > other.size

    def price_diff(self, other):
        return abs((self.size * self.price) - (other.size * other.price))

    def more_exp(self, other):
        return (self.size * self.price) > (other.size * other.price)

apt1 = Property(1, 16, 5500)
apt2 = Property(2, 38, 4200)
apt3 = Property(3, 78, 2500)

print("\nIs it bigger:")
print(apt1.bigger(apt2))
print(apt3.bigger(apt2))

print("\nPrice difference:")
print(apt1.price_diff(apt2))
print(apt3.price_diff(apt2))

print("\nIs it more expensive:")
print(apt1.more_exp(apt2))
print(apt3.more_exp(apt2), "\n")
