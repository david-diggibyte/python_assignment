import unittest

from src.assignment9.util import time_delta
class MyTestCase(unittest.TestCase):
    def test_something(self):
        t1 = "Tue 12 Mar 2024 08:00:00 +0530"
        t2 = "Tue 12 Mar 2024 14:30:00 +0100"
        expected_output = time_delta(t1,t2)
        actual_output = 39600
        self.assertEqual(expected_output,actual_output)  # testcase


if __name__ == '__main__':
    unittest.main()
