#!/usr/bin/python3
"""
Defines unittests for models/amenity.py.
Unittest classes:
    TestAmenityModel
"""
import os
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity
from models.base_model import BaseModel
from unittest.mock import patch


class TestAmenityModel(unittest.TestCase):
    """Unittests for the Amenity model."""

    def test_is_subclass(self):
        """Test that Amenity is a subclass of BaseModel."""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name_attribute(self):
        """Test that Amenity has name attribute, and it's an empty string."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        if os.getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertEqual(amenity.name, None)
        else:
            self.assertEqual(amenity.name, "")

    def test_to_dict_method(self):
        """Test to_dict method creates a dictionary with proper attributes."""
        am = Amenity()
        new_dict = am.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertFalse("_sa_instance_state" in new_dict)
        for attr in am.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_dict)
        self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """Test that values in dictionary returned from to_dict are correct."""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = Amenity()
        new_dict = am.to_dict()
        self.assertEqual(new_dict["__class__"], "Amenity")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"], am.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"], am.updated_at.strftime(t_format))

    def test_str_method(self):
        """Test that the str method has the correct output."""
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))


if __name__ == "__main__":
    unittest.main()

