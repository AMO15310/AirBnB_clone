#!/usr/bin/python3

"""
Test suits for the base model class

"""

import os
import re
import json
import uuid
import unittest
from time import sleep
from datetime import datetime
from models.base_model import BaseModel
import sys
sys.path.append(os.path.abspath('..'))


class TestBaseModel(unittest.TestCase):
    """
    Test attributes of the base model
    """
    def setUp(self):
        """
        Classes need for testing
        """
        pass

    def test_basic(self):
        """
        Tests basic inputs for baseModel class
        """
        my_model = BaseModel()
        my_model.name = "Amos"
        my_model.number = 501
        self.assertEqual([my_model.name, my_model.number], ["Amos",501])
        
    def test_datetime_format(self):
        """
        Tests that created_at and updated_at attributes are in correct format
        """
        my_model = BaseModel()
        created_at_match = re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}$", my_model.created_at.isoformat())
        updated_at_match = re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}$", my_model.updated_at.isoformat())
        self.assertIsNotNone(created_at_match)
        self.assertIsNotNone(updated_at_match)

if __name__ == '__main__':
    unittest.main()
