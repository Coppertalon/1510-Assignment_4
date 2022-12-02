"""
Assignment 4 Location Helper functions
"""
import random
import location_descriptions
import gameplay


def location_finder(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int]) -> \
                    tuple[int, bool]:
    """
    takes the players location on the map and finds if it has been visited or which location pool it should look for.
    
    if a player has already visited a location it will send them to that location.
    if it is a battle it will send a marker of whether the battle was beat or not.
    
    :param maps: dictionary
    :param player_character: dictionary
    :precondition: player_character and maps are set dictionaries and will have all needed values
    :postcondition: get updated player character and map based on location, 
                    get the outcome of the location and if the player wants to quit
    :return: dictionary, dictionary, integer, boolean
    """
    location = maps["map_locations"][player_character["player_position"][0]][player_character["player_position"][1]]

    locations = [location_descriptions.location_start_back, location_easy, location_hard,
                 location_descriptions.location_end, location_port, location_city, location_yawning_portal]

    location_options = ["1", "2", "3", "4", "p", "c", "y"]

    for i in range(0, 7):
        if location == location_options[i]:
            return locations[i](maps, player_character)

    if maps["map_visual"][player_character["player_position"][0]][player_character["player_position"][1]] == "!":
        outcome, quitter = location(maps, player_character, done=False)
        return outcome, quitter

    else:
        outcome, quitter = location(maps, player_character, done=True)
        return outcome, quitter


def location_port(maps:
                  dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                  player_character:
                  dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int]) -> \
                  tuple[int, bool]:
    """
    randomly assign the players current location one of the port locations and send them to that location.
    
    takes a list of locations by location type in maps and removes one of the locations at random, it then assigns that 
    location to the map so it will be returned to in the future. then send the player to the function for that location.
    
    :param maps: dictionary
    :param player_character: dictionary
    :precondition: player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map with the location function name, get updated player character based on location, 
                    get the outcome of the location and if the player wants to quit
    :return: dictionary, dictionary, integer, boolean
    """
    random_location = random.randint(0, (len(maps["locations"]["port"])-1))
    location = maps["locations"]["port"][random_location]
    del maps["locations"]["port"][random_location]

    outcome, quitter = location(maps, player_character)
    return outcome, quitter


def location_city(maps:
                  dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                  player_character:
                  dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int]) -> \
                  tuple[int, bool]:
    """
    randomly assign the players current location one of the city locations and send them to that location.

    takes a list of locations by location type in maps and removes one of the locations at random, it then assigns that 
    location to the map so it will be returned to in the future. then send the player to the function for that location.

    :param maps: dictionary
    :param player_character: dictionary
    :precondition: player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map with the location function name, get updated player character based on location, 
                    get the outcome of the location and if the player wants to quit
    :return: dictionary, dictionary, integer, boolean
    """
    random_location = random.randint(0, (len(maps["locations"]["city"])-1))
    location = maps["locations"]["city"][random_location]
    del maps["locations"]["city"][random_location]

    outcome, quitter = location(maps, player_character)
    return outcome, quitter


def location_yawning_portal(maps: dict
                            [str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                            player_character:
                            dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int]) -> \
                            tuple[int, bool]:
    """
    randomly assign the players current location one of the final bar locations and send them to that location.

    takes a list of locations by location type in maps and removes one of the locations at random, it then assigns that 
    location to the map so it will be returned to in the future. then send the player to the function for that location.

    :param maps: dictionary
    :param player_character: dictionary
    :precondition: player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map with the location function name, get updated player character based on location, 
                    get the outcome of the location and if the player wants to quit
    :return: dictionary, dictionary, integer, boolean
    """
    random_location = random.randint(0, (len(maps["locations"]["yawn"])-1))
    location = maps["locations"]["yawn"][random_location]
    del maps["locations"]["yawn"][random_location]

    outcome, quitter = location(maps, player_character)
    return outcome, quitter


def location_easy(maps:
                  dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                  player_character:
                  dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int]) -> \
                  tuple[int, bool]:
    """
    randomly assign the players current location one of the easy bar locations and send them to that location.

    takes a list of locations by location type in maps and removes one of the locations at random, it then assigns that 
    location to the map so it will be returned to in the future. then send the player to the function for that location.

    :param maps: dictionary
    :param player_character: dictionary
    :precondition: player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map with the location function name, get updated player character based on location, 
                    get the outcome of the location and if the player wants to quit
    :return: dictionary, dictionary, integer, boolean
    """

    random_location = random.randint(0, (len(maps["locations"]["easy"])-1))
    location = maps["locations"]["easy"][random_location]
    del maps["locations"]["easy"][random_location]
    outcome, quitter = location(maps, player_character)
    return outcome, quitter


def location_hard(maps:
                  dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                  player_character:
                  dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int]) ->\
                  tuple[int, bool]:
    """
    randomly assign the players current location one of the hard bar locations and send them to that location.

    takes a list of locations by location type in maps and removes one of the locations at random, it then assigns that 
    location to the map so it will be returned to in the future. then send the player to the function for that location.

    :param maps: dictionary
    :param player_character: dictionary
    :precondition: player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map with the location function name, get updated player character based on location, 
                    get the outcome of the location and if the player wants to quit
    :return: dictionary, dictionary, integer, boolean
    """
    random_location = random.randint(0, (len(maps["locations"]["difficult"])-1))
    location = maps["locations"]["difficult"][random_location]
    del maps["locations"]["difficult"][random_location]

    outcome, quitter = location(maps, player_character)
    return outcome, quitter


def dont_use_location(location_type: str) -> None:
    """
    take and display the status of a location that has been explored, a fight that is beaten / too easy / too hard.

    :param location_type: string
    :precondition: location type must be a string in ["easy", "hard", "explored", "beat"
    :postcondition: print the location status
    :return: none
    """
    if location_type == "easy":
        print("The players at this location do are not notable enough to be worth playing.")
        input("Press enter to continue")
    if location_type == "hard":
        print("You are not renowned enough to fight the players at this location.")
        input("Press enter to continue")
    if location_type == "explored":
        print("You have already been here.")
        input("Press enter to continue")
    if location_type == "beat":
        print("You have already beat the players at this location.")
        input("Press enter to continue")
    return


def mark_location(maps:
                  dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                  player_character:
                  dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                  location_name, location_name_map: str) -> None:
    """
    take the players position and update the maps.
    
    update the map of locations with the name of the location function that corresponds to that location.
    then update the visual map with a single character representing that location type.
    
    :param maps: a dictionary
    :param player_character: a dictionary
    :param location_name: a function
    :param location_name_map: a string
    :precondition: location_name must be the name of a location function, location_name must be a single character
                   player_character and maps are set dictionaries and will have all needed values
    :postcondition: update the map dictionary values: map_visual and map_locations
    :return: dictionary
    """
    maps["map_visual"][player_character["player_position"][0]][player_character["player_position"][1]] \
        = location_name_map
    maps["map_locations"][player_character["player_position"][0]][player_character["player_position"][1]] \
        = location_name
    return


def non_combat_location() -> bool:
    """
    give the user the choice to move or quit from a non-combat location.

    :postcondition: return boolean for if the user choose to quit or not
    :return: boolean
    """
    choice = "none"
    while choice not in ["1", "2"]:
        choice = input("1: Move \n2: Quit\n")
        if choice == "1":
            return True

        if choice == "2":
            return False

        else:
            print("That is not a valid choice.")


def combat_location(maps:
                    dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                    player_character:
                    dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                    location, difficulty: int) ->\
                        tuple[int, bool]:
    """
    give the user the choice to move quit or fight from a combat location.
    
    :param maps: dictionary
    :param player_character: dictionary
    :param location: function
    :param difficulty: int
    :precondition: difficulty must be a positive integer, location must be the name of a location function
                   player_character and maps are set dictionaries and will have all needed values
    :postcondition: return the result of if there was a battle, updated player_character, and if they player quit
    :return: dictionary, dictionary, integer, boolean
    """
    choice = "none"
    while choice not in ["1", "2", "3"]:
        choice = input("1: Play \n2: Leave \n3: Quit\n")
        if choice == "1":
            print("You sit down at the table and being a game of Baldur's Bones.")
            return gameplay.battle_starter(maps, player_character, location, difficulty)

        if choice == "2":
            mark_location(maps, player_character, location, "!")
            return 0, True

        if choice == "3":
            return 0, False

        else:
            print("That is not a valid choice.")


def location_check_easy(maps:
                        dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                        player_character:
                        dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                        done: bool, location) -> bool:
    """
    check if a location is too easy for the player or has been explored and update the map if necessary.
    
    if a player has already beaten a location or is too low a level for a location then it will inform the player and
    update the map if necessary then return a true to stop the player from fighting. otherwise it returns false.
    
    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :param location: a function
    :precondition: location must be the name of a location function,
                   player_character and maps are set dictionaries and will have all needed values
    :postcondition: call the appropriate function and return if the player can battle at that location
    :return: dictionary, dictionary, boolean
    """
    if done:
        dont_use_location("beat")
        return True

    elif player_character["level"] > 1:
        mark_location(maps, player_character, location, "!")
        dont_use_location("easy")
        return True

    else:
        return False


def location_check_hard(maps:
                        dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
                        player_character:
                        dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
                        done: bool, location) -> bool:
    """
    check if a location is too hard for the player or has been explored and update the map if necessary.

    if a player has already beaten a location or is too high level for a location then it will inform the player and
    update the map if necessary then return a true to stop the player from fighting. otherwise it returns false.

    :param maps: a dictionary
    :param player_character: a dictionary
    :param done: a boolean
    :param location: a function
    :precondition: location must be the name of a location function,
                   player_character and maps are set dictionaries and will have all needed values
    :postcondition: call the appropriate function and return if the player can battle at that location
    :return: dictionary, dictionary, boolean
    """
    if done:
        dont_use_location("beat")
        return True

    elif player_character["level"] == 1:
        mark_location(maps, player_character, location, "!")
        dont_use_location("hard")
        return True

    else:
        return False
