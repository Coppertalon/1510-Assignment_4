from unittest import TestCase
from unittest.mock import patch
from gameplay import rolling
import random

class Test(TestCase):

    @patch('random.randint', return_value=5)
    def test_rolling_roll(self, roll_setter):
        total, roll, quitter, player_character = rolling(10, 3, "1",
                                                              {"name": "test",
                                                               "player_position": [4, 0],
                                                               "health": 3,
                                                               "level": 2,
                                                               "exp": 0,
                                                               "add": 1,
                                                               "take_away": 1,
                                                               "re_roll": 1})
        self.assertEqual(total, 15)
        self.assertEqual(player_character, {"name": "test",
                                            "player_position": [4, 0],
                                            "health": 3,
                                            "level": 2,
                                            "exp": 0,
                                            "add": 1,
                                            "take_away": 1,
                                            "re_roll": 1})

    @patch('random.randint', return_value=5)
    def test_rolling_reroll(self, roll_setter):
        total, roll, quitter, player_character = rolling(10, 3, "2",
                                                              {"name": "test",
                                                               "player_position": [4, 0],
                                                               "health": 3,
                                                               "level": 2,
                                                               "exp": 0,
                                                               "add": 1,
                                                               "take_away": 1,
                                                               "re_roll": 1})
        self.assertEqual(total, 12)
        self.assertEqual(player_character, {"name": "test",
                                            "player_position": [4, 0],
                                            "health": 3,
                                            "level": 2,
                                            "exp": 0,
                                            "add": 1,
                                            "take_away": 1,
                                            "re_roll": 0})
