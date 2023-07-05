#!/usr/bin/python3
import os.path
import json
from models.base_model import BaseModel
"""
Import
"""


class FileStorage:
    """"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj
        """
        name = obj.__class__.__name__
        FileStorage.__objects[name + '.' + obj.id] = obj

    def save(self):
        """
        serializes __objects to the JSON file 
        """
        jData = {}
        for key, value in FileStorage.__objects.items():
            jData[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            data = json.dump(jData, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r') as jsonfile:
                jData = json.load(jsonfile)
                for key, obj in jData.items():
                    self.new(setattr(self, 'new', eval(
                        obj['__class__'])(**obj)))
        except FileNotFoundError:
            return
