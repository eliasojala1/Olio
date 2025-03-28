from animal import Animal

class Mammal(Animal):
    def __init__(self, species=6000):
        assert isinstance(species, int) and species > 0
        Animal.__init__(self, 4, species)

    def make_sound(self): 
        print("*mammal breathing*")