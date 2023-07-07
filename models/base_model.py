#!/usr/bin/python3
"""
Imports
"""
import uuid
from datetime import datetime
import models


"""BaseModel Module"""


class BaseModel:

    def __init__(self, *args, **kwargs):
        """Init Value"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Str return"""
        datad = self.__class__.__name__
        return "[{}] ({}) {}".format(datad, self.id, self.__dict__)

    def save(self):
        """Save"""
        models.storage.save()
        self.update_at = datetime.now()

    def to_dict(self):
        """Dict values"""
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
