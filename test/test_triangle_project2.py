#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

# You need to finish implementing triangle() in the file 'triangle.py'
from triangle import *


class AboutTriangleProject2(unittest.TestCase):
    # The first assignment did not talk about how to handle errors.
    # Let's handle that part now.
    def test_illegal_triangles_throw_exceptions(self):
        # Calls triangle(0, 0, 0)
        self.assertRaises(TriangleError, triangle, 0, 0, 0)

        self.assertRaises(TriangleError, triangle, 3, 4, -5)
        self.assertRaises(TriangleError, triangle, 1, 1, 3)
        self.assertRaises(TriangleError, triangle, 2, 5, 2)
