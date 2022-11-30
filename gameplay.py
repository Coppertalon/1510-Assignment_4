"""
Assignment 4 Gameplay functions
"""
import random
import location_callers


def battle_starter(maps: dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                   player_character:
                   dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                   location, roll_to_beat: int) -> \
                   tuple[dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                         dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                         int, bool]:
    """
    Takes the difficulty of a battle from a location and starts the battle then prints the result afterwards.
    
    :param maps: a dictionary
    :param player_character: a dictionary
    :param location: a function name
    :param roll_to_beat: an integer
    :preconditon: roll_to_beat must be greater than 0, location must be a function name,
                    maps and player character are set dictionaries and contain all needed values
    :postcondition: determine weather a player won or lost their battle and print the result
    :return: a dictionary, a dictionary, an int, and a boolean
    """

    roll, player_character = game_set_up(player_character)

    if roll_to_beat < roll < 22:
        location_callers.mark_location(maps, player_character, location, "@")
        print("win")
        return maps, player_character, 1, True

    else:
        location_callers.mark_location(maps, player_character, location, "!")
        print("lose")
        return maps, player_character, -1, True


def game_set_up(player_character:
                dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int]) \
                -> tuple[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int]:

    """
    create the players starting roll then inform them of their total and update it based on their actions.
    
    :param player_character: a dictionary
    :precondtion: player character is a set dictionary and contain all needed values
    :postcondition: find the total of the players rolls after the game and return it
    :return: an int
    """
    rolls = [random.randint(1, 6) for i in range(3)]
    print("\nYou rolled :", rolls)
    total = rolls[0] + rolls[1] + rolls[2]

    action = "roll"
    roll = rolls[2]

    while total < 27 and action != "hold":
        print("\n")
        print(total)

        if total > 21:
            print("You are currently over the max roll")

        print("Level 1 Skills:  re-rolls: ", player_character["re_roll"])

        if player_character["level"] > 1:
            print("Level 2 Skills:  add 1 to roll:", player_character["add"],
                  "remove 1 from roll:", player_character["take_away"])

        total, roll, action, player_character = game_choices(player_character, total, roll)

    return total, player_character


def game_choices(player_character:
                 dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                 total: int, roll: int) ->\
                 tuple[int, int, str,
                       dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int]]:

    """
    inform the player of their choices and call the function to check if it valid and perform it.
    
    :param player_character: a dictionary 
    :param total: int
    :param roll:  int
    :precondition: total and roll must be positive integers, 
                  player character is a set dictionary and contain all needed values
    :postcondition: return the total, roll, game action, and player updated based on the game action taken
    :return: an int, an int, a string, and a dictionary
    """

    moves1 = ["roll", "re-roll", "hold"]
    moves2 = ["roll", "re-roll",  "hold",  "add", "take_away"]

    if player_character["level"] == 1:
        print_choice = iter(moves1)
        for number, option in enumerate(range(len(moves1)), 1):
            print(number, next(print_choice))
        choice = input("moves1 \n")

    else:
        print_choice = iter(moves2)
        for number, option in enumerate(range(len(moves2)), 1):
            print(number, next(print_choice))
        choice = input("moves2 \n")

    if (choice in ["1", "2", "3"] and player_character["level"] == 1) \
            or (choice in ["1", "2", "3", "4", "5"] and player_character["level"] > 1):

        total, roll, action, player_character, = game_actions(total, roll, player_character, action=choice)
        return total, roll, action, player_character

    else:
        print("bad choice")
        return total, roll, "none", player_character


def game_actions(total: int, roll: int, player_character:
                 dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int], action: str)\
                 -> tuple[int, int, str,
                          dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int]]:
    """
    takes the users choice of action and performs it if it is valid. otherwise inform the player it is not.
    
    :param total: integer
    :param roll:  integer
    :param player_character: a dictionary 
    :param action: string
    :precondition: roll and total must be positive integers, action must be in ["1", "2", "3", "4", "5"] 
                   player character is a set dictionary and contains all needed values
    :return: int, int, sting, dictionary
    """
    if action == "1":
        total, roll, action, player_character = rolling(total, roll, action, player_character)
        return total, roll, action, player_character

    elif action == "2" and player_character["re_roll"] > 0:
        total, roll, action, player_character = rolling(total, roll, action, player_character)
        return total, roll, action, player_character

    elif action == "3":
        return total, roll, "hold", player_character

    elif action == "4" and player_character["add"] > 0:
        total, roll, action, player_character = total_modify(total, roll, action, player_character)
        return total, roll, action, player_character

    elif action == "5" and player_character["take_away"] > 0:
        total, roll, action, player_character = total_modify(total, roll, action, player_character)
        return total, roll, action, player_character

    else:
        print("you can't do that")
        return total, roll, "none", player_character


def rolling(total: int, roll: int, action: str,
            player_character: dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int]) \
            -> tuple[int, int, str,
                     dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int]]:
    """
    re-roll the previous roll or roll again and add to the total.

    :param total: integer
    :param roll: integer
    :param action: string
    :param player_character: dictionary
    :precondition: total and roll must be positive, action must be "1" or "2",
                   player character is a set dictionary and contains all needed values
    :postcondition: modify the total based on the chosen action
    :return: int, int, string, dictionary
    """
    if action == "1":
        roll = random.randint(1, 6)
        total += roll
        print(roll)
        return total, roll, "none", player_character

    elif action == "2":
        total -= roll
        roll = random.randint(1, 6)
        total += roll
        print(roll)
        player_character["re_roll"] -= 1
        return total, roll, "none", player_character


def total_modify(total: int, roll: int, action: str,
                 player_character:
                 dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int]) \
                 -> tuple[int, int, str,
                          dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int]]:
    """
    add 1 to the total or take away 1 from the total.
    
    :param total: integer
    :param roll: integer
    :param action: string
    :param player_character: dictionary
    :precondition: total and roll must be positive, action must be "4" or "5",
                   player character is a set dictionary and contains all needed values
    :postcondition: modify the total based on the chosen action
    :return: int, int, string, dictionary
    """
    if action == "4":
        total += 1
        player_character["add"] -= 1
        return total, roll, "none", player_character

    if action == "5":
        total -= 1
        player_character["take_away"] -= 1
        return total, roll, "none", player_character
