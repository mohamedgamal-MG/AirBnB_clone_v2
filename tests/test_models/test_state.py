#!/usr/bin/python3
import unittest
from models.state import State
from datetime import datetime

class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_name(self):
        self.assertEqual(self.state.name, "")

    def test_attributes(self):
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_attribute_types(self):
        self.assertIsInstance(self.state.id, str)
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_str_representation(self):
        expected_str = "[State] ({}) {}".format(self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), expected_str)

    def test_to_dict_method(self):
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(state_dict["id"], self.state.id)
        self.assertEqual(state_dict["created_at"], self.state.created_at.isoformat())
        self.assertEqual(state_dict["updated_at"], self.state.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()

