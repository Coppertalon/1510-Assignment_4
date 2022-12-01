from unittest import TestCase
from unittest.mock import patch
import io
from gameplay import game_actions


class Test(TestCase):

    def test_rolling_hold(self):
        total, roll, quitter, player_character = game_actions(10, 3, {"name": "test",
                                                          "player_position": [4, 0],
                                                          "health": 3,
                                                          "level": 2,
                                                          "exp": 0,
                                                          "add": 1,
                                                          "take_away": 1,
                                                          "re_roll": 1}, "3",)
        self.assertEqual(quitter, "hold")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_rolling_invalid_choice(self, get_output):
        game_actions(10, 3, {"name": "test",
                             "player_position": [4, 0],
                             "health": 3,
                             "level": 2,
                             "exp": 0,
                             "add": 1,
                             "take_away": 1,
                             "re_roll": 1}, "7",)
        output = get_output.getvalue()
        self.assertEqual(output, "you can't do that\n")
