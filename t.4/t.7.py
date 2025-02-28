class Recording:
    def __init__(self, length: int):
        self.__length = length
    
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, new_length: int):
        self.__length = new_length
