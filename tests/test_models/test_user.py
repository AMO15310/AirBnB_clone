#!/usr/bin/python3
"""Unittest module for the User class"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """Set up test environment"""
        self.user = User()

    def tearDown(self):
        """Tear down test environment"""
        del self.user

    def test_inheritance(self):
        """Test if User class inherits from BaseModel"""
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """Test attributes of User class"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_str(self):
        """Test __str__ method"""
        self.assertEqual(str(self.user), "[User] ({}) {}".
                         format(self.user.id, self.user.__dict__))

    def test_to_dict(self):
        """Test to_dict method"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)

    def test_save(self):
        """Test save method"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_create_user(self):
        """Test creating a new User"""
        new_user = User()
        self.assertIsInstance(new_user, User)

    def test_user_attributes(self):
        """Test setting User attributes"""
        new_user = User()
        new_user.email = "test@example.com"
        new_user.password = "password"
        new_user.first_name = "Test"
        new_user.last_name = "User"
        self.assertEqual(new_user.email, "test@example.com")
        self.assertEqual(new_user.password, "password")
        self.assertEqual(new_user.first_name, "Test")
        self.assertEqual(new_user.last_name, "User")

if __name__ == "__main__":
    unittest.main()

