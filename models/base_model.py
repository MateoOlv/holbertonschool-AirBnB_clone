#!/usr/bin/python3
import uuid
import datetime


class BaseModel:
    """ A class representing a BaseModel """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = self.created_at

    def __str__(self):
        """ return [<class name>] (<self.id>) <self.__dict__> """
        return f"[{self.__class__.__name__} ({self.id}) ({self.__dict__})]"

    def save(self):
        """ Update date of update_at """
        self.update_at = datetime.now()

    def to_dict(self):
        """ Return a dictionary representation of a instance"""

        new_dict = self.__dict__.copy()
        new_dict['__name__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['update_at'] = self.update_at.isoformast()
        return new_dict
