#!/usr/bin/python3
"""
This module defines a review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    public state class defined
    """

    place_id = ""
    user_id = ""
    text = ""
