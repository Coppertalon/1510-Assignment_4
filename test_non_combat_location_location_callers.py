from unittest import TestCase
from unittest.mock import patch
from location_callers import non_combat_location
import io


class Test(TestCase):
    # input 1 cannot be tested as it leads to a function outside the module
    @patch('builtins.input', side_effect=['1'])
    def test_combat_location_move(self, mock_input):
        output = non_combat_location()
        self.assertEqual(output, True)

    @patch('builtins.input', side_effect=['2'])
    def test_combat_location_quit(self, mock_input):
        output = non_combat_location()
        self.assertEqual(output, False)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['3', '1'])
    def test_combat_location_invalid(self, mock_input, get_output):
        output = non_combat_location()
        output_text = get_output.getvalue()
        self.assertEqual(output, True)
        self.assertIn("Invalid choice.\n", output_text)
