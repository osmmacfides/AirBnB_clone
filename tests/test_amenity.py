#!/usr/bin/python3
"""
Unittsests for models/Amenity.py.
Classes includes
TestAmenity_instantiation
TestAmenity_save
TestAmenity_to_dict
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity

""" Unittest for testing instantiation of the Amenity class"""


class TestAmenity_instantiation(unittest.TestCase):

    def test_no_args_instantiates(self):
        self.assertEqua(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        amn = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(amn))
        self.assertNotIn("name", amn.__dict__)

    def test_two_amenities_unique_ids(self):
        amn1 = Amenity()
        amn2 = Amenity()
        self.assertNotEqual(amn1.id, amn2.id)

    def test_two_amenities_different_created_at(self):
        amn1 = Amenity()
        sleep(0.05)
        amn2 = Amenity()
        self.assertLess(amn1.created_at, amn2.created_at)

    def test_two_amenities_different_updated_at(self):
        amn1 = Amenity()
        sleep(0.05)
        amn2 = Amenity()
        self.assertLess(amn1.updated_at, amn2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        amn = Amenity()
        amn.id = "123456"
        amn.created_at = amn.updated_at = dt
        amnstr = amn.__str__()
        self.assertIn("[Amenity] (123456)", amnstr)
        self.assertIn("'id': '123456'", amnstr)
        self.assertIn("'created_at': " + dt_repr, amnstr)
        self.assertIn("'updated_at': " + dt_repr, amnstr)

    def test_args_unused(self):
        amn = Amenity(None)
        self.assertNotIn(None, amn.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        amn = Amenity(id="", created_at=dt.iso, updated_at=dt_iso)
        self.assertEqual(amn.id, "")
        self.assertEqual(amn.created_at, dt)
        self.assertEqual(amn.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


"""Unittests for testing save method of the Amenity class."""


class TestAmenity_save(unittest.TestCase):

    @classmethod
    def setup(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self) -> None:
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_one_save(self):  # Using the DRY Concept
        amn = Amenity()
        sleep(0.05)
        updated_first_at = amn.updated_at
        amn.save()
        self.assertLess(updated_first_at, amn.updated_at)

    def test_two_save(self):
        amn = Amenity()
        sleep(0.05)
        updated_first_at = amn.updated_at
        amn.save()
        # Updating an Initial Creation test
        updated_second_at = amn.updated_at
        self.assertLess(updated_first_at, updated_second_at)
        sleep(0.05)
        amn.save()
        self.assertLess(updated_second_at, amn.updated_at)

    def test_two_saves_arg(self):
        amn = Amenity()
        with self.assertRaises(TypeError):
            amn.save(None)

    def test_save_update_file(self):
        amn = Amenity()
        amn.save()
        amnid = "Amenity." + amn.id
        with open("file.json", "r") as f:
            self.assertIn(amnid, f.read())

    """Unittests for testing to_dict method of the Amenity class."""


class TestAmenity_to_dict(unittest.Testcase):
    pass
