import random

import telebot

from igdb.IGDBHandler import IGDBHandler
from config import telegram_token
from telegram import utils

TEMPLATE_MESSAGE_GAME_NAME = "<b>{game_name}</b>"
TEMPLATE_MESSAGE_SHOW_GAME = "<b>{game_name}</b> -> /game{game_id}"
TEMPLATE_MESSAGE_GAME_DESCRIPTION = "\n{game_summary}"
TEMPLATE_MESSAGE_GAME_RATING = "\n<b>Rating: </b>{game_rating}/100"
TEMPLATE_MESSAGE_GAME_SITE = "\n<b>{website_name}:</b> {website_url}"

MESSAGE_WELCOME = "Hello, I'm a search bot who can " \
                  "help you to choose a game for playing." \
                  "This good guys create a whole site with " \
                  "games: https://www.igdb.com. I'm getting games from them. " \
                  "To find a game simply input it's name."

COMMANDS = {"/start": "show welcome message",
            "/find_game": "find games",
            "/random_game": "show random game",
            "/help": "show all commands with descriptions"}

bot = telebot.TeleBot(telegram_token)
__igdb_handler = IGDBHandler()
current_game = None


@bot.message_handler(commands=["start"])
def hello_user(message):
    bot.send_message(message.chat.id, MESSAGE_WELCOME)
    pass


@bot.message_handler(commands=["help"])
def show_help(message):
    msg = "\n".join(["{command}: {command_description}"
               .format(command=c, command_description=c_d)
           for c, c_d in sorted(COMMANDS.items())])
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=["random_game"])
def get_random_game(message):
    global __igdb_handler
    global current_game
    game_id = random.randint(1, 10000)
    current_game = __igdb_handler.get_game(game_id)

    send_message(current_game, message.chat.id)


@bot.message_handler(commands=["find_game"])
def find_game(message):
    bot.send_message(message.chat.id, "Input game name:")


@bot.message_handler(regexp="/game\\d+", content_types=["text"])
def get_game(message):
    global current_game
    game_id = int(message.text.replace("/game", ""))
    current_game = __igdb_handler.get_game(game_id)
    send_message(current_game, message.chat.id)


@bot.message_handler(content_types=["text"])
def search_game(message):
    games = __igdb_handler.search(message.text)

    if len(games) != 0:
        msg = "\n".join(
            [TEMPLATE_MESSAGE_SHOW_GAME.format(game_name=game.name, game_id=game.id)
             for game in games])
    else:
        msg = "Sorry, no games were found"

    bot.send_message(chat_id=message.chat.id, text=msg, parse_mode="HTML")


def send_message(game, chat_id):
    msg = TEMPLATE_MESSAGE_GAME_NAME.format(game_name=game.name)

    if game.summary:
        msg += TEMPLATE_MESSAGE_GAME_DESCRIPTION.format(game_summary=game.summary)
    if game.rating:
        msg += TEMPLATE_MESSAGE_GAME_RATING.format(game_rating=round(game.rating, 2))
    if len(game.websites) != 0:
        msg += "".join([TEMPLATE_MESSAGE_GAME_SITE
                           .format(website_name=site.name.capitalize(), website_url=site.url)
                            for site in sorted(game.websites, key=lambda w:w.name)])
    keyboard = utils.get_game_keyboard()
    m = bot.send_message(chat_id, msg, parse_mode="HTML",
                         reply_markup=keyboard)
    bot.register_next_step_handler(m, callback=show_more)

    # if game.cover:
    #     req = Request(game.cover_url, headers={'User-Agent': 'Mozilla/5.0'})
    #     bot.send_photo(chat_id, urlopen(req).read())


def show_more(message):
    keyboard_hider = telebot.types.ReplyKeyboardRemove()
    if not current_game:
        return

    command = message.text
    msg = None

    if command == "Developers":
        msg = "<b>Developers:</b>\n"
        for company in current_game.developers:
            msg += company.name + "\n"
            # TODO: add company request
    elif command == "Genres":
        msg = "<b>Genres:</b>\n"
        for genre in current_game.genres:
            msg += genre.name + "\n"
            # TODO: add genre request
    elif command == "Platforms":
        msg = "<b>Platforms:</b>\n"
        for platform in current_game.platforms:
            msg += platform.name + "\n"
            # TODO: add platform request
    elif command == "Expansions":
        msg = "<b>Expansions:</b>\n"
        for expansion in current_game.expansions:
            msg += expansion.name + "\n"
            # TODO: add expansion request

    if msg:
        bot.send_message(chat_id=message.chat.id,
                         text=msg,
                         parse_mode="HTML",
                         reply_markup=keyboard_hider)