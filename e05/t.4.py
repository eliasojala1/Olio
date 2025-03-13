class Computer:
    def __init__(self, model, speed):
        self.model = model
        self.speed = speed

class LaptopComputer(Computer):
    def __init__(self, model, speed, weight):
        self.model = model
        self.speed = speed
        self.weight = weight

    def __str__(self):
        return self.model + ", " + str(self.speed) + " MHz, " + str(self.weight) + " kg"

laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
print(laptop)
