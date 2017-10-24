from config import igdb_key
from igdb_api_python.igdb import igdb

from igdb.objects.Company import Company
from igdb.objects.Game import Game
from igdb.objects.Platform import Platform

from igdb.objects.Genre import Genre


class IGDBHandler:

    __COMPANY_FIELDS = {"fields": [
        "name",
        "logo",
        "description",
        "country",
        "website"
    ]}

    __COMPANY_EXPAND = {"expand": [
        "country"
    ]}

    __FIELDS = {"fields": [
        "name",
        "websites",
        "first_release_date",
        "developers",
        "summary",
        "rating",
        "cover"
    ]}

    __EXPAND = {"expand": [
        "game",
        "platforms",
        "genres",
        "expansions",
        "developers"
    ]}

    __GENRE_FIELDS = {"fields": [
        "name"
    ]}

    def __init__(self):
        self.__igdb = igdb(igdb_key)

    def get_game(self, game_id):
        params = {"ids": game_id}
        params.update(IGDBHandler.__FIELDS)
        params.update(IGDBHandler.__EXPAND)
        result = self.__igdb.games(params)

        return Game.as_game(result.body[0])

    def get_platforms(self, platforms_id):
        result = self.__igdb.platforms({
            "ids": platforms_id,
            "fields": "name"})
        platforms = [Platform.as_platform(d) for d in result.body]
        return platforms

    def get_genres(self, genres_id):
        params = {"ids": genres_id}
        params.update(IGDBHandler.__GENRE_FIELDS)
        result = self.__igdb.genres(params)
        genres = [Genre.as_genre(d) for d in result.body]
        return genres

    def search(self, query):
        params = {"search": query}
        params.update(IGDBHandler.__FIELDS)
        params.update(IGDBHandler.__EXPAND)
        result = self.__igdb.games(params)

        return [Game.as_game(d) for d in result.body]

    def get_company(self, company_id):
        fields = {"ids": company_id}
        fields.update(self.__COMPANY_FIELDS)
        result = self.__igdb.companies(fields)
        return Company.as_company(result.body[0])
