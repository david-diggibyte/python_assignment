import unittest

from src.assignment1.util import percentage
class MyTestCase(unittest.TestCase):
    def test_something1(self):   # 1st testcase
        expected_output = percentage({"david": [88,75,95],"susai": [66,77,88],"mani": [100,100,100]},"susai")
        actual_output = 77.0
        self.assertEqual(expected_output,format(actual_output,".2f"))

    def test_something2(self):   # 2nd testcase
        expected_output = percentage({"david": [88,75,95],"susai": [66,77,88],"mani": [100,100,100]},"david")
        actual_output = 86.00
        self.assertEqual(expected_output,format(actual_output,".2f"))

# if __name__ == '__main__':
#     unittest.main()