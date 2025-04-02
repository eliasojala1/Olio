class Movie:
    def __init__(self, name, director, genre, year):
        self.name = name
        self.director = director
        self.genre = genre
        self.year = year

def moviesgenre(movies, genre):
    result = []
    for movie in movies:
        if movie.genre == genre:
            result.append(movie)
    return result

movie1 = Movie("A Better Tomorrow", "John Woo", "action", 1986)
movie2 = Movie("Chinese Odyssey", "Stephen Chow", "comedy", 1993)
movie3 = Movie("The Legend", "Corey Yuen", "comedy", 1993)
movie4 = Movie("Potter", "Martti", "action", 20000)

movies = [movie1, movie2, movie3, movie4]

print("Movies in the action genre:")
for movie in moviesgenre(movies, "action"):
    print(f"{movie.director}: {movie.name}")
