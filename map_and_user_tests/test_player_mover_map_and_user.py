from unittest import TestCase
from unittest.mock import patch
import io
from map_and_user import player_mover


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_mover_invalid(self, get_output):
        player_mover({"player_position": [0, 1]}, "1")
        output = get_output.getvalue()
        expected_output = '" 1 "  is an invalid movement. Please try again'
        self.assertIn(expected_output, output)

    def test_player_mover_north(self):
        player_pos = {"player_position": [1, 1]}
        player_mover(player_pos, "1")
        expected_output = {"player_position": [0, 1]}
        self.assertEqual(player_pos["player_position"], expected_output["player_position"])

    def test_player_mover_south(self):
        player_pos = {"player_position": [1, 1]}
        player_mover(player_pos, "2")
        expected_output = {"player_position": [2, 1]}
        self.assertEqual(player_pos["player_position"], expected_output["player_position"])

    def test_player_mover_west(self):
        player_pos = {"player_position": [1, 1]}
        player_mover(player_pos, "3")
        expected_output = {"player_position": [1, 0]}
        self.assertEqual(player_pos["player_position"], expected_output["player_position"])

    def test_player_mover_east(self):
        player_pos = {"player_position": [1, 1]}
        player_mover(player_pos, "4")
        expected_output = {"player_position": [1, 2]}
        self.assertEqual(player_pos["player_position"], expected_output["player_position"])
