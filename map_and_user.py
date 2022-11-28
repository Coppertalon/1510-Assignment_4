"""
Assignment 4 Map and Player functions
"""
def move_decided(player_character: dict):

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
            player_character, movement = player_mover(player_character, movement)

        else:
            print('"', movement, '"', " is an invalid movement. Please try again")

    return player_character, True


def player_mover(player_character, movement):

    if movement == "1" and player_character["player_position"][0] > 0:
        player_character["player_position"][0] -= 1

    elif movement == "2" and player_character["player_position"][0] < 4:
        player_character["player_position"][0] += 1

    elif movement == "3" and player_character["player_position"][1] > 0:
        player_character["player_position"][1] -= 1

    elif movement == "4" and player_character["player_position"][1] < 4:
        player_character["player_position"][1] += 1

    else:
        print('"', movement, '"', " is an invalid movement. Please try again")
        movement = "false"

    return player_character, movement


def health(outcome: int, player_character: dict):
    if outcome == -1:
        player_character["health"] = player_character["health"] - 1
        print("lose health message")
        return player_character

    if outcome == -2:
        player_character["health"] = player_character["health"] - 2
        print("lose to boss method")
        return player_character

    else:
        return player_character


def experience(outcome: int, player_character: dict):
    if outcome == 1:
        player_character["exp"] = player_character["exp"] + 1

        if player_character["level"] == 1 and player_character["exp"] == 3:
            player_character["level"] = 2
            player_character["exp"] = 0
            return player_character, 1

        if player_character["level"] == 2 and player_character["exp"] == 5:
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

    if player_character["re_roll"] <= player_character["level"]:
        player_character["re_roll"] = player_character["re_roll"] + 1

    if player_character["take_away"] < player_character["level"]:
        player_character["take_away"] = player_character["take_away"] + 1

    if player_character["add"] < player_character["level"]:
        player_character["add"] = player_character["add"] + 1

    return player_character


def map_display(maps: dict, player_character: dict):
    print("\n \n \n")

    for height in range(len(maps["map_visual"])):
        for width in range(len(maps["map_visual"])):

            if height == player_character["player_position"][0] and width == player_character["player_position"][1]:
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

    print("Stats:  Renown:", player_character["level"], "  Reputation: ", player_character["exp"],
          "  Credibility", player_character["health"])
    print("Level 1 Skills:  Re-rolls: ", player_character["re_roll"])

    if player_character["level"] > 1:
        print("Level 2 Skills:  Add 1 to roll:", player_character["add"],
              "  Remove 1 from roll:", player_character["take_away"])

    return
