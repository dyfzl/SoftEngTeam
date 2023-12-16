import unittest
from unittest.mock import patch
from calculator import add, mul, sub

class TestAddCalculator(unittest.TestCase):
    @patch('builtins.input', return_value='10')
    def testAddValidInput(self, mock_input):
        result = add(5)
        self.assertEqual(result, 15)

    @patch('builtins.input', return_value='abc')
    def testAddInvalidInput(self, mock_input):
        result = add(5)
        self.assertFalse(result)

    @patch('builtins.input', return_value='7532')
    def testAddEvent7532(self, mock_input):
        result = add(3)
        self.assertIsNone(result)

    @patch('builtins.input', return_value='1015')
    def testAddEvent1015(self, mock_input):
        result = add(3)
        self.assertIsNone(result)

    @patch('builtins.input', return_value='7503')
    def testAddEvent7503(self, mock_input):
        result = add(3)
        self.assertIsNone(result)

class TestSubCalculator(unittest.TestCase):
    @patch('builtins.input', return_value='3')
    def testSubValidInput(self, mock_input):
        result = sub(5)
        self.assertEqual(result, 2)

    @patch('builtins.input', return_value='abc')
    def testSubInvalidInput(self, mock_input):
        result = sub(5)
        self.assertFalse(result)

    @patch('builtins.input', return_value='7532')
    def testSubEvent7532(self, mock_input):
        result = sub(3)
        self.assertIsNone(result)

    @patch('builtins.input', return_value='1015')
    def testSubEvent1015(self, mock_input):
        result = sub(3)
        self.assertIsNone(result)

    @patch('builtins.input', return_value='7503')
    def testSubEvent7503(self, mock_input):
        result = sub(3)
        self.assertIsNone(result)




if __name__ == '__main__':

    unittest.main(exit=False)

