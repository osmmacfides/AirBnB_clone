import unittest
import datetime
import os
from time import sleep
import models
from models.base_model import BaseModel


"""
Test Cases for the Base class
Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""

class TestBaseModel_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the BaseModel class"""

    def test_no_args_instantiation(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))
    
    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)


        # More code to be inserted when understood


"""Unittests for testing save method of the BaseModel class."""
class TestBaseModel_save(unittest.TestCase):

    @classmethod
    def setup(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        
    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
    
    def test_one_save(self):
        bm = BaseModel()
        sleep(0.05)
        updated_first_at = bm.updated_at
        bm.save()
        self.assertLess(updated_first_at, bm.updated_at)

    def test_two_save(self):
        bm = BaseModel()
        sleep(0.05)
        updated_first_at = bm.updated_at
        bm.save()
        # Updating an Initial Creation test
        bm = BaseModel()
        sleep(0.05)
        updated_second_at = bm.updated_at
        self.assertLess(updated_first_at, updated_second_at)
        sleep(0.05)
        bm.save()
        self.assertLess(updated_second_at, bm.updated_at)

    def test_two_saves_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_update_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())
    
        

# Yet to write a code for unit test for YestModel_to_dict.