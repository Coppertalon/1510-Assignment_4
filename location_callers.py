import random
import location_descriptions


def location_finder(maps: dict, player_character: dict):
    location = maps["map_locations"][player_character["player_position"][0]][player_character["player_position"][1]]
    locations = [location_descriptions.location_start_back, location_easy, location_hard,
                 location_descriptions.location_end, location_port, location_city, location_yawning_portal]

    location_options = ["1", "2", "3", "4", "p", "c", "y"]

    for i in range(0, 7):
        if location == location_options[i]:
            return locations[i](maps, player_character)

    if maps["map_visual"][player_character["player_position"][0]][player_character["player_position"][1]] == "!":
        return location(maps, player_character, done=False)
    else:
        return location(maps, player_character, done=True)


def location_port(maps: dict, player_character: dict):
    random_location = random.randint(0, (len(maps["locations"]["port"])-1))
    location = maps["locations"]["port"][random_location]
    del maps["locations"]["port"][random_location]
    return location(maps, player_character)


def location_city(maps: dict, player_character: dict):
    random_location = random.randint(0, (len(maps["locations"]["city"])-1))
    location = maps["locations"]["city"][random_location]
    del maps["locations"]["city"][random_location]
    return location(maps, player_character)


def location_yawning_portal(maps: dict, player_character: dict):
    random_location = random.randint(0, (len(maps["locations"]["yawn"])-1))
    location = maps["locations"]["yawn"][random_location]
    del maps["locations"]["yawn"][random_location]
    return location(maps, player_character)


def location_easy(maps: dict, player_character: dict):
    random_location = random.randint(0, (len(maps["locations"]["easy"])-1))
    location = maps["locations"]["easy"][random_location]
    del maps["locations"]["easy"][random_location]
    return location(maps, player_character)


def location_hard(maps: dict, player_character: dict):
    random_location = random.randint(0, (len(maps["locations"]["difficult"])-1))
    location = maps["locations"]["difficult"][random_location]
    del maps["locations"]["difficult"][random_location]
    return location(maps, player_character)


def dont_use_location(location_type: str):
    if location_type == "easy":
        print("too easy")
        input("Press enter to continue")
    if location_type == "hard":
        print("too hard")
        input("Press enter to continue")
    if location_type == "explored":
        print("explored")
        input("Press enter to continue")
    if location_type == "beat":
        print("beaten")
        input("Press enter to continue")
    return


def mark_location(maps: dict, player_character: dict, location_name, location_name_map: str):
    maps["map_visual"][player_character["player_position"][0]][player_character["player_position"][1]] \
        = location_name_map
    maps["map_locations"][player_character["player_position"][0]][player_character["player_position"][1]] \
        = location_name
    return maps
