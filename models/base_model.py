#!/usr/bin/python3
"""Imports"""
import uuid
from datetime import datetime


class BaseModel:
    """ A class representing a BaseModel """

    def __init__(self):
        """init values"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ return [<class name>] (<self.id>) <self.__dict__> """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Update date of update_at """
        self.update_at = datetime.now()

    def to_dict(self):
        """ Return a dictionary representation of a instance"""
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
