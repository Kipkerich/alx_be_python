import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        
        
        self.calc = SimpleCalculator()

    def test_subtraction(self):
        """Test the addition method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(1, -2), 3)
        
    
        self.calc = SimpleCalculator()

    def test_multiplication(self):
        """Test the addition method."""
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(1, -2), -2)
        
    
        self.calc = SimpleCalculator()

    def test_division(self):
        """Test the addition method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-8, 1), -8)
        self.assertEqual(self.calc.divide(1, -2), -2)