import io
from unittest import TestCase
from unittest.mock import patch
from game import lose


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_lose_print(self, get_output):
        player = {"name": "test"}
        lose(player)
        output = get_output.getvalue()
        expected_output = "Having faced several losses to the fickle hands of fate test has lost too much credibility" \
                          " in the town of Waterdeep. Your dreams of sailing the seas as a captain are not dissuaded " \
                          "and you being you venture to a further port in hopes that the chance to prove yourself " \
                          "is just around the corner.\nYou Lose\n"
        self.assertIn(expected_output, output)

    def test_lose_return(self):
        output = lose({"name": "test"})
        self.assertEqual(output, False)
