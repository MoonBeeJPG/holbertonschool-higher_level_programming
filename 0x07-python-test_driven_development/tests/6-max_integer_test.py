#!/usr/bin/python3
""" Write unittests fot the function def max_integer(list=[]) """

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Tests for max_integer """
    def test_normal(self):
        """ Check normal list of ints """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([[-1, -2], [1, 2]]), [1, 2])
        self.assertEqual(max_integer([[1, 2], [5, 6], [3, 4]]), [5, 6])

    def test_empty(self):
        """ Check if the list is empty """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_negatives(self):
        """ Check if the list has negative ints """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_one(self):
        """ Check if the list has only one item """
        self.assertEqual(max_integer([1]), 1)

    def test_raise(self):
        """ Check raises """
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, "Holberton"])


if __name__ == '__main__':
    unittest.main()
