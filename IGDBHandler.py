import json

from igdb_api_python.igdb import igdb

from Game import Game
from Genre import Genre
from Platform import Platform


class IGDBHandler:

    def __init__(self):
        self.__igdb = igdb(self.__load_key())

    @staticmethod
    def __load_key():
        with open("secret-key.json") as f:
            data = f.read()
        return json.loads(data)["key"]

    def get_game(self, game_id):
        result = self.__igdb.games(game_id)
        return Game.as_game(result.body[0])

    def get_platforms(self, platforms_id):
        result = self.__igdb.platforms({ "ids" : platforms_id, "fields" : "name"})
        platforms = [Platform.as_platform(d) for d in result.body]
        return platforms

    def get_genres(self, genres_id):
        result = self.__igdb.genres({ "ids" : genres_id, "fields" : "name"})
        genres = [Genre.as_genre(d) for d in result.body]
        return genres