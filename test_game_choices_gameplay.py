from unittest import TestCase
from unittest.mock import patch
from gameplay import game_choices
import io


class Test(TestCase):

    @patch('random.randint', return_value=5)
    @patch('builtins.input', side_effect=['1'])
    def test_game_choices_roll(self, mock_input, mock_random):
        total, roll, action, character = game_choices({"name": "test",
                        "player_position": [4, 0],
                        "health": 3,
                        "level": 1,
                        "exp": 0,
                        "add": 0,
                        "take_away": 0,
                        "re_roll": 0}, 10, 3)

        self.assertEqual(total, 15)

    @patch('random.randint', return_value=5)
    @patch('builtins.input', side_effect=['2'])
    def test_game_choices_re_roll(self, mock_input, mock_random):
        total, roll, action, character = game_choices({"name": "test",
                                                       "player_position": [4, 0],
                                                       "health": 3,
                                                       "level": 1,
                                                       "exp": 0,
                                                       "add": 0,
                                                       "take_away": 0,
                                                       "re_roll": 0}, 10, 3)

        self.assertEqual(total, 12)

    @patch('random.randint', return_value=5)
    @patch('builtins.input', side_effect=['3'])
    def test_game_choices_hold(self, mock_input, mock_random):
        total, roll, action, character = game_choices({"name": "test",
                                                       "player_position": [4, 0],
                                                       "health": 3,
                                                       "level": 1,
                                                       "exp": 0,
                                                       "add": 0,
                                                       "take_away": 0,
                                                       "re_roll": 0}, 10, 3)

        self.assertEqual(action, "hold")
        self.assertEqual(total, 10)

    @patch('random.randint', return_value=5)
    @patch('builtins.input', side_effect=['4'])
    def test_game_choices_re_roll(self, mock_input, mock_random):
        total, roll, action, character = game_choices({"name": "test",
                                                       "player_position": [4, 0],
                                                       "health": 3,
                                                       "level": 1,
                                                       "exp": 0,
                                                       "add": 0,
                                                       "take_away": 0,
                                                       "re_roll": 0}, 10, 3)

        self.assertEqual(total, 11)

    @patch('random.randint', return_value=5)
    @patch('builtins.input', side_effect=['5'])
    def test_game_choices_re_roll(self, mock_input, mock_random):
        total, roll, action, character = game_choices({"name": "test",
                                                       "player_position": [4, 0],
                                                       "health": 3,
                                                       "level": 1,
                                                       "exp": 0,
                                                       "add": 0,
                                                       "take_away": 0,
                                                       "re_roll": 0}, 10, 3)

        self.assertEqual(total, 9)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=5)
    @patch('builtins.input', side_effect=['5'])
    def test_game_choices_re_roll(self, mock_input, mock_random, get_output):
        total, roll, action, character = game_choices({"name": "test",
                                                       "player_position": [4, 0],
                                                       "health": 3,
                                                       "level": 1,
                                                       "exp": 0,
                                                       "add": 0,
                                                       "take_away": 0,
                                                       "re_roll": 0}, 10, 3)
        output = get_output.getvalue()
        self.assertIn("bad choice\n", output)
        self.assertEqual(total, 10)
