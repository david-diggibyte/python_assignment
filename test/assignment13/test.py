import unittest

from src.assignment13.util import calculate_statistics
class MyTestCase(unittest.TestCase):
    def test_something1(self):
        array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        excepted_output = calculate_statistics(array)
        actual_output = "[2. 5. 8.]\n[6. 6. 6.]\n2.58198889747"
        self.assertEqual(excepted_output,actual_output)  # first testcase


if __name__ == '__main__':
    unittest.main()

