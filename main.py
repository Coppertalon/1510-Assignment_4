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
    elif maps["map_beat"][player_character["player_pos"][0]][player_character["player_pos"][1]] == "0":
        return returned(maps, player_character, False)
    elif maps["map_beat"][player_character["player_pos"][0]][player_character["player_pos"][1]] == "1":
        return returned(maps, player_character, True)


def location_port(maps, player_character):
    random_location = random.randint(0, (len(maps["locations"]["port"])-1))
    location = maps["locations"]["port"][random_location]
    del maps["locations"]["port"][random_location]
    return location(maps, player_character)


def location_city(maps, player_character):
    random_location = random.randint(0, (len(maps["locations"]["city"])-1))
    location = maps["locations"]["city"][random_location]
    del maps["locations"]["city"][random_location]
    return location(maps, player_character)


def location_yawning_portal(maps, player_character):
    random_location = random.randint(0, (len(maps["locations"]["yawn"])-1))
    location = maps["locations"]["yawn"][random_location]
    del maps["locations"]["yawn"][random_location]
    return location(maps, player_character)


def location_easy(maps, player_character):
    random_location = random.randint(0, (len(maps["locations"]["easy"])-1))
    location = maps["locations"]["easy"][random_location]
    del maps["locations"]["easy"][random_location]
    return location(maps, player_character)


def location_hard(maps, player_character):
    random_location = random.randint(0, (len(maps["locations"]["difficult"])-1))
    location = maps["locations"]["difficult"][random_location]
    del maps["locations"]["difficult"][random_location]
    return location(maps, player_character)


def returned(maps, player_character, beat):
    location = maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]]
    return location(maps, player_character, beat)


def health(battle_result, player_character):
    if battle_result == -1:
        player_character["health"] -= 1
        print("lose health message")
        return player_character["health"]

    if battle_result == -2:
        player_character["health"] -= 2
        print("lose to boss method")
        return player_character["health"]

    else:
        return player_character["health"]


def experience(battle_result, player_character):
    if battle_result == 1:
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
        return player_character, False


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
    return maps, player_character, 0


def location_port_1(maps, player_character, beat=None):
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_port_1
    print("port_1")
    if beat:
        print("return")
    return maps, player_character, 0


def location_port_2(maps, player_character, beat=None):
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_port_2
    print("port_2")
    if beat:
        print("return")
    return maps, player_character, 0


def location_easy_1(maps, player_character, beat=None):
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_easy_1
    print("easy_1")
    print("player stats")

    if beat:
        print("return")

    choice = input("play or leave")

    if choice == "play":
        print("start")
        roll, player_character = game_set_up(player_character)
        if 10 < roll < 21:
            print("win")
            return maps, player_character, 1
        else:
            print("lose")
            return maps, player_character, -1

    else:
        return maps, player_character, 0


def location_easy_2(maps, player_character, beat=None):
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_easy_2
    print("player stats")

    if beat:
        print("return")

    choice = input("play or leave")

    if choice == "play":
        print("start")
        roll, player_character = game_set_up(player_character)
        if 10 < roll < 21:
            print("win")
            return maps, player_character, 1
        else:
            print("lose")
            return maps, player_character, -1

    else:
        return maps, player_character, 0


def location_easy_3(maps, player_character, beat=None):
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_easy_3
    print("easy_3")
    print("player stats")

    if beat:
        print("return")

    choice = input("play or leave")

    if choice == "play":
        print("start")
        roll, player_character = game_set_up(player_character)
        if 10 < roll < 21:
            print("win")
            return maps, player_character, 1
        else:
            print("lose")
            return maps, player_character, -1

    else:
        return maps, player_character, 0


def location_easy_4(maps, player_character, beat=None):
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_easy_4
    print("easy_4")
    print("player stats")

    if beat:
        print("return")

    choice = input("play or leave")

    if choice == "play":
        print("start")
        roll, player_character = game_set_up(player_character)
        if 10 < roll < 21:
            print("win")
            return maps, player_character, 1
        else:
            print("lose")
            return maps, player_character, -1

    else:
        return maps, player_character, 0


def location_easy_5(maps, player_character, beat=None):
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_easy_5
    print("easy_5")
    print("player stats")

    if beat:
        print("return")

    choice = input("play or leave")

    if choice == "play":
        print("start")
        roll, player_character = game_set_up(player_character)
        if 10 < roll < 21:
            print("win")
            return maps, player_character, 1
        else:
            print("lose")
            return maps, player_character, -1

    else:
        return maps, player_character, 0


def location_city_1(maps, player_character, beat=None):
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_city_1
    print("city_1")
    if beat:
        print("return")
    return maps, player_character, 0


def location_city_2(maps, player_character, beat=None):
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_city_2
    print("city_2")
    if beat:
        print("return")
    return maps, player_character, 0


def location_city_3(maps, player_character, beat=None):
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_city_3
    print("city_3")
    if beat:
        print("return")
    return maps, player_character, 0


def location_city_4(maps, player_character, beat=None):
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_city_4
    print("city_4")
    if beat:
        print("return")
    return maps, player_character, 0


def location_city_5(maps, player_character, beat=None):
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_city_5
    print("city_5")
    if beat:
        print("return")
    return maps, player_character, 0


def location_difficult_1(maps, player_character, beat=None):
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_difficult_1
    print("difficult_1")
    print("player stats")

    if beat:
        print("return")

    choice = input("play or leave")

    if choice == "play":
        print("start")
        roll, player_character = game_set_up(player_character)
        if 10 < roll < 21:
            print("win")
            return maps, player_character, 1
        else:
            print("lose")
            return maps, player_character, -1

    else:
        return maps, player_character, 0


def location_difficult_2(maps, player_character, beat=None):
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_difficult_2
    print("difficult_2")
    print("player stats")

    if beat:
        print("return")

    choice = input("play or leave")

    if choice == "play":
        print("start")
        roll, player_character = game_set_up(player_character)
        if 10 < roll < 21:
            print("win")
            return maps, player_character, 1
        else:
            print("lose")
            return maps, player_character, -1

    else:
        return maps, player_character, 0

def location_difficult_3(maps, player_character, beat=None):
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_difficult_3
    print("difficult_3")
    print("player stats")

    if beat:
        print("return")

    choice = input("play or leave")

    if choice == "play":
        print("start")
        roll, player_character = game_set_up(player_character)
        if 10 < roll < 21:
            print("win")
            return maps, player_character, 1
        else:
            print("lose")
            return maps, player_character, -1

    else:
        return maps, player_character, 0

def location_difficult_4(maps, player_character, beat=None):
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_difficult_4
    print("difficult_4")
    print("player stats")

    if beat:
        print("return")

    choice = input("play or leave")

    if choice == "play":
        print("start")
        roll, player_character = game_set_up(player_character)
        if 10 < roll < 21:
            print("win")
            return maps, player_character, 1
        else:
            print("lose")
            return maps, player_character, -1

    else:
        return maps, player_character, 0


def location_difficult_5(maps, player_character, beat=None):
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_difficult_5
    print("difficult_5")
    print("player stats")

    if beat:
        print("return")

    choice = input("play or leave")

    if choice == "play":
        print("start")
        roll, player_character = game_set_up(player_character)
        if 10 < roll < 21:
            print("win")
            return maps, player_character, 1
        else:
            print("lose")
            return maps, player_character, -1

    else:
        return maps, player_character, 0


def location_difficult_6(maps, player_character, beat=None):
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_difficult_6
    print("difficult_6")
    print("player stats")

    if beat:
        print("return")

    choice = input("play or leave")

    if choice == "play":
        print("start")
        roll, player_character = game_set_up(player_character)
        if 10 < roll < 21:
            print("win")
            return maps, player_character, 1
        else:
            print("lose")
            return maps, player_character, -1

    else:
        return maps, player_character, 0


def location_difficult_7(maps, player_character, beat=None):
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_difficult_7
    print("difficult_7")
    print("player stats")

    if beat:
        print("return")

    choice = input("play or leave")

    if choice == "play":
        print("start")
        roll, player_character = game_set_up(player_character)
        if 10 < roll < 21:
            print("win")
            return maps, player_character, 1
        else:
            print("lose")
            return maps, player_character, -1

    else:
        return maps, player_character, 0


def location_difficult_8(maps, player_character, beat=None):
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_difficult_8
    print("difficult_8")
    print("player stats")

    if beat:
        print("return")

    choice = input("play or leave")

    if choice == "play":
        print("start")
        roll, player_character = game_set_up(player_character)
        if 10 < roll < 21:
            print("win")
            return maps, player_character, 1
        else:
            print("lose")
            return maps, player_character, -1

    else:
        return maps, player_character, 0


def location_yawning_1(maps, player_character, beat=None):
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_yawning_1
    print("yawn_1")
    if beat:
        print("return")
    return maps, player_character, 0


def location_yawning_2(maps, player_character, beat=None):
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_yawning_2
    print("yawn_2")
    if beat:
        print("return")
    return maps, player_character, 0


def location_yawning_3(maps, player_character, beat=None):
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_yawning_3
    print("yawn_3")
    if beat:
        print("return")
    return maps, player_character, 0


def location_end(maps, player_character):
    print("end")
    roll, player_character = game_set_up(player_character)
    return maps, player_character


def game_set_up(player_character):
    rolls = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    print(rolls)
    total = rolls[0] + rolls[1] + rolls[2]
    action = "roll"
    roll = rolls[2]
    while total < 21 and action != "hold":
        print(total)
        total, roll, action, player_character = game_choices(player_character, total, roll)

    return total, player_character


def game_choices(player_character, total, roll):
    choices1 = ["1", "2", "3"]
    choices2 = ["1", "2", "3", "4", "5"]

    if player_character["level"] == 1:
        choice = input("choices 1")
    else:
        choice = input("choices 2")

    if (choice in choices1 and player_character["level"] == 1) or (
            choice in choices2 and player_character["level"] > 1):
        total, roll, action, player_character, = game_actions(total, roll, choice, player_character)
        return total, roll, action, player_character

    else:
        print("bad choice")
        return total, roll, "none", player_character


def game_actions(total, roll, action, player_character):
    if action == "1":
        return rolling(total, roll, action, player_character)

    elif action == "2" and player_character["re_roll"] > 0:
        return rolling(total, roll, action, player_character)

    elif action == "3":
        return total, roll, "hold", player_character

    elif action == "4" and player_character["add"] > 0:
        return total_modify(total, roll, action, player_character)

    elif action == "5" and player_character["take_away"] > 0:
        return total_modify(total, roll, action, player_character)

    else:
        print("you can't do that")
        return total, roll, "none", player_character


def rolling(total, roll, action, player_character):
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


def total_modify(total, roll, action, player_character):
    if action == "4":
        total += 1
        player_character["add"] -= 1
        return total, roll, "none", player_character

    if action == "5":
        total -= 1
        player_character["take_away"] -= 1
        return total, roll, "none", player_character


def play(maps, player_character, stop):
    # location_start()
    while stop:
        map_display(maps, player_character)
        player_character = move(player_character)
        map_display(maps, player_character)

        maps, player_character, result = location_finder(maps, player_character)

        # player_character = health(result, player_character)
        # player_character, up = experience(result, player_character)
        #
        # if up:
        #     player_character = level_up(player_character)
        #
        # if player_character["health"] < 1:
        #     stop = lose()
        #
        # if result == 2:
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
            "map_beat":      [["0", "0", "0", "0", "0"],
                              ["0", "0", "0", "0", "0"],
                              ["0", "0", "0", "0", "0"],
                              ["0", "0", "0", "0", "0"],
                              ["0", "0", "0", "0", "0"]],
            "locations": locations}

    player_character = {"player_pos": [4, 0], "health": 3, "level": 1, "exp": 0, "add": 0, "take_away": 0, "re_roll": 1}
    play(maps, player_character, True)


def main():
    var()


if __name__ == '__main__':
    main()
