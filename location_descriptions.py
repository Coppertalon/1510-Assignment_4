"""
Assignment 4 Location Description functions
"""
import game
import map_and_user
import location_callers
import gameplay


def location_start_back() -> None:

    """
    print the description of the start then return the player

    :precondition: player_character and maps are set dictionaries and will have all needed values
    :postcondition: inform the user they have returned to the start and return them to the move menu
    :return: dictionary, dictionary, int
    """
    print("start")
    input("press Enter to continue")
    return


def location_port_1(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> tuple[int, bool]:
    """
    update the map of locations, let the player choose to move or quit, then return (outcome) that no combat occurred.
    
    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :precondition: done must represent if a player has already been to this location
                   player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map of locations, get the choice of the player, state no combat happened
    :return: dictionary, dictionary, boolean
    """
    location_callers.mark_location(maps, player_character, location_port_1, "P")
    print("port_1")

    if done:
        location_callers.dont_use_location("found")

    quitter = location_callers.non_combat_location()
    outcome = 0

    return outcome, quitter


def location_port_2(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> tuple[int, bool]:
    """
    update the map of locations, let the player choose to move or quit, then return (outcome) that no combat occurred.

    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :precondition: done must represent if a player has already been to this location
                    player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map of locations, get the choice of the player, state no combat happened
    :return: dictionary, dictionary, boolean
    """
    location_callers.mark_location(maps, player_character, location_port_2, "P")
    print("port_2")

    if done:
        location_callers.dont_use_location("found")

    quitter = location_callers.non_combat_location()
    outcome = 0

    return outcome, quitter


def location_easy_1(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> tuple[int, bool]:
    """
    update the map of locations, let the player choose to move, battle or quit
     
    if the player moves or quits, return that no combat happened and the appropriate quit variable (true = quit).
    otherwise call the combat and return the result
     
    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :precondition: done must represent if a player has already been to this location
                   player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map of locations, get the choice of the player, 
                    call combat if necessary and return the outcome of the location
    :return: dictionary, dictionary, boolean
    """
    print("easy_1")

    stop = location_callers.location_check_easy(maps, player_character, done, location_easy_1)

    if stop:
        return 0, False

    map_and_user.player_stats(player_character)

    outcome, quitter = location_callers.combat_location(maps, player_character, location_easy_1, difficulty=15)

    return outcome, quitter


def location_easy_2(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> tuple[int, bool]:
    """
    update the map of locations, let the player choose to move, battle or quit

    if the player moves or quits, return that no combat happened and the appropriate quit variable (true = quit).
    otherwise call the combat and return the result

    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :precondition: done must represent if a player has already been to this location
                    player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map of locations, get the choice of the player, 
                    call combat if necessary and return the outcome of the location
    :return: dictionary, dictionary, boolean
    """
    print("easy_2")

    stop = location_callers.location_check_easy(maps, player_character, done, location_easy_2)

    if stop:
        return 0, False

    map_and_user.player_stats(player_character)

    outcome, quitter = location_callers.combat_location(maps, player_character, location_easy_2, difficulty=15)

    return outcome, quitter


def location_easy_3(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> tuple[int, bool]:
    """
    update the map of locations, let the player choose to move, battle or quit

    if the player moves or quits, return that no combat happened and the appropriate quit variable (true = quit).
    otherwise call the combat and return the result

    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :precondition: done must represent if a player has already been to this location
                    player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map of locations, get the choice of the player, 
                    call combat if necessary and return the outcome of the location
    :return: dictionary, dictionary, boolean
    """
    print("easy_3")

    stop = location_callers.location_check_easy(maps, player_character, done, location_easy_3)

    if stop:
        return 0, False
    map_and_user.player_stats(player_character)

    outcome, quitter = location_callers.combat_location(maps, player_character, location_easy_3, difficulty=16)

    return outcome, quitter


def location_easy_4(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> tuple[int, bool]:
    """
    update the map of locations, let the player choose to move, battle or quit

    if the player moves or quits, return that no combat happened and the appropriate quit variable (true = quit).
    otherwise call the combat and return the result

    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :precondition: done must represent if a player has already been to this location
                   player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map of locations, get the choice of the player, 
                    call combat if necessary and return the outcome of the location
    :return: dictionary, dictionary, boolean
    """
    print("easy_4")

    stop = location_callers.location_check_easy(maps, player_character, done, location_easy_4)

    if stop:
        return 0, False

    map_and_user.player_stats(player_character)

    outcome, quitter = location_callers.combat_location(maps, player_character, location_easy_4, difficulty=16)

    return outcome, quitter


def location_easy_5(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> tuple[int, bool]:
    """
    update the map of locations, let the player choose to move, battle or quit

    if the player moves or quits, return that no combat happened and the appropriate quit variable (true = quit).
    otherwise call the combat and return the result

    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :precondition: done must represent if a player has already been to this location
                   player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map of locations, get the choice of the player, 
                    call combat if necessary and return the outcome of the location
    :return: dictionary, dictionary, boolean
    """
    print("easy_5")

    maps, player_character, stop = location_callers.location_check_easy(maps, player_character, done, location_easy_5)

    if stop:
        return 0, False

    map_and_user.player_stats(player_character)

    outcome, quitter = location_callers.combat_location(maps, player_character, location_easy_5, difficulty=16)

    return outcome, quitter


def location_city_1(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> tuple[int, bool]:
    """
    update the map of locations, let the player choose to move or quit, then return (outcome) that no combat occurred.

    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :precondition: done must represent if a player has already been to this location
                    player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map of locations, get the choice of the player, state no combat happened
    :return: dictionary, dictionary, boolean
    """
    location_callers.mark_location(maps, player_character, location_city_1, "C")
    print("city_1")

    if done:
        location_callers.dont_use_location("found")

    quitter = location_callers.non_combat_location()
    outcome = 0

    return outcome, quitter


def location_city_2(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> tuple[int, bool]:
    """
    update the map of locations, let the player choose to move or quit, then return (outcome) that no combat occurred.

    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :precondition: done must represent if a player has already been to this location
                       player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map of locations, get the choice of the player, state no combat happened
    :return: dictionary, dictionary, boolean
    """
    location_callers.mark_location(maps, player_character, location_city_2, "C")
    print("city_2")

    if done:
        location_callers.dont_use_location("found")

    quitter = location_callers.non_combat_location()
    outcome = 0

    return outcome, quitter


def location_city_3(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> tuple[int, bool]:
    """
    update the map of locations, let the player choose to move or quit, then return (outcome) that no combat occurred.

    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :precondition: done must represent if a player has already been to this location
                   player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map of locations, get the choice of the player, state no combat happened
    :return: dictionary, dictionary, boolean
    """
    location_callers.mark_location(maps, player_character, location_city_3, "C")
    print("city_3")

    if done:
        location_callers.dont_use_location("found")

    quitter = location_callers.non_combat_location()
    outcome = 0

    return outcome, quitter


def location_city_4(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> tuple[int, bool]:
    """
    update the map of locations, let the player choose to move or quit, then return (outcome) that no combat occurred.

    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :precondition: done must represent if a player has already been to this location
                   player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map of locations, get the choice of the player, state no combat happened
    :return: dictionary, dictionary, boolean
    """
    location_callers.mark_location(maps, player_character, location_city_4, "C")
    print("city_4")

    if done:
        location_callers.dont_use_location("found")

    quitter = location_callers.non_combat_location()
    outcome = 0

    return outcome, quitter


def location_city_5(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> tuple[int, bool]:
    """
    update the map of locations, let the player choose to move or quit, then return (outcome) that no combat occurred.

    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :precondition: done must represent if a player has already been to this location
                    player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map of locations, get the choice of the player, state no combat happened
    :return: dictionary, dictionary, boolean
    """
    location_callers.mark_location(maps, player_character, location_city_5, "C")
    print("city_5")

    if done:
        location_callers.dont_use_location("found")

    quitter = location_callers.non_combat_location()
    outcome = 0

    return outcome, quitter


def location_difficult_1(maps:
                         dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                         player_character:
                         dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                         done=None) -> tuple[int, bool]:
    """
    update the map of locations, let the player choose to move, battle or quit

    if the player moves or quits, return that no combat happened and the appropriate quit variable (true = quit).
    otherwise call the combat and return the result

    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :precondition: done must represent if a player has already been to this location
                   player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map of locations, get the choice of the player, 
                    call combat if necessary and return the outcome of the location
    :return: dictionary, dictionary, boolean
    """
    print("difficult_1")

    stop = location_callers.location_check_hard(maps, player_character, done, location_difficult_1)

    if stop:
        return 0, False

    map_and_user.player_stats(player_character)

    outcome, quitter = location_callers.combat_location(maps, player_character, location_difficult_1, difficulty=17)

    return outcome, quitter


def location_difficult_2(maps:
                         dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                         player_character:
                         dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                         done=None) -> tuple[int, bool]:
    """
    update the map of locations, let the player choose to move, battle or quit

    if the player moves or quits, return that no combat happened and the appropriate quit variable (true = quit).
    otherwise call the combat and return the result

    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :precondition: done must represent if a player has already been to this location
                   player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map of locations, get the choice of the player, 
                    call combat if necessary and return the outcome of the location
    :return: dictionary, dictionary, boolean
    """
    print("difficult_2")

    stop = location_callers.location_check_hard(maps, player_character, done, location_difficult_2)

    if stop:
        return 0, False

    map_and_user.player_stats(player_character)

    outcome, quitter = location_callers.combat_location(maps, player_character, location_difficult_2, difficulty=17)

    return outcome, quitter


def location_difficult_3(maps:
                         dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                         player_character:
                         dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                         done=None) -> tuple[int, bool]:
    """
    update the map of locations, let the player choose to move, battle or quit

    if the player moves or quits, return that no combat happened and the appropriate quit variable (true = quit).
    otherwise call the combat and return the result

    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :precondition: done must represent if a player has already been to this location
                   player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map of locations, get the choice of the player, 
                    call combat if necessary and return the outcome of the location
    :return: dictionary, dictionary, boolean
    """
    print("difficult_3")

    stop = location_callers.location_check_hard(maps, player_character, done, location_difficult_3)

    if stop:
        return 0, False

    map_and_user.player_stats(player_character)

    outcome, quitter = location_callers.combat_location(maps, player_character, location_difficult_3, difficulty=17)

    return outcome, quitter


def location_difficult_4(maps:
                         dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                         player_character:
                         dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                         done=None) -> \
                         tuple[int, bool]:
    """
    update the map of locations, let the player choose to move, battle or quit

    if the player moves or quits, return that no combat happened and the appropriate quit variable (true = quit).
    otherwise call the combat and return the result

    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :precondition: done must represent if a player has already been to this location
                   player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map of locations, get the choice of the player, 
                    call combat if necessary and return the outcome of the location
    :return: dictionary, dictionary, boolean
    """
    print("difficult_4")

    stop = location_callers.location_check_hard(maps, player_character, done, location_difficult_4)

    if stop:
        return 0, False
    map_and_user.player_stats(player_character)

    outcome, quitter = location_callers.combat_location(maps, player_character, location_difficult_4, difficulty=17)

    return outcome, quitter


def location_difficult_5(maps:
                         dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                         player_character:
                         dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                         done=None) -> tuple[int, bool]:
    """
    update the map of locations, let the player choose to move, battle or quit

    if the player moves or quits, return that no combat happened and the appropriate quit variable (true = quit).
    otherwise call the combat and return the result

    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :precondition: done must represent if a player has already been to this location
                   player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map of locations, get the choice of the player, 
                    call combat if necessary and return the outcome of the location
    :return: dictionary, dictionary, boolean
    """
    print("difficult_5")

    stop = location_callers.location_check_hard(maps, player_character, done, location_difficult_5)

    if stop:
        return 0, False

    map_and_user.player_stats(player_character)

    outcome, quitter = location_callers.combat_location(maps, player_character, location_difficult_5, difficulty=17)

    return outcome, quitter


def location_difficult_6(maps:
                         dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                         player_character:
                         dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                         done=None) -> tuple[int, bool]:
    """
    update the map of locations, let the player choose to move, battle or quit

    if the player moves or quits, return that no combat happened and the appropriate quit variable (true = quit).
    otherwise call the combat and return the result

    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :precondition: done must represent if a player has already been to this location
                   player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map of locations, get the choice of the player, 
                    call combat if necessary and return the outcome of the location
    :return: dictionary, dictionary, boolean
    """
    print("difficult_6")

    stop = location_callers.location_check_hard(maps, player_character, done, location_difficult_6)

    if stop:
        return 0, False

    map_and_user.player_stats(player_character)

    outcome, quitter = location_callers.combat_location(maps, player_character, location_difficult_6, difficulty=18)

    return outcome, quitter


def location_difficult_7(maps:
                         dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                         player_character:
                         dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                         done=None) -> tuple[int, bool]:
    """
    update the map of locations, let the player choose to move, battle or quit

    if the player moves or quits, return that no combat happened and the appropriate quit variable (true = quit).
    otherwise call the combat and return the result

    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :precondition: done must represent if a player has already been to this location
                   player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map of locations, get the choice of the player, 
                    call combat if necessary and return the outcome of the location
    :return: dictionary, dictionary, boolean
    """
    print("difficult_7")

    stop = location_callers.location_check_hard(maps, player_character, done, location_difficult_7)

    if stop:
        return 0, False

    map_and_user.player_stats(player_character)

    outcome, quitter = location_callers.combat_location(maps, player_character, location_difficult_7, difficulty=18)

    return outcome, quitter


def location_difficult_8(maps:
                         dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                         player_character:
                         dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                         done=None) -> tuple[int, bool]:
    """
    update the map of locations, let the player choose to move, battle or quit

    if the player moves or quits, return that no combat happened and the appropriate quit variable (true = quit).
    otherwise call the combat and return the result

    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :precondition: done must represent if a player has already been to this location
                   player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map of locations, get the choice of the player, 
                    call combat if necessary and return the outcome of the location
    :return: dictionary, dictionary, boolean
    """
    print("difficult_8")

    stop = location_callers.location_check_hard(maps, player_character, done, location_difficult_8)

    if stop:
        return 0, False

    map_and_user.player_stats(player_character)

    outcome, quitter = \
        location_callers.combat_location(maps, player_character, location_difficult_8, difficulty=18)

    return outcome, quitter


def location_yawning_1(maps:
                       dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                       player_character:
                       dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                       done=None) -> tuple[int, bool]:
    """
    update the map of locations, let the player choose to move or quit, then return (outcome) that no combat occurred.

    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :precondition: done must represent if a player has already been to this location
                   player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map of locations, get the choice of the player, state no combat happened
    :return: dictionary, dictionary, boolean
    """
    location_callers.mark_location(maps, player_character, location_yawning_1, "Y")
    print("yawn_1")

    if done:
        location_callers.dont_use_location("found")

    quitter = location_callers.non_combat_location()
    outcome = 0

    return outcome, quitter


def location_yawning_2(maps:
                       dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                       player_character:
                       dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                       done=None) -> tuple[int, bool]:
    """
    update the map of locations, let the player choose to move or quit, then return (outcome) that no combat occurred.

    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :precondition: done must represent if a player has already been to this location
                       player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map of locations, get the choice of the player, state no combat happened
    :return: dictionary, dictionary, boolean
    """
    location_callers.mark_location(maps, player_character, location_yawning_2, "Y")
    print("yawn_2")

    if done:
        location_callers.dont_use_location("found")

    quitter = location_callers.non_combat_location()
    outcome = 0

    return outcome, quitter


def location_yawning_3(maps:
                       dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                       player_character:
                       dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                       done=None) -> tuple[int, bool]:
    """
    update the map of locations, let the player choose to move or quit, then return (outcome) that no combat occurred.

    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :precondition: done must represent if a player has already been to this location
                   player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map of locations, get the choice of the player, state no combat happened
    :return: dictionary, dictionary, boolean
    """
    location_callers.mark_location(maps, player_character, location_yawning_3, "Y")
    print("yawn_3")

    if done:
        location_callers.dont_use_location("found")

    quitter = location_callers.non_combat_location()
    outcome = 0

    return outcome, quitter


def location_end(player_character:
                 dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int]) -> \
                 tuple[int, bool]:
    """
    final boss battle. will return the player to movement if they are too low a level.
    
    the player will fight the boss in a best two out of three, with the roll to beat increasing the more they win.
    after the game ends it will call a function to inform the player of the outcome.
    
    :param player_character: dictionary
    :precondition: player_character and maps are set dictionaries and will have all needed values
    :postcondition: have a score for the battle and call the function to inform player of outcome 
    :return: dictionary, dictionary, int
    """
    print("As you walk to the back of the tavern the noise begins to swell. Sitting at the center of attention"
          " is a human with a well trimmed beard wearing a puffy white shirt and a small black cap."
          " Were it not for the crowd around him who hang on his words and laugh at his every joke he would not"
          " seem particularly notable. However as you approach, you are drawn in by his natural charisma"
          " and pleasant demeanor.")
    if player_character["level"] > 2:
        print(" As you approach he seems to pick you out of the crowd and says: "
              "'Well greeting there my young friend, you look like an enterprising fellow."
              "Care for a game of Baldur's Bones?'")
        print("Drawn in by his natural charm, you feel you cannot resist and take a seat at the table as one of his"
              " admirers stands. He rolls up his sleeves and draws a black leather cup from a poutch at his side"
              " and scoops up the finely carved ivory dice from the table."
              " 'As is custom I believe that you would roll first': ")
        print("Drawn in with no chance to refuse, the game for your chance to finally become a captain begins.")
        score = 0
        rounds = 0

        while score < 2 and rounds < 3:
            roll, player_character = gameplay.game_set_up(player_character)

            if (19 + score) < roll < 22:
                score += 1
                print("win")

            else:
                score -= 1
                print("lose")
            print(score)
            rounds += 1

        game.final_dialogue(score)
        return 0, False

    print("He does not seem to notice you and continues the friendly conversation with those at his table"
          "You are not renowned enough to play against the legendary Volo.")
    return 0, False
