import random
import location_callers


def battle_starter(maps: dict, player_character: dict, location, roll_to_beat: int):
    roll, player_character = game_set_up(player_character)
    if roll_to_beat < roll < 22:
        location_callers.mark_location(maps, player_character, location, "@")
        print("win")
        return maps, player_character, 1, True
    else:
        location_callers.mark_location(maps, player_character, location, "!")
        print("lose")
        return maps, player_character, -1, True


def game_set_up(player_character: dict):

    rolls = [random.randint(1, 6) for i in range(3)]
    print("\nYou rolled :", rolls)
    total = rolls[0] + rolls[1] + rolls[2]
    action = "roll"
    roll = rolls[2]

    while total < 27 and action != "hold":
        print("\n")
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
