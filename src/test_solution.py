from unittest import TestCase
import is_happy

__author__ = 'mgska'


class TestSolution(TestCase):
    def test_isHappy(self):
        s = is_happy.Solution()
        self.assertEqual(s.isHappy(7), True)
