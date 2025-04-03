class Person:
    def __init__(self, name):
        self.name = name
        self.numbers = []
        self.address = None

    def add_number(self, number):
        self.numbers.append(number)

    def add_address(self, address):
        self.address = address

    def __str__(self):
        numbers = ", ".join(self.numbers) if self.numbers else "No numbers"
        address = self.address if self.address else "No address"
        return f"{self.name}\nNumbers: {numbers}\nAddress: {address}"


class PhoneBook:
    def __init__(self):
        self.persons = {}

    def add_number(self, name, number):
        if name not in self.persons:
            self.persons[name] = Person(name)
        self.persons[name].add_number(number)

    def add_address(self, name, address):
        if name not in self.persons:
            self.persons[name] = Person(name)
        self.persons[name].add_address(address)

    def get_entry(self, name):
        return self.persons.get(name)


class PhoneBookApplication:
    def __init__(self):
        self.phonebook = PhoneBook()

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.phonebook.add_number(name, number)

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.phonebook.add_address(name, address)

    def search(self):
        name = input("name: ")
        entry = self.phonebook.get_entry(name)
        if entry:
            print(entry)
        else:
            print("number unknown")

    def execute(self):
        self.help()
        while True:
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()

application = PhoneBookApplication()
application.execute()
