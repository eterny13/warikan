from unittest import TestCase
from warikan.warikan import Warikan


class TestWarikan(TestCase):

    def test_calc_normal_zero(self):
        self.assertEqual(Warikan().calc_normal(0, 0), (0, 0))

    def test_calc_normal_kanji_2yen(self):
        self.assertEqual(Warikan().calc_normal(3330, 4), (833, 2))

    def test_calc_kanji_only_normal_2yen(self):
        self.assertEqual(Warikan().calc(3330, 4, 0, 0), (833, 0, 0, 2))

    def test_calc_kanji_only_normal_total_members_0(self):
        self.assertEqual(Warikan().calc(3330, 0, 0, 0), (0, 0, 0, 0))

    def test_calc_kanji_1yen(self):
        self.assertEqual(Warikan().calc(3330, 2, 1, 1), (833, 1249, 416, 1))
