from unittest import TestCase
from unittest.mock import patch
import io
from game import var


class Test(TestCase):

    @patch('builtins.input', side_effect="braden")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_var(self, get_output, mock_input):
        var()
        output = get_output.getvalue()
        expected_output = "player name \n\nHello braden, Welcome to Baldur's Bones\n Game Over"
        self.assertEqual(output, expected_output)
