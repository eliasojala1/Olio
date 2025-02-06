class Book:
    def __init__(self, name, author, genre, year):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1955)

print(python.author + ": " + python.name + " (" + str(python.year) + ")")
print("The genre of the book " + everest.name + " is " + everest.genre)
