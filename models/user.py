#!/usr/bin/python3
""" module that defines a class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """ class User that inherits BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """init model"""
        super().__init__(*args, **kwargs)
