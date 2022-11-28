"""
Assignment 4
"""
import map_and_user
import gameplay
import location_callers
import location_descriptions


def win():
    print("win text")
    return False


def lose():
    print("lose text")
    return False


def start(maps: dict, player_character: dict):
    location_callers.mark_location(maps, player_character,  "1", "O")

    print("Game Explanation")
    print("Practice battle")
    print("Battle Explanation")

    roll, player_character = gameplay.game_set_up(player_character)
    if 15 < roll < 21:
        print("win")
    else:
        print("lose")

    print("Lore")
    print("Goal")
    input("Press enter to contuinue")

    map_and_user.map_display(maps, player_character)
    print("Goodbye")
    player_character["re_roll"] = 1
    return maps, player_character


def final_dialogue(score: int):
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
    return ["*", "*", "*", "*", "*"]


def play(maps: dict, player_character: dict, run: bool):
    maps, player_character = start(maps, player_character)

    while run:
        map_and_user.map_display(maps, player_character)
        player_character, run = map_and_user.move(player_character)
        map_and_user.map_display(maps, player_character)

        maps, player_character, result, stop = location_callers.location_finder(maps, player_character)
        if stop is False:
            break
        player_character = map_and_user.health(result, player_character)
        player_character, up = map_and_user.experience(result, player_character)

        if up == 1:
            player_character = map_and_user.level_up(player_character)

        if player_character["health"] < 1:
            run = lose()

        if result == 2:
            run = win()
    return


def var():
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

    player_character = {"name": name,
                        "player_position": [4, 0],
                        "health": 3,
                        "level": 0,
                        "exp": 0,
                        "add": 0,
                        "take_away": 0,
                        "re_roll": 0}

    play(maps, player_character, run=True)
    print("Game Over")


def main():
    var()


if __name__ == '__main__':
    main()
