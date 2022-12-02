from unittest import TestCase
import location_callers
from unittest.mock import patch
from location_descriptions import location_yawning_2
import io

class Test(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_location_location_yawning_2_not_done_move(self, mock_input):
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

        output = location_yawning_2(maps, player_character, False)
        self.assertEqual(output, (0, True))
        self.assertEqual(maps["map_visual"], [["*", "*", "*", "*", "*"],
                                              ["*", "*", "*", "*", "*"],
                                              ["*", "*", "*", "*", "*"],
                                              ["*", "*", "*", "*", "*"],
                                              ["Y", "*", "*", "*", "*"]])
        self.assertEqual(maps["map_locations"], [["3", "3", "3", "y", "4"],
                                                 ["c", "c", "3", "y", "y"],
                                                 ["2", "2", "c", "3", "3"],
                                                 ["p", "2", "2", "c", "3"],
                                                 [location_yawning_2, "p", "2", "c", "3"]])

    @patch('builtins.input', side_effect=['2'])
    def test_location_location_yawning_2_not_done_quit(self, mock_input):
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

        output = location_yawning_2(maps, player_character, False)
        self.assertEqual(output, (0, False))

    # cannot check text displayed in outside functions
    # @patch('builtins.input', side_effect=['1'])
    # @patch('sys.stdout', new_callable=io.StringIO)
    # def test_location_location_yawning_2_found(self, get_output, mock_input):
    #     maps = {"map_visual": [["*", "*", "*", "*", "*"],
    #                            ["*", "*", "*", "*", "*"],
    #                            ["*", "*", "*", "*", "*"],
    #                            ["*", "*", "*", "*", "*"],
    #                            ["*", "*", "*", "*", "*"]],
    #             "map_locations": [["3", "3", "3", "y", "4"],
    #                               ["c", "c", "3", "y", "y"],
    #                               ["2", "2", "c", "3", "3"],
    #                               ["p", "2", "2", "c", "3"],
    #                               ["1", "p", "2", "c", "3"]]}
    #     player_character = {"name": "test",
    #                         "player_position": [4, 0],
    #                         "health": 3,
    #                         "level": 2,
    #                         "exp": 0,
    #                         "add": 0,
    #                         "take_away": 0,
    #                         "re_roll": 0}
    #
    #     location_yawning_2(maps, player_character, True)
    #     output = get_output.getvalue()
    #     expected_output = "explored"
    #     self.assertIn(expected_output, output)
