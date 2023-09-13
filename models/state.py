#!/usr/bin/python3
"""
This module defines a state class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    public state class defined
    """

    def __init__(self):
        """
        Instantiation of public attributes
        """
        self.name = str("")
