from telebot import types


def get_game_keyboard():
    game_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    for command in ["Developers", "Genres", "Platforms", "Expansions"]:
        game_keyboard.add(types.KeyboardButton(command))

    return game_keyboard
