import random

import telebot

from igdb.IGDBHandler import IGDBHandler
from config import telegram_token
from telegram import utils

bot = telebot.TeleBot(telegram_token)
igdb_handler = IGDBHandler()


@bot.message_handler(commands=["start"])
def hello_user(message):
    bot.send_message(message.chat.id, utils.Message.WELCOME)
    pass


@bot.message_handler(commands=["help"])
def show_help(message):
    msg = "\n".join([utils.Template.Command.NAME_DESCRIPTION
                    .format(command=c, command_description=c_d)
                     for c, c_d in sorted(utils.COMMANDS.items())])
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=["random_game"])
def get_random_game(message):
    game_id = random.randint(1, 10000)
    game = igdb_handler.get_game(game_id)

    send_message(game, message.chat.id)


@bot.message_handler(commands=["find_game"])
def find_game(message):
    bot.send_message(message.chat.id, "Input game name:")


@bot.message_handler(regexp="/game\\d+", content_types=["text"])
def get_game(message):
    game_id = int(message.text.replace("/game", ""))
    game = igdb_handler.get_game(game_id)
    send_message(game, message.chat.id)


@bot.message_handler(regexp="/company\\d+", content_types=["text"])
def get_company(message):
    company_id = int(message.text.replace("/company", ""))
    company = igdb_handler.get_company(company_id)
    send_message(company, message.chat.id)


@bot.message_handler(regexp="/genre\\d+", content_types=["text"])
def get_genre(message):
    genre_id = int(message.text.replace("/genre", ""))
    genre = igdb_handler.get_genre(genre_id)
    send_message(genre, message.chat.id)


@bot.message_handler(regexp="/platform\\d+", content_types=["text"])
def get_platform(message):
    platform_id = int(message.text.replace("/platform", ""))
    platform = igdb_handler.get_platform(platform_id)
    send_message(platform, message.chat.id)


@bot.message_handler(content_types=["text"])
def search(message):

    msg = None
    if " " in message.text:
        command, query = message.text.split(" ", 1)

        if command == "game":
            games = igdb_handler.search_game(query)
            if len(games) != 0:
                msg = "\n".join(
                    [utils.Template.Command.NAME_COMMAND.format(
                        name=game.name, command="game", id=game.id)
                        for game in games])
        elif command == "company":
            companies = igdb_handler.search_company(query)
            if len(companies) != 0:
                msg = "\n".join(
                    [utils.Template.Command.NAME_COMMAND.format(
                        name=company.name, command="company", id=company.id)
                        for company in companies])
        elif command == "genre":
            genres = igdb_handler.search_genre(query)
            if len(genres) != 0:
                msg = "\n".join(
                    [utils.Template.Command.NAME_COMMAND.format(
                        name=genre.name, command="genre", id=genre.id)
                        for genre in genres])
        elif command == "platform":
            platforms = igdb_handler.search_platform(query)
            if len(platforms) != 0:
                msg = "\n".join(
                    [utils.Template.Command.NAME_COMMAND.format(
                        name=p.name, command="platform", id=p.id)
                        for p in platforms])
    if not msg:
        msg = utils.Message.NO_RESULT

    bot.send_message(chat_id=message.chat.id, text=msg, parse_mode="HTML")


def send_message(obj, chat_id):
    msg = str(obj)
    bot.send_message(chat_id, msg, parse_mode="HTML")
