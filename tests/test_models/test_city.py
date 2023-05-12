#!/usr/bin/python3
"""Module for testing the City class."""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Tests for the City class."""

    def test_default_attributes(self):
        """Test that the default attributes of a new City instance are set correctly."""
        c = City()
        self.assertEqual(c.state_id, "")
        self.assertEqual(c.name, "")

    def test_setting_attributes(self):
        """Test that we can set attributes of a new City instance."""
        c = City()
        c.state_id = "123"
        c.name = "San Francisco"
        self.assertEqual(c.state_id, "123")
        self.assertEqual(c.name, "San Francisco")


if __name__ == "__main__":
    unittest.main()

