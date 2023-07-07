#!/usr/bin/python3
""" unittest from parent class fileStorage """
import unittest
from models.base_model import BaseModel
import os
import json
from models.engine.file_storage import FileStorage
storage = FileStorage()

class TestEngine(unittest.TestCase):
    """ Tests for HBNBCommand """

    if __name__ == "__main__":
        unittest.main()


