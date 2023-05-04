# Game Recommendation System This is a simple game recommendation system that allows users to find games by platform,
# type, and year. The system contains a database of games and their details, such as the platform, release year,
# type, and rating
# Search by platform: Users can search for games by platform and get a list of games that are available on that
# platform. Search by type: Users can search for games by type and get a list of games that fall under that category.
# Search by year: Users can search for games by year and get a list of games that were released in that year. Highest
# rated game on platform: Users can find the highest rated game on a specific platform. Average rating of type: Users
# can find the average rating of games of a specific type across all platforms. Newest game by type: Users can find
# the newest game of a specific type. Recommendation by platform: Users can get a list of recommended games based on
# a specific platform and their ratings.


class GameKB:
    games = {}

    def __init__(self):
        self.games = {
            "Mortal Kombat": {"type": "Fighting", "platform": "Multiple", "release_year": 1992, "rating": 4.3},
            "Fortnite": {"type": "Battle Royale", "platform": "Multiple", "release_year": 2017, "rating": 4.0},
            "The Legend of Zelda: Breath of the Wild": {"type": "Action-adventure", "platform": "Nintendo Switch",
                                                        "release_year": 2017, "rating": 4.5},
            "Overwatch": {"type": "Hero shooter", "platform": "Multiple", "release_year": 2016, "rating": 4.2},
            "Grand Theft Auto V": {"type": "Action-adventure", "platform": "Multiple", "release_year": 2013,
                                   "rating": 4.8},
            "World of Warcraft": {"type": "MMORPG", "platform": "PC", "release_year": 2004, "rating": 4.7},
            "Call of Duty: Warzone": {"type": "Battle Royale", "platform": "Multiple", "release_year": 2020,
                                      "rating": 3.9},
            "Super Mario Bros.": {"type": "Platformer", "platform": "Nintendo Switch", "release_year": 1985,
                                  "rating": 4.6},
            "Apex Legends": {"type": "Hero shooter", "platform": "Multiple", "release_year": 2019, "rating": 4.1},
            "Minecraft": {"type": "Sandbox", "platform": "Multiple", "release_year": 2011, "rating": 4.4},
            "Dark Souls": {"type": "Action RPG", "platform": "Multiple", "release_year": 2011, "rating": 4.3},
            "Destiny 2": {"type": "MMORPG", "platform": "Multiple", "release_year": 2017, "rating": 4.0},
            "Rainbow Six Siege": {"type": "Tactical shooter", "platform": "Multiple", "release_year": 2015,
                                  "rating": 4.2},
            "Resident Evil Village": {"type": "Survival horror", "platform": "Multiple", "release_year": 2021,
                                      "rating": 4.2},
            "Among Us": {"type": "Social deduction", "platform": "Multiple", "release_year": 2018, "rating": 4.0},
            "Mass Effect Legendary Edition": {"type": "Action RPG", "platform": "Multiple", "release_year": 2021,
                                              "rating": 4.5},
            "Hades": {"type": "Action RPG", "platform": "Multiple", "release_year": 2020, "rating": 4.7},
            "Valorant": {"type": "Hero shooter", "platform": "PC", "release_year": 2020, "rating": 4.2},
            "Genshin Impact": {"type": "Action RPG", "platform": "Multiple", "release_year": 2020, "rating": 4.3},
            "The Witcher 3: Wild Hunt": {"type": "Action RPG", "platform": "Multiple", "release_year": 2015,
                                         "rating": 4.0},
            "Red Dead Redemption 2": {"type": "Action-adventure", "platform": "Multiple", "release_year": 2018,
                                      "rating": 4.9},
            "Final Fantasy VII Remake": {"type": "Action RPG", "platform": "PlayStation 4", "release_year": 2020,
                                         "rating": 4.7},
            "Horizon Zero Dawn": {"type": "Action RPG", "platform": "PlayStation 4", "release_year": 2017,
                                  "rating": 4.8},
            "Persona 5": {"type": "Role-playing", "platform": "PlayStation 4", "release_year": 2016, "rating": 4.7},
            "The Last of Us Part II": {"type": "Action-adventure", "platform": "PlayStation 4", "release_year": 2020,
                                       "rating": 4.8},
            "Assassin's Creed Valhalla": {"type": "Action RPG", "platform": "Multiple", "release_year": 2020,
                                          "rating": 4.3},
            "Demon's Souls": {"type": "Action RPG", "platform": "PlayStation 5", "release_year": 2020, "rating": 4.8},
            "Stardew Valley": {"type": "Simulation", "platform": "Multiple", "release_year": 2016, "rating": 4.8},
            "Splatoon 2": {"type": "Third-person shooter", "platform": "Nintendo Switch", "release_year": 2017,
                           "rating": 4.7},
            "Hollow Knight": {"type": "Metroidvania", "platform": "Multiple", "release_year": 2017, "rating": 4.6},
            "Civilization VI": {"type": "Turn-based strategy", "platform": "Multiple", "release_year": 2016,
                                "rating": 4.5},
            "Subnautica": {"type": "Survival", "platform": "Multiple", "release_year": 2018, "rating": 4.7},
            "Ori and the Will of the Wisps": {"type": "Platformer", "platform": "Multiple", "release_year": 2020,
                                              "rating": 4.6},
            "Factorio": {"type": "Simulation", "platform": "PC", "release_year": 2020, "rating": 4.9},
            "Cities: Skylines": {"type": "Simulation", "platform": "Multiple", "release_year": 2015, "rating": 4.7},
            "Bioshock Infinite": {"type": "First-person shooter", "platform": "Multiple", "release_year": 2013,
                                  "rating": 4.6},
            "FIFA 22": {"type": "Sports", "platform": "Multiple", "release_year": 2021, "rating": 4.1},
            "Cyberpunk 2077": {"type": "Action RPG", "platform": "Multiple", "release_year": 2020, "rating": 3.2},
            "Monster Hunter Rise": {"type": "Action RPG", "platform": "Nintendo Switch", "release_year": 2021,
                                    "rating": 4.4},
            "Mario Kart 8 Deluxe": {"type": "Racing", "platform": "Nintendo Switch", "release_year": 2017,
                                    "rating": 4.7},
            "Civilization V": {"type": "Turn-based strategy", "platform": "Multiple", "release_year": 2010,
                               "rating": 4.2},
            "Nier Automata": {"type": "Action RPG", "platform": "Multiple", "release_year": 2017, "rating": 4.7},
            "Star Wars Jedi: Fallen Order": {"type": "Action-adventure", "platform": "Multiple", "release_year": 2019,
                                             "rating": 4.6},
            "Super Smash Bros. Ultimate": {"type": "Fighting", "platform": "Nintendo Switch", "release_year": 2018,
                                           "rating": 4.8},
            "Death Stranding": {"type": "Action", "platform": "Multiple", "release_year": 2019, "rating": 4.1},
            "Battlefield 2042": {"type": "First-person shooter", "platform": "Multiple", "release_year": 2021,
                                 "rating": 4.2},
            "The Elder Scrolls V: Skyrim": {"type": "Action RPG", "platform": "Multiple", "release_year": 2011,
                                            "rating": 4.7},
            "Bloodborne": {"type": "Action RPG", "platform": "PlayStation 4", "release_year": 2015, "rating": 4.7},
            "Dead by Daylight": {"type": "Survival horror", "platform": "Multiple", "release_year": 2016,
                                 "rating": 4.1},
            "Starcraft II": {"type": "Real-time strategy", "platform": "PC", "release_year": 2010, "rating": 4.2}
        }

    #  Assuming the game database is stored in the variable "gamesKB"
    #  Find all games that are available on "Xbox"
    #  xbox_games = game_database.get_games_by_platform("Xbox")
    #  print(xbox_games)  # Output: ["Halo", "Gears of War", "Forza Horizon"]
    #  Find all games that are available on "PC"
    #  pc_games = game_database.get_games_by_platform("PC")
    #  print(pc_games)  # Output: ["The Sims 4", "Minecraft", "Fortnite"]
    def get_games_by_platform(self, platform):
        platform_games = [game for game in self.games if self.games[game]["platform"] == platform]
        if platform_games:
            return platform_games
        else:
            return "Sorry, no games found for that platform."

    # Assuming the game database is stored in the variable "game_database"
    # Get information about the game "Halo"
    # game_info = game_database.get_type_and_platform_by_game("Halo")
    # print(game_info)  # Output: "Halo is a first-person shooter game on Xbox."
    # Get information about the game "The Legend of Zelda"
    # game_info = game_database.get_type_and_platform_by_game("The Legend of Zelda")
    # print(game_info)  # Output: "Sorry, that game is not in our database."
    def get_type_and_platform_by_game(self, game):
        if game in self.games:
            game_type = self.games[game]["type"]
            game_platform = self.games[game]["platform"]
            return f"{game} is a {game_type} game on {game_platform}."
        else:
            return "Sorry, that game is not in our database."

    # Assuming the game database is stored in the variable "game_database"
    # Find all action games
    # action_games = game_database.get_games_by_type("action")
    # print(action_games)  # Output: ["Halo", "Gears of War"]
    # Find all simulation games
    # simulation_games = game_database.get_games_by_type("simulation")
    # print(simulation_games)  # Output: ["The Sims 4"]
    def get_games_by_type(self, game_type):
        type_games = [game for game in self.games if self.games[game]["type"] == game_type]
        if type_games:
            return type_games
        else:
            return "Sorry, no games found for that type."

    def highest_rated_game_on_platform(self, platform):
        # Returns the name and information of the highest rated game on a given platform.
        platform_games = [(name, game) for name, game in GameKB.games if game['platform'] == platform]
        if not platform_games:
            return "Sorry, there are no games on that platform in the database."
        highest_rated_game = max(platform_games, key=lambda x: x[1]['rating'])
        return f"The highest rated game on {platform} is {highest_rated_game[0]} ({highest_rated_game[1]['type']}, {highest_rated_game[1]['year']})."

    # Example usage:
    # print(GameKB.highest_rated_game_on_platform("Xbox"))
    # Output: "The highest rated game on Xbox is Halo (Shooter, 2001)."

    def games_released_in_year(self, year):
        # Returns a list of all games released in a given year.
        released_games = [game for game in self.games if self.games[game]["release_year"] == year]
        # print(released_games)
        if not released_games:
            return "Sorry, there are no games released in that year in the database."
        return released_games

    # Example usage:
    # print(GameKB.games_released_in_year(2007))
    # Output: "The following games were released in 2007:
    #          BioShock (Shooter)
    #          Portal (Puzzle)"
    def average_rating_of_type(self, game_type):
        # Returns the average rating of all games of a given type across all platforms.
        type_games = [game for game in self.games.values() if game.get("type") == game_type and "rating" in game]
        if not type_games:
            return "Sorry, there are no games of that type in the database."
        rating_sum = sum([game['rating'] for game in type_games])
        average_rating = rating_sum / len(type_games)
        return f"The average rating of {game_type} games across all platforms is {average_rating:.2f}."

    # Example usage:
    # print(GameKB.average_rating_of_type("Adventure"))
    # Output: "The average rating of Adventure games across all platforms is 8.20."
    def newest_game_of_type(self, game_type):
        # Filter the games by type and store in type_games list
        type_games = [(name, game) for name, game in GameKB.games if game['type'] == game_type]
        # If no games of that type are found, return an error message
        if not type_games:
            return "Sorry, there are no games of that type in the database."
        # Find the newest game by sorting by year and returning the max
        newest_game = max(type_games, key=lambda x: x[1]['year'])
        # Return the newest game information in a formatted string
        return f"The newest {game_type} game is {newest_game[0]} (released on {newest_game[1]['platform']} in {newest_game[1]['year']})."

    def newest_game_by_type(self, game_type):
        newest_game = None
        # Loop through each game in the database
        for game, details in self.games.items():
            # Check if the game matches the requested type (ignoring case)
            if details['type'] == game_type:
                # If no newest game has been found yet or if this game is newer, store it as the newest game
                if newest_game is None or details['release_year'] > newest_game['release_year']:
                    newest_game = {'name': game, 'platform': details['platform'],
                                   'release_year': details['release_year']}
        # If no games of that type were found, return an error message
        if newest_game is None:
            return f"No {game_type} game found in the database."
        # Otherwise, return the newest game information in a formatted string
        else:
            return f"The newest {game_type} game is {newest_game['name']} released on {newest_game['platform']} in {newest_game['release_year']}."

    def recommendation_game_by_platform(self, platform):
        platform_games = []
        # Loop through each game in the database
        for game, details in self.games.items():
            # Check if the game matches the requested platform (ignoring case)
            if details['platform'] == platform:
                # If so, append the game and its rating to the platform_games list
                platform_games.append((game, details['rating']))
        # Sort the games by rating (highest to lowest)
        platform_games.sort(key=lambda x: x[1], reverse=True)
        # Return the first recommended game based on the platform
        if platform_games:
            return platform_games[0][0]
        else:
            return f"No games found on {platform}."


game_database = GameKB()

# Test success scenarios
print(f"success #1 \n - {game_database.get_type_and_platform_by_game('Mortal Kombat')} \n")
# Expected output: ('Mortal Kombat is a Fighting game on Multiple.')

print(f"success #2 \n - {game_database.get_games_by_type('Battle Royale')} \n")
# Expected output: ['Fortnite', 'Call of Duty: Warzone']

print(f"success #3 \n - {game_database.get_games_by_platform('PC')} \n")
# Expected output: ''World of Warcraft', 'Valorant', 'Factorio', 'Starcraft II''

print(f"success #4 \n - {game_database.games_released_in_year(2017)} \n")
# Expected output: 'The following games were released in 2017:\nSuper Mario Odyssey (platformer)\nHorizon Zero Dawn (
# action RPG)'

print(f"success #5 \n - {game_database.average_rating_of_type('Survival')} \n")
# Expected output: 'The average rating of platformer games across all platforms is 8.93.'

print(f"success #6 \n - {game_database.newest_game_by_type('Sports')} \n")
# Expected output: 'The newest sports game is FIFA 21 (released on various platforms in 2020).'

print(f"success #7 \n - {game_database.recommendation_game_by_platform('Multiple')} \n")
# Expected output: 'The newest sports game is FIFA 21 (released on various platforms in 2020).'


# Test failure scenarios
print(f"failure #1 \n - {game_database.get_type_and_platform_by_game('Mortasasasdasdasd')} \n")
# Expected output: - Sorry, that game is not in our database. e.

print(f"failure #2 \n - {game_database.get_games_by_type('Batasdasdtleasdasd asdasdRoyale')} \n")
# Expected output: - Sorry, no games found for that type.

print(f"failure #3 \n - {game_database.get_games_by_platform('PasdasdC')} \n")
# Expected output:  Sorry, no games found for that platform.

print(f"failure #4 \n - {game_database.games_released_in_year(20171)} \n")
# Expected output: 'Sorry, there are no games released in that year in the database.

print(f"failure #5 \n - {game_database.average_rating_of_type('Surasdasdavival')} \n")
# Expected output: 'Sorry, there are no games of that type in the database. '

print(f"failure #6 \n - {game_database.newest_game_by_type('Sporsdasdasdats')} \n")
# Expected output: 'No Sporsdasdasdats game found in the database.'

print(f"failure #7 \n - {game_database.recommendation_game_by_platform('Multisdasdasdple')} \n")
# Expected output: 'No games found on.'
