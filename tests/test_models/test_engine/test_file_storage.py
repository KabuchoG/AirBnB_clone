#!/usr/bin/python3
"""
file_storage Tests
"""
import unittest
import pycodestyle
import os
from models import storage
from models.base_model import BaseModel


class test_file_storage(unittest.TestCase):
    """Tests for file_storage.py"""

    @classmethod
    def setUpClass(cls):
        # self.BaseModel._BaseModel__nb_objects = 0
        cls.b1 = BaseModel()
        cls.b2 = BaseModel()

    @classmethod
    def tearDownClass(cls):
        del cls.b1
        del cls.b2
        os.remove("file.json")

    def test_pep8_self(self):
        """
        Test that checks pycodestyle
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['tests/test_models/test_file_storage.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in test_file_storage.py"
        )

    def test_pep8_engine_init(self):
        """
        Test that checks PEP8 base_model.py
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/engine/__init__.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in models/engine/__init__.py"
        )

    def test_pep8_file_storage(self):
        """
        Test that checks PEP8 base_model.py
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/engine/file_storage.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in file_storage.py"
        )

    def test_doc(self):
        """test for documentation"""
        self.assertTrue(len(storage.__doc__) > 0)

    def test_all(self):
        """check all()"""
        self.assertEqual(type(storage.all()), dict)

    def test_save(self):
        """check json"""
        self.b1.save()
        self.assertTrue(os.path.isfile("file.json"))


if __name__ == '__main__':
    unittest.main()
