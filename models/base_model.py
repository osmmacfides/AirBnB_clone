#!/usr/bin/python3
"""
This module defines a parent class
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    class that defines all common attributes/methods
    for other classes
    """

    def __init__(self):
        """
        Instantiation method
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        method to return string
        """
        class_name = self.__class__.__name__
        obj_id = self.id
        attributes = self.__dict__

        return ("[{}] ({}) {}".format(class_name, obj.id, attributes)

    def save(self):
        """
        Method to update updated_at
        when an attribute is set
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        class_name=self.__class__.__name__
        obj_id=self.id
        attributes=self.__dict__

        attributes['created_at']=self.created_at.isoformat()
        attributes['updated_at']=self.updated_at.isoformat()

        attributes['__class__']=class_name

        return attributes
