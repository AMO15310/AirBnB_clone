#!/usr/bin/python3
"""Module for testing the Amenity class."""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests for the Amenity class."""

    def test_default_attributes(self):
        """Test that the default attributes of a new Amenity instance are set correctly."""
        a = Amenity()
        self.assertEqual(a.name, "")

    def test_setting_attributes(self):
        """Test that we can set attributes of a new Amenity instance."""
        a = Amenity()
        a.name = "Wifi"
        self.assertEqual(a.name, "Wifi")


if __name__ == "__main__":
    unittest.main()

