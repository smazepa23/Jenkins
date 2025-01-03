import unittest
from xmlrunner import XMLTestRunner
from app import generate_message

class TestApp(unittest.TestCase):
    def test_generate_message(self):
        expected_message = "Witaj, świecie!"
        self.assertEqual(generate_message(), expected_message)

if __name__ == "__main__":
    with open('test-reports/results.xml', 'w') as output:
        unittest.main(testRunner=XMLTestRunner(output=output))

