import unittest

from src.assignment14.util import calculating_happiness
class MyTestCase(unittest.TestCase):
    def test_something(self):
        array = [1, 5, 3]
        set_a = {3, 1}
        set_b = {5, 7}
        expected_output = calculating_happiness(array, set_a, set_b)
        actual_output = 1
        self.assertEqual(expected_output,actual_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()

