#!/usr/bin/python3
"""
User class 
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    User Representation

    Attributes:
        email (str): user email
        password (str): user password
        first_name (str): first name
        last_name (str): last name

    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initialize User"""
        super().__init__(*args, **kwargs)
