#!/usr/bin/python3
import os.path
import json
from models.base_model import BaseModel
"""Import
"""


class FileStorage:
    """"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        all
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        new
        """
        if obj is not None:
            name = obj.__class__.__name__
            FileStorage.__objects[name + '.' + obj.id] = obj

    def save(self):
        """
        save
        """
        jData = {}
        for key, value in FileStorage.__objects.items():
            jData[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            data = json.dump(jData, f)

    def reload(self):
        """
        Reload
        """
        try:
            with open(FileStorage.__file_path, 'r') as jsonfile:
                jData = json.load(jsonfile)
                for key, obj in jData.items():
                    self.new(setattr(self, 'new', eval(
                        obj['__class__'])(**obj)))
        except FileNotFoundError:
            return
