import unittest

from src.assignment18.util import validating_emails
class MyTestCase(unittest.TestCase):
    def test_something1(self):
        emails = ["anthonyanand.a@diggibyte.com", "kashif.a@diggibyte.com", "selvam@diggibyte@m.com"]
        excepted_output = validating_emails(emails)
        actual_output = ['anthonyanand.a@diggibyte.com', 'kashif.a@diggibyte.com']
        self.assertEqual(excepted_output, actual_output)  # second testcase

    def test_something2(self):
        emails =["david.m@diggibyte.com","dhinakaran.a@diggibyte.com","kesavan.a@gmail.com","selvam@diggibyte@m.com"]
        excepted_output = validating_emails(emails)
        actual_output = ['david.m@diggibyte.com', 'dhinakaran.a@diggibyte.com', 'kesavan.a@gmail.com']
        self.assertEqual(excepted_output,actual_output)  # second testcase


if __name__ == '__main__':
    unittest.main()
