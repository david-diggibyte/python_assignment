import unittest
from src.assignment16.util import stack_cubes
class MyTestCase(unittest.TestCase):
    def test_something1(self):   # first testcase
        t = 2
        test_cases = [(6, [4, 3, 2, 1, 3, 4]), (3, [1, 3, 2])]
        excepted_output = stack_cubes(t,test_cases)
        actual_output = "Yes\nNo"
        self.assertEqual(excepted_output,actual_output)
    def test_something2(self):    # second testcase
        t = 3
        test_cases = [(4, [4, 3, 6, 7]), (3, [5, 3, 1]), (5, [4, 5, 6, 3, 2])]
        excepted_output = stack_cubes(t,test_cases)
        actual_output = "Yes\nYes\nNo"
        self.assertEqual(excepted_output,actual_output)



if __name__ == '__main__':
    unittest.main()
