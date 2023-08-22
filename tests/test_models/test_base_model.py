#!/usr/bin/python3
"""
 module that implements unit tests for the BaseModel class
"""
import unittest
from models import storage
from uuid import UUID
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModelMethods(unittest.TestCase):
    """
    Test The Base Class
    """
    def setUp(self):
        """
        Set up the test environment
        """
        storage.reset()

    def test_init(self):
        """
        Test the initialization of the BaseModel class
        """
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.created_at, model.updated_at)
        self.assertIs(model, storage.all()["{}.{}".format(model.__class__.__name__, model.id)])

        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

        model2 = BaseModel(**model_dict)
        self.assertEqual(model.id, model2.id)
        self.assertEqual(model.created_at, model2.created_at)
        self.assertEqual(model.updated_at, model2.updated_at)

    def test_str(self):
        """
        Test the string representation of the BaseModel object
        """
        model = BaseModel()
        model_str = str(model)

        self.assertEqual(model_str, "[BaseModel] ({}) {}".format(model.id, model.__dict__))

    def test_save(self):
        """
        Test the save method of the BaseModel object
        """
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        new_updated_at = model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of the BaseModel object
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())
        model_dict['new_attr'] = 'new_value'
        model2 = BaseModel(**model_dict)

        self.assertEqual(model2.new_attr, 'new_value')

if __name__ == '__main__':
    unittest.main()
