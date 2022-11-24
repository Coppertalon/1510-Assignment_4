def map_display(player_pos, map_visual, health, level, exp, re_rolls,  add, take_away):
    for height in range(len(map_visual)):
        for width in range(len(map_visual)):
            if width == player_pos[0] and height == player_pos[1]:
                print("#", end="")
            else:
                print(map_visual[width][height], end="")
        print("")
    print("Legend:"+ health + level + exp + re_rolls + add + take_away)
    return


def move(player_pos):

    valid_moves = ["n", "s", "w", "e", "north", "south", "west", "east"]
    movement = ""

    while movement not in valid_moves:
        movement = input("movement \n")
        if movement.lower() in valid_moves:
            if (movement.lower() == "n"  and player_pos[1] > 0) or (movement.lower() == "north" and player_pos[1] > 0):
                player_pos[1] += -1
            elif (movement.lower() == "s" and player_pos[1] < 4) or (movement.lower() == "south" and player_pos[1] < 4):
                player_pos[1] += 1
            elif (movement.lower() == "w" and player_pos[0] > 0) or (movement.lower() == "west" and player_pos[0] > 0):
                player_pos[0] -= 1
            elif (movement.lower() == "e" and player_pos[0] < 4) or (movement.lower() == "east" and player_pos[0] < 4):
                player_pos[0] += 1
            else:
                print('"' + movement + '"' + " is an invalid movement. Please try again")

        else:
            print('"' + movement + '"' + " is an invalid movement. Please try again")
    return player_pos


def location_finder(player_pos, map_visual,  map_locations,  re_rolls, add, take_away):
    if map_locations[player_pos[0]][player_pos[1]] == 1:
        return location_start_back(player_pos, map_visual,  map_locations,  re_rolls, add, take_away)
    if map_locations[player_pos[0]][player_pos[1]] == 2:
        return location_easy(player_pos, map_visual,  map_locations,  re_rolls, add, take_away)
    if map_locations[player_pos[0]][player_pos[1]] == 3:
        return location_hard(player_pos, map_visual,  map_locations,  re_rolls, add, take_away)
    if map_locations[player_pos[0]][player_pos[1]] == 4:
        return location_end(player_pos, map_visual,  map_locations,  re_rolls, add, take_away)
    if map_locations[player_pos[0]][player_pos[1]] == "p":
        return location_none_port(player_pos, map_visual,  map_locations,  re_rolls, add, take_away)
    if map_locations[player_pos[0]][player_pos[1]] == "c":
        return location_none_city(player_pos, map_visual,  map_locations,  re_rolls, add, take_away)
    if map_locations[player_pos[0]][player_pos[1]] == "y":
        return location_none_yawning_portal(player_pos, map_visual,  map_locations,  re_rolls, add, take_away)
    elif map_locations[player_pos[0]][player_pos[1]] in ["p1", "p2", "c1", "c2", "c3", "c4", "c5", "y1", "y2", "y3"]:
        return explored(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, True)
    else:
        return beaten(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, True)


def location_none_port(player_pos, map_visual, map_locations, re_rolls, add, take_away):


def location_none_city(player_pos, map_visual, map_locations, re_rolls, add, take_away):


def location_none_yawning_portal(player_pos, map_visual, map_locations, re_rolls, add, take_away):


def location_easy(player_pos, map_visual, map_locations, re_rolls, add, take_away):


def location_hard(player_pos, map_visual, map_locations, re_rolls, add, take_away):


def beaten(player_pos, map_visual, map_locations, re_rolls, add, take_away, beat):
    if map_locations[player_pos[0]][player_pos[1]] == \
            "easy1": location_easy_bar_1(player_pos, map_visual, map_locations, re_rolls, add, take_away, beat)
    if map_locations[player_pos[0]][player_pos[1]] == \
            "easy2": location_easy_bar_2(player_pos, map_visual, map_locations, re_rolls, add, take_away, beat)
    if map_locations[player_pos[0]][player_pos[1]] == \
            "easy3": location_easy_bar_3(player_pos, map_visual, map_locations, re_rolls, add, take_away, beat)
    if map_locations[player_pos[0]][player_pos[1]] == \
            "easy4": location_easy_bar_4(player_pos, map_visual, map_locations, re_rolls, add, take_away, beat)
    if map_locations[player_pos[0]][player_pos[1]] == \
            "easy5": location_easy_bar_5(player_pos, map_visual, map_locations, re_rolls, add, take_away, beat)
    if map_locations[player_pos[0]][player_pos[1]] == \
            "diff1": location_difficult_1(player_pos, map_visual, map_locations, re_rolls, add, take_away, beat)
    if map_locations[player_pos[0]][player_pos[1]] == \
            "diff2": location_difficult_2(player_pos, map_visual, map_locations, re_rolls, add, take_away, beat)
    if map_locations[player_pos[0]][player_pos[1]] == \
            "diff3": location_difficult_3(player_pos, map_visual, map_locations, re_rolls, add, take_away, beat)
    if map_locations[player_pos[0]][player_pos[1]] == \
            "diff4": location_difficult_4(player_pos, map_visual, map_locations, re_rolls, add, take_away, beat)
    if map_locations[player_pos[0]][player_pos[1]] == \
            "diff5": location_difficult_5(player_pos, map_visual, map_locations, re_rolls, add, take_away, beat)
    if map_locations[player_pos[0]][player_pos[1]] == \
            "diff6": location_difficult_6(player_pos, map_visual, map_locations, re_rolls, add, take_away, beat)
    if map_locations[player_pos[0]][player_pos[1]] == \
            "diff7": location_difficult_7(player_pos, map_visual, map_locations, re_rolls, add, take_away, beat)
    if map_locations[player_pos[0]][player_pos[1]] == \
            "diff8": location_difficult_8(player_pos, map_visual, map_locations, re_rolls, add, take_away, beat)


def explored(player_pos, map_visual, map_locations,re_rolls, add, take_away, found):
    if map_locations[player_pos[0]][player_pos[1]] == "p1":
        location_none_port_1(player_pos, map_visual, map_locations, re_rolls, add, take_away, found)
    if map_locations[player_pos[0]][player_pos[1]] == "p2":
        location_none_port_2(player_pos, map_visual, map_locations, re_rolls, add, take_away, found)
    if map_locations[player_pos[0]][player_pos[1]] == "c1":
        location_none_city_1(player_pos, map_visual, map_locations, re_rolls, add, take_away, found)
    if map_locations[player_pos[0]][player_pos[1]] == "c2":
        location_none_city_2(player_pos, map_visual, map_locations, re_rolls, add, take_away, found)
    if map_locations[player_pos[0]][player_pos[1]] == "c3":
        location_none_city_3(player_pos, map_visual, map_locations, re_rolls, add, take_away, found)
    if map_locations[player_pos[0]][player_pos[1]] == "c4":
        location_none_city_4(player_pos, map_visual, map_locations, re_rolls, add, take_away, found)
    if map_locations[player_pos[0]][player_pos[1]] == "c5":
        location_none_city_5(player_pos, map_visual, map_locations, re_rolls, add, take_away, found)
    if map_locations[player_pos[0]][player_pos[1]] == "y1":
        location_none_yawning_1(player_pos, map_visual, map_locations, re_rolls, add, take_away, found)
    if map_locations[player_pos[0]][player_pos[1]] == "y2":
        location_none_yawning_2(player_pos, map_visual, map_locations, re_rolls, add, take_away, found)
    if map_locations[player_pos[0]][player_pos[1]] == "y3":
        location_none_yawning_3(player_pos, map_visual, map_locations, re_rolls, add, take_away, found)


def player_health(modify, health):
    if modify == -1:
        health -= 1
        print("lose health message")
        return health

    if modify == -2:
        health -= 2
        print("lose to boss method")
        return health

    if modify == 0:
        return health


def experience(gain, level, exp):
    if gain != 1:
        return level, exp, False
    if gain == 1:
        exp += 1
        if level == 1 and exp == 4:
            level = 2
            exp = 0
            return level, exp, True
        if level == 2 and exp == 6:
            level = 3
            exp = 0
            return level, exp, True
        else:
            up = False
            return level, exp, up


def level_up(health, level, re_rolls, add, take_away):
    if level == 2:
        print("level up 2 message")
    if level == 3:
        print("level up 3 message")
    if health <= 3:
        health += 1
    if re_rolls <= level:
        re_rolls += 1
    if re_rolls < level:
        add += 1
    if re_rolls < level:
        take_away += 1
    return health, level, re_rolls, add, take_away


def lose():
    print("lose text")
    return False


def win():
    print("win text")
    return False


def location_start():
    print("start tutorial")


def location_start_back(player_pos, map_visual,  map_locations,  re_rolls, add, take_away):


def location_none_port_1(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, found = None):


def location_none_port_2(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, found = None):


def location_easy_bar_1(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, beat = None):


def location_easy_bar_2(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, beat = None):


def location_easy_bar_3(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, beat = None):


def location_easy_bar_4(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, beat = None):


def location_easy_bar_5(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, beat = None):


def location_none_city_1(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, found = None):


def location_none_city_2(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, found = None ):


def location_none_city_3(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, found = None):


def location_none_city_4(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, found = None):


def location_none_city_5(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, found = None):


def location_difficult_1(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, beat = None):


def location_difficult_2(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, beat = None):


def location_difficult_3(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, beat = None):


def location_difficult_4(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, beat = None):


def location_difficult_5(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, beat = None):


def location_difficult_6(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, beat = None):


def location_difficult_7(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, beat = None):


def location_difficult_8(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, beat = None):


def location_none_yawning_1(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, found = None):


def location_none_yawning_2(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, found = None):


def location_none_yawning_3(player_pos, map_visual,  map_locations,  re_rolls, add, take_away, found = None):


def location_end(player_pos, map_visual,  map_locations,  re_rolls, add, take_away):



def play(map_visual, map_locations, player_pos, health, level, exp, stop, add, take_away, re_rolls)
    location_start()
    while stop:
        map_display(player_pos, map_visual, health, level, exp, re_rolls, add, take_away)

        player_pos = move(player_pos, map_visual)
        map_display(player_pos, map_visual, health, level, exp, re_rolls, add, take_away)

        map_visual, map_locations, modify, gain, re_rolls, add, take_away  = location_finder(player_pos, map_visual, map_locations, re_rolls, add, take_away)

        health = player_health(modify, health)

        level, exp, up = experience(gain, level, exp)
        if up:
            health, level, re_rolls, add, take_away = level_up(health, level, re_rolls, add, take_away)

        if health < 1:
            stop = lose()

        if gain == 2:
            stop = win()
    return


def var():
    map_visual = [["*", "*", "*", "*", "*"],
                  ["*", "*", "*", "*", "*"],
                  ["*", "*", "*", "*", "*"],
                  ["*", "*", "*", "*", "*"],
                  ["*", "*", "*", "*", "*"]]

    map_locations = [["3", "3", "3", "y", "4"],
                     ["c", "c", "3", "y", "y"],
                     ["2", "2", "c", "3", "3"],
                     ["p", "2", "2", "c", "3"],
                     ["1", "p", "2", "c", "3"]]

    player_pos = [0, 4]
    health = 3
    level = 1
    exp = 0
    stop = True
    add = 0
    take_away = 0
    re_rolls = 1
    play(map_visual, map_locations, player_pos, health, level, exp, stop, add, take_away, re_rolls)


def main():
    var()


if __name__ == '__main__':
    main()
