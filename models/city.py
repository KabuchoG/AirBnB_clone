#!/usr/bin/python3
"""
Module that defines a class City inherit from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class City"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """init model"""
        super().__init__(*args, **kwargs)
