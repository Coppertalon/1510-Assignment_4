def map_display(player_pos, map_visual, health, level, exp):
    for height in range(len(map_visual)):
        for width in range(len(map_visual)):
            if width == player_pos[0] and height == player_pos[1]:
                print("#", end="")
            else:
                print(map_visual[width][height], end="")
        print("")
    print("Legend:"+ health + level + exp)
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




def player_health(modify, health):
    if modify == 1:
        health += 1
        if health > 3:
            health = 3
        print(health)
        return health

    if modify == -1:
        health -= 1
        print(health)
        return health

    if modify == 0:
        return health


def experience(gain, level, exp):
    if gain == 0:
        return
    if gain == 1:
        exp += 1
        if level == 1 and exp == 4:
            level = 2
            exp = 0
            up = True
            return level, exp, up
        if level == 2 and exp == 6:
            level = 3
            exp = 0
            up = True
            return level, exp, up
        else:
            up = False
            return level, exp, up


def level_up(health, level, re_rolls, add, take_away):
    if level == 2:
        print("level up 2 message")
    if level == 2:
        print("level up 3 message")
    player_health(1, health)

    if re_rolls <= level:
        re_rolls += 1
    if re_rolls < level:
        add += 1
    if re_rolls < level:
        take_away += 1


def lose():
    print("lose text")
    stop = 1
    return False


def win():
    print("win text")
    stop = 1
    return False


def play():
    map_visual = [["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"],
                  ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"]]
    player_pos = [0, 4]
    health = 3
    level = 1
    exp = 0
    stop = True
    add = 0
    take_away = 0
    re_rolls = 1
    location_start()

    while stop:
        map_display(player_pos, map_visual, health, level, exp, re_rolls, add, take_away)

        player_pos = move(player_pos, map_visual)
        map_display(player_pos, map_visual, health, level, exp, re_rolls, add, take_away)

        map_visual, modify, gain,  = location_finder(player_pos, map_visual, re_rolls, add, take_away)

        health = player_health(modify, health)
        if health < 1:
            stop = lose()

        if modify == 2 and gain == 2:
            stop = win()

        level, exp, up = experience(gain, level, exp)

        if up:
            level_up(health, level, re_rolls, add, take_away)

    return


def main():
    play()


if __name__ == '__main__':
    main()
