#!/usr/bin/python3
"""
This module defines a place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    public place class defined
    """

    def __init__(self):
        """
        Instantiation of public attributes
        """
        self.city_id = str("")
        self.user_id = str("")
        self.name = str("")
        self.description = str("")
        self.number_rooms = int(0)
        self.number_bathrooms = int(0)
        self.max_guest = int(0)
        self.price_by_night = int(0)
        self.latitude = float(0.0)
        self.longitude = float(0.0)
        self.amenity_ids = list()
