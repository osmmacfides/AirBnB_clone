#!/usr/bin/python3
"""
This module defines a city class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    public city class defined
    """

    def __init__(self):
        """
        Instantiation of public attributes
        """
        self.state_id = str("")
        self.name = str("")
