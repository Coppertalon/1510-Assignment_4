from unittest import TestCase


class Test(TestCase):

    #the play loop calls all other helper modules and is too hard to test
    def test_play(self):
        self.fail()
