class Movie:
    def __init__(self,name,director,date):
        self.name = name
        self.director = director
        self.date = date

    def info(self):
        info = f"Name: {self.name}, Director: {self.director}, Date: {self.date}"
        return info
        
movie_1 = Movie("Shawshank Redemption","Frank Darabont",2020)
movie_2 = Movie("Forrest Gump","Robert Zemeckis",2019)

print(movie_1.info())