import json

from igdb_api_python.igdb import igdb

from Game import Game


class IGDBHandler:

    def __init__(self):
        self.__igdb = igdb(self.__load_key())

    @staticmethod
    def __load_key():
        with open("secret-key.json") as f:
            data = f.read()
        return json.loads(data)["key"]

    def get_game_by_id(self, game_id):
        result = self.__igdb.games(game_id)
        return Game.as_game(result.body[0])