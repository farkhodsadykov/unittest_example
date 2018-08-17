import calc
import unittest

class TestClass(unittest.TestCase):
    def test_add(self):
        """Checking Add Function"""
        result = calc.add(10, 5)
        self.assertEqual(result, 15)
        self.assertEqual(calc.add(56, 5), 61)

    def test_subtract(self):
        """Checking Subtract Function"""
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(10, -5), 15)
        self.assertEqual(calc.subtract(-1, -5), 4)

    def test_multiply(self):
        """Checking Multiply Function"""
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(10, -5), -50)
        self.assertEqual(calc.multiply(-1, -5), 5)

    def test_divide(self):
        """Checking Multiply Function"""
        self.assertEqual(calc.divide(10, 5), 2.0)
        self.assertEqual(calc.divide(10, -5), -2.0)
        self.assertEqual(calc.divide(-1, -5), 0.2)

if __name__ == "__main__":
    unittest.main()
