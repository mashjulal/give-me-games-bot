# -*- coding: UTF-8 -*-


COMMANDS = {"/start": "show welcome message",
            "/find_game": "find games",
            "/random_game": "show random game",
            "/help": "show all commands with descriptions"}


class Template:

    class Command:
        NAME_DESCRIPTION = "{command}: {command_description}"

        NAME_COMMAND = "<b>{name}</b> -> /{command}{id}"

    @staticmethod
    def get_searching_result_message(igdb_handler, command, query):
        result = None

        if command == "game":
            result = igdb_handler.search_game(query)
        elif command == "company":
            result = igdb_handler.search_company(query)
        elif command == "genre":
            result = igdb_handler.search_genre(query)
        elif command == "platform":
            result = igdb_handler.search_platform(query)

        msg = None
        if len(result) != 0:
            msg = "\n".join(
                [Template.Command.NAME_COMMAND.format(
                    name=res_obj.name, command=command, id=res_obj.id)
                    for res_obj in result])

        return msg


class Emoji:

    HELLO = u'\U0001F603'
    SORRY = u'\U0001F614'
    COLD_SWEAT = u'\U0001F613'


class Message:

    WELCOME = "Hello, I'm a search bot who can " \
                  "help you to choose a game for playing." + Emoji.HELLO + \
                  "This good guys create a whole site with " \
                  "games: https://www.igdb.com. I'm getting games from them. "\
                  "To start searching input key word and request:\n" \
                  "<b>[game|company|genre|platform]</b> {your request}"

    NO_RESULT = "Sorry, no matches were found." + Emoji.SORRY

    WRONG_QUERY = "Sorry, can't understand you." + Emoji.COLD_SWEAT
