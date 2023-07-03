#!/usr/bin/python3
import uuid
import datetime


class BaseModel:
    """ A class representing a BaseModel """
    def __init__(self, *args, **kw):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()

    def __str__(self):
        pass

    def save(self):
        pass

    def to_dict(self):
