from Seats import Traincarriage

def trainbooker():

    trains = {
        "Stardust": Traincarriage(40, "medium"),
        "Bolt": Traincarriage(20, "fast")
    }

    pick = ""
    print("\nWelcome!")

    while pick != "Exit":
        print("\n1 = See the list of trains\n2 = Reserve a trip\n3 = remove reservatoin\n4 = remove all reservations\n5 = Exit")
        pick = input("\nWhat do you want to do?: ")

        if pick == "1":
            print("\nHere is list of our trains:\n")
            for name, train in trains.items():
                print(f"{name} - Speed: {train.speed}, Free seats: {train.Freeseats()}/{train.seats} available.")

        if pick == "2":
            pick = input("Which train do you want to book?: ").capitalize()
            
            if pick in trains:
                train = trains[pick]
                print(f"You picked {pick} with {train.Freeseats()} seats available")

                confirm = input("Do you want to confirm? (Yes/No): ").capitalize()
                if confirm == "Yes":   
                    train.bookedseats()
                    print("Your trip has confirmed!")
                    if input("Anything else you want to do? (Yes/No):").capitalize() == "Yes":
                        ""
                    else:
                        return print("Ok, Goodbye!")

                else:
                    next = input("Ok, do you want to switch train?: ").capitalize()
                    if next == "Yes":
                        ""

                    else:
                        return print("Ok, Goodbye!")
            else:
                print("Error, try again")

        if pick == "5":
            pick = "Exit"

    else:
        print("Goodbye!")

trainbooker()