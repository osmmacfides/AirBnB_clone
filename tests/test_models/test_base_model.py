#!/usr/bin/python3
"""
This module has unittest for bas_model file
"""

from unittest import TestCase
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(TestCase):
    """
    This module tests for methods in BaseModel class
    """
    def test_init(self):
        """
        method to test for instantiation
        """
        model1 = BaseModel()
        self.assertIsInstance(model1, BaseModel)
        self.assertTrue(hasattr(model1, "id"))
        self.assertTrue(hasattr(model1, "created_at"))
        self.assertTrue(hasattr(model1, "updated_at"))
        self.assertIsInstance(model1.id, str)
        self.assertIsInstance(model1.created_at, datetime)
        self.assertIsInstance(model1.updated_at, datetime)

        new_dict = model1.to_dict()
        model2 = BaseModel(**new_dict)
        self.assertIsInstance(model2, BaseModel)
        self.assertEqual(model1.id, model2.id)
        self.assertIsInstance(model2.created_at, datetime)
        self.assertIsInstance(model2.updated_at, datetime)

    def test_str(self):
        model1 = BaseModel()
        str_rep = "[BaseModel] ({}) {}".format(
                   model1.id, model1.__dict__)
        self.assertEqual(str(model1), str_rep)

    def test_save(self):
        model1 = BaseModel()
        first_updated_at = model1.updated_at
        model1.save()
        self.assertNotEqual(first_updated_at, model1.updated_at)

    def test_to_dict(self):
        model1 = BaseModel()
        obj_dict = model1.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], model1.id)
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
