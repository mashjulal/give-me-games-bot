# -*- coding: UTF-8 -*-

from telebot import types


COMMANDS = {"/start": "show welcome message",
            "/find_game": "find games",
            "/random_game": "show random game",
            "/help": "show all commands with descriptions"}


def get_game_keyboard():
    game_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    for command in ["Developers", "Genres", "Platforms", "Expansions"]:
        game_keyboard.add(types.KeyboardButton(command))

    return game_keyboard


class Template:

    class Game:
        NAME = "<b>{game_name}</b>"
        NAME_COMMAND = "<b>{game_name}</b> -> /game{game_id}"
        DESCRIPTION = "\n{game_summary}"
        RATING = "\n<b>Rating: </b>{game_rating}/100"
        SITE = "\n<b>{website_name}:</b> {website_url}"


class Emoji:

    HELLO = u'\U0001F603'
    SORRY = u'\U0001F614'


MESSAGE_WELCOME = "Hello, I'm a search bot who can " \
                  "help you to choose a game for playing." \
                  "This good guys create a whole site with " \
                  "games: https://www.igdb.com. I'm getting games from them. "\
                  "To find a game simply input it's name."  + Emoji.HELLO
