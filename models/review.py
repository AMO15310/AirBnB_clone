#!/usr/bin/python3

"""
Review class module
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    User Review class
    Attributes:
        place_id (str): id of the place
        user_id (str): id of the reviewing user
        text (str): the user's review

    """
    place_id = ""
    user_id = ""
    text = ""
