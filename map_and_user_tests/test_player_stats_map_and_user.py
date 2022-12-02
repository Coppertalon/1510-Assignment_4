from unittest import TestCase
from unittest.mock import patch
from map_and_user import player_stats
import io


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_stats(self, get_output):
        player = {"level": 1, "exp": 0, "health": 3, "add": 0, "take_away": 0, "re_roll": 1}
        player_stats(player)
        output = get_output.getvalue()
        expected_outputs = ["Renown: 1", "Reputation: 0", "Credibility: 3\n", "Re-rolls: 1\n"]
        self.assertIn(expected_outputs[0], output)
        self.assertIn(expected_outputs[1], output)
        self.assertIn(expected_outputs[2], output)
        self.assertIn(expected_outputs[3], output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_stats(self, get_output):
        player = {"level": 2, "exp": 0, "health": 3, "add": 1, "take_away": 1, "re_roll": 1}
        player_stats(player)
        output = get_output.getvalue()
        expected_outputs = ["Add 1 to roll: 1", "Remove 1 from roll: 1", "Level 2 Skills:"]
        self.assertIn(expected_outputs[0], output)
        self.assertIn(expected_outputs[1], output)
        self.assertIn(expected_outputs[2], output)
