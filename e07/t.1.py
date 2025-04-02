class MagicPotion:
    def __init__(self, name):
        self.name = name
        self.ingredients = []

    def add_ingredient(self, ingredient, amount):
        self.ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(self.name + " recipe:")
        for ingredient, amount in self.ingredients:
            print(f"{ingredient}: {amount} grams")

class SecretMagicPotion(MagicPotion):
    def __init__(self, name, password):
        super().__init__(name)
        self.password = password

    def add_ingredient(self, ingredient, amount, password):
        if password == self.password:
            super().add_ingredient(ingredient, amount)
        else:
            print("Wrong password!")

    def print_recipe(self, password):
        if password == self.password:
            super().print_recipe()
        else:
            print("Wrong password!")

potion = SecretMagicPotion("Diminuendo maximus", "hocuspocus")
potion.add_ingredient("Toadstool", 1.5, "hocuspocus")
potion.add_ingredient("Magic sand", 3.0, "hocuspocus")
potion.add_ingredient("Frogspawn", 4.0, "wrongpassword")  # Testataan väärää salasanaa
potion.print_recipe("hocuspocus")