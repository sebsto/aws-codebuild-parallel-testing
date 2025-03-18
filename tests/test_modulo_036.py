import unittest
import sys
import os

# Add parent directory to path to import calculator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from calculator import Calculator

class TestModulo36(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_modulo_36(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

if __name__ == '__main__':
    unittest.main()
