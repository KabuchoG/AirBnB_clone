#!/usr/bin/python3
"""
Review Tests
"""
import unittest
import pycodestyle
from models.review import Review


class test_file_storage(unittest.TestCase):
    """Tests for review.py"""

    @classmethod
    def setUpClass(cls):
        cls.a1 = Review()

    @classmethod
    def tearDownClass(cls):
        del cls.a1

    def test_pep8_self(self):
        """
        Test that checks pycodestyle
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in test_review.py"
        )

    def test_doc(self):
        """test for documentation"""
        self.assertTrue(len(Review.__doc__) > 0)

    def test_pep8_review(self):
        """
        Test that checks PEP8 review.py
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/review.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in review.py"
        )

    def test_create_review(self):
        """
        Test that checks review class
        """
        self.assertTrue(self.a1.id)

    def test_review_attr(self):
        """
        Test that checks review attr
        """
        self.a1 = Review()
        self.a1.place_id = "place_id"
        self.a1.user_id = "user_id"
        self.a1.text = "text"
        self.assertEqual(self.a1.place_id, "place_id")
        self.assertEqual(self.a1.user_id, "user_id")
        self.assertEqual(self.a1.text, "text")


if __name__ == '__main__':
    unittest.main()
