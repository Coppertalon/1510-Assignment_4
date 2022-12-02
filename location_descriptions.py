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
    print("As you walk back to your ship you take a moment to clear your mind and relax. 'I can do this' you think to"
          " yourself. I just need to remember to focus and think about the odds."
          " There is no one for you to play against here")
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
    print("As you walk towards the boardwalk you hear the sounds of partying and merriment"
          " in the distance. As you walk along the dock several fishermen offer you the 'fresh' catch pof the day."
          " You know better and ignore them as you continue along."
          " There does not seem to be anyone to play around here.")

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
    print("As you walk around the ports of Waterdeep you enter a largely abandoned area. Empty warehouses surround"
          " you on all sides as you hear the telltale skittering of rats. The air is thick smells of salt and fish."
          " It seems to be an abounded part of the docks and there does not seem to be anyone to play around here.")

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
    print("As you enter a dingy bar you see a number of sea worn sailors looking for an escape while they are docked."
          " Amongst them you see a game of Baldur's bones is in full swing. You may either approach the table and begin"
          " playing or continue your search elsewhere.")

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
    print("You walk into the must disgusting and run-down tavern you have ever seen. A mix of tired folk without much"
          " money and those with nowhere else to go make up the patronage. A group of me in cloaks seem to be playing "
          " dice and eagerly beckon you over to their table, their eyes lighting up at the prospect of a new player"
          " to freshen up the game.  You may either approach the table and begin "
          "playing or continue your search elsewhere.")

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
    print("You walk into a tavern that seems to be in decent shape, the bar is clean, the fire is lit, and the smell of"
          " fresh food wafts out from the kitchen. The average folk of the docks seem to come here after a long"
          " day seem to relax. You see a group of dock workers playing a game of Baldur's Bones. Recognizing you as"
          " one of their own, they gesture for you to join.  You may either approach the table and begin"
          " playing or continue your search elsewhere.")

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
    print("You enter one of the more upscale taverns along the docks, where adventuters who are hard up on cash go when"
          " they arrive in port. The clientelle is a mix of these adventurers and the more well to do of the docks,"
          " ships captains, warehouse manages, shopkeepers and the ilk. A group of rowdy adventures who seem to have"
          " had a bit too much to drink welcome you to their table to join their game of dice."
          " You may either approach the table and begin playing or continue your search elsewhere.")

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
    print("As you walk along the boardwalk you can't help but notice a few deckhands playing dice on one of the crates"
          " that litter the piers. From the outside they look like a bunch of ruffians or perhaps those who are down"
          " on their luck, but you recognise the rough and stained cloaks they wear as a fine way to keep the cold and"
          " damp of the sea from infecting the soul. Recognising your kinship with these kind you nod to them "
          " as you walk.  You may either approach the table and begin playing or continue your search elsewhere.")

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
    print("You enter a town square, the smell of freshly baked pies and roasting meats enters your nostrils"
          " As you top to admire the beautiful fountain you take a moment to relax and close your eyes."
          " Feeling refreshed and determined you decide to move onwards."
          " There does not seem to be anyone to play around here.")

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
    print("You walk down a  narrow alleyway, the sun above blocked by the buildings that begin to squeeze inwards"
          " by your sides. Small rodents scurry between broken furniture and other refuse that litters the street."
          " As you walk you swear that you saw someone look at you from behind the curtain of one of the windows that"
          " line the street. You get a feeling it is probably a good idea to move along."
          " There does not seem to be anyone to play around here.")

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
    print("As you walk down one of the main commercial ways of the city, you admire the wealth that is on display in a"
          " port city like Waterdeep. Fine cafes and restaurants line the street, the smell of delicious masterpieces "
          " would cost a weeks work on your ship fills wafts around you. You look at brilliant sculpted cakes,"
          " masterfully decorated pastries, and perfectly roasted meat on spits as you admire the scenery."
          " There does not seem to be anyone to play around here.")

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
    print("Entering one of the finer shopping districts within the city, you are taken by the extravagance around"
          " each corner. You pass beautiful fine clothing, perfectly tailored to manicures, weapons honed to the finest"
          " of edges and perfectly crafted tools with handles that fit you palm perfectly. Incredible magical phenomena"
          " of the natural world dazzles you senses and you are amazed and puzzled my items enchanted by magic that do"
          " the impossible. You could spend a lifetime here but alas you have work to do."
          " There does not seem to be anyone to play around here.")

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
    print("As you walk the uneven cobbled streets you can't help but overhear the cheerful din of music and laughter."
          " Somewhere nearby a tavern is in full swing of celebration. A little early for your tastes but the chance to"
          " prove yourself is all the intoxication you need. Now if only you could find where they were, but alas the"
          " maze of packed buildings makes it hard to pin-point the noise."
          " There does not seem to be anyone to play around here.")

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
    print("As you walk into the side entrance of the tavern you are stunned by a young creature with bright red skin"
          " who appears to be playing the fiddle. The air in the room is electric as the creature enters another "
          " quick and energetic song about a young halfling lad who outplayed a devil in a competition of song."
          " The crowd seems absolutely enraptured and there is no sign of the man you are here to play"
          " There does not seem to be anyone to play around here.")

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
    print("You walk into the main entrance of the tavern and see a large wooden plaque hanging over the bar with"
          " a picture of a swirling black portal. A gnome sitting at the front calls out to you, 'bartenders busy right"
          " noy, if you want a drink, you'll have to wait.' If your looking for Volo he's in the back somewhere making"
          " a ruckus. There does not seem to be anyone to play around here.")

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
    print("As you walk through the tavern you notice a large well sitting INSIDE the tavern. As you go to investigate"
          " the bartender - a talk half-orc with a finely groomed mustache and goatee - call out to you."
          " 'Oy there, that there is the Yawning Portal. Leads to the most dangerous dungeon this side of the coast"
          " it does. Best not go pocking around it unless you want to fall in. "
          " If you are looking for Volo I know he is somewhere around here.'"
          " You decide its probably best for you to leave it for now and look around."
          " There does not seem to be anyone to play around here.")

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
