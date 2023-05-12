#!/usr/bin/python3
"""Module for testing the State class."""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Tests for the State class."""

    def test_default_attributes(self):
        """Test that the default attributes of a new State instance are set correctly."""
        s = State()
        self.assertEqual(s.name, "")

    def test_setting_attributes(self):
        """Test that we can set attributes of a new State instance."""
        s = State()
        s.name = "California"
        self.assertEqual(s.name, "California")


if __name__ == "__main__":
    unittest.main()

