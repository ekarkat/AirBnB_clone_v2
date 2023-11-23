#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
from os import getenv

class test_basemodel(unittest.TestCase):
    """ """
    # @unittest.skipif(getenv("HBNB_TYPE_STORAGE") == "db")
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    # @unittest.skipif(getenv("HBNB_TYPE_STORAGE") == "db")
    def setUp(self):
        """ """
        pass

    # @unittest.skipif(getenv("HBNB_TYPE_STORAGE") == "db")
    def tearDown(self):
        try:
            os.remove('file.json')
        except Exception:
            pass

    # @unittest.skipif(getenv("HBNB_TYPE_STORAGE") == "db")
    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    # @unittest.skipif(getenv("HBNB_TYPE_STORAGE") == "db")
    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    # @unittest.skipif(getenv("HBNB_TYPE_STORAGE") == "db")
    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    # @unittest.skipif(getenv("HBNB_TYPE_STORAGE") == "db")
    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    # @unittest.skipif(getenv("HBNB_TYPE_STORAGE") == "db")
    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    # @unittest.skipif(getenv("HBNB_TYPE_STORAGE") == "db")
    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    # @unittest.skipif(getenv("HBNB_TYPE_STORAGE") == "db")
    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    # @unittest.skipif(getenv("HBNB_TYPE_STORAGE") == "db")
    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        new = self.value(**n)
        self.assertIn('Name', new.__dict__)

    # @unittest.skipif(getenv("HBNB_TYPE_STORAGE") == "db")
    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    # @unittest.skipif(getenv("HBNB_TYPE_STORAGE") == "db")
    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    # @unittest.skipif(getenv("HBNB_TYPE_STORAGE") == "db")
    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)


# class test_basemodel_db(unittest.TestCase):
#     """ test for db storage """
#     def __init__(self, *args, **kwargs):
#         """ """
#         super().__init__(*args, **kwargs)
#         self.name = 'BaseModel'
#         self.value = BaseModel 
#     """ """
#     @unittest.skipif(getenv("HBNB_TYPE_STORAGE") != "db")
#     def test_type(self):
#         """ Assert typo"""
#         i = self.value()
#         self.assertEqual(type(i), self.value)

#     @unittest.skipif(getenv("HBNB_TYPE_STORAGE") != "db")
#     def test_attribute(self):
#         """ tesst attribute"""
#         i = self.value()
#         self.assertIn("created_at", i.__dir__())
#         self.assertIn("updated_at", i.__dir__())
#         self.assertIn("id", i.__dir__())

#     @unittest.skipif(getenv("HBNB_TYPE_STORAGE") != "db")
#     def test_kwargs(self):
#         """ """
#         kwargs = {'id': '12345'}
#         ob = self.value(**kwargs)
#         self.assertEqual(kwargs['id'], ob.created_at)

