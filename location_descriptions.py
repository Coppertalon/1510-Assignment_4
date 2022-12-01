"""
Assignment 4 Location Description functions
"""
import game
import map_and_user
import location_callers
import gameplay


def location_start_back(maps:
                        dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                        player_character:
                        dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int]) -> \
                        tuple[dict[str: list, str: list,
                              str: dict[str: list, str: list, str: list, str: list, str: list]],
                              dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                              int]:

    """
    print the description of the start then return the player
    
    :param maps: a dictionary
    :param player_character: a dictionary
    :precondition: player_character and maps are set dictionaries and will have all needed values
    :postcondition: inform the user they have returned to the start and return them to the move menu
    :return: dictionary, dictionary, int
    """
    print("start")
    input("press Enter to continue")
    return maps, player_character, 0


def location_port_1(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> \
                    tuple[dict[str: list, str: list,
                          str: dict[str: list, str: list, str: list, str: list, str: list]],
                          dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                          int, bool]:
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

    return maps, player_character, outcome, quitter


def location_port_2(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> \
                    tuple[dict[str: list, str: list,
                          str: dict[str: list, str: list, str: list, str: list, str: list]],
                          dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                          int, bool]:
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

    return maps, player_character, outcome, quitter


def location_easy_1(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> \
                    tuple[dict[str: list, str: list,
                          str: dict[str: list, str: list, str: list, str: list, str: list]],
                          dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                          int, bool]:
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

    maps, player_character, stop = location_callers.location_check_easy(maps, player_character, done, location_easy_1)

    if stop:
        return maps, player_character, 0, False

    map_and_user.player_stats(player_character)

    maps, player_character, outcome, quitter = \
        location_callers.combat_location(maps, player_character, location_easy_1, difficulty=15)

    return maps, player_character, outcome, quitter


def location_easy_2(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> \
                    tuple[dict[str: list, str: list,
                          str: dict[str: list, str: list, str: list, str: list, str: list]],
                          dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                          int, bool]:
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

    maps, player_character, stop = location_callers.location_check_easy(maps, player_character, done, location_easy_2)

    if stop:
        return maps, player_character, 0, False

    map_and_user.player_stats(player_character)

    maps, player_character, outcome, quitter = \
        location_callers.combat_location(maps, player_character, location_easy_2, difficulty=15)

    return maps, player_character, outcome, quitter


def location_easy_3(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> \
                    tuple[dict[str: list, str: list,
                          str: dict[str: list, str: list, str: list, str: list, str: list]],
                          dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                          int, bool]:
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

    maps, player_character, stop = location_callers.location_check_easy(maps, player_character, done, location_easy_3)

    if stop:
        return maps, player_character, 0, False
    map_and_user.player_stats(player_character)

    maps, player_character, outcome, quitter = \
        location_callers.combat_location(maps, player_character, location_easy_3, difficulty=16)

    return maps, player_character, outcome, quitter


def location_easy_4(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> \
                    tuple[dict[str: list, str: list,
                          str: dict[str: list, str: list, str: list, str: list, str: list]],
                          dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                          int, bool]:
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

    maps, player_character, stop = location_callers.location_check_easy(maps, player_character, done, location_easy_4)

    if stop:
        return maps, player_character, 0, False

    map_and_user.player_stats(player_character)

    maps, player_character, outcome, quitter = \
        location_callers.combat_location(maps, player_character, location_easy_4, difficulty=16)

    return maps, player_character, outcome, quitter


def location_easy_5(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> \
                    tuple[dict[str: list, str: list,
                          str: dict[str: list, str: list, str: list, str: list, str: list]],
                          dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                          int, bool]:
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
        return maps, player_character, 0, False

    map_and_user.player_stats(player_character)

    maps, player_character, outcome, quitter = \
        location_callers.combat_location(maps, player_character, location_easy_5, difficulty=16)

    return maps, player_character, outcome, quitter


def location_city_1(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> \
                    tuple[dict[str: list, str: list,
                          str: dict[str: list, str: list, str: list, str: list, str: list]],
                          dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                          int, bool]:
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

    return maps, player_character, outcome, quitter


def location_city_2(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> \
                    tuple[dict[str: list, str: list,
                          str: dict[str: list, str: list, str: list, str: list, str: list]],
                          dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                          int, bool]:
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

    return maps, player_character, outcome, quitter


def location_city_3(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> \
                    tuple[dict[str: list, str: list,
                          str: dict[str: list, str: list, str: list, str: list, str: list]],
                          dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                          int, bool]:
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

    return maps, player_character, outcome, quitter


def location_city_4(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> \
                    tuple[dict[str: list, str: list,
                          str: dict[str: list, str: list, str: list, str: list, str: list]],
                          dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                          int, bool]:
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

    return maps, player_character, outcome, quitter


def location_city_5(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    done=None) -> \
                    tuple[dict[str: list, str: list,
                          str: dict[str: list, str: list, str: list, str: list, str: list]],
                          dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                          int, bool]:
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

    return maps, player_character, outcome, quitter


def location_difficult_1(maps:
                         dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                         player_character:
                         dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                         done=None) -> \
                         tuple[dict[str: list, str: list,
                               str: dict[str: list, str: list, str: list, str: list, str: list]],
                               dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                               int, bool]:
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

    maps, player_character, stop = \
        location_callers.location_check_hard(maps, player_character, done, location_difficult_1)

    if stop:
        return maps, player_character, 0, False

    map_and_user.player_stats(player_character)

    maps, player_character, outcome, quitter = \
        location_callers.combat_location(maps, player_character, location_difficult_1, difficulty=17)

    return maps, player_character, outcome, quitter


def location_difficult_2(maps:
                         dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                         player_character:
                         dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                         done=None) -> \
                         tuple[dict[str: list, str: list,
                               str: dict[str: list, str: list, str: list, str: list, str: list]],
                               dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                               int, bool]:
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

    maps, player_character, stop = \
        location_callers.location_check_hard(maps, player_character, done, location_difficult_2)

    if stop:
        return maps, player_character, 0, False

    map_and_user.player_stats(player_character)

    maps, player_character, outcome, quitter = \
        location_callers.combat_location(maps, player_character, location_difficult_2, difficulty=17)

    return maps, player_character, outcome, quitter


def location_difficult_3(maps:
                         dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                         player_character:
                         dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                         done=None) -> \
                         tuple[dict[str: list, str: list,
                               str: dict[str: list, str: list, str: list, str: list, str: list]],
                               dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                               int, bool]:
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

    maps, player_character, stop = \
        location_callers.location_check_hard(maps, player_character, done, location_difficult_3)

    if stop:
        return maps, player_character, 0, False

    map_and_user.player_stats(player_character)

    maps, player_character, outcome, quitter = \
        location_callers.combat_location(maps, player_character, location_difficult_3, difficulty=17)

    return maps, player_character, outcome, quitter


def location_difficult_4(maps:
                         dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                         player_character:
                         dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                         done=None) -> \
                         tuple[dict[str: list, str: list,
                               str: dict[str: list, str: list, str: list, str: list, str: list]],
                               dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                               int, bool]:
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

    maps, player_character, stop = \
        location_callers.location_check_hard(maps, player_character, done, location_difficult_4)
    if stop:
        return maps, player_character, 0, False
    map_and_user.player_stats(player_character)

    maps, player_character, outcome, quitter = \
        location_callers.combat_location(maps, player_character, location_difficult_4, difficulty=17)

    return maps, player_character, outcome, quitter


def location_difficult_5(maps:
                         dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                         player_character:
                         dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                         done=None) -> \
                         tuple[dict[str: list, str: list,
                               str: dict[str: list, str: list, str: list, str: list, str: list]],
                               dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                               int, bool]:
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

    maps, player_character, stop = \
        location_callers.location_check_hard(maps, player_character, done, location_difficult_5)

    if stop:
        return maps, player_character, 0, False

    map_and_user.player_stats(player_character)

    maps, player_character, outcome, quitter = \
        location_callers.combat_location(maps, player_character, location_difficult_5, difficulty=17)

    return maps, player_character, outcome, quitter


def location_difficult_6(maps:
                         dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                         player_character:
                         dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                         done=None) -> \
                         tuple[dict[str: list, str: list,
                               str: dict[str: list, str: list, str: list, str: list, str: list]],
                               dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                               int, bool]:
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

    maps, player_character, stop = \
        location_callers.location_check_hard(maps, player_character, done, location_difficult_6)

    if stop:
        return maps, player_character, 0, False

    map_and_user.player_stats(player_character)

    maps, player_character, outcome, quitter = \
        location_callers.combat_location(maps, player_character, location_difficult_6, difficulty=18)

    return maps, player_character, outcome, quitter


def location_difficult_7(maps:
                         dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                         player_character:
                         dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                         done=None) -> \
                         tuple[dict[str: list, str: list,
                               str: dict[str: list, str: list, str: list, str: list, str: list]],
                               dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                               int, bool]:
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

    maps, player_character, stop = \
        location_callers.location_check_hard(maps, player_character, done, location_difficult_7)

    if stop:
        return maps, player_character, 0, False

    map_and_user.player_stats(player_character)

    maps, player_character, outcome, quitter = \
        location_callers.combat_location(maps, player_character, location_difficult_7, difficulty=18)

    return maps, player_character, outcome, quitter


def location_difficult_8(maps:
                         dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                         player_character:
                         dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                         done=None) -> \
                         tuple[dict[str: list, str: list,
                               str: dict[str: list, str: list, str: list, str: list, str: list]],
                               dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                               int, bool]:
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

    maps, player_character, stop = \
        location_callers.location_check_hard(maps, player_character, done, location_difficult_8)

    if stop:
        return maps, player_character, 0, False

    map_and_user.player_stats(player_character)

    maps, player_character, outcome, quitter = \
        location_callers.combat_location(maps, player_character, location_difficult_8, difficulty=18)

    return maps, player_character, outcome, quitter


def location_yawning_1(maps:
                       dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                       player_character:
                       dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                       done=None) -> \
                       tuple[dict[str: list, str: list,
                             str: dict[str: list, str: list, str: list, str: list, str: list]],
                             dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                             int, bool]:
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
    location_callers.mark_location(maps, player_character, location_yawning_1, "X")
    print("yawn_1")

    if done:
        location_callers.dont_use_location("found")

    quitter = location_callers.non_combat_location()
    outcome = 0

    return maps, player_character, outcome, quitter


def location_yawning_2(maps:
                       dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                       player_character:
                       dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                       done=None) -> \
                       tuple[dict[str: list, str: list,
                             str: dict[str: list, str: list, str: list, str: list, str: list]],
                             dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                             int, bool]:
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
    location_callers.mark_location(maps, player_character, location_yawning_2, "X")
    print("yawn_2")

    if done:
        location_callers.dont_use_location("found")

    quitter = location_callers.non_combat_location()
    outcome = 0

    return maps, player_character, outcome, quitter


def location_yawning_3(maps:
                       dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                       player_character:
                       dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                       done=None) -> \
                       tuple[dict[str: list, str: list,
                             str: dict[str: list, str: list, str: list, str: list, str: list]],
                             dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                             int, bool]:
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
    location_callers.mark_location(maps, player_character, location_yawning_3, "X")
    print("yawn_3")

    if done:
        location_callers.dont_use_location("found")

    quitter = location_callers.non_combat_location()
    outcome = 0

    return maps, player_character, outcome, quitter


def location_end(maps:
                 dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                 player_character:
                 dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int]) -> \
                 tuple[dict[str: list, str: list,
                       str: dict[str: list, str: list, str: list, str: list, str: list]],
                       dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                       int, bool]:
    """
    final boss battle. will return the player to movement if they are too low a level.
    
    the player will fight the boss in a best two out of three, with the roll to beat increasing the more they win.
    after the game ends it will call a function to inform the player of the outcome.
    
    :param maps: dictionary
    :param player_character: dictionary
    :precondition: player_character and maps are set dictionaries and will have all needed values
    :postcondition: have a score for the battle and call the function to inform player of outcome 
    :return: dictionary, dictionary, int
    """
    if player_character["level"] > 2:
        print("end")
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
        return maps, player_character, 0, False

    print("too low")
    return maps, player_character, 0, False
