# -*- coding: UTF-8 -*-


COMMANDS = {"/start": "show welcome message",
            "/find_game": "find games",
            "/random_game": "show random game",
            "/help": "show all commands with descriptions"}


class Template:

    class Command:
        NAME_DESCRIPTION = "{command}: {command_description}"

        NAME_COMMAND = "<b>{name}</b> -> /{command}{id}"


class Emoji:

    HELLO = u'\U0001F603'
    SORRY = u'\U0001F614'


class Message:

    WELCOME = "Hello, I'm a search bot who can " \
                  "help you to choose a game for playing." \
                  "This good guys create a whole site with " \
                  "games: https://www.igdb.com. I'm getting games from them. "\
                  "To find a game simply input it's name." + Emoji.HELLO

    NO_RESULT = "Sorry, no matches were found." + Emoji.SORRY
