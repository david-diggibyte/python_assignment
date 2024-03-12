import unittest

from src.assignment3.util import change_string

class MyTestCase(unittest.TestCase):
    def test_something1(self):
        expected_output = change_string("ravid",0,"d")
        self.assertEqual(expected_output,"david")  # 1st testcase

    def test_something2(self):
        expected_output = change_string("vani", 0, "m")
        self.assertEqual(expected_output, "mani")  # 2nd testcase


if __name__ == '__main__':
    unittest.main()
