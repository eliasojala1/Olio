def main():

    book = {}

    while True:
 
        command = None
        while command == None:
            try:
                command = int(input("1 = search, 2 = add, 3 = quit: "))

            except:
                pass

        if command == 1: #search
            name = input("Give a name: ")
            if name in book:
                print(book[name])
            else:
                print("not found")


        elif command == 2: #add
            name = input("Give a name: ")            
            number = input("Give a number: ")
            book[name] = number
            print("contact added")        


        elif command == 3: #quit
            print("Goodbye!")
            break


        else:
            print("something went wrong, give number from 1 to 3")


main()