class Traincarriage:
    def __init__(self, id, seats, speed):
        self.id = id
        self.seats = seats
        self.reserved_seats = set()
        self.speed = speed
    
    def Freeseats(self):
        return self.seats - len(self.reserved_seats)
    
    def bookedseats(self, seatid):

        if 1 <= seatid <= self.seats and seatid not in self.reserved_seats:
                self.reserved_seats.add(seatid)
                print(f"Seat {seatid} on train {self.id} has been booked")
        
        else:
             print("This seat is already taken!")

    def cancel(self, seatid):
        if seatid in self.reserved_seats:
              self.reserved_seats.remove(seatid)
              print(f"reservation for seat {seatid} has been removed")
        else:
             print("Error, this seat is not reserved.")

    def reset(self):
         self.reserved_seats.clear()
         print("All reservations has been cleared!")

    def status(self):
         
        
    def bookedseats(self):
        if self.Freeseats() > 0:
            self.reserved_seats += 1

        else:
            print("Sorry, there is not any seats left!")
