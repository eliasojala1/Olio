class Traincarriage:
    def __init__(self, identifier, seats, speed):
        self.identifier = identifier
        self.seats = seats
        self.speed = speed
        self.reserved_seats = set() 

    def freeseats(self):
        return self.seats - len(self.reserved_seats)

    def book_seat(self, seat_number):
        if seat_number < 1 or seat_number > self.seats:
            print("Error")
        elif seat_number in self.reserved_seats:
            print("Error")
        else:
            self.reserved_seats.add(seat_number)
            print(f"Seat {seat_number} on train {self.identifier} booked successfully!")

    def cancel_reservation(self, seat_number):
        if seat_number in self.reserved_seats:
            self.reserved_seats.remove(seat_number)
            print(f"Reservation for seat {seat_number} cancelled.")
        else:
            print("Error")

    def reset_reservations(self):
        self.reserved_seats.clear()
        print("reservations have been reset")

    def reservation_status(self):
        booked = sorted(self.reserved_seats)
        free = [seat for seat in range(1, self.seats + 1) if seat not in self.reserved_seats]
        return f"{self.identifier} - Speed: {self.speed}\nReserved: {booked}\nFree: {free}"

    def is_full(self):
        return len(self.reserved_seats) == self.seats