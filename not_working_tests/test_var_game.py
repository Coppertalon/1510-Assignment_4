from unittest import TestCase
from unittest.mock import patch
import io
from game import var
from game import play


class Test(TestCase):

    @patch('builtins.input', side_effect=['braden'])
    @patch(play({}, {}, True), return_value=(17, {"name": "test",
                                                           "player_position": [4, 0],
                                                           "health": 3,
                                                           "level": 1,
                                                           "exp": 0,
                                                           "add": 0,
                                                           "take_away": 0,
                                                           "re_roll": 0}))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_var(self, get_output, mock_input):
        var()
        output = get_output.getvalue()
        expected_output = "player name \n\nHello braden, Welcome to Baldur's Bones\n Game Over"
        self.assertEqual(output, expected_output)
