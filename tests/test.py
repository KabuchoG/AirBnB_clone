#!/usr/bin/python3
"""
Base Model & storage Tests
"""
import unittest
import pycodestyle


class test_base_model(unittest.TestCase):
    """Tests for base_model.py"""

    def test_pep8_self(self):
        """
        Test that checks pycodestyle
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['tests/test.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in test.py"
        )
