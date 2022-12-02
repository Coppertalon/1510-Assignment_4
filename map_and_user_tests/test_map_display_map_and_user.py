from unittest import TestCase
from unittest.mock import patch
from map_and_user import map_display
import io


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_map_display(self, get_output):
        player = {"name": "test",
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
                               ["*", "*", "*", "*", "*"]]}
        map_display(maps, player)
        output = get_output.getvalue()
        expected_outputs = ["*****\n*****\n*****\n*****\n#****",
                            "Legend:  * = Unexplored,    # = Player,    ! = Found Bar,   @ = Beaten Bar,\n",
                            "Legend:  O = Your Ship,    X = Yawning Portal,    P = Found Port,   C = Found City,\n"]
        self.assertIn(expected_outputs[0], output)
        self.assertIn(expected_outputs[1], output)
        self.assertIn(expected_outputs[2], output)
