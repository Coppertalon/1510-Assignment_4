from unittest import TestCase
from unittest.mock import patch
from gameplay import battle_starter
from gameplay import game_set_up
import io

class Test(TestCase):

    # this function calls a function inside another module and is too difficult to test
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch(game_set_up, return_value=(17, {"name": "test",
                                                  "player_position": [4, 0],
                                                  "health": 3,
                                                  "level": 1,
                                                  "exp": 0,
                                                  "add": 0,
                                                  "take_away": 0,
                                                  "re_roll": 0}))
    def test_battle_starter(self, get_output):
        battle_starter({}, {}, 10)
        output = get_output.getvalue()
        self.assertEqual(output, "win")
