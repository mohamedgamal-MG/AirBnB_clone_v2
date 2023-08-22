#!/usr/bin/python3

import unittest
from models.review import Review
import datetime

class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_place_id(self):
        self.assertEqual(self.review.place_id, "")

    def test_user_id(self):
        self.assertEqual(self.review.user_id, "")

    def test_text(self):
        self.assertEqual(self.review.text, "")

    def test_attributes(self):
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))

    def test_attribute_types(self):
        self.assertIsInstance(self.review.id, str)
        self.assertIsInstance(self.review.created_at, datetime.datetime)
        self.assertIsInstance(self.review.updated_at, datetime.datetime)

    def test_str_representation(self):
        expected_str = "[Review] ({}) {}".format(self.review.id, self.review.__dict__)
        self.assertEqual(str(self.review), expected_str)

    def test_to_dict_method(self):
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertEqual(review_dict["id"], self.review.id)
        self.assertEqual(review_dict["created_at"], self.review.created_at.isoformat())
        self.assertEqual(review_dict["updated_at"], self.review.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()

