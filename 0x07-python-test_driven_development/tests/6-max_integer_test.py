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
