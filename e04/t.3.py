class Car:
    def __init__(self, make, speed):
        self.make = make
        self.speed = speed

def fastest(cars):
    return max(cars, key=lambda c: c.speed).make

cars = [Car("Toyota", 180), Car("BMW", 250), Car("Audi", 240)]
print(fastest(cars))  # BMW
