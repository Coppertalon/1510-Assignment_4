from unittest import TestCase
from unittest.mock import patch
import io
from map_and_user import move_decider


class Test(TestCase):

    @patch('builtins.input', side_effect=['5'])
    def test_move_decider_quit(self, mock_input):
        output = move_decider({})
        self.assertEqual(output, False)

    @patch('builtins.input', side_effect=['6', '5'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_decider_invalid(self, get_output, mock_input):
        move_decider({})
        output = get_output.getvalue()
        expected_output = '" 6 " is an invalid movement. Please try again.\n'
        self.assertIn(expected_output, output)
