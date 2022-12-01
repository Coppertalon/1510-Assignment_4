import io
from unittest import TestCase
from unittest.mock import patch
from game import final_dialogue


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_dialogue_hard_loss(self, get_output):
        return_int = final_dialogue(-2)
        output = get_output.getvalue()
        self.assertEqual(output, "hard loss\n")
        self.assertEqual(return_int, -2)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_dialogue_close_loss(self, get_output):
        return_int = final_dialogue(-1)
        output = get_output.getvalue()
        self.assertEqual(output, "close loss\n")
        self.assertEqual(return_int, -2)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_dialogue_close_win(self, get_output):
        return_int = final_dialogue(1)
        output = get_output.getvalue()
        self.assertEqual(output, "close win\n")
        self.assertEqual(return_int, 2)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_dialogue_solid_win(self, get_output):
        return_int = final_dialogue(2)
        output = get_output.getvalue()
        self.assertEqual(output, "solid win\n")
        self.assertEqual(return_int, 2)