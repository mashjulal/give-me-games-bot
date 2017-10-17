import random
from urllib.request import urlopen, Request

import telebot

from igdb.IGDBHandler import IGDBHandler
from config import telegram_token


bot = telebot.TeleBot(telegram_token)
__igdb_handler = IGDBHandler()


@bot.message_handler(commands=["start"])
def hello_user():
    # TODO: add welcome message
    pass


@bot.message_handler(commands=["help"])
def hello_user():
    # TODO: add help message
    pass


@bot.message_handler(commands=["random_game"])
def get_random_game(message):
    global __igdb_handler
    game_id = random.randint(1, 10000)
    game = __igdb_handler.get_game(game_id)

    send_message(game, message.chat.id)


@bot.message_handler(commands=["find_game"])
def find_game(message):
    bot.send_message(message.chat.id, "Input game name:")


@bot.message_handler(regexp="/game\\d+", content_types=["text"])
def get_game(message):
    game_id = int(message.text.replace("/game", ""))
    game = __igdb_handler.get_game(game_id)
    send_message(game, message.chat.id)


@bot.message_handler(content_types=["text"])
def search_game(message):
    games = __igdb_handler.search(message.text)

    bot.send_message(message.chat.id, "\n".join(
        ["<b>{}</b>".format(game.name) +
         " -> " + "/game" + str(game.id) for game in games]), parse_mode="HTML")


def send_message(game, chat_id):
    msg = "<b>{}</b>".format(game.name)

    if game.summary:
        msg += "\n" + "Description: " + game.summary
    if game.rating:
        msg += "\n" + "Rating: " + str(int(game.rating)) + "/100"
    if len(game.websites) != 0:
        msg += "\n" + "Sites: " + "\n" \
               + "\n".join(["{}: {}".format(site.name, site.url) for site in game.websites])
    bot.send_message(chat_id, msg, parse_mode="HTML")

    if game.cover:
        req = Request(game.cover.url, headers={'User-Agent': 'Mozilla/5.0'})
        bot.send_photo(chat_id, urlopen(req).read())