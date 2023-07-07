#!/usr/bin/python3
""" Unittest for HBNBCommand class and his attributes and methods"""

import unittest
from console import HBNBCommand
from io import StringIO
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
storage = FileStorage()

class TestConsole(unittest.TestCase):
    """ Tests for HBNBCommand """

    if __name__ == "__main__":
        unittest.main()
