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

    def get_platform(self, platform_id):
        result = self.__igdb.platforms({ "ids" : platform_id, "fields" : "name"})
        return Platform.as_platform(result.body[0])

    def get_genre(self, genre_id):
        result = self.__igdb.genres({ "ids" : genre_id, "fields" : "name"})
        return Genre.as_genre(result.body[0])