import unittest
from app import generate_message

class TestApp(unittest.TestCase):
    def test_generate_message(self):
        expected_message = "Witaj, świecie!"
        self.assertEqual(generate_message(), expected_message)

if __name__ == "__main__":
    unittest.main()
