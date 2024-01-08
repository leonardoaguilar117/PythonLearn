class spotify:
    musicGenres = []

    # constructor
    def __init__(self, play, pay, version):
        self.play = play
        self.pay = pay
        self.version = version

    # destructor
    def __delattr__(self):
        return

    # methods
    def addGenres(self, *genres):
        for genre in genres:
            self.musicGenres.append(genre)

    def __str__(self):
        return "\n".join(str(genre) for genre in self.musicGenres)


class musicGenre:
    # Constructor
    def __init__(self, title, popularRating):
        self.title = title
        self.Rating = popularRating

    # Getter and setter
    @property
    def rating(self):
        return self.Rating

    @rating.setter
    def rating(self, value):
        if 0 < value <= 10:
            self.Rating = value

    # method

    def __str__(self):
        return f"Genre: {self.title} - Popular Rating: {self.Rating}"


if __name__ == "__main__":
    rock = musicGenre("Rock", 10)
    pop = musicGenre("Pop", 8)

    spoty = spotify(True, True, "1.3.11")
    spoty.addGenres(rock, pop)
    print(spoty)
