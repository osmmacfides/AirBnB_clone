#!/usr/bin/python3
"""
This module defines a program that contains
the entry point of the command interpreter:
"""
import cmd
import json
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    class definition for the command interpreter
    """
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, line):
        """
        method to exit the program
        """
        return True

    def do_help(self, arg):
        """
        List available commands with "help" or detailed help with "help cmd"
        """
        return super().do_help(arg)

    def do_EOF(self, line):
        """
        method to exit the program
        """
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, line):
        """
        method to create new instance of BaseModel
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return

        try:
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)

        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        method to print the string representation of an
        instance based on the class name and id
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        # Load the data from the JSON file
        try:
            with open("file.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        # Construct the key to search for
        key = "{}.{}".format(class_name, instance_id)
        # Check if the key exists in the data
        if key in data:
            print(data[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        method to delete an instance based on the class name
        and id (save the change into the JSON file)
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        try:
            # Attempt to retrieve the instance based on
            # class_name and instance_id
            instance = storage.get(class_name, instance_id)
            if instance:
                storage.delete(instance)
                storage.save()
            else:
                print("** no instance found **")
        except Exception as e:
            pass

    def do_all(self, line):
        """
        method to prints all string representation of all
        instances based or not on the class name
        """
        args = line.split()
        instances = []
        all_objects = storage.all()

        if len(args) > 0:
            class_name = args[0]
            if class_name not in self.__classes:
                print("** class doesn't exist **")
                return

        else:
            for obj in all_objects.values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    instances.append(obj.__str__())
                elif len(args) == 0:
                    instances.append(obj.__str__())
            print(instances)

    def do_update(self, line):
        """
        method to Updates an instance based on the class name
        and id by adding or updating attribute (save the
        change into the JSON file)
        """
        args = line.split()
        all_data = storage.all()

        if not args:
            print("** class name missing **")
            return False

        class_name = args[0]

        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return False

        if len(args) < 2:
            print("** instance id missing **")
            return False

        instance_id = args[1]

        if len(args) < 3:
            print("** attribute name missing **")
            return False

        att_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return False

        att_val = args[3]

        # Construct the key to search for
        key = "{}.{}".format(class_name, instance_id)

        # Check if the key exists in the dictionary of objects
        if key not in storage.all():
            print("** no instance found **")
            return False

        if len(args) == 4:
            obj = all_data[key]
            if att_name in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[att_name])
                obj.__dict__[att_name] = valtype(att_val)

            else:
                obj.__dict__[att_name] = att_val

        elif type(eval(att_name)) == dict:
            obj = all_data[key]
            for k, v in eval(att_name).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
