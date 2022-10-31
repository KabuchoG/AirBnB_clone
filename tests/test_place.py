#!/usr/bin/python3
"""
Place Tests
"""
import unittest
import pycodestyle
from models.place import Place


class test_place(unittest.TestCase):
    """Tests for file_storage.py"""

    @classmethod
    def setUpClass(cls):
        # self.BaseModel._BaseModel__nb_objects = 0
        cls.a1 = Place()
        cls.a2 = Place()

    @classmethod
    def tearDownClass(cls):
        del cls.a1
        del cls.a2

    def test_pep8_self(self):
        """
        Test that checks pycodestyle
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in test_place.py"
        )

    def test_pep8_place(self):
        """
        Test that checks PEP8 place.py
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/place.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Pycodestyle errors found in place.py"
        )

    def test_doc(self):
        """test for documentation"""
        self.assertTrue(len(Place.__doc__) > 0)

    def test_create_place(self):
        """
        Test that checks place class
        """
        self.assertTrue(self.a1.id)

    def test_place_attr(self):
        """
        Test that checks place attr
        """
        self.a1.city_id = "city_id"
        self.a1.user_id = "user_id"
        self.a1.name = "name"
        self.a1.description = "description"
        self.a1.number_rooms = 2
        self.a1.number_bathrooms = 2
        self.a1.max_guest = 2
        self.a1.price_by_night = 2
        self.a1.latitude = 2.5
        self.a1.longitude = 2.5
        self.a1.amenity_ids = ["test_id"]
        self.assertEqual(self.a1.city_id, "city_id")
        self.assertEqual(self.a1.user_id, "user_id")
        self.assertEqual(self.a1.name, "name")
        self.assertEqual(self.a1.description, "description")
        self.assertEqual(self.a1.number_rooms, 2)
        self.assertEqual(self.a1.number_bathrooms, 2)
        self.assertEqual(self.a1.max_guest, 2)
        self.assertEqual(self.a1.price_by_night, 2)
        self.assertEqual(self.a1.latitude, 2.5)
        self.assertEqual(self.a1.longitude, 2.5)
        self.assertEqual(self.a1.amenity_ids, ["test_id"])


if __name__ == '__main__':
    unittest.main()
