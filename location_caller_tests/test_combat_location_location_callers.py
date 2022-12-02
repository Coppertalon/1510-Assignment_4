from unittest import TestCase
from unittest.mock import patch
from location_callers import combat_location
import io


class Test(TestCase):
    # input 1 cannot be tested as it leads to a function outside the module
    @patch('builtins.input', side_effect=['2'])
    def test_combat_location_move(self, mock_input):
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
        output = combat_location(maps, player_character, "test", 2)
        self.assertEqual(output, (0, True))

    @patch('builtins.input', side_effect=['3'])
    def test_combat_location_quit(self, mock_input):
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
        output = combat_location(maps, player_character, "test", 2)
        self.assertEqual(output, (0, False))

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['4', '3'])
    def test_combat_location_invalid(self, mock_input, get_output):
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
        output = combat_location(maps, player_character, "test", 2)
        output_text = get_output.getvalue()
        self.assertEqual(output, (0, False))
        self.assertIn("That is not a valid choice.\n", output_text)
