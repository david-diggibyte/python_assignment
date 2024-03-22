import unittest

from src.assignment7.util import find_day_of_week
class MyTestCase(unittest.TestCase):
    def test_something1(self):
        expected_output = "TUESDAY"
        actual_output = find_day_of_week(3, 12, 2024)
        self.assertEqual(expected_output,actual_output)  # first testcase

    def test_something2(self):
        expected_output = "MONDAY"
        actual_output = find_day_of_week(11, 6, 2000)
        self.assertEqual(expected_output,actual_output)  # second testcase


if __name__ == '__main__':
    unittest.main()

