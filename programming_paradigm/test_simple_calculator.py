import simple_calculator
import unittest 


class TestSimpleCalculator(unittest.TestCase):
    
    def test_simple_calculator(self):
        self.assertEqual(simple_calculator.add(1, 3), 4)
        self.assertEqual(simple_calculator.add(-1, 3), 2)
        self.assertEqual(simple_calculator.add(1, -3), 2)
        self.assertEqual(simple_calculator.add(-1, -3), -4)
        
        self.assertEqual(simple_calculator.subtract(1, 3), -2)
        self.assertEqual(simple_calculator.subtract(-1, 3), -4)
        self.assertEqual(simple_calculator.subtract(1, -3), 4)
        self.assertEqual(simple_calculator.subtract(-1, -3), -2)