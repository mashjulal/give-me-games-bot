import json

from igdb_api_python.igdb import igdb

from objects.Game import Game
from objects.Genre import Genre
from objects.Platform import Platform


class IGDBHandler:

    __FIELDS = {"fields": [
        "name",
        "websites",
        "first_release_date",
        "developers"
                    ]}

    __EXPAND = {"expand": [
        "game",
        "platforms",
        "genres",
        "expansions",
        "developers"
            ]}

    def __init__(self):
        self.__igdb = igdb(self.__load_key())

    @staticmethod
    def __load_key():
        with open("secret-key.json") as f:
            data = f.read()
        return json.loads(data)["key"]

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
        result = self.__igdb.genres({"ids": genres_id, "fields": "name"})
        genres = [Genre.as_genre(d) for d in result.body]
        return genres

    def search_game(self, query):
        params = {"search": query}
        params.update(IGDBHandler.__FIELDS)
        params.update(IGDBHandler.__EXPAND)
        result = self.__igdb.games(params)

        return [Game.as_game(d) for d in result.body]