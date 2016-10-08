#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class AboutTrueAndFalse(unittest.TestCase):
    def truth_value(self, condition):
        if condition == True:
            return 'true stuff'
        elif condition == False:
            return 'false stuff'
        else:
            return 'else stuff'

    def test_true_is_treated_as_true(self):
        self.assertEqual('true stuff', self.truth_value(True))

    def test_false_is_treated_as_false(self):
        self.assertEqual('false stuff', self.truth_value(False))

    def test_none_is_treated_as_false(self):
        self.assertEqual('else stuff', self.truth_value(None))

    def test_zero_is_treated_as_false(self):
        self.assertEqual('false stuff', self.truth_value(0))

    def test_empty_collections_are_treated_as_false(self):
        self.assertEqual('else stuff', self.truth_value([]))
        self.assertEqual('else stuff', self.truth_value(()))
        self.assertEqual('else stuff', self.truth_value({}))
        self.assertEqual('else stuff', self.truth_value(set()))

    def test_blank_strings_are_treated_as_false(self):
        self.assertEqual('else stuff', self.truth_value(""))

    def test_everything_else_is_treated_as_true(self):
        self.assertEqual('true stuff', self.truth_value(1))
        self.assertEqual('else stuff', self.truth_value([0]))
        self.assertEqual('else stuff', self.truth_value((0,)))
        self.assertEqual(
            'else stuff',
            self.truth_value("Python is named after Monty Python"))
        self.assertEqual('else stuff', self.truth_value(' '))
        self.assertEqual('else stuff', self.truth_value('0'))


if __name__ == "__main__":
    unittest.main()
