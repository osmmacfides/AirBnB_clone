#!/usr/bin/python3
"""
This module defines a review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    public state class defined
    """

    def __init__(self):
        """
        Instantiation of public attributes
        """
        self.place_id = ""
        self.user_id = str("")
        self.text = str("")
