#!/usr/bin/python3
"""
This module defines a parent class
"""

import uuid
from datetime import datetime
import models

time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    class that defines all common attributes/methods
    for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Instantiation method
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs["created_at"],
                                                    "%Y-%m-%dT%H:%M:%S.%f")
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                    "%Y-%m-%dT%H:%M:%S.%f")

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        method to return string
        """
        class_name = self.__class__.__name__
        obj_id = self.id
        attributes = self.__dict__

        return ("[{}] ({}) {}".format(class_name, obj_id, attributes))

    def __repr__(self):
        """
        returns string repr
        """
        return (self.__str__())

    def save(self):
        """
        Method to update updated_at
        when an attribute is set
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        class_name = self.__class__.__name__
        obj_id = self.id
        attributes = self.__dict__.copy()

        if isinstance(self.created_at, str):
            attributes["created_at"] = self.created_at
        else:
            attributes["created_at"] = self.created_at.isoformat()

        if isinstance(self.updated_at, str):
            attributes["updated_at"] = self.updated_at
        else:
            attributes['updated_at'] = self.updated_at.isoformat()

        attributes['__class__'] = class_name

        return attributes
