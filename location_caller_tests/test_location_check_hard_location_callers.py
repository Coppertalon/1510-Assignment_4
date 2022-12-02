from unittest import TestCase
from unittest.mock import patch
from location_callers import location_check_hard


class Test(TestCase):

    @patch('builtins.input', side_effect=[''])
    def test_location_check_hard(self, mock_input):
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
        player_character = {"name": "test",
                            "player_position": [4, 0],
                            "health": 3,
                            "level": 2,
                            "exp": 0,
                            "add": 0,
                            "take_away": 0,
                            "re_roll": 0}
        outcome = location_check_hard(maps, player_character, False, "test")
        self.assertEqual(outcome, False)

    @patch('builtins.input', side_effect=[''])
    def test_location_check_hard_beaten(self, mock_input):
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
        player_character = {"name": "test",
                            "player_position": [4, 0],
                            "health": 3,
                            "level": 2,
                            "exp": 0,
                            "add": 0,
                            "take_away": 0,
                            "re_roll": 0}
        outcome = location_check_hard(maps, player_character, True, "test")
        self.assertEqual(outcome, True)

    @patch('builtins.input', side_effect=[''])
    def test_location_check_hard_too_low_level(self, mock_input):
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
        player_character = {"name": "test",
                            "player_position": [4, 0],
                            "health": 3,
                            "level": 1,
                            "exp": 0,
                            "add": 0,
                            "take_away": 0,
                            "re_roll": 0}
        outcome = location_check_hard(maps, player_character, False, "test")
        self.assertEqual(outcome, True)
