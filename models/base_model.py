#!/usr/bin/python3
"""Imports"""
import uuid
import datetime


class BaseModel:
    """ A class representing a BaseModel """
    def __init__(self, *args, **kw):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ return [<class name>] (<self.id>) <self.__dict__> """
        return f"[{self.__class__.__name__} ({self.id}) ({self.__dict__})]"

    def save(self):
        """ Update date of update_at """
        self.update_at = datetime.now()

    def to_dict(self):
        pass