import unittest

from src.assignment15.util import count_word
class MyTestCase(unittest.TestCase):
    def test_something1(self):
        n = 4
        word_list = ["david", "akilan", "david", "sasi"]
        expected_output = count_word(n,word_list)
        actual_output = "3\n2 1 1"
        self.assertEqual(expected_output,actual_output)  # first testcase
    def test_something2(self):
        n = 3
        word_list = ["selvam", "david", "selvam"]
        expected_output = count_word(n,word_list)
        actual_output = "2\n2 1"
        self.assertEqual(expected_output,actual_output)   # second testcase


if __name__ == '__main__':
    unittest.main()
