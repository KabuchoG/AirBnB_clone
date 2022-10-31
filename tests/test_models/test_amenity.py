#!/usr/bin/python3
"""
amenity Tests
"""
import unittest
import pycodestyle
from models.amenity import Amenity


class test_file_storage(unittest.TestCase):
    """Tests for amenity.py"""

    @classmethod
    def setUpClass(cls):
        # self.BaseModel._BaseModel__nb_objects = 0
        cls.a1 = Amenity()
        cls.a2 = Amenity()

    @classmethod
    def tearDownClass(cls):
        del cls.a1
        del cls.a2

    def test_pep8_self(self):
        """
        Test that checks pycodestyle
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in test_amenity.py"
        )

    def test_pep8_amenity(self):
        """
        Test that checks PEP8 amenity.py
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/amenity.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in amenity.py"
        )

    def test_create_amenity(self):
        """
        Test that checks amenity class
        """
        self.assertTrue(self.a1.id)

    def test_doc(self):
        """test for documentation"""
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_amenity_attr(self):
        """
        Test that checks amenity attr
        """
        self.a1.name = "name"
        self.assertEqual(self.a1.name, "name")


if __name__ == '__main__':
    unittest.main()
