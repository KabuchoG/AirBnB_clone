#!/usr/bin/python3
"""
module that defines a FileStorage class
"""
import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review


class FileStorage:
    """ class that  that serializes instances to a
    JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}
    __classes = {
        'BaseModel': BaseModel,
        'User': User,
        "Amenity": Amenity,
        "City": City,
        "State": State,
        "Place": Place,
        "Review": Review
                }

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj
        with key <obj class name>.id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the
        JSON file (path: __file_path) """
        tmp = {}
        for k, v in self.__objects.items():
            tmp[k] = v.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(tmp, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if path.isfile(self.__file_path) is False:
            return

        with open(self.__file_path, encoding="utf-8") as f:
            des = json.load(f)
            for k, v in des.items():
                cls = v['__class__']
                self.__objects[k] = self.__classes[cls](**v)
