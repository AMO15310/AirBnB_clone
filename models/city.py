#!/usr/bin/python3
"""
Define the city class 
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    The city class
    Attributes:
        state_id (str): id of the state
    """
    state_id = ""
    name = ""
