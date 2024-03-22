import unittest

from src.assignment5.util import string_formatted
class MyTestCase(unittest.TestCase):
    def test_something(self):
        expected_output = string_formatted(4).strip()
        actual_output = " 1   1   1   1\n  2   2   2  10\n  3   3   3  11\n  4   4   4 100".strip()
        self.assertEqual(expected_output, actual_output)  # add assertion here


if __name__ == '__main__':
     unittest.main()

