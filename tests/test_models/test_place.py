#!/usr/bin/python3
"""Unittest module for Place class"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests for the Place class"""

    def test_attr(self):
        """Test Place attributes"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])
        place.city_id = "SF"
        place.user_id = "1234"
        place.name = "Luxury Apartment"
        place.description = "A luxurious apartment in downtown SF"
        place.number_rooms = 3
        place.number_bathrooms = 2
        place.max_guest = 6
        place.price_by_night = 200
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["wifi", "pool", "gym"]
        self.assertEqual(place.city_id, "SF")
        self.assertEqual(place.user_id, "1234")
        self.assertEqual(place.name, "Luxury Apartment")
        self.assertEqual(place.description, "A luxurious apartment in downtown SF")
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 6)
        self.assertEqual(place.price_by_night, 200)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["wifi", "pool", "gym"])


if __name__ == "__main__":
    unittest.main()
