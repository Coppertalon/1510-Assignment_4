import io
from unittest import TestCase
from unittest.mock import patch
from game import win


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_win_print(self, get_output):
        win()
        output = get_output.getvalue()
        self.assertEqual(output, "win text\n")

    def test_win_return(self):
        output = win()
        self.assertEqual(output, False)
