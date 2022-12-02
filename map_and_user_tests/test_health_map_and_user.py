from unittest import TestCase
from map_and_user import health


class Test(TestCase):

    def test_health_regular_loss(self):
        player_health = {"health": 3}
        health(-1, player_health)
        self.assertEqual(player_health["health"], 2)

    def test_health_boss_loss(self):
        player_health = {"health": 3}
        health(-2, player_health)
        self.assertEqual(player_health["health"], 1)

    def test_health_other(self):
        player_health = {"health": 3}
        health(0, player_health)
        self.assertEqual(player_health["health"], 3)
