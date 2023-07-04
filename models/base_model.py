#!/usr/bin/python3
"""
Imports
"""
import uuid
from datetime import datetime


"""
    BaseModel class.

    Attributes:
    id: identifier
    created_at: date and time of creation.
    update_at: date and time of update.

    __str__() - method:
    - Rewrite __str__ method.

    save() - method:
    - Update the date of created.

    to_dict() - method:
    - To create a dictionary that it contain:
      . All attributes of class.
      . Name of class.
      . created_at attribute in ISO format.
      . instance_at attribute in ISO format.
"""


"""BaseModel Module"""


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Init Value"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime(
                            value,
                            "%Y-%m-%dT%H:%M:%S.%f",
                        ))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Str return"""
        datad = self.__class__.__name__
        return "[{}] ({}) {}".format(datad, self.id, self.__dict__)

    def save(self):
        """Save"""
        self.update_at = datetime.now()

    def to_dict(self):
        """Dict values"""
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
