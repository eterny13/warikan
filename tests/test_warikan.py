from unittest import TestCase
from warikan.warikan import Warikan


class TestWarikan(TestCase):

    def test_calc_zero(self):
        self.assertEqual(Warikan().calc(0, 0), (0, 0))

    def test_calc_kanji_2yen(self):
        self.assertEqual(Warikan().calc(3330, 4), (833, 2))

