import datetime

from igdb.objects.Company import Company
from igdb.objects.Genre import Genre
from igdb.objects.Platform import Platform
from igdb.objects.Website import Website

from igdb.objects.Cover import Cover


class Game:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.genres = []
        self.url = ""
        self.first_release_date = 0
        self.expansions = []
        self.developers = []
        self.summary = ""
        self.rating = 0.0
        self.platforms = []
        self.websites = []
        self.cover = None

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
            elif key == "websites":
                for website_dict in d[key]:
                    g.websites.append(Website.as_website(website_dict))
            elif key == "first_release_date":
                g.first_release_date = datetime.date.fromtimestamp(d[key] / 1000.0)
            elif key == "developers":
                for dev_dict in d[key]:
                    g.developers.append(Company.as_company(dev_dict))
            else:
               g.__dict__[key] = d[key]
        return g
