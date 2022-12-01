from unittest import TestCase
from unittest.mock import patch

import gameplay
from gameplay import game_set_up
from game import start
import io


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch(gameplay.game_set_up(player_character={"name": "test",
                        "player_position": [4, 0],
                        "health": 3,
                        "level": 1,
                        "exp": 0,
                        "add": 0,
                        "take_away": 0,
                        "re_roll": 0}))
    def test_start_win(self, mock_function, get_output):

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

        mock_function.return_value = (17, player_character)

        start(maps, player_character)
        output = get_output.getvalue()
        expected_output = "\n\nwin\n"
        self.assertIn(expected_output, output)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch(gameplay.game_set_up(player_character={"name": "test",
                                                  "player_position": [4, 0],
                                                  "health": 3,
                                                  "level": 1,
                                                  "exp": 0,
                                                  "add": 0,
                                                  "take_away": 0,
                                                  "re_roll": 0}))
    def test_start_win(self, mock_function, get_output):
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

        mock_function.return_value = (13, player_character)

        start(maps, player_character)
        output = get_output.getvalue()
        expected_output = "\n\nlose\n"
        self.assertIn(expected_output, output)
