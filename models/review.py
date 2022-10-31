#!/usr/bin/python3
"""
Module that defines a class Review inherit from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """init model"""
        super().__init__(*args, **kwargs)
