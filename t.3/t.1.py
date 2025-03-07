class Carriage:
    def __init__(self, seats):
        if seats < 1:
            raise ValueError("No seat")
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
        if not carriages or not all(isinstance(c, Carriage) for c in carriages):
            raise ValueError("No seat")
        self.id = id
        self.carriages = carriages
        self.departure = None
        self.destination = None

    def add_carriage(self, carriage):
        if isinstance(carriage, Carriage):
            self.carriages.append(carriage)

    def remove_carriage(self):
        if len(self.carriages) > 1:
            self.carriages.pop()

    def reserve_seat(self):
        for i, c in enumerate(self.carriages):
            if c.reserve():
                print(f"Seat reserved in Carriage {i+1}")
                return True
        print("No seats left")
        return False

    def show_seats(self):
        print("\nTrain seat layout:")
        for i, c in enumerate(self.carriages):
            print(f"Carriage {i+1}: {c}")
        print()

    def set_route(self, departure, destination):
        self.departure = departure
        self.destination = destination

    def __str__(self):
        route = f" ({self.departure} -> {self.destination})" if self.departure and self.destination else ""
        return f"Train {self.id}{route}"


if __name__ == "__main__":
    c1 = Carriage(5)
    c2 = Carriage(3)
    t = Train("IC123", [c1, c2])

    t.show_seats()
    t.reserve_seat()
    t.show_seats()
    t.set_route("Helsinki", "Tampere")
    print(t)

    t.remove_carriage()
    t.show_seats()

    t.remove_carriage()
