import unittest
from test1 import distance

class TestDistance(unittest.TestCase):
    def test_zero(self):
        res = (distance(0,0,0,0))
        self.assertEqual(res,0)