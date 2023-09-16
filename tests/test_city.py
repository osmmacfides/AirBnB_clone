#!/usr/bin/python3
"""
Unittsests for models/city.py.
Classes includes
TestCity_instantiation
TestCity_save
TestCity_to_dict
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City

""" Unittest for testing instantiation of the City class"""


class TestCity_instantiation(unittest.TestCase):

    def test_no_args_instantiates(self):
        self.assertEqua(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        cy = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cy))
        self.assertNotIn("state_id", cy.__dict__)

    def test_name_is_public_class_attribute(self):
        cy = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cy))
        self.assertNotIn("name", cy.__dict__)

    def test_two_cities_unique_ids(self):
        cy1 = City()
        cy2 = City()
        self.assertNotEqual(cy1.id, cy2.id)

    def test_two_cities_different_created_at(self):
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.created_at, cy2.created_at)

    def test_two_cities_different_updated_at(self):
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.updated_at, cy2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        cystr = cy.__str__()
        self.assertIn("[City] (123456)", cystr)
        self.assertIn("'id': '123456'", cystr)
        self.assertIn("'created_at': " + dt_repr, cystr)
        self.assertIn("'updated_at': " + dt_repr, cystr)

    def test_args_unused(self):
        cy = City(None)
        self.assertNotIn(None, cy.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        cy = City(id="", created_at=dt.iso, updated_at=dt_iso)
        self.assertEqual(cy.id, "")
        self.assertEqual(cy.created_at, dt)
        self.assertEqual(cy.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


"""Unittests for testing save method of the City class."""


class TestCity_save(unittest.TestCase):

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
        cy = City()
        sleep(0.05)
        updated_first_at = cy.updated_at
        cy.save()
        self.assertLess(updated_first_at, cy.updated_at)

    def test_two_save(self):
        cy = City()
        sleep(0.05)
        updated_first_at = cy.updated_at
        cy.save()
        # Updating an Initial Creation test
        updated_second_at = cy.updated_at
        self.assertLess(updated_first_at, updated_second_at)
        sleep(0.05)
        cy.save()
        self.assertLess(updated_second_at, cy.updated_at)

    def test_two_saves_arg(self):
        cy = City()
        with self.assertRaises(TypeError):
            cy.save(None)

    def test_save_update_file(self):
        cy = City()
        cy.save()
        cyid = "City." + cy.id
        with open("file.json", "r") as f:
            self.assertIn(cyid, f.read())

    """Unittests for testing to_dict method of the City class."""


class TestCity_to_dict(unittest.Testcase):
    pass
