import unittest

from src.assignment12.util import calculating_determinant
class MyTestCase(unittest.TestCase):
    def test_something1(self):
        n = 2
        matrix_elements = [[1.1, 1.1], [1.1, 1.1]]
        excepted_input = calculating_determinant(n,matrix_elements)
        actual_output = 0.0
        self.assertEqual(excepted_input,actual_output)  # first testcase

    def test_something2(self):
        n = 3
        matrix_elements = [[2.0, 1.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
        expected_output = calculating_determinant(n, matrix_elements)
        actual_output = -9.0
        self.assertEqual(expected_output, actual_output)  # second testcase


if __name__ == '__main__':
    unittest.main()
