class Carriage:
    def __init__(self, seats):
        self.seats = [False] * seats

    def reserve(self):
        for i in range(len(self.seats)):
            if not self.seats[i]:
                self.seats[i] = True
                return True
        return False

    def __str__(self):
        return "".join("X" if s else "O" for s in self.seats)

class Train:
    def __init__(self, id, carriages):
        if not carriages:
            raise ValueError("A train must have at least one carriage.")
        self.id = id
        self.carriages = carriages
        self.departure = None
        self.destination = None

    def add_carriage(self, carriage):
        self.carriages.append(carriage)

    def remove_carriage(self):
        if len(self.carriages) > 1:
            self.carriages.pop()

    def reserve_seat(self):
        for c in self.carriages:
            if c.reserve():
                return True
        return False

    def show_seats(self):
        for i, c in enumerate(self.carriages):
            print(f"Carriage {i+1}: {c}")

    def set_route(self, departure, destination):
        self.departure = departure
        self.destination = destination

    def __str__(self):
        return f"Train {self.id} ({self.departure} -> {self.destination})"

if __name__ == "__main__":
    c1 = Carriage(5)
    c2 = Carriage(3)
    t = Train("IC123", [c1, c2])

    t.show_seats()
    t.reserve_seat()
    t.show_seats()
    t.set_route("Helsinki", "Tampere")
    print(t)
