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
    
    def testKwargs(self):
        """ Test Kwargs - Representation """
        test_k = {
            'id': '323',
            'created_at': '2023-01-22T22:00:00.000000',
            'update_at': '2023-01-22T22:00:00.000000'
        }
        model = BaseModel(**test_k)
        self.assertEqual(model.id, '323')
        self.assertEqual(model.created_at, datetime.strptime(
                '2023-01-22T22:00:00.000000', '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(model.update_at, datetime.strptime(
                '2023-01-22T22:00:00.000000', '%Y-%m-%dT%H:%M:%S.%f'))

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
        dataId = self.model.id
        dataDict = self.model.__dict__
        string = "[{}] ({}) {}".format(datad, dataId, dataDict)
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
        format = '%Y-%m-%dT%H:%M:%S.%f'
        create_ex = (dict_model['created_at'], format)
        update_ex = (dict_model['updated_at'], format)
        self.assertIsInstance(datetime.strptime(create_ex, datetime))
        self.assertIsInstance(datetime.strptime(update_ex, datetime))

    if __name__ == "__main__":
        unittest.main()
