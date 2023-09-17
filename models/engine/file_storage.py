#!/usr/bin/python3
"""
module that defines FileStorage class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    This class serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        This method returns the dictionary
        __object
        """
        return self.__objects

    def new(self, obj):
        """
        This method sets in __objects the obj
        with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        This method serializes __objects to the
        JSON file (path: __file_path)
        """
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(serialized_objects, f, indent=4)

    def reload(self):
        """
        This method deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing. If the file doesn't exist,
        no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            keys_to_delete = []  # Create a list to store keys to delete

            for key in FileStorage.__objects.keys():
                if key not in data:
                    keys_to_delete.append(key)

            # Delete keys that are not present in the new data
            for key in keys_to_delete:
                del FileStorage.__objects[key]

            for key, value in data.items():
                class_name = value['__class__']
                obj = eval(class_name)(**value)
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
