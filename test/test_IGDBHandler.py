import datetime
import unittest

from igdb.IGDBHandler import IGDBHandler


class TestIGDBHandler(unittest.TestCase):

    _igdb_handler = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls._igdb_handler = IGDBHandler()

    def test_get_game(self):
        game = self._igdb_handler.get_game(1942)

        self.assertEqual(1942, game.id)
        self.assertEqual("The Witcher 3: Wild Hunt", game.name)
        self.assertEqual(datetime.date(2015, 5, 19), game.first_release_date)
        self.assertEqual("https://images.igdb.com/igdb/image/upload/tri1c6vbydeosoqajwt1.jpg",
                         game.cover_url)
        self.assertEqual(98.83106585906918, game.rating)

        websites = [['https://www.twitch.tv/cdprojektred', 'twitch'],
                    ['https://store.steampowered.com/app/292030', 'steam'],
                    ['https://www.youtube.com/user/WitcherGame', 'youtube'],
                    ['https://www.instagram.com/cdpred', 'instagram'],
                    ['https://twitter.com/witchergame', 'twitter'],
                    ['https://www.facebook.com/CDPROJEKTRED', 'facebook'],
                    ['https://en.wikipedia.org/wiki/The_Witcher_3:_Wild_Hunt', 'wikipedia'],
                    ['http://witcher.wikia.com/wiki/The_Witcher_3:_Wild_Hunt', 'wikia'],
                    ['http://thewitcher.com', 'official']]
        for i in range(len(websites)):
            expected_website_name = websites[i][1]
            actual_website_name = game.websites[i].name
            self.assertEqual(expected_website_name, actual_website_name)

            expected_website_url = websites[i][0]
            actual_website_url = game.websites[i].url
            self.assertEqual(expected_website_url, actual_website_url)

        summary = "The Witcher: Wild Hunt is a story-driven, " \
                  "next-generation open world role-playing game " \
                  "set in a visually stunning fantasy universe " \
                  "full of meaningful choices and impactful consequences. " \
                  "In The Witcher you play as the professional monster hunter, " \
                  "Geralt of Rivia, tasked with finding a child of prophecy in a " \
                  "vast open world rich with merchant cities, viking pirate islands, " \
                  "dangerous mountain passes, and forgotten caverns to explore."
        self.assertEqual(summary, game.summary)

        genres = [[12, 'Role-playing (RPG)'],
                  [31, 'Adventure']]
        for i in range(len(genres)):
            expected_genre_id = genres[i][0]
            actual_genre_id = game.genres[i].id
            self.assertEqual(expected_genre_id, actual_genre_id)

            expected_genre_name = genres[i][1]
            actual_genre_name = game.genres[i].name
            self.assertEqual(expected_genre_name, actual_genre_name)

        developers = [['CD Projekt RED', 908]]
        for i in range(len(developers)):
            expected_developer_id = developers[i][1]
            actual_developer_id = game.developers[i].id
            self.assertEqual(expected_developer_id, actual_developer_id)

            expected_developer_name = developers[i][0]
            actual_developer_name = game.developers[i].name
            self.assertEqual(expected_developer_name, actual_developer_name)

        platforms = [[48, 'PlayStation 4'],
                     [49, 'Xbox One'],
                     [6, 'PC (Microsoft Windows)']]
        for i in range(len(platforms)):
            expected_platform_id = platforms[i][0]
            actual_platform_id = game.platforms[i].id
            self.assertEqual(expected_platform_id, actual_platform_id)

            expected_platform_name = platforms[i][1]
            actual_platform_name = game.platforms[i].name
            self.assertEqual(expected_platform_name, actual_platform_name)

    def test_get_platforms(self):
        expected_platforms = [[48, 'PlayStation 4'],
                     [49, 'Xbox One'],
                     [6, 'PC (Microsoft Windows)']]
        platforms = self._igdb_handler.get_platforms([pl[0] for pl in expected_platforms])
        for i in range(len(platforms)):
            expected_platform_id = expected_platforms[i][0]
            actual_platform_id = platforms[i].id
            self.assertEqual(expected_platform_id, actual_platform_id)

            expected_platform_name = expected_platforms[i][1]
            actual_platform_name = platforms[i].name
            self.assertEqual(expected_platform_name, actual_platform_name)

    def test_get_genres(self):
        expected_genres = [[12, 'Role-playing (RPG)'],
                  [31, 'Adventure']]
        genres = self._igdb_handler.get_genres([g[0] for g in expected_genres])
        for i in range(len(expected_genres)):
            expected_genre_id = expected_genres[i][0]
            actual_genre_id = genres[i].id
            self.assertEqual(expected_genre_id, actual_genre_id)

            expected_genre_name = expected_genres[i][1]
            actual_genre_name = genres[i].name
            self.assertEqual(expected_genre_name, actual_genre_name)

    def test_search(self):
        pass


if __name__ == "__main__":
    unittest.main()
