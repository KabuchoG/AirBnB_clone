#!/usr/bin/python3
"""
City Tests
"""
import unittest
import pycodestyle
from models.city import City


class test_file_storage(unittest.TestCase):
    """Tests for city.py"""

    @classmethod
    def setUpClass(cls):
        cls.a1 = City()

    @classmethod
    def tearDownClass(cls):
        del cls.a1

    def test_pep8_self(self):
        """
        Test that checks pycodestyle
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in test_city.py"
        )

    def test_pep8_city(self):
        """
        Test that checks PEP8 city.py
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/city.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in city.py"
        )

    def test_doc(self):
        """test for documentation"""
        self.assertTrue(len(City.__doc__) > 0)

    def test_create_city(self):
        """
        Test that checks city class
        """
        self.assertTrue(self.a1.id)

    def test_city_attr(self):
        """
        Test that checks city attr
        """
        self.a1.state_id = "state_id"
        self.a1.name = "name"
        self.assertEqual(self.a1.state_id, "state_id")
        self.assertEqual(self.a1.name, "name")


if __name__ == '__main__':
    unittest.main()
