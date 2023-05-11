#!/usr/bin/python3

"""Custom base class for all models"""

import uuid
from datetime import datetime
import models

class BaseModel:
    """ Base class for all classes in the Airbnb console project

    Attributes:
        id(str): unique user identifier which is a string
        created_at: stamps the current datetime
        updated_at: updates the datetime stamp

    Methods:
        __str__: prints the class name, id, and creates dictionary representations                  of input values
        save(self): initiates instance attributes with current datetime
        to_dict(self): returns the dictionary values of the instance object

     """

    def __init__(self, *args, **kwargs):
        """Public instance attributes initialization
         Args:
            *args: arguments passed
            **kwargs: key with arguments attribute values
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns string representation of the class."""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute 'updated_at' with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all kes and values of __dict__ instance"""
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = dict_copy["created_at"].isoformat()
        dict_copy["updated_at"] = dict_copy["updated_at"].isoformat()
        dict_copy["__class__"] = type(self).__name__
        return dict_copy

