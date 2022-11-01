#!/usr/bin/python3
"""
module that defines a class BaseModel
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ class BaseModel that defines all common
    attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """ initializes the data """
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k != "created_at" and k != "updated_at":
                        setattr(self, k, v)
                    else:
                        setattr(self, k, datetime.strptime(
                            v, "%Y-%m-%dT%H:%M:%S.%f"))
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ prints: [<class name>] (<self.id>) <self.__dict__> """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute
        updated_at with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all
        keys/values of __dict__ of the instance """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = dict_copy["created_at"].isoformat()
        dict_copy["updated_at"] = dict_copy["updated_at"].isoformat()
        return dict_copy
