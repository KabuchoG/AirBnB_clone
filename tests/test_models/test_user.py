#!/usr/bin/python3
"""
User Tests
"""
import unittest
import pycodestyle
from models.user import User


class test_file_storage(unittest.TestCase):
    """Tests for file_storage.py"""

    @classmethod
    def setUpClass(cls):
        # self.BaseModel._BaseModel__nb_objects = 0
        cls.a1 = User()

    @classmethod
    def tearDownClass(cls):
        del cls.a1

    def test_pep8_self(self):
        """
        Test that checks pycodestyle
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in test_user.py"
        )

    def test_pep8_user(self):
        """
        Test that checks pycodestyle user.py
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/user.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in user.py"
        )

    def test_doc(self):
        """test for documentation"""
        self.assertTrue(len(User.__doc__) > 0)

    def test_create_state(self):
        """
        Test that checks user class
        """
        self.assertTrue(self.a1.id)

    def test_state_attr(self):
        """
        Test that checks state attr
        """
        self.a1.email = "email"
        self.a1.password = "password"
        self.a1.first_name = "first_name"
        self.a1.last_name = "last_name"
        self.assertEqual(self.a1.email, "email")
        self.assertEqual(self.a1.password, "password")
        self.assertEqual(self.a1.first_name, "first_name")
        self.assertEqual(self.a1.last_name, "last_name")


if __name__ == '__main__':
    unittest.main()
