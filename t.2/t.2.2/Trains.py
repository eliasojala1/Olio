from Seats import Traincarriage

def trainbooker():
    trains = {
        "Stardust": Traincarriage("Stardust", 40, "medium"),
        "Bolt": Traincarriage("Bolt", 20, "fast")
    }

    while True:
        print("\n1 = See the list of trains\n2 = Reserve a seat\n3 = Cancel a reservation\n4 = Reset all reservations\n5 = Check reservation status\n6 = Exit")
        choice = input("What do you want to do?: ")

        if choice == "1":
            print("\nAvailable trains:")
            for name, train in trains.items():
                print(f"{name} - Speed: {train.speed}, Free seats: {train.freeseats()}/{train.seats}")

        elif choice == "2":
            train_name = input("Which train do you want to book?: ").capitalize()
            if train_name in trains:
                train = trains[train_name]
                if train.is_full():
                    print("Sorry, this train is fully booked!")
                else:
                    seat_number = int(input(f"Enter seat number (1-{train.seats}): "))
                    train.book_seat(seat_number)
            else:
                print("Error: Train not found!")

        elif choice == "3":
            train_name = input("Which train's reservation do you want to cancel?: ").capitalize()
            if train_name in trains:
                train = trains[train_name]
                seat_number = int(input("Enter seat number to cancel: "))
                train.cancel_reservation(seat_number)
            else:
                print("Error")

        elif choice == "4":
            train_name = input("Which train do you want to reset?: ").capitalize()
            if train_name in trains:
                trains[train_name].reset_reservations()
            else:
                print("Error")

        elif choice == "5":
            train_name = input("Enter train name to check reservations: ").capitalize()
            if train_name in trains:
                print(trains[train_name].reservation_status())
            else:
                print("Error")

        elif choice == "6":
            print("bye")
            break

        else:
            print("Error")

trainbooker()