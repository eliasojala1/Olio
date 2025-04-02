class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

class Room:
    def __init__(self):
        self.people = []
    
    def add(self, person: Person):
        self.people.append(person)
    
    def is_empty(self):
        return len(self.people) == 0
    
    def print_contents(self):
        for person in self.people:
            print(f"{person.name} ({person.height} cm)")
    
    def shortest(self):
        return min(self.people, key=lambda p: p.height) if self.people else None
    
    def remove_shortest(self):
        if self.people:
            shortest_person = self.shortest()
            self.people.remove(shortest_person)
            return shortest_person
        return None