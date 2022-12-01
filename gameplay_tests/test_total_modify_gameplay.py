from unittest import TestCase
from gameplay import total_modify


class Test(TestCase):

    def test_total_modify_add(self):
        total, roll, quitter, player_character = total_modify(10, 1, "4",
                                                              {"name": "test",
                                                               "player_position": [4, 0],
                                                               "health": 3,
                                                               "level": 2,
                                                               "exp": 0,
                                                               "add": 1,
                                                               "take_away": 1,
                                                               "re_roll": 1})
        self.assertEqual(total, 11)
        self.assertEqual(player_character, {"name": "test",
                                            "player_position": [4, 0],
                                            "health": 3,
                                            "level": 2,
                                            "exp": 0,
                                            "add": 0,
                                            "take_away": 1,
                                            "re_roll": 1})

    def test_total_modify_take_away(self):
        total, roll, quitter, player_character = total_modify(10, 1, "5",
                                                              {"name": "test",
                                                               "player_position": [4, 0],
                                                               "health": 3,
                                                               "level": 2,
                                                               "exp": 0,
                                                               "add": 1,
                                                               "take_away": 1,
                                                               "re_roll": 1})
        self.assertEqual(total, 9)
        self.assertEqual(player_character, {"name": "test",
                                            "player_position": [4, 0],
                                            "health": 3,
                                            "level": 2,
                                            "exp": 0,
                                            "add": 1,
                                            "take_away": 0,
                                            "re_roll": 1})
