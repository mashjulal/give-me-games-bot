import datetime

from igdb.objects.Company import Company
from igdb.objects.Genre import Genre
from igdb.objects.Platform import Platform
from igdb.objects.Website import Website


class Game:

    __NAME = "<b>{game_name}</b>"
    __DESCRIPTION = "\n{game_summary}"
    __RATING = "\n<b>Rating: </b>{game_rating}/100"
    __PLATFORMS = "\n<b>Platforms:</b> {platform_list}"
    __GENRES = "\n<b>Genres:</b> {genre_list}"
    __DEVELOPERS = "\n<b>Developers:</b> {developer_list}"
    __WEBSITES = "\n<b>Websites:</b> {website_list}"

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

    @staticmethod
    def as_game(d):
        g = Game()
        for key in d:
            if key == "platforms":
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

    def __str__(self):
        msg = Game.__NAME\
            .format(game_name=self.name)

        if self.summary:
            msg += Game.__DESCRIPTION\
                .format(game_summary=self.summary)

        if self.rating:
            msg += Game.__RATING\
                .format(game_rating=round(self.rating, 2))

        if len(self.genres) != 0:
            msg += Game.__GENRES\
                .format(genre_list=", ".join([g.name for g in self.genres]))

        if len(self.platforms) != 0:
            msg += Game.__PLATFORMS\
                .format(platform_list=", ".join([p.name for p in self.platforms]))

        if len(self.developers) != 0:
            msg += Game.__DEVELOPERS\
                .format(developer_list=", ".join([d.name for d in self.developers]))

        if len(self.websites) != 0:
            msg += Game.__WEBSITES\
                .format(website_list=", ".join(
                [str(site) for site in sorted(self.websites, key=lambda w: w.name)]))

        return msg
