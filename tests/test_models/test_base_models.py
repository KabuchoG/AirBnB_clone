#!/usr/bin/python3
"""
Base Model & storage Tests
"""
import unittest
import pycodestyle
import os
from datetime import datetime
from models.base_model import BaseModel


class test_base_model(unittest.TestCase):
    """Tests for base_model.py"""

    @classmethod
    def setUpClass(cls):
        cls.b1 = BaseModel()
        cls.b2 = BaseModel()

    @classmethod
    def tearDownClass(cls):
        del cls.b1
        del cls.b2

    def test_pep8_base_model(self):
        """
        Test that checks PEP8 base_model.py
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/base_model.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in base_model.py"
        )

    def test_pep8_self(self):
        """
        Test that checks PEP8 test_base_model.py
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in test_base.py"
        )

    def test_pep8_base_model_init(self):
        """
        Test that checks PEP8 base_model.py
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/__init__.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in models/__init__.py"
        )

    def test_pep8_test_init(self):
        """
        Test that checks PEP8 base_model.py
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['tests/test_models/__init__.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in tests/__init__.py"
        )

    def test_pep8_console(self):
        """
        Test that checks PEP8 base_model.py
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['console.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in console.py"
        )

    def test_doc(self):
        """test for documentation"""
        self.assertTrue(len(BaseModel.__doc__) > 0)

    """================Task 3================"""

    def test_id(self):
        """check id"""
        self.assertEqual(type(self.b1.id), str)

    def test_id_uniq(self):
        """check uniq id"""
        self.assertTrue(self.b1.id != self.b2.id)

    def test_name(self):
        """check name"""
        self.b1.name = "name test"
        self.assertEqual(self.b1.name, "name test")

    def test_my_number(self):
        """check my_number"""
        self.b1.my_number = 89
        self.assertEqual(self.b1.my_number, 89)

    def test_created_at_type(self):
        """check created_a type"""
        self.assertEqual(type(self.b1.created_at), datetime)

    def test_update_at_type(self):
        """check update_at type"""
        self.assertEqual(type(self.b1.updated_at), datetime)

    def test_str(self):
        """check __str__"""
        self.assertTrue(self.b1.__str__)

    def test_to_dict(self):
        """check to_dict"""
        self.assertEqual(type(self.b1.to_dict()), dict)

    def test_str(self):
        """check str"""
        self.assertTrue(self.b1.__str__)

    """================Task 4================"""

    def test_dict_rep(self):
        """re-create an instance with dictionary representation"""
        json = self.b1.to_dict()
        new = BaseModel(**json)
        self.assertCountEqual(self.b1.id, new.id)

    def test_dict_rep_empty(self):
        """re-create an instance with empty dictionary"""
        self.assertTrue(BaseModel({}))


if __name__ == '__main__':
    unittest.main()
