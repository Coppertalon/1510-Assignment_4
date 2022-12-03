from unittest import TestCase
from unittest.mock import patch
from location_descriptions import location_difficult_4


class Test(TestCase):
    # testing the combat section would involve entering the gameplay loop and is too hard to test
    @patch('builtins.input', side_effect=[''])
    def test_location_difficult_4(self, mock_input):
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
        output = location_difficult_4(maps, player_character, True)
        self.assertEqual(output, (0, True))
