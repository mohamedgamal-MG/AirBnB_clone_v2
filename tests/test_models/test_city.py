#!/usr/bin/python3
""" """
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_id(self):
        city = City()
        city.id = "test_id"
        self.assertEqual(city.id, "test_id")

    def test_name(self):
        city = City()
        city.name = "test_name"
        self.assertEqual(city.name, "test_name")

    def test_save(self):
        city = City()
        city.save()
        self.assertIsNotNone(city.created_at)
        self.assertIsNotNone(city.updated_at)

    def test_to_dict(self):
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict["__class__"], "City")

if __name__ == '__main__':
    unittest.main()
