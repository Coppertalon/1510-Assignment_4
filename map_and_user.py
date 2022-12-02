"""
Assignment 4 Map and Player functions
"""


def move_decider(player_character:
                 dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int]) -> bool:
    """
    let the user chose how to move their character or quit the game then call the mover function.
    
    :param player_character: a dictionary
    :precondition: player character is a set dictionary and contain all needed values
    :postcondition: update the player characters location or quit the game
    :return: dictionary, boolean
    """

    valid_moves = ["north", "south", "east", "west", "quit"]
    movement = ""

    while movement not in ["1", "2", "3", "4"]:

        print_choice = iter(valid_moves)
        for number, option in enumerate(range(len(valid_moves)), 1):
            print(number, next(print_choice))
        movement = input("movement \n")

        if movement == "5":
            return False

        if movement in ["1", "2", "3", "4"]:
            player_character, movement = player_mover(player_character, movement)

        else:
            print('"', movement, '"', " is an invalid movement. Please try again")

    return True


def player_mover(player_character:
                 dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                 movement: str) -> str:
    """
    take the users movement and update the character position if it is valid, other wise tell the user it is invalid.
    
    :param player_character: a dictionary
    :param movement: a string
    :precondition: movement is in ["1", "2", "3", "4", "5"]
                  player character is a set dictionary and contain all needed values
    :postcondition: update player character if possible
    :return: dictionary, string
    """
    if movement == "1" and player_character["player_position"][0] > 0:
        player_character["player_position"][0] -= 1

    elif movement == "2" and player_character["player_position"][0] < 4:
        player_character["player_position"][0] += 1

    elif movement == "3" and player_character["player_position"][1] > 0:
        player_character["player_position"][1] -= 1

    elif movement == "4" and player_character["player_position"][1] < 4:
        player_character["player_position"][1] += 1

    else:
        print('"', movement, '"', " is an invalid movement. Please try again")
        movement = "false"

    return movement


def health(outcome: int, player_character:
           dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int]) -> None:
    """
    update the players health based on the outcome of their previous location. 
    
    :param outcome: an int
    :param player_character: a dictionary
    :precondition: outcome must be in [-2, -1, 0, 1, 2]
                   player character is a set dictionary and contain all needed values
    :postcondition: update the players health if it is necessary
    :return: dictionary
    """
    if outcome == -1:
        player_character["health"] = player_character["health"] - 1
        print("lose health message")
        return

    if outcome == -2:
        player_character["health"] = player_character["health"] - 2
        print("lose to boss method")
        return

    else:
        return


def experience(outcome: int, player_character:
               dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int]) -> int:
    """
    update the players experience and level based on their combat and return 1 if they leveled up.

    :param outcome: an int
    :param player_character: a dictionary
    :precondition: outcome must be in [-2, -1, 0, 1, 2]
                       player character is a set dictionary and contain all needed values
    :postcondition: update the players experience and level them up if necessary
    :return: dictionary, int
    """
    if outcome == 1:
        player_character["exp"] = player_character["exp"] + 1

        if player_character["level"] == 1 and player_character["exp"] == 3:
            player_character["level"] = 2
            player_character["exp"] = 0
            return 1

        if player_character["level"] == 2 and player_character["exp"] == 5:
            player_character["level"] = 3
            player_character["exp"] = 0
            return 1

        else:
            return 0
    else:
        return 0


def level_up(player_character: dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int]) \
        -> None:
    """
    update and increase the players stats for leveling up.

    :param player_character: a dictionary
    :precondition: level > 1, player character is a set dictionary and contain all needed values
    :postcondition: health is increased by 1 and abilities are increased by 1 if below maximum.
    :return: dictionary
    """
    if player_character["level"] == 2:
        print("level up 2 message")

    if player_character["level"] == 3:
        print("level up 3 message")

    player_character["health"] = player_character["health"] + 1

    if player_character["re_roll"] <= player_character["level"]:
        player_character["re_roll"] = player_character["re_roll"] + 1

    if player_character["take_away"] < player_character["level"]:
        player_character["take_away"] = player_character["take_away"] + 1

    if player_character["add"] < player_character["level"]:
        player_character["add"] = player_character["add"] + 1

    return


def map_display(maps: dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                player_character:
                dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int])\
                -> None:
    """
    display the map, the players current location, and a legend of the players stats.
    
    :param maps: dictionary
    :param player_character: dictionary
    :precondition:  player_character and maps are set dictionaries and will have all needed values
    :postcondition: display the map as well as the players location and stats
    :return: none
    """
    print("\n \n \n")

    for height in range(len(maps["map_visual"])):
        for width in range(len(maps["map_visual"])):

            if height == player_character["player_position"][0] and width == player_character["player_position"][1]:
                print("#", end="")

            else:
                print(maps["map_visual"][height][width], end="")
        print("")

    print("")
    print("Legend:  * = Unexplored,    # = Player,    ! = Found Bar,   @ = Beaten Bar,")
    print("Legend:  O = Your Ship,    X = Yawning Portal,    P = Found Port,   C = Found City,")

    player_stats(player_character)
    print("")

    return


def player_stats(player_character:
                 dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int]) -> None:
    """
    displays a legend of the players stats and abilities.
    
    :param player_character: dictionary
    :precondition:  player_character is a set dictionary and will have all needed values
    :postcondition: display the users stats
    :return: none
    """
    print("Stats:  Renown:", player_character["level"], "  Reputation:", player_character["exp"],
          "  Credibility:", player_character["health"])
    print("Level 1 Skills:  Re-rolls:", player_character["re_roll"])

    if player_character["level"] > 1:
        print("Level 2 Skills:  Add 1 to roll:", player_character["add"],
              "  Remove 1 from roll:", player_character["take_away"])

    return
