from IGDBHandler import IGDBHandler

if __name__ == "__main__":
    igdb_handler = IGDBHandler()

    game = igdb_handler.get_game(1942)
    for platform in igdb_handler.get_platforms(game.platforms):
        print(platform.name)

    for genre in igdb_handler.get_genres(game.genres):
        print(genre.name)

