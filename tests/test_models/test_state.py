#!/usr/bin/python3
"""
State Tests
"""
import unittest
import pycodestyle
from models.state import State


class test_file_storage(unittest.TestCase):
    """Tests for state.py"""

    @classmethod
    def setUpClass(cls):
        # self.BaseModel._BaseModel__nb_objects = 0
        cls.a1 = State()

    @classmethod
    def tearDownClass(cls):
        del cls.a1

    def test_pep8_self(self):
        """
        Test that checks pycodestyle
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in test_state.py"
        )

    def test_pep8_state(self):
        """
        Test that checks PEP8 state.py
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/state.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in state.py"
        )

    def test_doc(self):
        """test for documentation"""
        self.assertTrue(len(State.__doc__) > 0)

    def test_create_state(self):
        """
        Test that checks state class
        """
        self.assertTrue(self.a1.id)

    def test_state_attr(self):
        """
        Test that checks state attr
        """
        self.a1.name = "name"
        self.assertEqual(self.a1.name, "name")


if __name__ == '__main__':
    unittest.main()
