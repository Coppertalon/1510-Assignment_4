from unittest import TestCase
from unittest.mock import patch
from map_and_user import level_up
import io


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_2(self, get_output):
        player = {"level": 2, "health": 3, "add": 0, "take_away": 0, "re_roll": 1}
        level_up(player)
        output = get_output.getvalue()
        self.assertEqual(player["health"], 4)
        self.assertEqual(player["add"], 1)
        self.assertEqual(player["take_away"], 1)
        self.assertEqual(player["re_roll"], 2)
        self.assertEqual(output, "level up 2 message\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_3(self, get_output):
        player = {"level": 3, "health": 4, "add": 1, "take_away": 1, "re_roll": 2}
        level_up(player)
        output = get_output.getvalue()
        self.assertEqual(player["health"], 5)
        self.assertEqual(player["add"], 2)
        self.assertEqual(player["take_away"], 2)
        self.assertEqual(player["re_roll"], 3)
        self.assertEqual(output, "level up 3 message\n")
