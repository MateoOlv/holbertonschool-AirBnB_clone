#!/usr/bin/python3
""" Unittest for BaseModel class and his attributes and methods"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def tearDown(self):
        del self.model

    """ Test types of attributes """
    def testAttributesId(self):
        """ id """
        self.assertIsInstance(self.model.id, str)

    def testAttributeCreated_at(self):
        """ created_at """
        self.assertIsInstance(self.model.created_at, datetime)

    def testAttributeUpdated_at(self):
        """ updated_at """
        self.assertIsInstance(self.model.updated_at, datetime)

    """ Test methods """
    def testStrMethod(self):
        """ Representation """
        datad = self.model.__class__.__name__
        string = "[{}] ({}) {}".format(datad, self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), string)

    def testSaveMethod(self):
        """ Representation """
        previous_date = self.model.updated_at
        self.model.save()
        self.assertNotEqual(previous_date, self.model.updated_at)

    def testToDictMethod(self):
        """ Representation """
        dict_model = self.model.to_dict()
        self.assertIsInstance(dict_model, dict)
        self.assertEqual(dict_model['__class__'], "BaseModel")
        self.assertIsInstance(datetime.strptime(dict_model['created_at'], '%Y-%m-%dT%H:%M:%S.%f'), datetime)
        self.assertIsInstance(datetime.strptime(dict_model['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'), datetime)

    if __name__ == "__main__":
        unittest.main()
