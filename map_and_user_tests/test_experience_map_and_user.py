from unittest import TestCase
from map_and_user import experience


class Test(TestCase):

    def test_experience_lvl_1_no_exp(self):
        player = {"level": 1, "exp": 0}
        up = experience(1, player)
        self.assertEqual(player["level"], 1)
        self.assertEqual(up, 0)
        self.assertEqual(player["exp"], 1)

    def test_experience_lvl_1_level_up(self):
        player = {"level": 1, "exp": 2}
        up = experience(1, player)
        self.assertEqual(player["level"], 2)
        self.assertEqual(up, 1)
        self.assertEqual(player["exp"], 0)

    def test_experience_lvl_2_no_exp(self):
        player = {"level": 2, "exp": 0}
        up = experience(1, player)
        self.assertEqual(player["level"], 2)
        self.assertEqual(up, 0)
        self.assertEqual(player["exp"], 1)

    def test_experience_lvl_2_level_up(self):
        player = {"level": 2, "exp": 4}
        up = experience(1, player)
        self.assertEqual(player["level"], 3)
        self.assertEqual(up, 1)
        self.assertEqual(player["exp"], 0)

    def test_experience_lvl_3_any_exp(self):
        player = {"level": 3, "exp": 1}
        up = experience(1, player)
        self.assertEqual(player["level"], 3)
        self.assertEqual(up, 0)
        self.assertEqual(player["exp"], 2)
