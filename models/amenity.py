#!/usr/bin/python3
"""
This module defines an amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    public amenity class defined
    """

    def __init__(self):
        """
        Instantiation of public attributes
        """
        self.name = str("")
