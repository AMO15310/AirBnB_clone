#!/usr/bin/python3
"""Unittest for Review class"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_review_instantiation(self):
        """Test Review class instantiation"""
        r = Review()
        self.assertIsInstance(r, Review)
        self.assertTrue(hasattr(r, "id"))
        self.assertTrue(hasattr(r, "created_at"))
        self.assertTrue(hasattr(r, "updated_at"))
        self.assertEqual(r.place_id, "")
        self.assertEqual(r.user_id, "")
        self.assertEqual(r.text, "")

    def test_review_attributes(self):
        """Test Review class attributes"""
        r = Review()
        r.place_id = "123"
        r.user_id = "456"
        r.text = "great place"
        self.assertEqual(r.place_id, "123")
        self.assertEqual(r.user_id, "456")
        self.assertEqual(r.text, "great place")

    def test_review_to_dict(self):
        """Test Review class to_dict method"""
        r = Review()
        r_dict = r.to_dict()
        self.assertIsInstance(r_dict, dict)
        self.assertTrue("id" in r_dict)
        self.assertTrue("created_at" in r_dict)
        self.assertTrue("updated_at" in r_dict)
        self.assertTrue("__class__" in r_dict)

    def test_review_str_representation(self):
        """Test Review class __str__ method"""
        r = Review()
        r_str = r.__str__()
        self.assertIsInstance(r_str, str)


if __name__ == "__main__":
    unittest.main()

