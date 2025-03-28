from wolf import Wolf

class Dog(Wolf):
    def __init__(self):
        Wolf.__init__(self, "Mysti", species=340) 
        self.legs = 4 
        self._species = "Dog"

    def make_sound(self):
        print("*dog barking*")

    def number_of_legs(self):
        return self.legs

    def get_species(self):
        return self._species

    def wag_tail(self):
        print("*dog wags tail*")
