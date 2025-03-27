from animal import Animal

class Bird(Animal):
    def __init__(self, species=10000):
        assert isinstance(species, int) and species > 0
        Animal.__init__(self, 2, species)

    def make_sound(self):
        print("*clear bird singing*")
