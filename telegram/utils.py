# -*- coding: UTF-8 -*-

from telebot import types


COMMANDS = {"/start": "show welcome message",
            "/find_game": "find games",
            "/random_game": "show random game",
            "/help": "show all commands with descriptions"}


class Keyboard:

    BUTTON_TEXT_DEVELOPERS = "Developers"
    BUTTON_TEXT_GENRES = "Genres"
    BUTTON_TEXT_PLATFORMS = "Platforms"
    BUTTON_TEXT_EXPANSIONS = "Expansions"

    @staticmethod
    def get_game_keyboard(game):
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

        if game.developers:
            keyboard.add(types.ReplyKeyboardMarkup(Keyboard.BUTTON_TEXT_DEVELOPERS))

        if game.genres:
            keyboard.add(types.ReplyKeyboardMarkup(Keyboard.BUTTON_TEXT_GENRES))

        if game.platforms:
            keyboard.add(types.ReplyKeyboardMarkup(Keyboard.BUTTON_TEXT_PLATFORMS))

        if game.expansions:
            keyboard.add(types.ReplyKeyboardMarkup(Keyboard.BUTTON_TEXT_EXPANSIONS))

        return keyboard

    @staticmethod
    def get_keyboard_hider():
        return types.ReplyKeyboardRemove()


class Template:

    class Game:
        NAME = "<b>{game_name}</b>"
        NAME_COMMAND = "<b>{game_name}</b> -> /game{game_id}"
        DESCRIPTION = "\n{game_summary}"
        RATING = "\n<b>Rating: </b>{game_rating}/100"
        SITE = "\n<b>{website_name}:</b> {website_url}"

    class Command:
        NAME_DESCRIPTION = "{command}: {command_description}"


class Emoji:

    HELLO = u'\U0001F603'
    SORRY = u'\U0001F614'


class Message:

    WELCOME = "Hello, I'm a search bot who can " \
                  "help you to choose a game for playing." \
                  "This good guys create a whole site with " \
                  "games: https://www.igdb.com. I'm getting games from them. "\
                  "To find a game simply input it's name." + Emoji.HELLO

    NO_GAMES = "Sorry, no games were found." + Emoji.SORRY
