from unittest import TestCase
from unittest.mock import patch

from gameplay import game_set_up
from game import start
import io


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1', '3', '1'])
    @patch(game_set_up({"name": "test",
                        "player_position": [4, 0],
                        "health": 3,
                        "level": 1,
                        "exp": 0,
                        "add": 0,
                        "take_away": 0,
                        "re_roll": 0}), return_value=(17, {"name": "test",
                        "player_position": [4, 0],
                        "health": 3,
                        "level": 1,
                        "exp": 0,
                        "add": 0,
                        "take_away": 0,
                        "re_roll": 0}))
    def test_start_win(self, mock_function, mock_inputs, get_output):

        player_character = {"name": "test",
                        "player_position": [4, 0],
                        "health": 3,
                        "level": 1,
                        "exp": 0,
                        "add": 0,
                        "take_away": 0,
                        "re_roll": 0}

        maps = {"map_visual": [["*", "*", "*", "*", "*"],
                              ["*", "*", "*", "*", "*"],
                              ["*", "*", "*", "*", "*"],
                              ["*", "*", "*", "*", "*"],
                              ["*", "*", "*", "*", "*"]],
                "map_locations": [["3", "3", "3", "y", "4"],
                              ["c", "c", "3", "y", "y"],
                              ["2", "2", "c", "3", "3"],
                              ["p", "2", "2", "c", "3"],
                              ["1", "p", "2", "c", "3"]]}

        start(maps, player_character)

        output = get_output.getvalue()
        expected_output = "\n\nwin\n"

        self.assertIn(expected_output, output)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch(game_set_up({"name": "test",
                        "player_position": [4, 0],
                        "health": 3,
                        "level": 1,
                        "exp": 0,
                        "add": 0,
                        "take_away": 0,
                        "re_roll": 0}), return_value=(13, {"name": "test",
                                                           "player_position": [4, 0],
                                                           "health": 3,
                                                           "level": 1,
                                                           "exp": 0,
                                                           "add": 0,
                                                           "take_away": 0,
                                                           "re_roll": 0}))
    def test_start_lose_low(self, mock_function, get_output):
        player_character = {"name": "test",
                            "player_position": [4, 0],
                            "health": 3,
                            "level": 1,
                            "exp": 0,
                            "add": 0,
                            "take_away": 0,
                            "re_roll": 0}

        maps = {"map_visual": [["*", "*", "*", "*", "*"],
                               ["*", "*", "*", "*", "*"],
                               ["*", "*", "*", "*", "*"],
                               ["*", "*", "*", "*", "*"],
                               ["*", "*", "*", "*", "*"]],
                "map_locations": [["3", "3", "3", "y", "4"],
                                  ["c", "c", "3", "y", "y"],
                                  ["2", "2", "c", "3", "3"],
                                  ["p", "2", "2", "c", "3"],
                                  ["1", "p", "2", "c", "3"]]}

        start(maps, player_character)

        output = get_output.getvalue()
        expected_output = "\n\nlose\n"

        self.assertIn(expected_output, output)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch(game_set_up({"name": "test",
                        "player_position": [4, 0],
                        "health": 3,
                        "level": 1,
                        "exp": 0,
                        "add": 0,
                        "take_away": 0,
                        "re_roll": 0}), return_value=(23, {"name": "test",
                                                           "player_position": [4, 0],
                                                           "health": 3,
                                                           "level": 1,
                                                           "exp": 0,
                                                           "add": 0,
                                                           "take_away": 0,
                                                           "re_roll": 0}))
    def test_start_lose_low(self, mock_function, get_output):
        player_character = {"name": "test",
                            "player_position": [4, 0],
                            "health": 3,
                            "level": 1,
                            "exp": 0,
                            "add": 0,
                            "take_away": 0,
                            "re_roll": 0}

        maps = {"map_visual": [["*", "*", "*", "*", "*"],
                               ["*", "*", "*", "*", "*"],
                               ["*", "*", "*", "*", "*"],
                               ["*", "*", "*", "*", "*"],
                               ["*", "*", "*", "*", "*"]],
                "map_locations": [["3", "3", "3", "y", "4"],
                                  ["c", "c", "3", "y", "y"],
                                  ["2", "2", "c", "3", "3"],
                                  ["p", "2", "2", "c", "3"],
                                  ["1", "p", "2", "c", "3"]]}

        start(maps, player_character)

        output = get_output.getvalue()
        expected_output = "\n\nlose\n"

        self.assertIn(expected_output, output)

