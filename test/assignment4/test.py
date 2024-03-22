import unittest

from src.assignment4.util import merge_the_tools
class MyTestCase(unittest.TestCase):
    def test_something1(self):
        expected_output = merge_the_tools("davidselvam",3)
        actual_output = "dav\nids\nelv"
        self.assertEqual(expected_output, actual_output)  # 1st testcase

    def test_something2(self):
        expected_output = merge_the_tools("arokiyamaey",4)
        actual_output = "arok\niyam"
        self.assertEqual(expected_output, actual_output)  # 2nd testcase




if __name__ == '__main__':
    unittest.main()
