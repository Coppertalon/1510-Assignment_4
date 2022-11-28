import random


def win():
    print("win text")
    return False


def lose():
    print("lose text")
    return False


def location_finder(maps: dict, player_character: dict):
    location = maps["map_locations"][player_character["player_pos"][0]][player_character["player_pos"][1]]
    locations = [location_start_back, location_easy, location_hard, location_end,
                 location_port, location_city, location_yawning_portal]
    location_options = ["1", "2", "3", "4", "p", "c", "y"]

    for i in range(0, 7):
        if location == location_options[i]:
            return locations[i](maps, player_character)

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


def dont_use_location(location_type: str):
    if location_type == "easy":
        print("too east")
    if location_type == "hard":
        print("too hard")
    if location_type == "explored":
        print("explored")
    if location_type == "beat":
        print("beaten")
    return


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
        dont_use_location("found")

    choice = input("move or quit \n")

    if choice == "quit":
        return maps, player_character, 0, False

    else:
        return maps, player_character, 0, True



def location_port_2(maps: dict, player_character: dict, done=None):
    mark_location(maps, player_character, location_port_2, "P")
    print("port_2")
    if done:
        dont_use_location("found")

    choice = input("move or quit \n")

    if choice == "quit":
        return maps, player_character, 0, False

    else:
        return maps, player_character, 0, True


def location_easy_1(maps: dict, player_character: dict, done=None):
    print("easy_1")
    if done:
        dont_use_location("beat")
    elif player_character["level"] > 1:
        mark_location(maps, player_character, location_easy_1, "!")
        dont_use_location("easy")

    player_stats(player_character)
    choice = input("play, leave, or quit \n")

    if choice == "play":
        return battle_starter(maps, player_character, location_easy_1, 16)

    if choice == "quit":
        return maps, player_character, 0, False

    else:
        mark_location(maps, player_character, location_easy_1, "!")
        return maps, player_character, 0, True


def location_easy_2(maps: dict, player_character: dict, done=None):
    print("easy_2")
    if done:
        dont_use_location("beat")
    elif player_character["level"] > 1:
        mark_location(maps, player_character, location_easy_2, "!")
        dont_use_location("easy")

    player_stats(player_character)
    choice = input("play or leave \n")

    if choice == "play":
        print("start")
        return battle_starter(maps, player_character, location_easy_2, 16)

    if choice == "quit":
        return maps, player_character, 0, False

    else:
        mark_location(maps, player_character, location_easy_1, "!")
        return maps, player_character, 0, True


def location_easy_3(maps: dict, player_character: dict, done=None):
    print("easy_3")
    if done:
        dont_use_location("beat")
    elif player_character["level"] > 1:
        mark_location(maps, player_character, location_easy_3, "!")
        dont_use_location("easy")

    player_stats(player_character)
    choice = input("play or leave \n")

    if choice == "play":
        print("start")
        return battle_starter(maps, player_character, location_easy_3, 16)

    if choice == "quit":
        return maps, player_character, 0, False

    else:
        mark_location(maps, player_character, location_easy_1, "!")
        return maps, player_character, 0, True


def location_easy_4(maps: dict, player_character: dict, done=None):
    print("easy_4")
    if done:
        dont_use_location("beat")
    elif player_character["level"] > 1:
        mark_location(maps, player_character, location_easy_4, "!")
        dont_use_location("easy")

    player_stats(player_character)
    choice = input("play or leave \n")

    if choice == "play":
        print("start")
        return battle_starter(maps, player_character, location_easy_4, 17)

    if choice == "quit":
        return maps, player_character, 0, False

    else:
        mark_location(maps, player_character, location_easy_1, "!")
        return maps, player_character, 0, True


def location_easy_5(maps: dict, player_character: dict, done=None):
    print("easy_5")
    if done:
        dont_use_location("beat")
    elif player_character["level"] > 1:
        mark_location(maps, player_character, location_easy_5, "!")
        dont_use_location("easy")

    player_stats(player_character)
    choice = input("play or leave \n")

    if choice == "play":
        return battle_starter(maps, player_character, location_easy_5, 17)

    if choice == "quit":
        return maps, player_character, 0, False

    else:
        mark_location(maps, player_character, location_easy_1, "!")
        return maps, player_character, 0, True

def location_city_1(maps: dict, player_character: dict, done=None):
    mark_location(maps, player_character, location_city_1, "C")
    print("city_1")
    if done:
        dont_use_location("found")

    choice = input("move or quit \n")

    if choice == "quit":
        return maps, player_character, 0, False

    else:
        return maps, player_character, 0, True



def location_city_2(maps: dict, player_character: dict, done=None):
    mark_location(maps, player_character, location_city_2, "C")
    print("city_2")
    if done:
        dont_use_location("found")

    choice = input("move or quit \n")

    if choice == "quit":
        return maps, player_character, 0, False

    else:
        return maps, player_character, 0, True


def location_city_3(maps: dict, player_character: dict, done=None):
    mark_location(maps, player_character, location_city_3, "C")
    print("city_3")
    if done:
        dont_use_location("found")

    choice = input("move or quit \n")

    if choice == "quit":
        return maps, player_character, 0, False

    else:
        return maps, player_character, 0, True


def location_city_4(maps: dict, player_character: dict, done=None):
    mark_location(maps, player_character, location_city_4, "C")
    print("city_4")
    if done:
        dont_use_location("found")

    choice = input("move or quit \n")

    if choice == "quit":
        return maps, player_character, 0, False

    else:
        return maps, player_character, 0, True


def location_city_5(maps: dict, player_character: dict, done=None):
    mark_location(maps, player_character, location_city_5, "C")
    print("city_5")
    if done:
        dont_use_location("found")

    choice = input("move or quit \n")

    if choice == "quit":
        return maps, player_character, 0, False

    else:
        return maps, player_character, 0, True


def location_difficult_1(maps: dict, player_character: dict, done=None):
    print("difficult_1")
    if done:
         dont_use_location("beat")
    elif player_character["level"] == 1:
        mark_location(maps, player_character, location_difficult_1, "!")
        dont_use_location("hard")

    player_stats(player_character)
    choice = input("play or leave \n")

    if choice == "play":
        print("start")
        return battle_starter(maps, player_character, location_difficult_1, 18)

    if choice == "quit":
        return maps, player_character, 0, False

    else:
        mark_location(maps, player_character, location_easy_1, "!")
        return maps, player_character, 0, True

def location_difficult_2(maps: dict, player_character: dict, done=None):
    print("difficult_2")
    if done:
        dont_use_location("beat")
    elif player_character["level"] == 1:
        mark_location(maps, player_character, location_difficult_2, "!")
        dont_use_location("hard")

    player_stats(player_character)
    choice = input("play or leave \n")

    if choice == "play":
        print("start")
        return battle_starter(maps, player_character, location_difficult_2, 18)

    if choice == "quit":
        return maps, player_character, 0, False

    else:
        mark_location(maps, player_character, location_easy_1, "!")
        return maps, player_character, 0, True


def location_difficult_3(maps: dict, player_character: dict, done=None):
    print("difficult_3")
    if done:
        dont_use_location("beat")
    elif player_character["level"] == 1:
        mark_location(maps, player_character, location_difficult_3, "!")
        dont_use_location("hard")

    player_stats(player_character)
    choice = input("play or leave \n")

    if choice == "play":
        print("start")
        return battle_starter(maps, player_character, location_difficult_3, 18)

    if choice == "quit":
        return maps, player_character, 0, False

    else:
        mark_location(maps, player_character, location_easy_1, "!")
        return maps, player_character, 0, True

def location_difficult_4(maps: dict, player_character: dict, done=None):
    print("difficult_4")
    if done:
        dont_use_location("beat")
    elif player_character["level"] == 1:
        mark_location(maps, player_character, location_difficult_4, "!")
        dont_use_location("hard")

    player_stats(player_character)
    choice = input("play or leave \n")

    if choice == "play":
        print("start")
        return battle_starter(maps, player_character, location_difficult_4, 18)

    if choice == "quit":
        return maps, player_character, 0, False

    else:
        mark_location(maps, player_character, location_easy_1, "!")
        return maps, player_character, 0, True


def location_difficult_5(maps: dict, player_character: dict, done=None):
    print("difficult_5")
    if done:
        dont_use_location("beat")
    elif player_character["level"] == 1:
        mark_location(maps, player_character, location_difficult_5, "!")
        dont_use_location("hard")

    player_stats(player_character)
    choice = input("play or leave \n")

    if choice == "play":
        print("start")
        return battle_starter(maps, player_character, location_difficult_5, 18)

    if choice == "quit":
        return maps, player_character, 0, False

    else:
        mark_location(maps, player_character, location_easy_1, "!")
        return maps, player_character, 0, True


def location_difficult_6(maps: dict, player_character: dict, done=None):
    print("difficult_6")
    if done:
        dont_use_location("beat")
    elif player_character["level"] == 1:
        mark_location(maps, player_character, location_difficult_6, "!")
        dont_use_location("hard")

    player_stats(player_character)
    choice = input("play or leave \n")

    if choice == "play":
        print("start")
        return battle_starter(maps, player_character, location_difficult_6, 19)

    if choice == "quit":
        return maps, player_character, 0, False

    else:
        mark_location(maps, player_character, location_easy_1, "!")
        return maps, player_character, 0, True


def location_difficult_7(maps: dict, player_character: dict, done=None):
    print("difficult_7")
    if done:
        dont_use_location("beat")
    elif player_character["level"] == 1:
        mark_location(maps, player_character, location_difficult_7, "!")
        dont_use_location("hard")

    player_stats(player_character)
    choice = input("play or leave \n")

    if choice == "play":
        print("start")
        return battle_starter(maps, player_character, location_difficult_7, 19)

    if choice == "quit":
        return maps, player_character, 0, False

    else:
        mark_location(maps, player_character, location_easy_1, "!")
        return maps, player_character, 0, True


def location_difficult_8(maps: dict, player_character: dict, done=None):
    print("difficult_8")

    if done:
        dont_use_location("beat")
    elif player_character["level"] > 1:
        mark_location(maps, player_character, location_difficult_8, "!")
        dont_use_location("easy")

    player_stats(player_character)
    choice = input("play or leave \n")

    if choice == "play":
        print("start")
        return battle_starter(maps, player_character, location_difficult_8, 19)

    if choice == "quit":
        return maps, player_character, 0, False

    else:
        mark_location(maps, player_character, location_easy_1, "!")
        return maps, player_character, 0, True


def location_yawning_1(maps: dict, player_character: dict, done=None):
    mark_location(maps, player_character, location_yawning_1, "X")
    print("yawn_1")
    if done:
        dont_use_location("found")

    choice = input("move or quit \n")

    if choice == "quit":
        return maps, player_character, 0, False

    else:
        return maps, player_character, 0, True


def location_yawning_2(maps: dict, player_character: dict, done=None):
    mark_location(maps, player_character, location_yawning_2, "X")
    print("yawn_2")
    if done:
        dont_use_location("found")

    choice = input("move or quit \n")

    if choice == "quit":
        return maps, player_character, 0, False

    else:
        return maps, player_character, 0, True


def location_yawning_3(maps: dict, player_character: dict, done=None):
    mark_location(maps, player_character, location_yawning_3, "X")
    print("yawn_3")
    if done:
        dont_use_location("found")

    choice = input("move or quit \n")

    if choice == "quit":
        return maps, player_character, 0, False

    else:
        return maps, player_character, 0, True


def location_end(maps: dict, player_character: dict):
    if player_character["level"] > 1:
        print("end")
        score = 0
        rounds = 0

        while score < 2 and rounds < 3:
            roll, player_character = game_set_up(player_character)

            if (19 + score) > roll > 21:
                score += 1
                print("win")
            else:
                score -= 1
                print("lose")

            rounds += 1
        return final_dialogue(score)

    print("too low")
    return maps, player_character, 0


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


def location_start(maps: dict, player_character: dict):
    mark_location(maps, player_character,  "1", "O")

    print("Game Explanation")
    print("Practice battle")
    print("Battle Explanation")

    roll, player_character = game_set_up(player_character)
    if 15 < roll < 21:
        print("win")
    else:
        print("lose")

    print("Lore")
    print("Goal")
    input("Press enter to contuinue")

    map_display(maps, player_character)
    print("Goodbye")
    player_character["re_roll"] = 1
    return maps, player_character


def battle_starter(maps: dict, player_character: dict, location, roll_to_beat: int):
    roll, player_character = game_set_up(player_character)
    if roll_to_beat < roll < 21:
        mark_location(maps, player_character, location, "@")
        print("win")
        return maps, player_character, 1, True
    else:
        mark_location(maps, player_character, location, "!")
        print("lose")
        return maps, player_character, -1, True


def game_set_up(player_character: dict):
    rolls = [random.randint(1, 6) for i in range(3)]
    print(rolls)
    total = rolls[0] + rolls[1] + rolls[2]
    action = "roll"
    roll = rolls[2]
    while total < 27 and action != "hold":
        print(total)
        if total > 21:
            print("You are currently over the max roll")

        print("Level 1 Skills:  re-rolls: ", player_character["re_roll"])

        if player_character["level"] > 1:
            print("Level 2 Skills:  add 1 to roll:", player_character["add"],
                  "remove 1 from roll:", player_character["take_away"])

        total, roll, action, player_character = game_choices(player_character, total, roll)

    return total, player_character


def game_choices(player_character: dict, total: int, roll: int):
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
    valid_moves = ["north", "south", "east", "west", "quit"]
    movement = ""
    while movement not in ["1", "2", "3", "4"]:
        print_choice = iter(valid_moves)
        for number, option in enumerate(range(len(valid_moves)), 1):
            print(number, next(print_choice))
        movement = input("movement \n")

        if movement == "5":
            return player_character, False

        if movement in ["1", "2", "3", "4"]:
            if movement == "1" and player_character["player_pos"][0] > 0:
                player_character["player_pos"][0] -= 1
            elif movement == "2" and player_character["player_pos"][0] < 4:
                player_character["player_pos"][0] += 1
            elif movement == "3" and player_character["player_pos"][1] > 0:
                player_character["player_pos"][1] -= 1
            elif movement == "4" and player_character["player_pos"][1] < 4:
                player_character["player_pos"][1] += 1
            else:
                print('"', movement, '"', " is an invalid movement. Please try again")
                movement = "false"

        else:
            print('"', movement, '"', " is an invalid movement. Please try again")
    return player_character, True


def health(battle_result: int, player_character: dict):
    if battle_result == -1:
        player_character["health"] = player_character["health"] - 1
        print("lose health message")
        return player_character

    if battle_result == -2:
        player_character["health"] = player_character["health"] - 2
        print("lose to boss method")
        return player_character

    else:
        return player_character


def experience(battle_result: int, player_character: dict):
    if battle_result == 1:
        player_character["exp"] = player_character["exp"] + 1

        if player_character["level"] == 1 and player_character["exp"] == 4:
            player_character["level"] = 2
            player_character["exp"] = 0
            return player_character, 1

        if player_character["level"] == 2 and player_character["exp"] == 6:
            player_character["level"] = 3
            player_character["exp"] = 0
            return player_character, 1
        else:
            return player_character, 0
    else:
        return player_character, 0


def level_up(player_character: dict):
    if player_character["level"] == 2:
        print("level up 2 message")

    if player_character["level"] == 3:
        print("level up 3 message")

    player_character["health"] = player_character["health"] + 1

    if player_character["re_rolls"] <= player_character["level"]:
        player_character["re_rolls"] = player_character["re_rolls"] + 1

    if player_character["take_away"] < player_character["level"]:
        player_character["take_away"] = player_character["take_away"] + 1

    if player_character["add"] < player_character["level"]:
        player_character["add"] = player_character["add"] + 1

    return player_character


def map_display(maps: dict, player_character: dict):
    for height in range(len(maps["map_visual"])):
        for width in range(len(maps["map_visual"])):
            if height == player_character["player_pos"][0] and width == player_character["player_pos"][1]:
                print("#", end="")
            else:
                print(maps["map_visual"][height][width], end="")
        print("")

    print("")
    print("Legend:  * = Unexplored,    # = Player,    ! = Found Bar,   @ = Beaten Bar,")
    print("Legend:  O = Your Ship,    X = Yawning Portal,    P = Found Port,   C = Found City,")
    player_stats(player_character)
    print("")
    return


def player_stats(player_character: dict):
    print("Stats:  Renown:", player_character["level"], "Reputation: ", player_character["exp"],
          "Credibility", player_character["health"])
    print("Level 1 Skills:  re-rolls: ", player_character["re_roll"])

    if player_character["level"] > 1:
        print("Level 2 Skills:  add 1 to roll:", player_character["add"],
              "remove 1 from roll:", player_character["take_away"])
    return


def play(maps: dict, player_character: dict, run: bool):
    # maps, player_character = location_start(maps, player_character)

    while run:
        map_display(maps, player_character)
        player_character, run = move(player_character)
        map_display(maps, player_character)

        maps, player_character, result, stop = location_finder(maps, player_character)

        player_character = health(result, player_character)
        player_character, up = experience(result, player_character)

        if up == 1:
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
    name = input("player name \n")
    player_character = {"name": name, "player_pos": [4, 0], "health": 3, "level": 1, "exp": 0,
                        "add": 0, "take_away": 0, "re_roll": 1}

    play(maps, player_character, run=True)
    print("Game Over")


def main():
    var()


if __name__ == '__main__':
    main()
