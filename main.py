from IGDBHandler import IGDBHandler

if __name__ == "__main__":
    igdb_handler = IGDBHandler()

    game = igdb_handler.get_game(1942)
    for platform_id in game.platforms:
        platform = igdb_handler.get_platform(platform_id)
        print(platform.name)

    for genre_id in game.genres:
        genre = igdb_handler.get_genre(genre_id)
        print(genre.name)

