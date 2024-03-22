import unittest

from src.assignment11.util import min_max
class MyTestCase(unittest.TestCase):
    def test_something(self):
        rows = 4
        cols = 2
        elements = [[2, 5], [3, 7], [1, 3], [4, 0]]
        excepted_output = min_max(rows,cols,elements)
        actual_output = 3
        self.assertEqual(excepted_output,actual_output)  # testcase


if __name__ == '__main__':
    unittest.main()

