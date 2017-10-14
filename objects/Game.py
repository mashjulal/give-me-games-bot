from objects.Cover import Cover


class Game:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.genres = []
        self.keywords = []
        self.url = ""
        self.first_release_date = 0
        self.expansions = []
        self.developers = []
        self.summary = ""
        self.rating = 0.0
        self.platforms = []
        self.websites = []
        self.cover = ""

    @staticmethod
    def as_game(d):
        g = Game()
        for key in d:
            if key == "cover":
                g.cover = Cover.as_cover(d[key])
            else:
               g.__dict__[key] = d[key]
        return g