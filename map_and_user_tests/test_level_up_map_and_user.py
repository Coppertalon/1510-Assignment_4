from unittest import TestCase
from unittest.mock import patch
from map_and_user import level_up
import io


class Test(TestCase):
    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_2(self, get_output, mock_input):
        player = {"level": 2, "health": 3, "add": 0, "take_away": 0, "re_roll": 1}
        level_up(player)
        output = get_output.getvalue()
        expected_output = "Congratulations, you are now renown 2, by beating 3 players you increased your renown." \
                          " You have gained an addition point of credibility," \
                          " which means you can lose another battle and still" \
                          " have the respect of others. In addition you regain a re-roll and" \
                          " the talisman now lets you add 1 to your total" \
                          " and remove 1 from your total once (per ability)." \
                          " As you now have a higher reputation, battles in the bars" \
                          " near the docks are now below you and are unavailable."
        self.assertEqual(player["health"], 4)
        self.assertEqual(player["add"], 1)
        self.assertEqual(player["take_away"], 1)
        self.assertEqual(player["re_roll"], 2)
        self.assertIn(expected_output, output)

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_3(self, get_output, mock_input):
        player = {"level": 3, "health": 4, "add": 1, "take_away": 1, "re_roll": 2}
        level_up(player)
        output = get_output.getvalue()
        expected_output = "Congratulations, you are now renown 2, by beating 3 players you increased your renown. " \
                          " You gain another point of credibility as well as" \
                          " another re-roll, add to roll, and take away from roll." \
                          " You now have enough credibility to go against Volo in the yawning portal" \
                          " (Hint: go to the north east)" \
                          " You can also to continue to practice but will gain nothing from it and risk credibility."
        self.assertEqual(player["health"], 5)
        self.assertEqual(player["add"], 2)
        self.assertEqual(player["take_away"], 2)
        self.assertEqual(player["re_roll"], 3)
        self.assertIn(expected_output, output)
