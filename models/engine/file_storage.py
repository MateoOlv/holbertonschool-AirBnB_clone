import json
import os.path
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        if obj is not None and hasattr(obj, 'id'):
            name = obj.__class__.__name__
            FileStorage.__objects[name + '.' + obj.id] = obj

    def save(self):
        jData = {}
        for key, value in FileStorage.__objects.items():
            jData[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(jData, f)

    def reload(self):
        try:
            if os.path.exists(FileStorage.__file_path):
                with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for key, obj in data.items():
                        newObj = eval(obj['__class__'])(**obj)
                        FileStorage.__objects[key] = newObj
        except FileNotFoundError:
            pass
