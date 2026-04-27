import unittest
from app import add, subtract, multiply, divide

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 5), 10)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

if __name__ == "__main__":
    unittest.main()