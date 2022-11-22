
player_pos = [0, 4]
map = [["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"],
       ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"]]


def map_display():
    for height in range(len(map)):
        for width in range(len(map)):
            if width == player_pos[0] and height == player_pos[1]:
                print("#", end="")
            else:
                print(map[width][height], end="")
        print("")
    print("Legend:")
    return


def move():
    valid_moves = ["n", "s", "w", "e", "north", "south", "west", "east"]
    map_display()
    while True:
        movement = input("movement \n")
        if movement.lower() in valid_moves:
            if (movement.lower() == "n"  and player_pos[1] > 0) or (movement.lower() == "north" and player_pos[1] > 0):
                player_pos[1] += -1
                map_display()
            elif (movement.lower() == "s" and player_pos[1] < 4) or (movement.lower() == "south" and player_pos[1] < 4):
                player_pos[1] += 1
                map_display()
            elif (movement.lower() == "w" and player_pos[0] > 0) or (movement.lower() == "west" and player_pos[0] > 0):
                player_pos[0] -= 1
                map_display()
            elif (movement.lower() == "e" and player_pos[0] < 4) or (movement.lower() == "east" and player_pos[0] < 4):
                player_pos[0] += 1
                map_display()
            else:
                print('"' + movement + '"' + " is an invalid movement. Please try again")

        else:
            print('"' + movement + '"' + " is an invalid movement. Please try again")


def main():
    move()


if __name__ == '__main__':
    main()
