from IGDBHandler import IGDBHandler

if __name__ == "__main__":
    igdb_handler = IGDBHandler()

    game = igdb_handler.get_game(1942)

    for platform in game.platforms:
        print(platform.name)

    for genre in game.genres:
        print(genre.name)

    for website in game.websites:
        print(website.name, website.url)

