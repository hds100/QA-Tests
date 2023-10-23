# Importing python unit tests framework

import unittest

# Simple addition function with two numbers that will be tested

def add_numbers(a, b):
    return a + b

#  implementing the test class and testing the function in different cases

class TestAddNumbers(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add_numbers(2, 7)
        self.assertEqual(result, 9)  # Checks if 2 + 7 is equal to 9

    def test_add_negative_numbers(self):
        result = add_numbers(-12, -15)
        self.assertEqual(result, -27)  # Checks if -12 + (-15) equals -27

    def test_add_mixed_numbers(self):
        result = add_numbers(14, -9)
        self.assertEqual(result, 5)  # Checks if 14 + (-9) equals 5

if __name__ == '__main__':
    unittest.main()

"""
Result: Ran 3 tests in 0.000s

OK

"""
