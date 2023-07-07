import json
import os.path
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """ FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        name = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[name] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        jData = {}
        for key, value in FileStorage.__objects.items():
            jData[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(jData, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for key, obj in data.items():
                    newObj = eval(obj['__class__'])(**obj)
                    FileStorage.__objects[key] = newObj
