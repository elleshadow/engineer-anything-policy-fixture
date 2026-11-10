import unittest

from calc import value


class CalculatorTest(unittest.TestCase):
    def test_value(self):
        self.assertEqual(value(), 1)
