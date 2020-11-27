from unittest import TestCase
from warikan.warikan import Warikan


class TestWarikan(TestCase):

    def test_calc(self):
        self.assertEqual(Warikan().calc(0, 0), (0, 0))


