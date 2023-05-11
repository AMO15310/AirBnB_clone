#!/usr/bin/python3

"""
Module file_storage serializes and deserializes JSON types
"""

import json
from typing import Dict
from models.user import User
from models.base_model import BaseModel

class FileStorage:
    """
    This class handles the serialization and deserialization of JSON types
    """

    def __init__(self,file_path: str = "file.json") -> None:
        """
        Initializes an instance of FileStorage with a file path to store objects

        Args:
            file_path(str): The file path to store objects.
        """
        self._file_path = file_path
        self._objects = {}
        
    def all(self) -> Dict[str, BaseModel]:
        """
        Returns a dictionary of all objects in the storage.
        
        Returns:
            dict: A dictionary of all objects in the storage.
        """
        return self._objects

    def new(self, obj:BaseModel) -> None:
        """
        Sets an object in the storage with a key of the object's class Name and Id
        Args:
            obj (BaseModel): The object to add to the storage.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self._objects[key] = obj

    def save(self) -> None:
        """
        Serializes the objects in the storage to a JSON file.
        """
        with open(self._file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self._objects.items()}, f)

    def reload(self) -> None:
        """
        Deserializes the objects from a JSON file to the storage.
        """
        try:
            with open(self._file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    obj = eval(class_name)(**value)
                    self._object[key] = obj
        except FileNotFoundError:
            pass

