from unittest import TestCase
from unittest.mock import patch
from map_and_user import health
import io

class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_health_regular_loss(self, get_output):
        player_health = {"health": 3}
        health(-1, player_health)
        output = get_output.getvalue()
        expected_output = "After your unfortunate loss you have lost some credibility.\n" \
                          "If your credibility reaches 0 you will lose respect permanently" \
                          " and will have to leave Waterdeep."
        self.assertEqual(player_health["health"], 2)
        self.assertIn(expected_output, output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_health_boss_loss(self, get_output):
        player_health = {"health": 3}
        health(-2, player_health)
        output = get_output.getvalue()
        expected_output = "After your unfortunate loss to the esteemed Volo you have lost some credibility." \
                          " Unfortunately as a well respected figure you lost more credibility then usual.\n" \
                          "If your credibility reaches 0 you will lose respect permanently" \
                          " and will have to leave Waterdeep."
        self.assertEqual(player_health["health"], 1)
        self.assertIn(expected_output, output)

    def test_health_other(self):
        player_health = {"health": 3}
        health(0, player_health)
        self.assertEqual(player_health["health"], 3)
