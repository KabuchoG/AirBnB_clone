#!/usr/bin/python3
"""
Module that defines a class State inherit from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class State"""
    name = ""

    def __init__(self, *args, **kwargs):
        """init model"""
        super().__init__(*args, **kwargs)
