from unittest import TestCase
from unittest.mock import patch
from location_callers import location_city


class Test(TestCase):

    # this program relies on calling randomized functions and is too difficult to test
    @patch('random.randint', return_value=1)
    def test_location_hard_remove_location(self, location_setter):
        locations = {"difficult": [1, 2, 3, 4, 5]}
        maps = {"locations": locations}
        location_city(maps, {})
        self.assertEqual(maps["locations"]["difficult"], [1, 3, 4, 5])
