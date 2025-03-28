from mammal import Mammal

class Wolf(Mammal):
    def __init__(self, pack, species=3):
        assert isinstance(pack, str) and len(pack) > 0
        assert isinstance(species, int) and species > 0
        Mammal.__init__(self, species)
        self.__pack_name = pack

    def get_species(self):
        return self._species

    def another_make_sound(self):
        print("*wolf howling*")

    def get_pack_name(self):
        return self.__pack_name

    def set_pack_name(self, pack_name):
        self.__pack_name = pack_name
