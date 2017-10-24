# -*- coding: UTF-8 -*-

from telebot import types


COMMANDS = {"/start": "show welcome message",
            "/find_game": "find games",
            "/random_game": "show random game",
            "/help": "show all commands with descriptions"}


class Keyboard:

    BUTTON_TEXT_DEVELOPERS = Template.Company.TITLE_DEVELOPERS
    BUTTON_TEXT_GENRES = Template.Genre.TITLE
    BUTTON_TEXT_PLATFORMS = Template.Platform.TITLE
    BUTTON_TEXT_EXPANSIONS = Template.Game.TITLE_EXPANSIONS

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

        TITLE_EXPANSIONS = "<b>Expansions:</b>\n"

        NAME = "<b>{game_name}</b>"
        NAME_COMMAND = "<b>{game_name}</b> -> /game{game_id}"
        DESCRIPTION = "\n{game_summary}"
        RATING = "\n<b>Rating: </b>{game_rating}/100"
        SITE = "\n<b>{website_name}:</b> {website_url}"

        @staticmethod
        def format(game):
            msg = Template.Game.NAME.format(
                game_name=game.name)
            if game.summary:
                msg += Template.Game.DESCRIPTION.format(
                    game_summary=game.summary)
            if game.rating:
                msg += Template.Game.RATING.format(
                    game_rating=round(game.rating, 2))
            if len(game.websites) != 0:
                msg += "".join([Template.Game.SITE.format(
                    website_name=site.name.capitalize(),
                    website_url=site.url)
                    for site in sorted(game.websites, key=lambda w: w.name)])
            return msg

    class Company:

        TITLE_DEVELOPERS = "<b>Developers:</b>\n"

        NAME = "<b>{company_name}</b>"
        DESCRIPTION = "\n{company_summary}"
        COUNTRY = "<b>Country:</b> {company_country}"
        SITE = "\n<b>{website_name}:</b> {website_url}"

        @staticmethod
        def format(company):
            msg = Template.Company.NAME.format(
                company_name=company.name)
            if company.description:
                msg += Template.Company.DESCRIPTION.format(
                    company_summary=company.description)
            if company.country:
                msg += Template.Company.COUNTRY.format(
                    company_country=company.country)
            if company.website:
                msg += Template.Company.SITE.format(
                    website_name=company.website.name.capitalize(),
                    website_url=company.website.url)
            return msg

    class Genre:
        TITLE = "<b>Genres:</b>\n"

        NAME = "<b>{genre_name}</b>"

        @staticmethod
        def format(genre):
            msg = Template.Genre.NAME.format(
                genre_name=genre.name)
            return msg

    class Command:
        NAME_DESCRIPTION = "{command}: {command_description}"

        DEVELOPERS = "Developers"
        GENRES = "Genres"
        PLATFORMS = "Platforms"
        EXPANSIONS = "Expansions"

    class Platform:
        TITLE = "<b>Platforms:</b>\n"


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
