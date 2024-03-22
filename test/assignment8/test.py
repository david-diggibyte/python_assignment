import unittest

from src.assignment8.util import find_avg
class MyTestCase(unittest.TestCase):
    def test_something(self):
        n = 4
        columns = ['NAME', 'ID', 'CLASS', 'MARKS']
        data =[
            ['david', 1, 12, 95],
            ['mani', 2, 10, 82],
            ['selvam', 3, 11, 90],
            ['siva', 4, 9, 88]
        ]
        expected_output = find_avg(n, columns, data)
        actual_output = 88.75
        self.assertEqual(expected_output, actual_output)  # testcase


if __name__ == '__main__':
    unittest.main()

