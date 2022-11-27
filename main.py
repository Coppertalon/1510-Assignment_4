import random


def win():
    print("win text")
    return False


def lose():
    print("lose text")
    return False


def location_finder(maps: dict, player_character: dict):
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
        if maps["map_visual"][player_character["player_pos"][0]][player_character["player_pos"][1]] == "!":
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


def dont_use_location(maps: dict, player_character: dict, location_type: str):
    if location_type == "easy":
        print("too east")
        return maps, player_character, 0
    if location_type == "hard":
        print("too hard")
        return maps, player_character, 0
    if location_type == "explored":
        print("explored")
        return maps, player_character, 0
    if location_type == "beat":
        print("beaten")
        return maps, player_character, 0


def mark_location(maps: dict, player_character: dict, location_name, location_name_map: str):
    maps["map_visual"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_name_map
    maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]] = location_name
    return maps


def location_start_back(maps: dict, player_character: dict):
    print("start")
    return maps, player_character, 0


def location_port_1(maps: dict, player_character: dict, done=None):
    mark_location(maps, player_character, location_port_1, "P")
    print("port_1")
    if done:
        return dont_use_location(maps, player_character, "found")
    return maps, player_character, 0


def location_port_2(maps: dict, player_character: dict, done=None):
    mark_location(maps, player_character, location_port_2, "P")
    print("port_2")
    if done:
        return dont_use_location(maps, player_character, "found")
    return maps, player_character, 0


def location_easy_1(maps: dict, player_character: dict, done=None):
    print("easy_1")
    if done:
        return dont_use_location(maps, player_character, "beat")
    elif player_character["level"] > 1:
        mark_location(maps, player_character, location_easy_1, "!")
        return dont_use_location(maps, player_character, "easy")

    print("player stats")
    choice = input("play or leave")

    if choice == "play":
        print("start")
        roll, player_character = game_set_up(player_character)
        if 10 < roll < 21:
            mark_location(maps, player_character, location_easy_1, "@")
            print("win")
            return maps, player_character, 1
        else:
            mark_location(maps, player_character, location_easy_1, "!")
            print("lose")
            return maps, player_character, -1

    else:
        mark_location(maps, player_character, location_easy_1, "!")
        return maps, player_character, 0


def location_easy_2(maps: dict, player_character: dict, done=None):
    print("easy_2")
    if done:
        return dont_use_location(maps, player_character, "beat")
    elif player_character["level"] > 1:
        mark_location(maps, player_character, location_easy_2, "!")
        return dont_use_location(maps, player_character, "easy")

    print("player stats")
    choice = input("play or leave")

    if choice == "play":
        print("start")
        roll, player_character = game_set_up(player_character)
        if 10 < roll < 21:
            mark_location(maps, player_character, location_easy_2, "@")
            print("win")
            return maps, player_character, 1
        else:
            mark_location(maps, player_character, location_easy_2, "!")
            print("lose")
            return maps, player_character, -1

    else:
        mark_location(maps, player_character, location_easy_2, "!")
        return maps, player_character, 0


def location_easy_3(maps: dict, player_character: dict, done=None):
    print("easy_3")
    if done:
        return dont_use_location(maps, player_character, "beat")
    elif player_character["level"] > 1:
        mark_location(maps, player_character, location_easy_3, "!")
        return dont_use_location(maps, player_character, "easy")

    print("player stats")
    choice = input("play or leave")

    if choice == "play":
        print("start")
        roll, player_character = game_set_up(player_character)
        if 10 < roll < 21:
            mark_location(maps, player_character, location_easy_3, "@")
            print("win")
            return maps, player_character, 1
        else:
            mark_location(maps, player_character, location_easy_3, "!")
            print("lose")
            return maps, player_character, -1

    else:
        mark_location(maps, player_character, location_easy_3, "!")
        return maps, player_character, 0


def location_easy_4(maps: dict, player_character: dict, done=None):
    print("easy_4")
    if done:
        return dont_use_location(maps, player_character, "beat")
    elif player_character["level"] > 1:
        mark_location(maps, player_character, location_easy_4, "!")
        return dont_use_location(maps, player_character, "easy")

    print("player stats")
    choice = input("play or leave")

    if choice == "play":
        print("start")
        roll, player_character = game_set_up(player_character)
        if 10 < roll < 21:
            mark_location(maps, player_character, location_easy_4, "@")
            print("win")
            return maps, player_character, 1
        else:
            mark_location(maps, player_character, location_easy_4, "!")
            print("lose")
            return maps, player_character, -1

    else:
        mark_location(maps, player_character, location_easy_4, "!")
        return maps, player_character, 0


def location_easy_5(maps: dict, player_character: dict, done=None):
    print("easy_5")
    if done:
        return dont_use_location(maps, player_character, "beat")
    elif player_character["level"] > 1:
        mark_location(maps, player_character, location_easy_5, "!")
        return dont_use_location(maps, player_character, "easy")

    print("player stats")
    choice = input("play or leave")

    if choice == "play":
        print("start")
        roll, player_character = game_set_up(player_character)
        if 10 < roll < 21:
            mark_location(maps, player_character, location_easy_5, "@")
            print("win")
            return maps, player_character, 1
        else:
            mark_location(maps, player_character, location_easy_5, "!")
            print("lose")
            return maps, player_character, -1

    else:
        mark_location(maps, player_character, location_easy_5, "!")
        return maps, player_character, 0


def location_city_1(maps: dict, player_character: dict, done=None):
    mark_location(maps, player_character, location_city_1, "C")
    print("city_1")
    if done:
        return dont_use_location(maps, player_character, "found")
    return maps, player_character, 0


def location_city_2(maps: dict, player_character: dict, done=None):
    mark_location(maps, player_character, location_city_2, "C")
    print("city_2")
    if done:
        return dont_use_location(maps, player_character, "found")
    return maps, player_character, 0


def location_city_3(maps: dict, player_character: dict, done=None):
    mark_location(maps, player_character, location_city_3, "C")
    print("city_3")
    if done:
        return dont_use_location(maps, player_character, "found")
    return maps, player_character, 0


def location_city_4(maps: dict, player_character: dict, done=None):
    mark_location(maps, player_character, location_city_4, "C")
    print("city_4")
    if done:
        return dont_use_location(maps, player_character, "found")
    return maps, player_character, 0


def location_city_5(maps: dict, player_character: dict, done=None):
    mark_location(maps, player_character, location_city_5, "C")
    print("city_5")
    if done:
        return dont_use_location(maps, player_character, "found")
    return maps, player_character, 0


def location_difficult_1(maps: dict, player_character: dict, done=None):
    print("difficult_1")
    if done:
        return dont_use_location(maps, player_character, "beat")
    elif player_character["level"] == 1:
        mark_location(maps, player_character, location_difficult_1, "!")
        return dont_use_location(maps, player_character, "hard")

    print("player stats")
    choice = input("play or leave")

    if choice == "play":
        print("start")
        roll, player_character = game_set_up(player_character)
        if 10 < roll < 21:
            mark_location(maps, player_character, location_difficult_1, "@")
            print("win")
            return maps, player_character, 1
        else:
            mark_location(maps, player_character, location_difficult_1, "!")
            print("lose")
            return maps, player_character, -1

    else:
        mark_location(maps, player_character, location_difficult_1, "!")
        return maps, player_character, 0


def location_difficult_2(maps: dict, player_character: dict, done=None):
    print("difficult_2")
    if done:
        return dont_use_location(maps, player_character, "beat")
    elif player_character["level"] == 1:
        mark_location(maps, player_character, location_difficult_2, "!")
        return dont_use_location(maps, player_character, "hard")

    print("player stats")
    choice = input("play or leave")

    if choice == "play":
        print("start")
        roll, player_character = game_set_up(player_character)
        if 10 < roll < 21:
            mark_location(maps, player_character, location_difficult_2, "@")
            print("win")
            return maps, player_character, 1
        else:
            mark_location(maps, player_character, location_difficult_2, "!")
            print("lose")
            return maps, player_character, -1

    else:
        mark_location(maps, player_character, location_difficult_2, "!")
        return maps, player_character, 0


def location_difficult_3(maps: dict, player_character: dict, done=None):
    print("difficult_3")
    if done:
        return dont_use_location(maps, player_character, "beat")
    elif player_character["level"] == 1:
        mark_location(maps, player_character, location_difficult_3, "!")
        return dont_use_location(maps, player_character, "hard")

    print("player stats")
    choice = input("play or leave")

    if choice == "play":
        print("start")
        roll, player_character = game_set_up(player_character)
        if 10 < roll < 21:
            mark_location(maps, player_character, location_difficult_3, "@")
            print("win")
            return maps, player_character, 1
        else:
            mark_location(maps, player_character, location_difficult_3, "!")
            print("lose")
            return maps, player_character, -1

    else:
        mark_location(maps, player_character, location_difficult_3, "!")
        return maps, player_character, 0


def location_difficult_4(maps: dict, player_character: dict, done=None):
    print("difficult_4")
    if done:
        return dont_use_location(maps, player_character, "beat")
    elif player_character["level"] == 1:
        mark_location(maps, player_character, location_difficult_4, "!")
        return dont_use_location(maps, player_character, "hard")

    print("player stats")
    choice = input("play or leave")

    if choice == "play":
        print("start")
        roll, player_character = game_set_up(player_character)
        if 10 < roll < 21:
            mark_location(maps, player_character, location_difficult_4, "@")
            print("win")
            return maps, player_character, 1
        else:
            mark_location(maps, player_character, location_difficult_4, "!")
            print("lose")
            return maps, player_character, -1

    else:
        mark_location(maps, player_character, location_difficult_4, "!")
        return maps, player_character, 0


def location_difficult_5(maps: dict, player_character: dict, done=None):
    print("difficult_5")
    if done:
        return dont_use_location(maps, player_character, "beat")
    elif player_character["level"] == 1:
        mark_location(maps, player_character, location_difficult_5, "!")
        return dont_use_location(maps, player_character, "hard")

    print("player stats")
    choice = input("play or leave")

    if choice == "play":
        print("start")
        roll, player_character = game_set_up(player_character)
        if 10 < roll < 21:
            mark_location(maps, player_character, location_difficult_5, "@")
            print("win")
            return maps, player_character, 1
        else:
            mark_location(maps, player_character, location_difficult_5, "!")
            print("lose")
            return maps, player_character, -1

    else:
        mark_location(maps, player_character, location_difficult_5, "!")
        return maps, player_character, 0


def location_difficult_6(maps: dict, player_character: dict, done=None):
    print("difficult_6")
    if done:
        return dont_use_location(maps, player_character, "beat")
    elif player_character["level"] == 1:
        mark_location(maps, player_character, location_difficult_6, "!")
        return dont_use_location(maps, player_character, "hard")

    print("player stats")
    choice = input("play or leave")

    if choice == "play":
        print("start")
        return battle_starter(maps, player_character, location_difficult_6, 10)

    else:
        mark_location(maps, player_character, location_difficult_6, "!")
        return maps, player_character, 0


def location_difficult_7(maps: dict, player_character: dict, done=None):
    print("difficult_7")
    if done:
        return dont_use_location(maps, player_character, "beat")
    elif player_character["level"] == 1:
        mark_location(maps, player_character, location_difficult_7, "!")
        return dont_use_location(maps, player_character, "hard")

    print("player stats")
    choice = input("play or leave")

    if choice == "play":
        print("start")
        return battle_starter(maps, player_character, location_difficult_7, 10)

    else:
        mark_location(maps, player_character, location_difficult_7, "!")
        return maps, player_character, 0


def location_difficult_8(maps: dict, player_character: dict, done=None):
    print("difficult_8")

    if done:
        return dont_use_location(maps, player_character, "beat")
    elif player_character["level"] > 1:
        mark_location(maps, player_character, location_difficult_8, "!")
        return dont_use_location(maps, player_character, "easy")

    print("player stats")
    choice = input("play or leave")

    if choice == "play":
        print("start")
        return battle_starter(maps, player_character, location_difficult_8, 10)

    else:
        mark_location(maps, player_character, location_difficult_8, "!")
        return maps, player_character, 0


def location_yawning_1(maps: dict, player_character: dict, done=None):
    mark_location(maps, player_character, location_yawning_1, "X")
    print("yawn_1")
    if done:
        return dont_use_location(maps, player_character, "found")
    return maps, player_character, 0


def location_yawning_2(maps: dict, player_character: dict, done=None):
    mark_location(maps, player_character, location_yawning_2, "X")
    print("yawn_2")
    if done:
        return dont_use_location(maps, player_character, "found")
    return maps, player_character, 0


def location_yawning_3(maps: dict, player_character: dict, done=None):
    mark_location(maps, player_character, location_yawning_3, "X")
    print("yawn_3")
    if done:
        return dont_use_location(maps, player_character, "found")
    else:
        return maps, player_character, 0


def location_end(maps: dict, player_character: dict):
    print("end")
    roll, player_character = game_set_up(player_character)
    return maps, player_character


def location_start(maps: dict, player_character: dict):
    mark_location(maps, player_character,  "1", "O")

    print("Game Explanation")
    print("Practice battle")
    print("Battle Explanation")

    roll, player_character = game_set_up(player_character)
    if 16 < roll < 21:
        print("win")
    else:
        print("lose")

    print("Lore")
    print("Goal")
    map_display(maps, player_character)
    print("Goodbye")

    player_character["re_roll"] = 1
    return maps, player_character


def battle_starter(maps: dict, player_character: dict, location, roll_to_beat: int):
    roll, player_character = game_set_up(player_character)
    if roll_to_beat < roll < 21:
        mark_location(maps, player_character, location, "@")
        print("win")
        return maps, player_character, 1
    else:
        mark_location(maps, player_character, location, "!")
        print("lose")
        return maps, player_character, -1


def game_set_up(player_character: dict):
    rolls = [random.randint(1, 6) for i in range(3)]
    print(rolls)
    total = rolls[0] + rolls[1] + rolls[2]
    action = "roll"
    roll = rolls[2]
    while total < 21 and action != "hold":
        print(total)
        total, roll, action, player_character = game_choices(player_character, total, roll)

    return total, player_character


def game_choices(player_character: dict, total: int, roll: int):
    choices1 = ["1", "2", "3"]
    choices2 = ["1", "2", "3", "4", "5"]

    if player_character["level"] == 1:
        choice = input("choices 1")
    else:
        choice = input("choices 2")

    if (choice in choices1 and player_character["level"] == 1) or (
            choice in choices2 and player_character["level"] > 1):
        total, roll, action, player_character, = game_actions(total, roll, player_character, action=choice)
        return total, roll, action, player_character

    else:
        print("bad choice")
        return total, roll, "none", player_character


def game_actions(total: int, roll: int, player_character: dict, action: str):
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


def rolling(total: int, roll: int, action: str, player_character: dict):
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


def total_modify(total: int, roll: int, action: str, player_character: dict):
    if action == "4":
        total += 1
        player_character["add"] -= 1
        return total, roll, "none", player_character

    if action == "5":
        total -= 1
        player_character["take_away"] -= 1
        return total, roll, "none", player_character


def move(player_character: dict):
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


def health(battle_result: int, player_character: dict):
    if battle_result == -1:
        player_character["health"] -= 1
        print("lose health message")
        return player_character

    if battle_result == -2:
        player_character["health"] -= 2
        print("lose to boss method")
        return player_character

    else:
        return player_character


def experience(battle_result: int, player_character: dict):
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


def level_up(player_character: dict):
    if player_character["level"] == 2:
        print("level up 2 message")

    if player_character["level"] == 3:
        print("level up 3 message")

    player_character["health"] += 1

    if player_character["re_rolls"] <= player_character["level"]:
        player_character["re_rolls"] += 1

    if player_character["take_away"] < player_character["level"]:
        player_character["take_away"] += 1

    if player_character["add"] < player_character["level"]:
        player_character["add"] += 1

    return player_character


def map_display(maps: dict, player_character: dict):
    for height in range(len(maps["map_visual"])):
        for width in range(len(maps["map_visual"])):
            if height == player_character["player_pos"][0] and width == player_character["player_pos"][1]:
                print("#", end="")
            else:
                print(maps["map_visual"][height][width], end="")

    print("")
    print("Legend:  * = Unexplored,    # = Player,    ! = Found Bar,   @ = Beaten Bar,")
    print("Legend:  O = Your Ship,    X = Yawning Portal,    P = Found Port,   C = Found City,")
    print("Stats:  Renown:" + player_character["level"] + "reputation: " + player_character["exp"] +
          "Credibility" + player_character["health"])
    print("Level 1 Skills:  re-rolls: " + player_character["re_roll"])

    if player_character["level"] > 1:
        print("Level 2 Skills:  add 1 to roll:" + player_character["add"] +
              "remove 1 from roll:" + player_character["take_away"])
    return


def play(maps: dict, player_character: dict, run: bool):
    maps, player_character = location_start(player_character, maps)

    while run:
        map_display(maps, player_character)
        player_character = move(player_character)
        map_display(maps, player_character)

        maps, player_character, result = location_finder(maps, player_character)

        player_character = health(result, player_character)
        player_character, up = experience(result, player_character)

        if up:
            player_character = level_up(player_character)

        if player_character["health"] < 1:
            run = lose()

        if result == 2:
            run = win()
    return


def map_maker(user_map: list):
    return ["*", "*", "*", "*", "*"]


def var():
    locations = {"port": [location_port_1, location_port_2],
                 "easy": [location_easy_1, location_easy_2, location_easy_3, location_easy_4, location_easy_5],
                 "city": [location_city_1, location_city_2, location_city_3, location_city_4, location_city_5],
                 "difficult": [location_difficult_1, location_difficult_2, location_difficult_3, location_difficult_4,
                               location_difficult_5, location_difficult_6, location_difficult_7, location_difficult_8],
                 "yawn": [location_yawning_1, location_yawning_2, location_yawning_3]}

    player_map = list(map(map_maker, [[], [], [], [], []]))

    maps = {"map_visual": player_map,
            "map_locations": [["3", "3", "3", "y", "4"],
                              ["c", "c", "3", "y", "y"],
                              ["2", "2", "c", "3", "3"],
                              ["p", "2", "2", "c", "3"],
                              ["1", "p", "2", "c", "3"]],
            "locations": locations}
    name = input("player name")
    player_character = {"name": name, "player_pos": [4, 0], "health": 3, "level": 1, "exp": 0,
                        "add": 0, "take_away": 0, "re_roll": 0}

    play(maps, player_character, run=True)


def main():
    var()


if __name__ == '__main__':
    main()
