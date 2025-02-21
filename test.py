import unittest
from main import *
from unittest.mock import patch
from io import StringIO


class TestMainFunction(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='51')
    def test_valid_integer_input(self, mock_input, mock_stdout):
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Your grade is B")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='100')
    def test_valid_integer_input(self, mock_input, mock_stdout):
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Your grade is A")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='abc')
    def test_invalid_input(self, mock_input, mock_stdout):
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Invalid input. Please enter a valid integer.")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='120')
    def test_out_of_range_input(self, mock_input, mock_stdout):
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Your grade is Invalid mark")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='-5')
    def test_out_of_range_input(self, mock_input, mock_stdout):
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Your grade is Invalid mark")


if __name__ == '__main__':
    unittest.main()
