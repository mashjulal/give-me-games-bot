from IGDBHandler import IGDBHandler

if __name__ == "__main__":
    igdb_handler = IGDBHandler()
    game = igdb_handler.get_game_by_id(1942)
