#!/usr/bin/python3

import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = "file.json"
        self.storage = FileStorage()
        self.storage.reset()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_empty(self):
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        user = User()
        self.storage.new(user)
        self.assertIn("User.{}".format(user.id), self.storage.all())

    def test_save(self):
        user = User()
        self.storage.new(user)
        self.storage.save()

        with open(self.file_path, mode="r") as f:
            file_contents = json.load(f)
            self.assertIn("User.{}".format(user.id), file_contents)

    def test_reload(self):
        user = User()
        self.storage.new(user)
        self.storage.save()
        self.storage.reset()
        self.storage.reload()
        self.assertIn("User.{}".format(user.id), self.storage.all())

    def test_reset(self):
        user = User()
        self.storage.new(user)
        self.storage.reset()
        self.assertEqual(self.storage.all(), {})

    def test_all(self):
        user = User()
        state = State()
        amenity = Amenity()
        city = City()
        place = Place()
        review = Review()

        self.storage.new(user)
        self.storage.new(state)
        self.storage.new(amenity)
        self.storage.new(city)
        self.storage.new(place)
        self.storage.new(review)

        all_objects = self.storage.all()
        self.assertIn("User.{}".format(user.id), all_objects)
        self.assertIn("State.{}".format(state.id), all_objects)
        self.assertIn("Amenity.{}".format(amenity.id), all_objects)
        self.assertIn("City.{}".format(city.id), all_objects)
        self.assertIn("Place.{}".format(place.id), all_objects)
        self.assertIn("Review.{}".format(review.id), all_objects)
 def test_instances(self):
        """chequeamos instantation"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)
 def test_docs(self):
        """Test docstrings"""
        self.assertIsNotNone(FileStorage.all)
        self.assertIsNotNone(FileStorage.new)
        self.assertIsNotNone(FileStorage.save)
        self.assertIsNotNone(FileStorage.reload)

    
if __name__ == "__main__":
    unittest.main()

