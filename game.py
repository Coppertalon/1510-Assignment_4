"""
Assignment 4 Base Function
"""
import map_and_user
import gameplay
import location_callers
import location_descriptions


def win() -> bool:
    """
    Displays the winning text for when a user beats the game then returns false to stop the game loop

    :postcondition: display the win game message
    :return: boolean false
    """
    print("win text")

    return False


def lose() -> bool:
    """
    Displays the winning text for when a user loses the game then returns false to stop the game loop

    :postcondition: display the lose game message
    :return: boolean false
    """
    print("lose text")

    return False


def start(maps: dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
          player_character: dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int])\
          -> None:
    """
    Introduces the player to the game world and their goal then plays a practice round with no consequences.

    :param maps: a dictionary of the games maps
    :param player_character: a dictionary of the players characteristics
    :precondition: player_character and maps are set dictionaries and will have all needed values
    :postconditon: add 1 to "re-roll" and return player_character and map
    :return: updated map and player dictionaries
    """
    location_callers.mark_location(maps, player_character,  "1", "O")

    print("Game Explanation")
    print("Practice Battle")
    print("Battle Explanation")
    input("Press enter to continue")

    roll, player_character = gameplay.game_set_up(player_character)

    if 15 < roll < 22:
        print("\n \nwin")
    else:
        print("\n \nlose")

    print("Lore")
    print("Goal")
    input("Press enter to continue")

    player_character["re_roll"] = 1

    return


def final_dialogue(score: int) -> int:
    """
    Print unique dialog depending on how the final battle then return a value to show if the player won or lost.

    :param score: an int
    :precondition: score should always be [-2, -1, 1, 2]
    :postconditon: print text and return an int representing if a player won [2] or lost [-2]
    :return: int
    """
    if score == -2:
        print("hard loss")
        return -2

    if score == -1:
        print("close loss")
        return -2

    if score == 1:
        print("close win")
        return 2

    if score == 2:
        print("solid win")
        return 2


def map_maker(user_map: list):
    """
    makes a list item a list of "*"'s - called only as part of a map function.

    :param user_map: a list
    :preconditon: user_map should be a list inside a list
    :return: a list of five "*"
    """
    return ["*", "*", "*", "*", "*"]


def play(maps: dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
         player_character: dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
         run: bool) -> None:
    """
    Primary gameplay loop of the game. takes the player to the tutorial then enters a loop of the following:

    display the map, let the player move, show mapa again, take the player to that location, check if they quit
    update player health and experience, update level if necessary, check if the player won or lost the game.

    :param maps: a dictionary
    :param player_character: a dictionary
    :param run: a boolean
    :precondition: maps must contain the game maps, player_character must contain player stats, run = True
    :postcondition: have run the game and displayed if the player won or lost the game
    :return: none
    """
    start(maps, player_character)

    while run:

        map_and_user.map_display(maps, player_character)
        run = map_and_user.move_decider(player_character)
        map_and_user.map_display(maps, player_character)

        outcome, quitter = location_callers.location_finder(maps, player_character)

        if quitter is False:
            break

        map_and_user.health(outcome, player_character)
        up = map_and_user.experience(outcome, player_character)

        if up == 1:
            map_and_user.level_up(player_character)

        if player_character["health"] < 1:
            run = lose()

        if outcome == 2:
            run = win()

    return


def var():
    """
    Initialize all variables for the game. Print game over when game stops

    :postcondition: all game variables are initialized, game over is printed
    """
    locations = {"port": [location_descriptions.location_port_1, location_descriptions.location_port_2],
                 "easy": [location_descriptions.location_easy_1, location_descriptions.location_easy_2,
                          location_descriptions.location_easy_3, location_descriptions.location_easy_4,
                          location_descriptions.location_easy_5],

                 "city": [location_descriptions.location_city_1, location_descriptions.location_city_2,
                          location_descriptions.location_city_3, location_descriptions.location_city_4,
                          location_descriptions.location_city_5],

                 "difficult": [location_descriptions.location_difficult_1, location_descriptions.location_difficult_2,
                               location_descriptions.location_difficult_3, location_descriptions.location_difficult_4,
                               location_descriptions.location_difficult_5, location_descriptions.location_difficult_6,
                               location_descriptions.location_difficult_7, location_descriptions.location_difficult_8],

                 "yawn": [location_descriptions.location_yawning_1,
                          location_descriptions.location_yawning_2,
                          location_descriptions.location_yawning_3]}

    player_map = list(map(map_maker, [[], [], [], [], []]))
    maps = {"map_visual": player_map,

            "map_locations": [["3", "3", "3", "y", "4"],
                              ["c", "c", "3", "y", "y"],
                              ["2", "2", "c", "3", "3"],
                              ["p", "2", "2", "c", "3"],
                              ["1", "p", "2", "c", "3"]],

            "locations": locations}

    name = input("player name \n")
    print("Hello", name, ", Welcome to Baldur's Bones")
    player_character = {"name": name,
                        "player_position": [4, 0],
                        "health": 3,
                        "level": 1,
                        "exp": 0,
                        "add": 0,
                        "take_away": 0,
                        "re_roll": 0}

    play(maps, player_character, run=True)
    print("Game Over")


def main():
    """driver"""
    var()


if __name__ == '__main__':
    main()
