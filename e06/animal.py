class Animal:
    def __init__(self, number_of_legs, species=None):
        assert isinstance(number_of_legs, int) and number_of_legs >= 0
        assert isinstance(species, int) and species > 0
        self.__legs = number_of_legs
        self.__species = species

    def number_of_legs(self): 
        return self.__legs

    def make_sound(self):
        print("*it's quiet*")
        
    def get_species(self):
        return self.__species  
