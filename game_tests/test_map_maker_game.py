from unittest import TestCase
from game import map_maker


class Test(TestCase):

    def test_map_maker(self):
        output = map_maker([])
        self.assertEqual(output, ["*", "*", "*", "*", "*"])
