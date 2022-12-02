"""
Assignment 4 Base Function
"""
import map_and_user
import gameplay
import location_callers
import location_descriptions


def win(player_character: dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int]) \
        -> bool:
    """
    Displays the winning text for when a user beats the game then returns false to stop the game loop

    :postcondition: display the win game message
    :return: boolean false
    """
    name = player_character["name"]
    print(f"Having defeated the famous adventurer Volo, {name} has proven themselves as a capable leader"
          " and earned the reputation necessary to captain a vessel."
          " Able to achieve their dream of sailing the oceans wide, you walk back into the city,"
          " grinning as your mind fills with tales of the sea")
    print("You Win")
    return False


def lose(player_character: dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int])\
        -> bool:
    """
    Displays the winning text for when a user loses the game then returns false to stop the game loop

    :postcondition: display the lose game message
    :return: boolean false
    """

    name = player_character["name"]
    print(f"Having faced several losses to the fickle hands of fate {name} "
          f"has lost too much credibility in the town of Waterdeep. "
          f"Your dreams of sailing the seas as a captain are not dissuaded"
          f" and you being you venture to a further port in hopes that the chance to prove yourself "
          f"is just around the corner.")
    print("You Lose")
    return False


def start(maps: dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
          player_character: dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int])\
          -> None:
    """
    Introduces the player to the game world and their goal then plays a practice round with no consequences.

    :param maps: a dictionary of the games maps
    :param player_character: a dictionary of the players characteristics
    :precondition: player_character and maps are set dictionaries and will have all needed values
    :postconditon: add 1 to "re-roll" and return player_character and map
    :return: updated map and player dictionaries
    """
    location_callers.mark_location(maps, player_character,  "1", "O")

    print("Game Explanation")
    print("Practice Battle")
    print("Battle Explanation")
    input("Press enter to continue")

    roll = gameplay.game_set_up(player_character)

    if 15 < roll < 22:
        print("\n \nwin")
    else:
        print("\n \nlose")

    print("Lore")
    print("Goal")
    input("Press enter to continue")

    player_character["re_roll"] = 1

    return


def final_dialogue(score: int) -> int:
    """
    Print unique dialog depending on how the final battle then return a value to show if the player won or lost.

    :param score: an int
    :precondition: score should always be [-2, -1, 1, 2]
    :postconditon: print text and return an int representing if a player won [2] or lost [-2]
    :return: int
    """
    if score == -2:
        print("'Ahh an excellent set of games my good fellow, a shame about you luck, it does happen to the best of us."
              " Still I thank you for the chance to engage in lighthearted merriment and wish all the best"
              " in your future endeavors. Now if you will excuse me, i do believe i hear a drink calling my name.")
        return -2

    if score == -1:
        print("Good show, ahh a good show indeed, you almost had me for a second there,"
              " but no creature can best Volo! Ah, I jest of course,"
              " such vanities lead only to an early grave in my profession."
              " Thank thee anyhow for a chance at such joyous games. I wish you well,"
              " for I hear a fan to whom i must attend my attentions.")
        return -2

    if score == 1:
        print("Oh, Oh my, it would seem that my good fortunes for the day are dwindling. Well then I am a man of "
              "honor and will admit when I am beat. There are not many who can best the great Volo in a game "
              "of fortunes so you should hold yourself in high esteem for that. I pronounce you the winner and wish "
              "you the best in your future endeavors. For now I must go, my next literary masterpiece awaits.")
        return 2

    if score == 2:
        print("Good show, oh good show indeed! It has been far too long since someone has been able to show such a "
              " performance against my talents, wit, and impeccable luck."
              " Well far be it for me to deny such as skillful player their rightful reward. "
              "I pronounce you the winner and that you have bested the mighty Volo!"
              " Forgive me for now i must away as there are might beasts and blood pumping adventures that await me"
              " beyond these walls. Good dayyyyy!")
        return 2


def map_maker(user_map: list):
    """
    makes a list item a list of "*"'s - called only as part of a map function.

    :param user_map: a list
    :preconditon: user_map should be a list inside a list
    :return: a list of five "*"
    """
    return ["*", "*", "*", "*", "*"]


def play(maps: dict[str: list, str: list, str: dict[str: list, str: list, str: list, str: list, str: list]],
         player_character: dict[str: str, str: tuple, str: int, str: int, str: int, str: int, str: int, str: int],
         run: bool) -> None:
    """
    Primary gameplay loop of the game. takes the player to the tutorial then enters a loop of the following:

    display the map, let the player move, show mapa again, take the player to that location, check if they quit
    update player health and experience, update level if necessary, check if the player won or lost the game.

    :param maps: a dictionary
    :param player_character: a dictionary
    :param run: a boolean
    :precondition: maps must contain the game maps, player_character must contain player stats, run = True
    :postcondition: have run the game and displayed if the player won or lost the game
    :return: none
    """
    start(maps, player_character)

    while run:

        map_and_user.map_display(maps, player_character)
        run = map_and_user.move_decider(player_character)
        map_and_user.map_display(maps, player_character)

        outcome, quitter = location_callers.location_finder(maps, player_character)

        if quitter is False:
            break

        map_and_user.health(outcome, player_character)
        up = map_and_user.experience(outcome, player_character)

        if up == 1:
            map_and_user.level_up(player_character)

        if player_character["health"] < 1:
            run = lose(player_character)

        if outcome == 2:
            run = win(player_character)

    return


def var():
    """
    Initialize all variables for the game. Print game over when game stops

    :postcondition: all game variables are initialized, game over is printed
    """
    locations = {"port": [location_descriptions.location_port_1, location_descriptions.location_port_2],
                 "easy": [location_descriptions.location_easy_1, location_descriptions.location_easy_2,
                          location_descriptions.location_easy_3, location_descriptions.location_easy_4,
                          location_descriptions.location_easy_5],

                 "city": [location_descriptions.location_city_1, location_descriptions.location_city_2,
                          location_descriptions.location_city_3, location_descriptions.location_city_4,
                          location_descriptions.location_city_5],

                 "difficult": [location_descriptions.location_difficult_1, location_descriptions.location_difficult_2,
                               location_descriptions.location_difficult_3, location_descriptions.location_difficult_4,
                               location_descriptions.location_difficult_5, location_descriptions.location_difficult_6,
                               location_descriptions.location_difficult_7, location_descriptions.location_difficult_8],

                 "yawn": [location_descriptions.location_yawning_1,
                          location_descriptions.location_yawning_2,
                          location_descriptions.location_yawning_3]}

    player_map = list(map(map_maker, [[], [], [], [], []]))
    maps = {"map_visual": player_map,

            "map_locations": [["3", "3", "3", "y", "4"],
                              ["c", "c", "3", "y", "y"],
                              ["2", "2", "c", "3", "3"],
                              ["p", "2", "2", "c", "3"],
                              ["1", "p", "2", "c", "3"]],

            "locations": locations}

    name = input("Please enter the Name of your character\n")
    player_character = {"name": name,
                        "player_position": [4, 0],
                        "health": 3,
                        "level": 1,
                        "exp": 0,
                        "add": 0,
                        "take_away": 0,
                        "re_roll": 0}

    play(maps, player_character, run=True)
    print("Game Over")


def main():
    """driver"""
    var()


if __name__ == '__main__':
    main()
