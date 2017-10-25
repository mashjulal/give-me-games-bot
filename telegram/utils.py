# -*- coding: UTF-8 -*-


COMMANDS = {"/start": "show welcome message",
            "/find_game": "find games",
            "/random_game": "show random game",
            "/help": "show all commands with descriptions"}


class Template:

    class Game:

        NAME = "<b>{game_name}</b>"
        DESCRIPTION = "\n{game_summary}"
        RATING = "\n<b>Rating: </b>{game_rating}/100"
        SITE = "\n<b>{website_name}:</b> {website_url}"
        PLATFORMS = "\n<b>Platforms:</b> {platform_list}"
        GENRES = "\n<b>Genres:</b> {genre_list}"
        DEVELOPERS = "\n<b>Developers:</b> {developer_list}"

        NAME_COMMAND = "<b>{game_name}</b> -> /game{game_id}"

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

            if len(game.genres) != 0:
                msg += Template.Game.GENRES.format(
                    genre_list=", ".join([g.name for g in game.genres]))

            if len(game.platforms) != 0:
                msg += Template.Game.PLATFORMS.format(
                    platform_list=", ".join([p.name for p in game.platforms]))

            if len(game.developers) != 0:
                msg += Template.Game.DEVELOPERS.format(
                    developer_list=", ".join([d.name for d in game.developers]))

            return msg

    class Company:

        NAME = "\n<b>{company_name}</b>"
        DESCRIPTION = "\n{company_summary}"
        COUNTRY = "\n<b>Country:</b> {company_country}"
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
