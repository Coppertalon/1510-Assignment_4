import game
import map_and_user
import location_callers
import gameplay


def location_start_back(maps: dict, player_character: dict):
    print("start")
    return maps, player_character, 0


def location_port_1(maps: dict, player_character: dict, done=None):
    choice = "none"
    location_callers.mark_location(maps, player_character, location_port_1, "P")
    print("port_1")
    if done:
        location_callers.dont_use_location("found")

    while choice not in ["1", "2"]:
        choice = input("1: Move \n 2: Quit")
        if choice == "1":
            return maps, player_character, 0, False

        if choice == "2":
            return maps, player_character, 0, True

        else:
            print("Invalid choice.")


def location_port_2(maps: dict, player_character: dict, done=None):
    choice = "none"
    location_callers.mark_location(maps, player_character, location_port_2, "P")
    print("port_2")
    if done:
        location_callers.dont_use_location("found")

    while choice not in ["1", "2"]:
        choice = input("1: Move \n 2: Quit")
        if choice == "1":
            return maps, player_character, 0, False

        if choice == "2":
            return maps, player_character, 0, True

        else:
            print("Invalid choice.")


def location_easy_1(maps: dict, player_character: dict, done=None):
    choice = "none"
    print("easy_1")
    if done:
        location_callers.dont_use_location("beat")
        return maps, player_character, 0, True
    elif player_character["level"] > 1:
        location_callers.mark_location(maps, player_character, location_easy_1, "!")
        location_callers.dont_use_location("easy")
        return maps, player_character, 0, True

    map_and_user.player_stats(player_character)

    while choice not in ["1", "2", "3"]:
        choice = input("1: Play \n 2: Leave \n 3: Quit")
        if choice == "1":
            print("start")
            return gameplay.battle_starter(maps, player_character, location_easy_1, 15)

        if choice == "2":
            location_callers.mark_location(maps, player_character, location_easy_1, "!")
            return maps, player_character, 0, True

        if choice == "3":
            return maps, player_character, 0, False

        else:
            print("Invalid choice.")


def location_easy_2(maps: dict, player_character: dict, done=None):
    choice = "none"
    print("easy_2")
    if done:
        location_callers.dont_use_location("beat")
        return maps, player_character, 0, True
    elif player_character["level"] > 1:
        location_callers.mark_location(maps, player_character, location_easy_2, "!")
        location_callers.dont_use_location("easy")
        return maps, player_character, 0, True

    map_and_user.player_stats(player_character)

    while choice not in ["1", "2", "3"]:
        choice = input("1: Play \n 2: Leave \n 3: Quit")
        if choice == "1":
            print("start")
            return gameplay.battle_starter(maps, player_character, location_easy_2, 15)

        if choice == "2":
            location_callers.mark_location(maps, player_character, location_easy_2, "!")
            return maps, player_character, 0, True

        if choice == "3":
            return maps, player_character, 0, False

        else:
            print("Invalid choice.")


def location_easy_3(maps: dict, player_character: dict, done=None):
    choice = "none"
    print("easy_3")
    if done:
        location_callers.dont_use_location("beat")
        return maps, player_character, 0, True
    elif player_character["level"] > 1:
        location_callers.mark_location(maps, player_character, location_easy_3, "!")
        location_callers.dont_use_location("easy")
        return maps, player_character, 0, True

    map_and_user.player_stats(player_character)

    while choice not in ["1", "2", "3"]:
        choice = input("1: Play \n 2: Leave \n 3: Quit")
        if choice == "1":
            print("start")
            return gameplay.battle_starter(maps, player_character, location_easy_3, 16)

        if choice == "2":
            location_callers.mark_location(maps, player_character, location_easy_3, "!")
            return maps, player_character, 0, True

        if choice == "3":
            return maps, player_character, 0, False

        else:
            print("Invalid choice.")


def location_easy_4(maps: dict, player_character: dict, done=None):
    choice = "none"
    print("easy_4")
    if done:
        location_callers.dont_use_location("beat")
        return maps, player_character, 0, True
    elif player_character["level"] > 1:
        location_callers.mark_location(maps, player_character, location_easy_4, "!")
        location_callers.dont_use_location("easy")
        return maps, player_character, 0, True

    map_and_user.player_stats(player_character)

    while choice not in ["1", "2", "3"]:
        choice = input("1: Play \n 2: Leave \n 3: Quit")
        if choice == "1":
            print("start")
            return gameplay.battle_starter(maps, player_character, location_easy_4, 16)

        if choice == "2":
            location_callers.mark_location(maps, player_character, location_easy_4, "!")
            return maps, player_character, 0, True

        if choice == "3":
            return maps, player_character, 0, False

        else:
            print("Invalid choice.")


def location_easy_5(maps: dict, player_character: dict, done=None):
    choice = "none"
    print("easy_5")
    if done:
        location_callers.dont_use_location("beat")
        return maps, player_character, 0, True
    elif player_character["level"] > 1:
        location_callers.mark_location(maps, player_character, location_easy_5, "!")
        location_callers.dont_use_location("easy")
        return maps, player_character, 0, True

    map_and_user.player_stats(player_character)
    while choice not in ["1", "2", "3"]:
        choice = input("1: Play \n 2: Leave \n 3: Quit")
        if choice == "1":
            print("start")
            return gameplay.battle_starter(maps, player_character, location_easy_5, 16)

        if choice == "2":
            location_callers.mark_location(maps, player_character, location_easy_5, "!")
            return maps, player_character, 0, True

        if choice == "3":
            return maps, player_character, 0, False

        else:
            print("Invalid choice.")


def location_city_1(maps: dict, player_character: dict, done=None):
    choice = "none"
    location_callers.mark_location(maps, player_character, location_city_1, "C")
    print("city_1")
    if done:
        location_callers.dont_use_location("found")

    while choice not in ["1", "2"]:
        choice = input("1: Move \n 2: Quit")
        if choice == "1":
            return maps, player_character, 0, False

        if choice == "2":
            return maps, player_character, 0, True

        else:
            print("Invalid choice.")


def location_city_2(maps: dict, player_character: dict, done=None):
    choice = "none"
    location_callers.mark_location(maps, player_character, location_city_2, "C")
    print("city_2")
    if done:
        location_callers.dont_use_location("found")

    while choice not in ["1", "2"]:
        choice = input("1: Move \n 2: Quit")
        if choice == "1":
            return maps, player_character, 0, False

        if choice == "2":
            return maps, player_character, 0, True

        else:
            print("Invalid choice.")


def location_city_3(maps: dict, player_character: dict, done=None):
    choice = "none"
    location_callers.mark_location(maps, player_character, location_city_3, "C")
    print("city_3")
    if done:
        location_callers.dont_use_location("found")

    while choice not in ["1", "2"]:
        choice = input("1: Move \n 2: Quit")
        if choice == "1":
            return maps, player_character, 0, False

        if choice == "2":
            return maps, player_character, 0, True

        else:
            print("Invalid choice.")


def location_city_4(maps: dict, player_character: dict, done=None):
    choice = "none"
    location_callers.mark_location(maps, player_character, location_city_4, "C")
    print("city_4")
    if done:
        location_callers.dont_use_location("found")

    while choice not in ["1", "2"]:
        choice = input("1: Move \n 2: Quit")
        if choice == "1":
            return maps, player_character, 0, False

        if choice == "2":
            return maps, player_character, 0, True

        else:
            print("Invalid choice.")


def location_city_5(maps: dict, player_character: dict, done=None):
    choice = "none"
    location_callers.mark_location(maps, player_character, location_city_5, "C")
    print("city_5")
    if done:
        location_callers.dont_use_location("found")

    while choice not in ["1", "2"]:
        choice = input("1: Move \n 2: Quit")
        if choice == "1":
            return maps, player_character, 0, False

        if choice == "2":
            return maps, player_character, 0, True

        else:
            print("Invalid choice.")


def location_difficult_1(maps: dict, player_character: dict, done=None):
    choice = "none"
    print("difficult_1")
    if done:
        location_callers.dont_use_location("beat")
        return maps, player_character, 0, True
    elif player_character["level"] == 1:
        location_callers.mark_location(maps, player_character, location_difficult_1, "!")
        location_callers.dont_use_location("hard")
        return maps, player_character, 0, True

    map_and_user.player_stats(player_character)

    while choice not in ["1", "2", "3"]:
        choice = input("1: Play \n 2: Leave \n 3: Quit")
        if choice == "1":
            print("start")
            return gameplay.battle_starter(maps, player_character, location_difficult_1, 17)

        if choice == "2":
            location_callers.mark_location(maps, player_character, location_difficult_1, "!")
            return maps, player_character, 0, True

        if choice == "3":
            return maps, player_character, 0, False

        else:
            print("Invalid choice.")


def location_difficult_2(maps: dict, player_character: dict, done=None):
    choice = "none"
    print("difficult_2")
    if done:
        location_callers.dont_use_location("beat")
        return maps, player_character, 0, True
    elif player_character["level"] == 1:
        location_callers.mark_location(maps, player_character, location_difficult_2, "!")
        location_callers.dont_use_location("hard")
        return maps, player_character, 0, True

    map_and_user.player_stats(player_character)

    while choice not in ["1", "2", "3"]:
        choice = input("1: Play \n 2: Leave \n 3: Quit")
        if choice == "1":
            print("start")
            return gameplay.battle_starter(maps, player_character, location_difficult_2, 17)

        if choice == "2":
            location_callers.mark_location(maps, player_character, location_difficult_2, "!")
            return maps, player_character, 0, True

        if choice == "3":
            return maps, player_character, 0, False

        else:
            print("Invalid choice.")


def location_difficult_3(maps: dict, player_character: dict, done=None):
    choice = "none"
    print("difficult_3")
    if done:
        location_callers.dont_use_location("beat")
        return maps, player_character, 0, True
    elif player_character["level"] == 1:
        location_callers.mark_location(maps, player_character, location_difficult_3, "!")
        location_callers.dont_use_location("hard")
        return maps, player_character, 0, True

    map_and_user.player_stats(player_character)

    while choice not in ["1", "2", "3"]:
        choice = input("1: Play \n 2: Leave \n 3: Quit")
        if choice == "1":
            print("start")
            return gameplay.battle_starter(maps, player_character, location_difficult_3, 17)

        if choice == "2":
            location_callers.mark_location(maps, player_character, location_difficult_3, "!")
            return maps, player_character, 0, True

        if choice == "3":
            return maps, player_character, 0, False

        else:
            print("Invalid choice.")


def location_difficult_4(maps: dict, player_character: dict, done=None):
    choice = "none"
    print("difficult_4")
    if done:
        location_callers.dont_use_location("beat")
        return maps, player_character, 0, True
    elif player_character["level"] == 1:
        location_callers.mark_location(maps, player_character, location_difficult_4, "!")
        location_callers.dont_use_location("hard")
        return maps, player_character, 0, True

    map_and_user.player_stats(player_character)

    while choice not in ["1", "2", "3"]:
        choice = input("1: Play \n 2: Leave \n 3: Quit")
        if choice == "1":
            print("start")
            return gameplay.battle_starter(maps, player_character, location_difficult_4, 17)

        if choice == "2":
            location_callers.mark_location(maps, player_character, location_difficult_4, "!")
            return maps, player_character, 0, True

        if choice == "3":
            return maps, player_character, 0, False

        else:
            print("Invalid choice.")


def location_difficult_5(maps: dict, player_character: dict, done=None):
    choice = "none"
    print("difficult_5")
    if done:
        location_callers.dont_use_location("beat")
        return maps, player_character, 0, True
    elif player_character["level"] == 1:
        location_callers.mark_location(maps, player_character, location_difficult_5, "!")
        location_callers.dont_use_location("hard")
        return maps, player_character, 0, True

    map_and_user.player_stats(player_character)

    while choice not in ["1", "2", "3"]:
        choice = input("1: Play \n 2: Leave \n 3: Quit")
        if choice == "1":
            print("start")
            return gameplay.battle_starter(maps, player_character, location_difficult_5, 17)

        if choice == "2":
            location_callers.mark_location(maps, player_character, location_difficult_5, "!")
            return maps, player_character, 0, True

        if choice == "3":
            return maps, player_character, 0, False

        else:
            print("Invalid choice.")


def location_difficult_6(maps: dict, player_character: dict, done=None):
    choice = "none"
    print("difficult_6")
    if done:
        location_callers.dont_use_location("beat")
        return maps, player_character, 0, True
    elif player_character["level"] == 1:
        location_callers.mark_location(maps, player_character, location_difficult_6, "!")
        location_callers.dont_use_location("hard")
        return maps, player_character, 0, True

    map_and_user.player_stats(player_character)

    while choice not in ["1", "2", "3"]:
        choice = input("1: Play \n 2: Leave \n 3: Quit")
        if choice == "1":
            print("start")
            return gameplay.battle_starter(maps, player_character, location_difficult_6, 18)

        if choice == "2":
            location_callers.mark_location(maps, player_character, location_difficult_6, "!")
            return maps, player_character, 0, True

        if choice == "3":
            return maps, player_character, 0, False

        else:
            print("Invalid choice.")


def location_difficult_7(maps: dict, player_character: dict, done=None):
    choice = "none"
    print("difficult_7")
    if done:
        location_callers.dont_use_location("beat")
        return maps, player_character, 0, True
    elif player_character["level"] == 1:
        location_callers.mark_location(maps, player_character, location_difficult_7, "!")
        location_callers.dont_use_location("hard")
        return maps, player_character, 0, True

    map_and_user.player_stats(player_character)

    while choice not in ["1", "2", "3"]:
        choice = input("1: Play \n 2: Leave \n 3: Quit")
        if choice == "1":
            print("start")
            return gameplay.battle_starter(maps, player_character, location_difficult_7, 18)

        if choice == "2":
            location_callers.mark_location(maps, player_character, location_difficult_7, "!")
            return maps, player_character, 0, True

        if choice == "3":
            return maps, player_character, 0, False

        else:
            print("Invalid choice.")


def location_difficult_8(maps: dict, player_character: dict, done=None):
    choice = "none"
    print("difficult_8")
    if done:
        location_callers.dont_use_location("beat")
        return maps, player_character, 0, True
    elif player_character["level"] == 1:
        location_callers.mark_location(maps, player_character, location_difficult_8, "!")
        location_callers.dont_use_location("hard")
        return maps, player_character, 0, True

    map_and_user.player_stats(player_character)

    while choice not in ["1", "2", "3"]:
        choice = input("1: Play \n 2: Leave \n 3: Quit")
        if choice == "1":
            print("start")
            return gameplay.battle_starter(maps, player_character, location_difficult_8, 18)

        if choice == "2":
            location_callers.mark_location(maps, player_character, location_difficult_8, "!")
            return maps, player_character, 0, True

        if choice == "3":
            return maps, player_character, 0, False

        else:
            print("Invalid choice.")


def location_yawning_1(maps: dict, player_character: dict, done=None):
    choice = "none"
    location_callers.mark_location(maps, player_character, location_yawning_1, "X")
    print("yawn_1")
    if done:
        location_callers.dont_use_location("found")

    while choice not in ["1", "2"]:
        choice = input("1: Move \n 2: Quit")
        if choice == "1":
            return maps, player_character, 0, False

        if choice == "2":
            return maps, player_character, 0, True

        else:
            print("Invalid choice.")


def location_yawning_2(maps: dict, player_character: dict, done=None):
    choice = "none"
    location_callers.mark_location(maps, player_character, location_yawning_2, "X")
    print("yawn_2")
    if done:
        location_callers.dont_use_location("found")

    while choice not in ["1", "2"]:
        choice = input("1: Move \n 2: Quit")
        if choice == "1":
            return maps, player_character, 0, False

        if choice == "2":
            return maps, player_character, 0, True

        else:
            print("Invalid choice.")


def location_yawning_3(maps: dict, player_character: dict, done=None):
    choice = "none"
    location_callers.mark_location(maps, player_character, location_yawning_3, "X")
    print("yawn_3")
    if done:
        location_callers.dont_use_location("found")

    while choice not in ["1", "2"]:
        choice = input("1: Move \n 2: Quit")
        if choice == "1":
            return maps, player_character, 0, False

        if choice == "2":
            return maps, player_character, 0, True

        else:
            print("Invalid choice.")


def location_end(maps: dict, player_character: dict):
    if player_character["level"] > 2:
        print("end")
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
        return maps, player_character, 0, False

    print("too low")
    return maps, player_character, 0, False
