from config import igdb_key
from igdb_api_python.igdb import igdb

from igdb.objects.Company import Company
from igdb.objects.Game import Game
from igdb.objects.Platform import Platform

from igdb.objects.Genre import Genre


class IGDBHandler:

    __SEARCH_FIELDS = {"fields": [
        "name"
    ]}

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

    __GAME_FIELDS = {"fields": [
        "name",
        "websites",
        "first_release_date",
        "developers",
        "summary",
        "rating",
        "cover"
    ]}

    __GAME_EXPAND = {"expand": [
        "game",
        "platforms",
        "genres",
        "expansions",
        "developers"
    ]}

    __GENRE_FIELDS = {"fields": [
        "name"
    ]}

    __PLATFORM_FIELDS = {"fields": [
        "name"
    ]}

    def __init__(self):
        self.__igdb = igdb(igdb_key)

    def get_game(self, game_id):
        params = {"ids": game_id}
        params.update(IGDBHandler.__GAME_FIELDS)
        params.update(IGDBHandler.__GAME_EXPAND)
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

    def search_game(self, query):
        params = {"search": query}
        params.update(IGDBHandler.__SEARCH_FIELDS)
        result = self.__igdb.games(params)

        return [Game.as_game(d) for d in result.body]

    def search_company(self, query):
        params = {"search": query}
        params.update(IGDBHandler.__SEARCH_FIELDS)
        result = self.__igdb.companies(params)

        return [Company.as_company(d) for d in result.body]

    def search_genre(self, query):
        params = {"search": query}
        params.update(IGDBHandler.__SEARCH_FIELDS)
        result = self.__igdb.genres(params)

        return [Genre.as_genre(d) for d in result.body]

    def search_platform(self, query):
        params = {"search": query}
        params.update(IGDBHandler.__SEARCH_FIELDS)
        result = self.__igdb.platforms(params)

        return [Platform.as_platform(d) for d in result.body]

    def get_company(self, company_id):
        fields = {"ids": company_id}
        fields.update(self.__COMPANY_FIELDS)
        result = self.__igdb.companies(fields)
        return Company.as_company(result.body[0])
