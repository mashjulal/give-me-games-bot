import unittest
from telegram import utils


class test_telegram(unittest.TestCase):

    def test_add_keyboard(self):
        keyboard = utils.get_game_keyboard()
        print(keyboard.__dict__)


if __name__ == '__main__':
    unittest.main()