from unittest import TestCase
from unittest.mock import patch
from location_callers import location_yawning_portal


class Test(TestCase):

    #  this program relies on calling randomized functions and is too difficult to test
    @patch('random.randint', return_value=1)
    def test_location_yawning_remove_location(self, location_setter):
        locations = {"difficult": [1, 2, 3]}
        maps = {"locations": locations}
        location_yawning_portal(maps, {})
        self.assertEqual(maps["locations"]["difficult"], [1, 3])
