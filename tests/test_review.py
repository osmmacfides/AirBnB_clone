#!/usr/bin/python3
"""
Unittsests for models/Review.py.
Classes includes
TestReview_instantiation
TestReview_save
TestReview_to_dict
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review

""" Unittest for testing instantiation of the Review class"""


class TestReview_instantiation(unittest.TestCase):

    def test_no_args_instantiates(self):
        self.assertEqua(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rv))
        self.assertNotIn("place_id", rv.__dict__)

    def test_user_id_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rv))
        self.assertNotIn("user_id", rv.__dict__)

    def test_text_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rv))
        self.assertNotIn("text", rv.__dict__)

    def test_two_reviews_unique_ids(self):
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)

    def test_two_reviews_different_created_at(self):
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.created_at, rv2.created_at)

    def test_two_reviews_different_updated_at(self):
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.updated_at, rv2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
        rvstr = rv.__str__()
        self.assertIn("[Review] (123456)", rvstr)
        self.assertIn("'id': '123456'", rvstr)
        self.assertIn("'created_at': " + dt_repr, rvstr)
        self.assertIn("'updated_at': " + dt_repr, rvstr)

    def test_args_unused(self):
        rv = Review(None)
        self.assertNotIn(None, rv.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        rv = Review(id="", created_at=dt.iso, updated_at=dt_iso)
        self.assertEqual(rv.id, "")
        self.assertEqual(rv.created_at, dt)
        self.assertEqual(rv.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


"""Unittests for testing save method of the Review class."""


class TestReview_save(unittest.TestCase):

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
        rv = Review()
        sleep(0.05)
        updated_first_at = rv.updated_at
        rv.save()
        self.assertLess(updated_first_at, rv.updated_at)

    def test_two_save(self):
        rv = Review()
        sleep(0.05)
        updated_first_at = rv.updated_at
        rv.save()
        # Updating an Initial Creation test
        updated_second_at = rv.updated_at
        self.assertLess(updated_first_at, updated_second_at)
        sleep(0.05)
        rv.save()
        self.assertLess(updated_second_at, rv.updated_at)

    def test_two_saves_arg(self):
        rv = Review()
        with self.assertRaises(TypeError):
            rv.save(None)

    def test_save_update_file(self):
        rv = Review()
        rv.save()
        rvid = "Review." + rv.id
        with open("file.json", "r") as f:
            self.assertIn(rvid, f.read())

    """Unittests for testing to_dict method of the Review class."""


class TestReview_to_dict(unittest.Testcase):
    pass
