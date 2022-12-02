import io
from unittest import TestCase
from unittest.mock import patch
from game import final_dialogue


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_dialogue_hard_loss(self, get_output):
        return_int = final_dialogue(-2)
        output = get_output.getvalue()
        expected_output = "'Ahh an excellent set of games my good fellow, a shame about you luck," \
                          " it does happen to the best of us." \
                          " Still I thank you for the chance to engage in lighthearted merriment " \
                          "and wish all the best in your future endeavors. " \
                          "Now if you will excuse me, I do believe I hear a drink calling my name.'"
        self.assertIn(expected_output, output)
        self.assertEqual(return_int, -2)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_dialogue_close_loss(self, get_output):
        return_int = final_dialogue(-1)
        output = get_output.getvalue()
        expected_output = "'Good show, ahh a good show indeed, you almost had me for a second there," \
                          " but no creature can best Volo! Ah, I jest of course," \
                          " such vanities lead only to an early grave in my profession." \
                          " Thank thee anyhow for a chance at such joyous games. I wish you well," \
                          " for I hear a fan to whom i must attend my attentions.'"
        self.assertIn(expected_output, output)
        self.assertEqual(return_int, -2)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_dialogue_close_win(self, get_output):
        return_int = final_dialogue(1)
        output = get_output.getvalue()
        expected_output = "'Oh, Oh my, it would seem that my good fortunes for the day are dwindling. " \
                          "Well then I am a man of honor and will admit when I am beat." \
                          " There are not many who can best the great Volo in a game of fortunes" \
                          " so you should hold yourself in high esteem for that. I pronounce you the winner and wish " \
                          "you the best in your future endeavors." \
                          " For now I must go, my next literary masterpiece awaits.'"
        self.assertIn(expected_output, output)
        self.assertEqual(return_int, 2)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_dialogue_solid_win(self, get_output):
        return_int = final_dialogue(2)
        output = get_output.getvalue()
        expected_output = "'Good show, oh good show indeed! It has been far too long since " \
                          "someone has been able to show such a " \
                          " performance against my talents, wit, and impeccable luck." \
                          " Well far be it for me to deny such as skillful player their rightful reward. " \
                          "I pronounce you the winner and that you have bested the mighty Volo!" \
                          " Forgive me for now I must away as there are might beasts" \
                          " and blood pumping adventures that await me" \
                          " beyond these walls. Good dayyyyy!'"
        self.assertIn(expected_output, output)
        self.assertEqual(return_int, 2)
