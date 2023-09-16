#!/usr/bin/python3
"""
This module defines a user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    public user class defined
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
