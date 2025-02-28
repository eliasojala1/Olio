class BankAccount:
    def __init__(self, owner: str, account_number: str, balance: float):
        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance
    
    def deposit(self, amount: float):
        self.__balance += amount
        self.__service_charge()
    
    def withdraw(self, amount: float):
        if self.__balance >= amount:
            self.__balance -= amount
            self.__service_charge()
    
    def __service_charge(self):
        self.__balance *= 0.99
    
    @property
    def balance(self):
        return self.__balance
