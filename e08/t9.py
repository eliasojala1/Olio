#original code  

class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

class UserService:
    def send_email(self, user, message):
        print(f"Sending email to {user.email}: {message}")

#delete userservice class

class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def send_email(self, user, message):
        print(f"Sending email to {user.email}: {message}")