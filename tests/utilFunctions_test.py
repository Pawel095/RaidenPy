import unittest
from utils.utilFunctions import isRemoveable

class tests(unittest.TestCase):
    def test_isRemoveable(self):
        falsePoints = ((-100, -100), (700, 700), (-100, 700), (700, -100))
        truePoints = ((0, 0),(500, 500),(-99, -99),(699, 699))
        for p in falsePoints:
            self.assertFalse(isRemoveable(p))
        for p in truePoints:
            self.assertTrue(isRemoveable(p))