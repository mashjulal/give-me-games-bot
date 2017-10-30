import random

import telebot

from igdb.IGDBHandler import IGDBHandler
from config import telegram_token
from telegram import utils

bot = telebot.TeleBot(telegram_token)
igdb_handler = IGDBHandler()


@bot.message_handler(commands=["start"])
def hello_user(message):
    send_message(utils.Message.WELCOME, message.chat.id)


@bot.message_handler(commands=["help"])
def show_help(message):
    msg = "\n".join([utils.Template.Command.NAME_DESCRIPTION
                    .format(command=c, command_description=c_d)
                     for c, c_d in sorted(utils.COMMANDS.items())])
    send_message(msg, message.chat.id)


@bot.message_handler(commands=["random_game"])
def get_random_game(message):
    game_id = random.randint(1, 10000)
    game = igdb_handler.get_game(game_id)

    send_message(game, message.chat.id)


@bot.message_handler(commands=["find_game"])
def find_game(message):
    send_message("Input game name:", message.chat.id)


@bot.message_handler(func=lambda c: True, regexp="/game\\d+", content_types=["text"])
def get_game(message):
    game_id = int(message.text.replace("/game", ""))
    game = igdb_handler.get_game(game_id)
    send_message(game, message.chat.id)


@bot.message_handler(func=lambda c: True, regexp="/company\\d+", content_types=["text"])
def get_company(message):
    company_id = int(message.text.replace("/company", ""))
    company = igdb_handler.get_company(company_id)
    send_message(company, message.chat.id)


@bot.message_handler(func=lambda c: True, regexp="/genre\\d+", content_types=["text"])
def get_genre(message):
    genre_id = int(message.text.replace("/genre", ""))
    genre = igdb_handler.get_genre(genre_id)
    send_message(genre, message.chat.id)


@bot.message_handler(func=lambda c: True, regexp="/platform\\d+", content_types=["text"])
def get_platform(message):
    platform_id = int(message.text.replace("/platform", ""))
    platform = igdb_handler.get_platform(platform_id)
    send_message(platform, message.chat.id)


@bot.message_handler(content_types=["text"])
def search(message):

    msg = None
    if " " in message.text:
        command, query = message.text.split(" ", 1)
        msg = utils.Template.get_searching_result_message(igdb_handler, command, query)

    if not msg:
        msg = utils.Message.WRONG_QUERY

    send_message(msg, message.chat.id)


def send_message(obj, chat_id):
    msg = str(obj)
    bot.send_message(chat_id, msg, parse_mode="HTML")
