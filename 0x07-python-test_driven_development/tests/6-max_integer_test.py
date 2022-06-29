#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for mat_integer"""
    def test_module_docstring(self):
        """Tests for module docsting"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """Tests for funstion docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_list_is_itterable(self):
        """Tests that param is a iterable"""
        # with self.assertRaises(TypeError):
        #     max_integer(4)
        self.assertRaises(TypeError, max_integer, 4)

    def test_list_size(self):
        """Tests for no parameter"""
        self.assertEqual(max_integer(), None)

    def test_list_output(self):
        """right output is gotten"""
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

    def test_non_int_arg(self):
        """Tests for a non-int type in list"""
        string = [1, 2, "Hello", 4, 5]
        self.assertRaises(TypeError, max_integer, string)

    def test_empty_list(self):
        """Tests for empty list []"""
        e = []
        self.assertIsNone(max_integer(e))


if __name__ == "__main__":
    unittest.main()
