import io
from unittest import TestCase
from unittest.mock import patch
from game import lose


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_lose_print(self, get_output):
        lose()
        output = get_output.getvalue()
        self.assertEqual(output, "lose text\n")

    def test_lose_return(self):
        output = lose()
        self.assertEqual(output, False)
