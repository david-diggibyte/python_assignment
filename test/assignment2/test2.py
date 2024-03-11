import unittest

from src.assignment2.util import second_large
class MyTestCase(unittest.TestCase):
    def test_something(self):
        res = second_large()
        self.assertEqual(res, 300)


if __name__ == '__main__':
    unittest.main()
