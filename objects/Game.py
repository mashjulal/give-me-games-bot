from objects.Cover import Cover
from objects.Genre import Genre
from objects.Platform import Platform


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
            elif key == "platforms":
                for platform_dict in d[key]:
                    g.platforms.append(Platform.as_platform(platform_dict))
            elif key == "genres":
                for genre_dict in d[key]:
                    g.genres.append(Genre.as_genre(genre_dict))
            # elif key == "expansions":
            #     for game_dict in d[key]:
            #         g.expansions.append(Game.as_game(game_dict))
            else:
               g.__dict__[key] = d[key]
        return g