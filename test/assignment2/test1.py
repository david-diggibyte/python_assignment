import unittest

from src.assignment2.util import second_large
class MyTestCase(unittest.TestCase):
    def test_something1(self):
        res = second_large()
        self.assertEqual(res, 55)  # 1st testcase
    def test_something2(self):
        res = second_large()
        self.assertEqual(res, 33)  # 2nd testcase
    def test_something3(self):
        res = second_large()
        self.assertEqual(res,6)    # 3rd testcase

if __name__ == '__main__':
    unittest.main()
