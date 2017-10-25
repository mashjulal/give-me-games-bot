class Genre:

    __NAME = "<b>{genre_name}</b>"

    def __init__(self):
        self.id = 0
        self.name = ""

    @staticmethod
    def as_genre(d):
        g = Genre()
        g.__dict__.update(d)
        return g

    def __str__(self):
        s = Genre.__NAME.format(genre_name=self.name)

        return s
