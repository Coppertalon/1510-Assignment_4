from unittest import TestCase
from unittest.mock import patch
from location_callers import dont_use_location
import io


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[''])
    def test_dont_use_location_easy(self, mock_input, get_output):
        dont_use_location("easy")
        output = get_output.getvalue()
        expected_output = "too easy"
        self.assertIn(expected_output, output)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[''])
    def test_dont_use_location_hard(self, mock_input, get_output):
        dont_use_location("hard")
        output = get_output.getvalue()
        expected_output = "too hard"
        self.assertIn(expected_output, output)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[''])
    def test_dont_use_location_beaten(self, mock_input, get_output):
        dont_use_location("beat")
        output = get_output.getvalue()
        expected_output = "beaten"
        self.assertIn(expected_output, output)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[''])
    def test_dont_use_location_explored(self, mock_input, get_output):
        dont_use_location("explored")
        output = get_output.getvalue()
        expected_output = "explored"
        self.assertIn(expected_output, output)
