#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_list_is_itterable(self):
        # with self.assertRaises(TypeError):
        #     max_integer(4)
        self.assertRaises(TypeError, max_integer, 4)

    def test_list_size(self):
        self.assertEqual(max_integer(), None)

    def test_list_output(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_one_element(self):
        """Tests for only one number in the list"""
        self.assertEqual(max_integer([1]), 1)

    def test_all_negative(self):
        """Tests for list with all negative numbers"""
        n = [-6, -50, -75, -1, -100]
        self.assertEqual(max_integer(n), -1)

    def test_none(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == "__main__":
    unittest.main()