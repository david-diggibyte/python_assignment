import unittest

from src.assignment10.util import array_operations
class MyTestCase(unittest.TestCase):
    def test_something1(self):
        array = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
        expected_output = array_operations(array)
        actual_output = "[1. 2. 3. 4. 5. 6. 7. 8. 9.]\n[ 2.  3.  4.  5.  6.  7.  8.  9. 10.]\n[ 1.  2.  3.  4.  6.  7.  8.  9. 10.]"
        self.assertEqual(expected_output, actual_output)  # first testcase

    def test_something2(self):
        array = [2.5, 3.8, 6.2, 4.1, 7.9, 9.3, 5.4, 8.6, 1.7]
        expected_output = array_operations(array)
        actual_output = "[2. 3. 6. 4. 7. 9. 5. 8. 1.]\n[ 3.  4.  7.  5.  8. 10.  6.  9.  2.]\n[2. 4. 6. 4. 8. 9. 5. 9. 2.]"
        self.assertEqual(expected_output, actual_output)   # second testcase

if __name__ == '__main__':
    unittest.main()
