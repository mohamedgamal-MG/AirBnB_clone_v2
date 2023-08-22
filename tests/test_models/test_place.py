#!/usr/bin/python3
""" """
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Set up any necessary test dependencies.
        """
        cls.place = Place()

    def test_city_id(self):
        """
        Test that the city_id attribute is initialized correctly.
        """
        self.assertEqual(self.place.city_id, "")

    def test_user_id(self):
        """
        Test that the user_id attribute is initialized correctly.
        """
        self.assertEqual(self.place.user_id, "")

    def test_name(self):
        """
        Test that the name attribute is initialized correctly.
        """
        self.assertEqual(self.place.name, "")

    def test_description(self):
        """
        Test that the description attribute is initialized correctly.
        """
        self.assertEqual(self.place.description, "")

    def test_number_rooms(self):
        """
        Test that the number_rooms attribute is initialized correctly.
        """
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms(self):
        """
        Test that the number_bathrooms attribute is initialized correctly.
        """
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest(self):
        """
        Test that the max_guest attribute is initialized correctly.
        """
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night(self):
        """
        Test that the price_by_night attribute is initialized correctly.
        """
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude(self):
        """
        Test that the latitude attribute is initialized correctly.
        """
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude(self):
        """
        Test that the longitude attribute is initialized correctly.
        """
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids(self):
        """
        Test that the amenity_ids attribute is initialized correctly.
        """
        self.assertEqual(self.place.amenity_ids, [])

if __name__ == '__main__':
    unittest.main()

