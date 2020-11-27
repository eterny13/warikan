from unittest import TestCase
from warikan.warikan import Warikan


class TestWarikan(TestCase):

    def test_calc_normal_zero(self):
        self.assertEqual(Warikan().calc_normal(0, 0), (0, 0))

    def test_calc_normal_kanji_2yen(self):
        self.assertEqual(Warikan().calc_normal(3330, 4), (833, 2))

    def test_calc_kanji_1yen(self):
        self.assertEqual(Warikan().calc(3330, 4, 0, 0), (833, 0, 0, 1))
