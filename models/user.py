#!/usr/bin/python3
"""
This module defines a user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    public user class defined
    """

    def __init__(self):
        """
        Instantiation of public attributes
        """
        self.email = str("")
        self.password = str("")
        self.first_name = str("")
        self.last_name = str("")
