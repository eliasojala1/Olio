5. Present and Box
class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

class Box:
    def __init__(self):
        self.presents = []
    
    def add_present(self, present: Present):
        self.presents.append(present)
    
    def total_weight(self):
        return sum(p.weight for p in self.presents)
