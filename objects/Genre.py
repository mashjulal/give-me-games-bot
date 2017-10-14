class Genre:

    def __init__(self):
        self.id = 0
        self.name = ""

    @staticmethod
    def as_genre(d):
        g = Genre()
        g.__dict__.update(d)
        return g