import random


def map_display(maps, player_character):
    for height in range(len(maps["map_visual"])):
        for width in range(len(maps["map_visual"])):
            if height == player_character["player_pos"][0] and width == player_character["player_pos"][1]:
                print("#", end="")
            else:
                print(maps["map_visual"][height][width], end="")
        print("")
    print("Legend:")
    return


def move(player_character):
    valid_moves = ["n", "s", "e", "w"]
    movement = ""
    while movement not in valid_moves:
        movement = input("movement \n")

        if movement.lower() in valid_moves:
            if movement == "n":
                player_character["player_pos"][0] += -1
            elif movement == "s":
                player_character["player_pos"][0] += 1
            elif movement == "w":
                player_character["player_pos"][1] -= 1
            elif movement == "e":
                player_character["player_pos"][1] += 1
            else:
                print('"' + movement + '"' + " is an invalid movement. Please try again")

        else:
            print('"' + movement + '"' + " is an invalid movement. Please try again")
    return player_character


def location_finder(maps, player_character):
    location = maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]]
    if location == "1":
        return location_start_back(maps, player_character)
    if location == "2":
        return location_easy(maps, player_character)
    if location == "3":
        return location_hard(maps, player_character)
    if location == "4":
        return location_end(maps, player_character)
    if location == "p":
        return location_port(maps, player_character)
    if location == "c":
        return location_city(maps, player_character)
    if location == "y":
        return location_yawning_portal(maps, player_character)
    else:
        return beaten(maps, player_character, True)


def location_port(maps, player_character):
    random_location = random.randint(0, (len(maps["locations"]["port"])-1))
    location = maps["locations"]["port"][random_location]
    return location(maps, player_character)


def location_city(maps, player_character):
    random_location = random.randint(0, (len(maps["locations"]["city"])-1))
    location = maps["locations"]["city"][random_location]
    return location(maps, player_character)


def location_yawning_portal(maps, player_character):
    random_location = random.randint(0, (len(maps["locations"]["yawn"])-1))
    location = maps["locations"]["yawn"][random_location]
    return location(maps, player_character)


def location_easy(maps, player_character):
    random_location = random.randint(0, (len(maps["locations"]["easy"])-1))
    location = maps["locations"]["easy"][random_location]
    return location(maps, player_character)


def location_hard(maps, player_character):
    random_location = random.randint(0, (len(maps["locations"]["difficult"])-1))
    location = maps["locations"]["difficult"][random_location]
    return location(maps, player_character)


def beaten(maps, player_character, beat):
    location = maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]]
    return location(maps, player_character, beat)


def player_health(battle_health, player_character):
    if battle_health == -1:
        player_character["health"] -= 1
        print("lose health message")
        return player_character["health"]

    if battle_health == -2:
        player_character["health"] -= 2
        print("lose to boss method")
        return player_character["health"]

    if battle_health == 0:
        return player_character["health"]


def experience(battle_exp, player_character):
    if battle_exp != 1:
        return player_character, False
    if battle_exp == 1:
        player_character["exp"] += 1
        if player_character["level"] == 1 and player_character["exp"] == 4:
            player_character["level"] = 2
            player_character["exp"] = 0
            return player_character, True
        if player_character["level"] == 2 and player_character["exp"] == 6:
            player_character["level"] = 3
            player_character["exp"] = 0
            return player_character, True
        else:
            up = False
            return player_character, up


def level_up(player_character):
    if player_character["level"] == 2:
        print("level up 2 message")
    if player_character["level"] == 3:
        print("level up 3 message")
    if player_character["health"] <= 3:
        player_character["health"] += 1
    if player_character["re_rolls"] <= player_character["level"]:
        player_character["re_rolls"] += 1
    if player_character["take_away"] < player_character["level"]:
        player_character["take_away"] += 1
    if player_character["add"] < player_character["level"]:
        player_character["add"] += 1
    return player_character


def lose():
    print("lose text")
    return False


def win():
    print("win text")
    return False


def location_start():
    print("start tutorial")
    return


def location_start_back(maps, player_character):
    print("start")
    return maps, player_character


def location_port_1(maps, player_character, beat=None):
    print("port_1")
    if beat:
        print("return")
    return maps, player_character


def location_port_2(maps, player_character, beat=None):
    print("port_2")
    if beat:
        print("return")
    return maps, player_character


def location_easy_1(maps, player_character, beat=None):
    print("easy_1")
    if beat:
        print("return")
    return maps, player_character


def location_easy_2(maps, player_character, beat=None):
    print("easy_2")
    if beat:
        print("return")
    return maps, player_character


def location_easy_3(maps, player_character, beat=None):
    print("easy_3")
    if beat:
        print("return")
    return maps, player_character


def location_easy_4(maps, player_character, beat=None):
    print("easy_4")
    if beat:
        print("return")
    return maps, player_character


def location_easy_5(maps, player_character, beat=None):
    print("easy_5")
    if beat:
        print("return")
    return maps, player_character


def location_city_1(maps, player_character, beat=None):
    print("city_1")
    if beat:
        print("return")
    return maps, player_character


def location_city_2(maps, player_character, beat=None):
    print("city_2")
    if beat:
        print("return")
    return maps, player_character


def location_city_3(maps, player_character, beat=None):
    print("city_3")
    if beat:
        print("return")
    return maps, player_character


def location_city_4(maps, player_character, beat=None):
    print("city_4")
    if beat:
        print("return")
    return maps, player_character


def location_city_5(maps, player_character, beat=None):
    print("city_5")
    if beat:
        print("return")
    return maps, player_character


def location_difficult_1(maps, player_character, beat=None):
    print("difficult_1")
    if beat:
        print("return")
    return maps, player_character


def location_difficult_2(maps, player_character, beat=None):
    print("difficult_2")
    if beat:
        print("return")
    return maps, player_character


def location_difficult_3(maps, player_character, beat=None):
    print("difficult_3")
    if beat:
        print("return")
    return maps, player_character


def location_difficult_4(maps, player_character, beat=None):
    print("difficult_4")
    if beat:
        print("return")
    return maps, player_character


def location_difficult_5(maps, player_character, beat=None):
    print("difficult_5")
    if beat:
        print("return")
    return maps, player_character


def location_difficult_6(maps, player_character, beat=None):
    print("difficult_6")
    if beat:
        print("return")
    return maps, player_character


def location_difficult_7(maps, player_character, beat=None):
    print("difficult_7")
    if beat:
        print("return")
    return maps, player_character


def location_difficult_8(maps, player_character, beat=None):
    print("difficult_8")
    if beat:
        print("return")
    return maps, player_character


def location_yawning_1(maps, player_character, beat=None):
    print("yawn_2")
    if beat:
        print("return")
    return maps, player_character


def location_yawning_2(maps, player_character, beat=None):
    print("yawn_2")
    if beat:
        print("return")
    return maps, player_character


def location_yawning_3(maps, player_character, beat=None):
    print("yawn_3")
    if beat:
        print("return")
    return maps, player_character


def location_end(maps, player_character):
    print("end")
    return maps, player_character


def play(maps, player_character, stop):
    # location_start()
    while stop:
        map_display(maps, player_character)
        player_character = move(player_character)
        map_display(maps, player_character)

        maps, player_character = location_finder(maps, player_character)

        # battle_health, battle_exp
        # player_character = player_health(battle_health, player_character)
        #
        # player_character, up = experience(battle_exp, player_character)
        # if up:
        #     player_character = level_up(player_character)
        #
        # if player_character["health"] < 1:
        #     stop = lose()
        #
        # if battle_exp == 2:
        #     stop = win()
    return


def var():
    locations = {"port": [location_port_1, location_port_2],
                 "easy": [location_easy_1, location_easy_2, location_easy_3, location_easy_4, location_easy_5],
                 "city": [location_city_1, location_city_2, location_city_3, location_city_4, location_city_5],
                 "difficult": [location_difficult_1, location_difficult_2, location_difficult_3, location_difficult_4,
                               location_difficult_5, location_difficult_6, location_difficult_7, location_difficult_8],
                 "yawn": [location_yawning_1, location_yawning_2, location_yawning_3]}

    maps = {"map_visual": [["*", "*", "*", "*", "*"],
                           ["*", "*", "*", "*", "*"],
                           ["*", "*", "*", "*", "*"],
                           ["*", "*", "*", "*", "*"],
                           ["*", "*", "*", "*", "*"]],
            "map_locations": [["3", "3", "3", "y", "4"],
                              ["c", "c", "3", "y", "y"],
                              ["2", "2", "c", "3", "3"],
                              ["p", "2", "2", "c", "3"],
                              ["1", "p", "2", "c", "3"]],
            "locations": locations}

    player_character = {"player_pos": [4, 0], "health": 3, "level": 1, "exp": 0, "add": 0, "take_away": 0, "re_roll": 0}
    play(maps, player_character, True)


def main():
    var()


if __name__ == '__main__':
    main()
