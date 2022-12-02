from unittest import TestCase
from unittest.mock import patch
from location_callers import location_easy


class Test(TestCase):

    # this would work as a test but the program calls functions in another module
    @patch('random.randint', return_value=1)
    def test_location_easy_remove_location(self, location_setter):
        locations = {"difficult": [1, 2, 3, 4, 5, 6, 7, 8]}
        maps = {"locations": locations}
        location_easy(maps, {})
        self.assertEqual(maps["locations"]["difficult"], [1, 3, 4, 5])
