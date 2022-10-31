#!/usr/bin/python3
"""
Module that defines a class Amenity inherit from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class Amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """init model"""
        super().__init__(*args, **kwargs)
