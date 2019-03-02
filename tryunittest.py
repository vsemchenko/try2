import unittest
from test1 import distance

class TestDistance(unittest.TestCase):
    def test_zero(self):
        res = (distance(2,2,2,2))
        self.assertEqual(res,0)