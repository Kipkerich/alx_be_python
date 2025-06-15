import unittest 
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def test_simple_calculator(self):
        self.add(1,2, 3)