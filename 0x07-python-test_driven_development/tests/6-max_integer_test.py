#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_regular_list(self):
        """Test with regular list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with a list of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_duplicate_numbers(self):
        """Test with a list of duplicate numbers"""
        self.assertEqual(max_integer([4, 4, 4]), 4)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_mixed_list(self):
        """Test with a list containing both positive and negative numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4, -1, -2, -3, -4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4, 1, 2, 3, 4]), 4)

    def test_single_element_list(self):
        """Test with a list containing only one element"""
        self.assertEqual(max_integer([5]), 5)


if __name__ == '__main__':
    unittest.main()
