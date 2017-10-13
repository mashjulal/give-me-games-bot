class Game:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.genres = []
        self.keywords = []
        self.url = ""
        self.first_release_date = 0
        self.expansions = []
        self.franchise = 0
        self.developers = []
        self.summary = ""
        self.rating = 0.0
        self.category = 0
        self.platforms = []
        self.tags = []
        self.websites = []

    @staticmethod
    def as_game(d):
        g = Game()
        g.__dict__.update(d)
        return g