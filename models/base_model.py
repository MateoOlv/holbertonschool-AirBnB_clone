#!/usr/bin/python3
"""
Imports
"""
import uuid
from datetime import datetime
import models


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
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        models.storage.net(self)
        if kwargs is not None:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

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

def main():
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)

main()