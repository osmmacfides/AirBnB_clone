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
        model1 = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model1, "id"))
        self.assertTrue(hasattr(model1, "created_at"))
        self.assertTrue(hasattr(model1, "updated_at"))
        self.assertIsInstance(model1.id, str)
        self.assertIsInstance(model1.created_at, datetime)
        self.assertIsInstance(model1.updated_at, datetime)

        new_dict = model.to_dict()
        model2 = BaseModel(**new_dict)
        self.assertIsInstance(model2, BaseModel)
        self.assertEqual(model1.id, model2.id)
        self.assertIsInstance(model2.created_at, datetime)
        self.assertIsInstance(model2.updated_at, datetime)
