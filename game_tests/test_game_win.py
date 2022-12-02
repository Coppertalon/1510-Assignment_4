import io
from unittest import TestCase
from unittest.mock import patch
from game import win


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_win_print(self, get_output):
        win({"name": "test"})
        output = get_output.getvalue()
        expected_output = "Having defeated the famous adventurer Volo, test has proven themselves as a capable leader" \
                          " and earned the reputation necessary to captain a vessel." \
                          " Able to achieve their dream of sailing the oceans wide, you walk back into the city," \
                          " grinning as your mind fills with tales of the sea\nYou Win\n"
        self.assertIn(expected_output, output)

    def test_win_return(self):
        output = win({"name": "test"})
        self.assertEqual(output, False)
