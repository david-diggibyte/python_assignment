import unittest

from src.assignment17.util import calculate_probability
class MyTestCase(unittest.TestCase):
    def test_something1(self):
        excepted_output = calculate_probability(4,"a a c d",2)
        actual_output = 0.524
        self.assertEqual(excepted_output,actual_output)  # first testcase
    def test_something2(self):
        excepted_output = calculate_probability(6,"aa bb cc aa dd ff",2)
        actual_output = 0.426
        self.assertEqual(excepted_output,actual_output)  # second testcase



if __name__ == '__main__':
    unittest.main()
