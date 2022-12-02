from unittest import TestCase
from location_callers import mark_location


class Test(TestCase):

    def test_mark_location(self):
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
        expected_output = [["*", "*", "*", "*", "*"],
                           ["*", "*", "*", "*", "*"],
                           ["*", "*", "*", "*", "*"],
                           ["*", "*", "*", "*", "*"],
                           ["test 2", "*", "*", "*", "*"]]
        mark_location(maps, player_character, "test 1", "test 2")
        self.assertEqual(maps["map_visual"], expected_output)

    def test_mark_location(self):
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
        expected_output = [["3", "3", "3", "y", "4"],
                           ["c", "c", "3", "y", "y"],
                           ["2", "2", "c", "3", "3"],
                           ["p", "2", "2", "c", "3"],
                           ["test 1", "p", "2", "c", "3"]]
        mark_location(maps, player_character, "test 1", "test 2")
        self.assertEqual(maps["map_locations"], expected_output)
